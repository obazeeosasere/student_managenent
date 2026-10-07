from datetime import date

from flask import Blueprint, render_template, request, redirect, url_for
from model.student import db, Student

students_bp = Blueprint("students", __name__, url_prefix="/students")


def parse_date(value):
    if not value:
        return None

    try:
        return date.fromisoformat(value)
    except ValueError:
        return None


@students_bp.route("/")
def list_students():
    students = Student.query.all()
    return render_template("students.html", students=students)


@students_bp.route("/new", methods=["GET", "POST"])
def create_student():
    if request.method == "POST":
        student = Student(
            first_name=request.form.get("first_name"),
            last_name=request.form.get("last_name"),
            email=request.form.get("email"),
            date_of_birth=parse_date(request.form.get("date_of_birth")),
            class_name=request.form.get("class_name")
        )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for("students.list_students"))


    return render_template("student_form.html")  


@students_bp.route("/<int:student_id>/edit", methods=["GET", "POST"])
def edit_student(student_id):
    student = Student.query.get_or_404(student_id)
    if request.method == "POST":
        student.first_name = request.form.get("first_name")
        student.last_name = request.form.get("last_name")
        student.email = request.form.get("email")
        student.date_of_birth = parse_date(request.form.get("date_of_birth"))
        student.class_name = request.form.get("class_name")
        db.session.commit()
        return redirect(url_for("students.list_students"))

    return render_template("student_form.html", student=student)


@students_bp.route("/<int:student_id>/delete", methods=["POST"])
def delete_student(student_id):
    
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for("students.list_students"))


@students_bp.route("/<int:student_id>")
def view_student(student_id):

    student = Student.query.get_or_404(student_id)

    return render_template("student_detail.html", student=student)