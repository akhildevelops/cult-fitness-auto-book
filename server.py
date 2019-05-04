from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/',methods = ['GET','POST'])
def test():
    print(request.headers)
    print(request.url)
    print(request.json)
    return jsonify(True)

@app.route('/<str1>',methods = ['POST'])
def test_p(str1):
    print(request.headers)
    print(request.url)
    print(request.json)
    return jsonify(True)

if __name__ == '__main__':
    app.run('localhost', 8080, True)