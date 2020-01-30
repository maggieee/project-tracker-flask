"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)



@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    return render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)


@app.route("/create_student")
def show_create_student_form():

    return render_template('create_student.html')


@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""

    first = request.form.get('first_name')
    last = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(first, last, github)

    return render_template("successfully_added.html",
                           first=first,
                           last=last,
                           github=github)


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")

