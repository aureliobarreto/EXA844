from flask import Flask, render_template, request, redirect, session, make_response
from datetime import datetime, timedelta, timezone
app = Flask(__name__, template_folder='templates')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=30)
app.secret_key = 'EXA844'
count = 0
counter_value = 0
@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
        running_time = (datetime.now(timezone.utc) - session.get('_creation_time'))
        remaining_time = app.permanent_session_lifetime - running_time
        
        counter_value = request.args.get('counter',default=0, type=int) + 1
        
        if 'counter' in request.cookies:
            count = int(request.cookies.get('counter'))
        else:
            count = 0                   
        resp =  make_response(render_template('session.html', counter=counter_value, username = username, remaining_time = remaining_time, counter_cookie = count))
        resp.set_cookie('counter', str(count + 1).encode('utf-8'), max_age=60*60) 
        return resp
    else:
        return 'Welcome to Flask Session Example! <a href="/login">Login</a>'

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login1():
    username = request.form['username']
    session['username'] = username
    session['_creation_time'] = datetime.now(timezone.utc)
    return redirect('/')

   
if __name__ == '__main__':
    app.run(debug=True)