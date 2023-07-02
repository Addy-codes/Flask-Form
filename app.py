from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Dummy list to store submitted student data
students = []

connection = mysql.connector.connect(
    host="localhost",
    port="3307",
    database="user-system",
    user="root",
    password="qwerty123",
)
cursor = connection.cursor()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        college = request.form["college"]
        # Add more fields as needed

        # Create a dictionary to store the student data
        student = {
            "name": name,
            "college": college
            # Add more fields as needed
        }

        # Append the student dictionary to the students list
        students.append(student)

        # Redirect to the submit page
        return redirect("/submit")

    return render_template("form.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    return render_template("submit.html")


@app.route("/show")
def show():
    return render_template("show.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)
