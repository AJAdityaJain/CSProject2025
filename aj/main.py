import json
from flask import Flask, jsonify,request

from response import Response, ResponseCode
from session import SessionManager






def get(arg):
    return request.args.get(arg)

def get_hash(email):
    return ''

def get_user(email, suid):
    return ''

app = Flask(__name__)

@app.route('/signin', methods=['GET'])
def get_date():
    email = get('email')
    hash = get('hash')
    

    res = Response()
    if hash == get_hash(email):
        suid = sm.add_session()
        res.code = ResponseCode.OK
        res.data = get_user(email,suid)
    else:
        res.code = ResponseCode.FAIL
        res.data = None
    print()
    return json.dumps(res.obj())





@app.route("/")
def index():
    return "<h1>Hello!</h1>"

sm = SessionManager()
if __name__ == '__main__':
    app.run()