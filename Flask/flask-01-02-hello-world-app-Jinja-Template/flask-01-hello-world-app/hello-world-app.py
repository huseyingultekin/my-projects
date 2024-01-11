from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world from Flask!"

@app.route('/second')
def second():
    return "Merhabalar"

@app.route('/third/subthird')
def third():
    return "This is the subpage of third page"

@app.route('/forth/<string:id>')
def forth(id):
    return f"Id number of this page {id} "

if __name__ == "__main__":
    app.run(debug=True, port=2000)