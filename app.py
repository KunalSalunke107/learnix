from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login_page.html')  # Make sure the filename matches

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    role = request.form['role']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=? AND password=? AND role=?", (email, password, role))
    user = cursor.fetchone()
    conn.close()

    if user:
        if role == 'student':
            return redirect('/student.html')
        else:
            return redirect('/teacher.html')
    else:
        return "Invalid login, please try again."

if __name__ == '__main__':
    app.run(debug=True)
