from flask import Flask, render_template, request

app = Flask(__name__, template_folder = "templates")

@app.route('/')
def home():
    return render_template("parent.html")

@app.route('/me')
def me():
    return render_template("about_me.html")

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        message = request.form.get("message")
        print(f"Wiadomość: {message}")
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
