from flask import Flask
from config import Config
from model.student import db
from routes.students import students_bp


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(students_bp)


@app.route("/")
def home():
    return "Student Management System"


if __name__ == "__main__":
    app.run(debug=True)