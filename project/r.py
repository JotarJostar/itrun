from flask import Flask, render_template

app = Flask(__name__)
menu = ["Home", "About", "Contact"] 
@app.route('/')
def index():
    return render_template("q.html")

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)