from flask import Flask
app = Flask(__name__)

@app.route("/")
def hw():
   return "Hello World, testing"

@app.route("/<name>")
def test(name):
   return f"Hello {name}"
       

if __name__ == '__main__':
   app.run(debug=True)