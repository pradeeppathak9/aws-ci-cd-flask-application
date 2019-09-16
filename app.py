from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Testing CI/CD with Dockerized Flask using AWS Code Pipeline 2+2=4'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
