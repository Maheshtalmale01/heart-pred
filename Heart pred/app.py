from flask import Flask

app = Flask(__name__)


@app.route('/2')
def heart():
    return "Hello sir"

if __name__=='__main__':
    app.run(debug=True)