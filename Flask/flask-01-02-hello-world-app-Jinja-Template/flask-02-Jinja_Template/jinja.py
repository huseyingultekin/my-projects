from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def head():
    return render_template("index.html", number1=123456789, number2=987654321)

@app.route("/toplama")
def number():
    num1 = 23
    num2 = 54
    return render_template("body.html", value1=num1, value2=num2, sum=num1+num2)


 
if __name__== "__main__":
    app.run(debug=True, port=2000)