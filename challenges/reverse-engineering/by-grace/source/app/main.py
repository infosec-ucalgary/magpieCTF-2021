import flask
from PIL import Image
from PIL import ImageDraw
import sys
from flask_cors import CORS, cross_origin
import uuid
from werkzeug.utils import secure_filename
import os
import filetype

CARDWIDTH=1475             # The width of the card
CARDHEIGHT=650             # The height of the card
HOLEWIDTH=10                # The width of a punched hole
HOLEHEIGHT=20              # The height of a punched hole
COLSPACING=17.35           # Horizontal separation of hole centres
ROWSPACING=CARDHEIGHT/13   # Vertical separation of hole centres
FIRSTCOLUMN=51             # Centre of first column of holes
PUNCHX=6                  
PUNCHY=12
THRESHOLD=240              # The value above which we detect a punch on the card

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png'} # file extensions they're allowed to download
ANSWERS = ["NANOSECOND", "A NANOSECOND", "ONE NANOSECOND", "1 NANOSECOND", "ONE BILLIONTH OF A SECOND",
            "A BILLIONTH OF A SECOND"]

# labeling for the card.  the first two rows are usually labelled "R" and "X" or "12" and "11"
# but the rows are relabled here to make it easier to program.
"""
    ________________________________________________________________
   / &-0123456789ABCDEFGHIJKLMNOPQR/STUVWXYZ#@()]"+.;:,![$*><^,%?=~
 1|  x           xxxxxxxxx                        xxxxxx
 2|   x                   xxxxxxxxx              x      xxxxxx
 3|    x                           xxxxxxxxx     x            xxxxx
 4|     x        x        x        x
 5|      x        x        x        x             x     x
 6|       x        x        x        x      x      x     x    x
 7|        x        x        x        x      x      x     x    x
 8|         x        x        x        x      x      x     x    x
 9|          x        x        x        x      x      x     x    x
10|           x        x        x        x      x      x     x    x
11|            x        x        x        x xxxxx xxxxxxxxxxxxxxxxx 
12|             x        x        x        x
  |_________________________________________________________________

"""

# defines a bitmask for encoding each character in the card
def C(l):
    m = {0:  0b001000000000, 1:   0b000100000000, 2:   0b000010000000,
         3:  0b000001000000, 4:   0b000000100000, 5:   0b000000010000,
         6:  0b000000001000, 7:   0b000000000100, 8:   0b000000000010,
         9:  0b000000000001, 'R': 0b100000000000, 'X': 0b010000000000
        }

    return sum([m[i] for i in l])

# define the squares that need to be punched for each character
codes = {
    ' ': [],
    '0': [3],
    '1': [4],
    '2': [5],
    '3': [6],
    '4': [7],
    '5': [8],
    '6': [9],
    '7': [10],
    '8': [11],
    '9': [12],
    '&': [1],
    '#': [6,11],
    '@': [7,11],
    '(': [8,11],
    ')': [9,11],
    ']': [10,11],
    'A': [1,4],
    'B': [1,5],
    'C': [1,6],
    'D': [1,7],
    'E': [1,8],
    'F': [1,9],
    'G': [1,10],
    'H': [1,11],
    'I': [1,12],
    'J': [2,4],
    'K': [2,5],
    'L': [2,6],
    'M': [2,7],
    'N': [2,8],
    'O': [2,9],
    'P': [2,10],
    'Q': [2,11],
    'R': [2,12],
    'S': [3,5],
    'T': [3,6],
    'U': [3,7],
    'V': [3,8],
    'W': [3,9],
    'X': [3,10],
    'Y': [3,11],
    'Z': [3,12],
    '-': [2],
    '"': [2,3],
    '/': [3,4],
    '+': [1,5,11],
    '.': [1,6,11],
    ';': [1,7,11],
    ':': [1,8,11],
    ',': [1,9,11],
    '!': [1,10,11],
    '[': [2,5,11],
    '$': [2,6,11],
    '*': [2,7,11],
    '>': [2,8,11],
    '<': [2,9,11],
    '^': [2,10,11],        # Should be up arrow
    ',': [3,6,11],
    '%': [3,7,11],
    '?': [3,8,11],
    '=': [3,9,11],
    '~': [3,10,11],        # Should be left arrow
}

# dictionary mappying of each character to it's corresponding code
punchCodes = {
    C([]):        ' ',
    C([0]):       '0',
    C([1]):       '1',
    C([2]):       '2',
    C([3]):       '3',
    C([4]):       '4',
    C([5]):       '5',
    C([6]):       '6',
    C([7]):       '7',
    C([8]):       '8',
    C([9]):       '9',
    C(['R']):     '&',
    C(['R',0]):   '&', # Undocumented but seems to match our cards
    C([3,8]):     '#',
    C([4,8]):     '@',
    C([5,8]):     '(',
    C([6,8]):     ')',
    C([7,8]):     ']',
    C(['R',1]):   'A',
    C(['R',2]):   'B',
    C(['R',3]):   'C',
    C(['R',4]):   'D',
    C(['R',5]):   'E',
    C(['R',6]):   'F',
    C(['R',7]):   'G',
    C(['R',8]):   'H',
    C(['R',9]):   'I',
    C(['X',1]):   'J',
    C(['X',2]):   'K',
    C(['X',3]):   'L',
    C(['X',4]):   'M',
    C(['X',5]):   'N',
    C(['X',6]):   'O',
    C(['X',7]):   'P',
    C(['X',8]):   'Q',
    C(['X',9]):   'R',
    C([0,2]):     'S',
    C([0,3]):     'T',
    C([0,4]):     'U',
    C([0,5]):     'V',
    C([0,6]):     'W',
    C([0,7]):     'X',
    C([0,8]):     'Y',
    C([0,9]):     'Z',
    C(['X']):     '-',
    C(['X',0]):   '"',
    C([0,1]):     '/',
    C(['R',2,8]): '+',
    C(['R',3,8]): '.',
    C(['R',4,8]): ';',
    C(['R',5,8]): ':',
    C(['R',6,8]): ',',
    C(['R',7,8]): '!',
    C(['X',2,8]): '[',
    C(['X',3,8]): '$',
    C(['X',4,8]): '*',
    C(['X',5,8]): '>',
    C(['X',6,8]): '<',
    C(['X',7,8]): '^',        # Should be up arrow
    C([0,2,8]):   u'\u00A3',  # UK pounds sign
    C([0,3,8]):   ',',
    C([0,4,8]):   '%',
    C([0,5,8]):   '?',
    C([0,6,8]):   '=',
    C([0,7,8]):   '~',        # Should be left arrow
    C([5,8]):     '\''
}

def pixel_is_bright(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    return (r + g + b) / 3 > THRESHOLD

def deleteFile(fileLocation):
    os.remove(fileLocation)

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = False
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/punch', methods=['POST'])
@cross_origin(origin='*')
def punch():
    # DON'T THINK THIS IS RIGHT...NEED TO SPECIFY JSON?
    toPunch = flask.request.form['textInput']

    # Our punched card
    image = Image.open("static/blankcard.png")
    bitmap = image.load()

    # A graphics context for drawing our decisions on the image
    graphics_context = ImageDraw.Draw(image)

    # counter to make sure we don't go over 80 letters
    count = 0

    # make the text upper case
    toPunch = toPunch.upper()

    # replace any tabs with 8 spaces
    toPunch = toPunch.replace("\t", "        ")

    # iterate over each letter
    for i in range(len(toPunch)):
        
        # count up
        count += 1

        # get the position of the punches for the letter
        punches = codes[toPunch[i]]

        # punch the holes
        for j in range(len(punches)):
            x = FIRSTCOLUMN + i*COLSPACING
            y = (CARDHEIGHT*punches[j])/13
            graphics_context.rectangle(((x-PUNCHX, y-PUNCHY), (x+PUNCHX, y+PUNCHY)), fill='white')
    
        # kick out of the loop
        if count > 80:
            break

    fileName = str(uuid.uuid4()) + ".png"
    filePath = "cards/" + fileName

    image.save(filePath) # save the image
    return flask.send_file(filePath, as_attachment=True, mimetype='application/download', attachment_filename='card.png')

@app.route('/submit', methods = ['POST'])
def upload_file():
    try:
        f = flask.request.files['myfile']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        kind = filetype.guess("uploads/" + filename)
        if kind == None or kind.extension != "png":
            deleteFile("uploads/" + filename)
            return flask.send_from_directory('templates/', 'wrongExtension.html')

        fileLocation = "uploads/" + filename

        # text on the card, initialized to blank    
        text = ''
        # Our punched card
        image = Image.open(fileLocation)
        bitmap = image.load()

        # There are eighty columns on the card.
        for col in range(80):

            # Each time we find a hole, we accumulate its value here:
            code = 0

            # If you divide the card into thirteen equally spaced rows, the
            # holes occupy rows 1 to 13. Process each row in turn
            for row in range(1,13):

            # The expected centre of this hole
                x = FIRSTCOLUMN + col*COLSPACING
                y = CARDHEIGHT*row / 13

                if pixel_is_bright(bitmap[x,y]):
                    bit_position = 12 - row
                    code |= (1 << bit_position)

                    # Look the code up in our character map
            text += punchCodes[code]

        text = text.rstrip()
        if text in ANSWERS:
            deleteFile(fileLocation)
            return flask.send_from_directory('DaJackpot/', 'jh4tkdfg$@jb^&asd#$%ff.html')
        else:
            deleteFile(fileLocation)
            return flask.send_from_directory('templates/', 'sorry.html')
    except:
        deleteFile(fileLocation)
        return flask.send_from_directory('templates/', 'sorry.html')

@app.route("/", methods=["GET"])
def index():
    return flask.render_template("index.html")

@app.route("/banner.html", methods=["GET"])
def banner():
    return flask.render_template("banner.html")

@app.route("/menu.html", methods=["GET"])
def menu():
    return flask.render_template("menu.html")

@app.route("/homepage.html", methods=["GET"])
def homepage():
    return flask.render_template("homepage.html")

@app.route("/sidebar.html", methods=["GET"])
def sidebar():
    return flask.render_template("sidebar.html")

@app.route("/aboutus.html", methods=["GET"])
def aboutus():
    return flask.render_template("aboutus.html")

@app.route("/numwrite.html", methods=["GET"])
def numwrite():
    return flask.render_template("numwrite.html")

@app.route("/punchcard.html", methods=["GET"])
def punchcard():
    return flask.render_template("punchcard.html")

@app.route("/careers.html", methods=["GET"])
def careers():
    return flask.render_template("careers.html")

@app.route("/guestbook.html", methods=["GET"])
def guestbook():
    return flask.render_template("guestbook.html")

@app.route("/robots.txt")
@app.route("/humans.txt")
def static_from_root():
    return flask.send_from_directory("static/", flask.request.path[1:])