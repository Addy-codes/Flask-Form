from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    host="localhost",
    port="3307",
    database="student-form",
    user="root",
    password="qwerty123",
)
cursor = connection.cursor()

student = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        college = request.form["college"]
        email = request.form["email"]
        major = request.form["major"]

        cursor.execute(
            "INSERT INTO students(name, age, college, email, major) VALUES (%s,%s,%s,%s,%s)",
            (name, age, college, email, major),
        )
        connection.commit()

        # Redirect to the submit page
        return redirect("/submit")

    return render_template("form.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    return render_template("submit.html")


@app.route("/show")
def show():
    cursor.execute("SELECT * FROM students;")
    students = cursor.fetchall()
    print(students)
    return render_template("show.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)
