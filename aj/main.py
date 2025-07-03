import json
from flask import Flask, jsonify,request

from response import Response, ResponseCode
from session import SessionManager

import mysql.connector
import random




connection = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="",
  database="bob"
)


def get(arg):
    return request.args.get(arg)

def get_hash(email):
    return get_user(email)[6]

def get_user(email):
    with connection.cursor() as cursor:

        cursor.execute("""
            SELECT * FROM users WHERE email = %(email)s;
        """, {
            'email': email
        })

        result = cursor.fetchone()

    result = list(result)
    print(result)
    if result is None:
        return None
    return result

def post_user(username, phno, email, hash):

     with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO users VALUES (
                UUID(),
                'Sample name',
                %(username)s,
                %(phno)s,
                %(email)s,
                %(hex)s,
                %(pw)s                
            );
            
            
        """, {
            'username' : username,
            'phno' : phno,
            'email' : email,
            'hex' : hex(random.randrange(0, 2**24))[2:],
            'pw' : hash
        })

def post_msg(send,recieve,msg):
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO messages VALUES (
                UUID(),
                %(send)s,
                %(receive)s,
                %(msg)s,
                NOW(),
                0                
            );
            
            
        """, {
            'send' : send,
            'receive' : recieve,
            'msg' : msg
        })


app = Flask(__name__)


@app.route('/sendmsg', methods=['POST'])
def sendmsg():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        res = Response()

        send = sm.get_uuid_from(json['send'])
        rec = json['rec']
        msg = json['msg']

        post_msg(send,rec,msg)
        

        print(res.obj())
        return json.dumps(res.obj())
    else:
        return 'Content-Type not supported!'


@app.route('/signup', methods=['POST'])
def signup():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()

        res = Response()
        res.code = ResponseCode.OK
        res.data = sm.add_session(data['uuid'])
        post_user(data['username'], data['phno'], data['email'], data['hash'])
        print(res.obj())
        return json.dumps(res.obj())
    else:
        return 'Content-Type not supported!'

@app.route('/signin', methods=['GET'])
def signin():
    email = get('email')
    hash = get('hash')

    res = Response()
    if hash == get_hash(email):
        res.code = ResponseCode.OK
        res.data = get_user(email)
        res.data[0] = sm.add_session(res.data[0])
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