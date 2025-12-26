from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"   # required for session

# Dummy login credentials
USERNAME = "admin"
PASSWORD = "1234"

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']

        if user == USERNAME and pwd == PASSWORD:
            session['user'] = user
            return redirect(url_for('result'))
        else:
            error = "Invalid Username or Password"

    return render_template('login.html', error=error)


@app.route('/result', methods=['GET', 'POST'])
def result():
    if 'user' not in session:
        return redirect(url_for('login'))

    result = None
    if request.method == 'POST':
        name = request.form['name']
        m1 = int(request.form['m1'])
        m2 = int(request.form['m2'])
        m3 = int(request.form['m3'])

        total = m1 + m2 + m3
        percentage = total / 3

        if percentage >= 80:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 40:
            grade = "C"
        else:
            grade = "Fail"

        result = {
            'name': name,
            'total': total,
            'percentage': percentage,
            'grade': grade
        }

    return render_template('index.html', result=result)


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)



# Username: admin
# Password: 1234
