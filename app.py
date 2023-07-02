from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    port="3307",
    database="student-form",
    user="root",
    password="qwerty123",
)

# Create a cursor object to execute MySQL queries
cursor = connection.cursor()

student = []


@app.route("/")
def index():
    # Render the index.html template for the landing page
    return render_template("index.html")


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Retrieve form data submitted by the user
        name = request.form["name"]
        age = request.form["age"]
        college = request.form["college"]
        email = request.form["email"]
        major = request.form["major"]

        # Insert the student data into the MySQL database
        cursor.execute(
            "INSERT INTO students(name, age, college, email, major) VALUES (%s,%s,%s,%s,%s)",
            (name, age, college, email, major),
        )
        connection.commit()

        # Redirect to the submit page
        return redirect("/submit")

    # Render the form.html template for the student form
    return render_template("form.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    # Render the submit.html template for the submit page
    return render_template("submit.html")


@app.route("/show")
def show():
    # Retrieve all student records from the MySQL database
    cursor.execute("SELECT * FROM students;")
    students = cursor.fetchall()
    print(students)

    # Render the show.html template and pass the students data
    return render_template("show.html", students=students)


if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run(debug=True)
