from flask import Flask, request, render_template, flash
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        size = request.form['inputShoulder']
        try:
            size = eval(size)
            jacket = (size * 20) + 2
        except:
            jacket = 'There was an error calculating your jacket size.'

        return render_template('index.html', size=size, jacket=jacket)

    else:
        return render_template('index.html', size='', jacket='')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)