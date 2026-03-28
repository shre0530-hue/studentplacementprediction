from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route('/')
def home():
    return render_template('home.html')

# ---------------- SIGNUP ----------------
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS users(name TEXT, email TEXT, password TEXT)")
        cur.execute("INSERT INTO users VALUES(?,?,?)",(name,email,password))

        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template('signup.html')

# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE email=? AND password=?",(email,password))
        user = cur.fetchone()

        conn.close()

        if user:
            return redirect('/predict')
        else:
            return "Invalid Login"

    return render_template('login.html')

# ---------------- PREDICT PAGE ----------------
@app.route('/predict')
def predict():
    return render_template('predict.html')

# ---------------- RESULT ----------------
@app.route('/result', methods=['POST'])
def result():

    cgpa = float(request.form['cgpa'])
    internship = int(request.form['internship'])
    projects = int(request.form['projects'])
    communication = int(request.form['communication'])
    certifications = int(request.form['certifications'])
    resume = int(request.form['resume'])
    mock = int(request.form['mock'])

    management = request.form.getlist('management')
    technical = request.form.getlist('technical')
    digital = request.form.getlist('digital')

    score = (
        cgpa * 10 +
        internship * 20 +
        projects * 15 +
        communication * 10 +
        certifications * 10 +
        resume * 5 +
        mock * 10 +
        len(management) * 5 +
        len(technical) * 5 +
        len(digital) * 5
    )

    percentage = int((score / 300) * 100)

    # Placement level
    if percentage >= 75:
        level = "HIGH chance of Placement"
    elif percentage >= 50:
        level = "MEDIUM chance of Placement"
    else:
        level = "LOW chance of Placement"

    # Course Suggestions
    courses = []

    if len(technical) < 3:
        courses.append("Python Programming")
        courses.append("SQL for Beginners")

    if len(management) < 2:
        courses.append("Advanced Excel")
        courses.append("Business Analytics")

    if len(digital) < 2:
        courses.append("Digital Marketing Course")

    if communication < 3:
        courses.append("Communication Skills Training")

    if internship == 0:
        courses.append("Internship Preparation Course")

    return render_template("result.html",
                           level=level,
                           percentage=percentage,
                           courses=courses)

# ---------------- ABOUT ----------------
@app.route('/about')
def about():
    return render_template('about.html')

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)