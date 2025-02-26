from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")  # Explicitly set the templates folder

@app.route("/")
def home():
    return render_template("index.html")  # Ensure the filename matches

if __name__ == "__main__":
    app.run(debug=True)
