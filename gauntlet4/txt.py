from flask import Flask, request, make_response, redirect, render_template, render_template_string;
import subprocess
import hashlib
import sqlite3 
import time 
import os 
active_sessions = {}
# flag{they_fell_for_one_of_the_classic_blunders}
app = Flask(__name__) 
def generate_token(): 
    return os.urandom(32).hex() 

def check_token(token): 
    if token not in active_sessions: 
        return None 
    token_info = active_sessions[token]
    if token_info[3] < time.time(): del active_sessions[token] return None return token_info @app.route('/') def root(): return make_response(redirect("/login")) @app.route('/login', methods=['GET']) def login(): return render_template('login.html') 

@app.route('/login', methods=['POST']) 
def login_post(): 
    username = request.form.get('username') 
    password = request.form.get('password') # idk why we do this, just got this from a coworker 
    if 'system' in username or 'system' in password: 
        return render_template_string(f'<span style="color:red">Error: invalid input.</span>') # prevent special characters so they can't do sql injection 
    if "'" in username or '"' in username: 
        return render_template_string(f'<span style="color:red">Error: username "{username}" contains invalid characters!</span>') 
    if "'" in password or '"' in password: 
        return render_template_string(f'<span style="color:red">Error: password "{password}" contains invalid characters!</span>') 
    users_db = sqlite3.connect('users.db') 
    pass_hash = hashlib.md5(password.encode('utf-8')).hexdigest()[::-1] # reverse for extra security 
    logins_cur = users_db.execute(f"select * from logins where username='{username}' and password_hashed='{pass_hash}'")
    users = logins_cur.fetchall() 
    users_db.close() 
    if len(users) == 0: 
        return render_template_string(f'<span style="color:red">Error: login was incorrect!</span>') 

    user = users[0]




expire_time = time.time() + 60 * 60 * 2 new_token = generate_token() active_sessions[new_token] = (username, password, user[2], expire_time) resp = make_response(redirect("/home")) resp.set_cookie("LoginToken", new_token) return resp @app.route('/home') def home(): auth_header = request.cookies.get("LoginToken") user = check_token(auth_header) if user == None: resp = make_response('<span style="color:red">Error: token expired or is invalid!</span>') resp.delete_cookie('LoginToken') return resp info_resp = subprocess.check_output(['../secret/info', user[1], 'A'], cwd='../secret').decode('utf-8') return render_template('welcome.html', banner=info_resp, is_admin=user[2]) @app.route('/file-management') def file_management(): auth_header = request.cookies.get("LoginToken") user = check_token(auth_header) if user == None: resp = make_response('<span style="color:red">Error: token expired or is invalid!</span>') resp.delete_cookie('LoginToken') return resp info_resp = subprocess.check_output(['../secret/info', user[1], 'A'], cwd='../secret').decode('utf-8') fm_resp = subprocess.check_output(['../secret/info', user[1], 'I'], cwd='../secret').decode('utf-8') return render_template('file_management.html', banner=info_resp, fm_notice=fm_resp, is_admin=user[2]) @app.route('/game') def game(): auth_header = request.cookies.get("LoginToken") user = check_token(auth_header) if user == None: resp = make_response('<span style="color:red">Error: token expired or is invalid!</span>') resp.delete_cookie('LoginToken') return resp info_resp = subprocess.check_output(['../secret/info', user[1], 'A'], cwd='../secret').decode('utf-8') return render_template('game.html', banner=info_resp, is_admin=user[2]) @app.route('/status') def status(): auth_header = request.cookies.get("LoginToken") user = check_token(auth_header) if user == None: resp = make_response('<span style="color:red">Error: token expired or is invalid!</span>') resp.delete_cookie('LoginToken') return resp info_resp = subprocess.check_output(['../secret/info', user[1], 'A'], cwd='../secret').decode('utf-8') status_resp = subprocess.check_output(['../secret/info', user[1], 'S'], cwd='../secret').decode('utf-8') return render_template('status.html', banner=info_resp, status=status_resp, is_admin=user[2]) @app.route('/settings') def settings(): auth_header = request.cookies.get("LoginToken") user = check_token(auth_header) if user == None: resp = make_response('<span style="color:red">Error: token expired or is invalid!</span>') resp.delete_cookie('LoginToken') return resp info_resp = subprocess.check_output(['../secret/info', user[1], 'A'], cwd='../secret').decode('utf-8') return render_template('settings.html', banner=info_resp, is_admin=user[2]) if __name__ == '__main__': app.run(host='0.0.0.0', port=8080)" contains invalid characters!
