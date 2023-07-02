Student Form Flask App Documentation:

This Flask app allows users to fill out a student form, submit the data, and view the submitted data. The app utilizes a MySQL database to store and retrieve student information.

Prerequisites:
Python installed
Flask framework installed
MySQL server installed

Setup:
- Install the required packages by running pip install flask mysql-connector-python in the command line.
- Set up a MySQL database to store the student data. Modify the connection variable in app.py to provide the appropriate database details (host, port, database name, user, and password).

Functionality:
- The landing page ("/") displays an introductory page with a link to access the student form.
- The student form ("/form") allows users to enter their name, age, college, email, and major. Upon form submission, the data is inserted into the MySQL database and users are redirected to the submit page ("/submit").
- The submit page ("/submit") displays a simple confirmation message.
- The show page ("/show") retrieves all student records from the MySQL database and displays them in a tabular format.

Running the App:
- Navigate to the project directory in the command line.
- Run the Flask app by executing the command python app.py or flask run.
- Open a web browser and go to http://localhost:5000 to access the landing page.
- Click the "Fill out the Form" link to access the student form and submit data.
- After submitting the form, you will be redirected to the submit page.
- To view the submitted data, go to http://localhost:5000/show.

Note: Ensure that your MySQL server is running before executing the Flask app.