from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

FORM = """
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <!-- code drop here -->
            <form action="/" method="POST">
                <label for="rot">Rotations</label>
                <br>
                <input name="rot" type="text" value="0"></input>
                <textarea name="text" type="text">{0}</textarea>
                <button type="submit">Encode</button>
            </form>
        </body>
    </html>
"""

@app.route("/")
def index():
    return FORM.format("")

@app.route("/", methods=["POST"])
def encodedMessage():
    rot = request.form['rot']
    text = request.form['text']

    encoded_message = encrypt(text, rot)

    return FORM.format(encoded_message)

app.run()
