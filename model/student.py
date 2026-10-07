from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Student(db.Model):
    __tablename__="students"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True)
    date_of_birth = db.Column(db.Date)
    class_name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(
       db.DateTime,
       server_default=db.func.current_timestamp()
    )