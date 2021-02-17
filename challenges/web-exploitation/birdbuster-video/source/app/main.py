from flask import Flask, render_template, request, redirect, url_for
import werkzeug
from pyzbar.pyzbar import decode
from PIL import Image, UnidentifiedImageError
import sqlite3

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 500 * 1024

ALLOWED_EXTENSIONS = {"jpeg", "jpg", "png", "gif"}

# Connect to database
db_con = sqlite3.connect("database.db")
db_con.row_factory = sqlite3.Row
db_cur = db_con.cursor()


@app.route("/")
def index():
    error = request.args.get('error')

    if error == None:
        return render_template("index.html")

    if error == "0":
        return render_template("index.html", error="Error: File too large to upload")

    if error == "1":
        return render_template("index.html", error="Error: Incorrect file type")

    if error == "2":
        return render_template("index.html", error="Error: Couldn't read image file")

    if error == "3":
        return render_template("index.html", error="Error: An internal error occurred")

    if error == "4":
        return render_template("index.html", error="Error: That is not a valid barcode")

@app.errorhandler(werkzeug.exceptions.RequestEntityTooLarge)
def request_entity_too_large(e):
    return redirect(url_for('index', error=0))

@app.route("/upload", methods=["GET", "POST"])
def upload_file():

    if request.method == "POST":
        f = request.files["uploaded_file"]

        # No file was sent with the post request
        if not f:
            return redirect(url_for('index'))

        # Check the file extension of the uploaded file
        if not f.filename.split(".")[-1] in ALLOWED_EXTENSIONS:
            return redirect(url_for('index', error=1))

        # Open image and decode using pyzbar
        try:
            image = Image.open(f)
            result = decode(image)

        # Pillow couldn't read the image file
        except UnidentifiedImageError:
            return redirect(url_for('index', error=2))

        produce = []
        error = None

        # result is a valid barcode
        if result:
            item_name = result[0].data.decode("utf-8")

            try:
                db_cur.execute(
                    "SELECT * FROM Movies WHERE name='"
                    + item_name
                    + "' COLLATE NOCASE;"
                )
                query_result = db_cur.fetchall()

                # Format query result for html
                for row in query_result:
                    produce.append(
                        {"name": row["name"], "price": "{0:.2f}".format(row["price"])}
                    )

                if not query_result:
                    error = "The barcode '" + item_name + "' returned no results"

            # Error with the sql query or multiple statements detected
            except (sqlite3.Warning, sqlite3.Error):
                return redirect(url_for('index', error=3))

        # result is not a valid barcode
        else:
            return redirect(url_for('index', error=4))

        return render_template("index.html", produce=produce, error=error)

    # Reached if user sent get request
    return render_template("index.html", produce=None, error="")
