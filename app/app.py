import os


from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
from datetime import timedelta


from models import db, TokenBlocklist


from routes.auth import auth_bp, jwt
from routes.users_bp import user_bp, bcrypt
from routes.course_bp import courses_bp
from routes.course_semester_bp import course_sem_bp
from routes.course_work_bp import coursework_bp
from routes.department_bp import department_bp
from routes.exam_bp import exam_bp
from routes.faculty_bp import faculty_bp
from routes.lecturer_bp import lecturer_bp
from routes.lecturer_unit_bp import lecturer_unit_bp
from routes.semester_bp import semester_bp
from routes.student_bp import student_bp
from routes.student_course_bp import student_course_bp
from routes.unit_bp import unit_bp
from routes.enrollment_bp import enrollment_bp
from routes.fee_bp import fees_bp


def create_app():
    app = Flask(__name__)

    load_dotenv()
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=2)

    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    ma = Marshmallow(app)
    migrate = Migrate(app, db)

    @jwt.token_in_blocklist_loader
    def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
        jti = jwt_payload["jti"]
        token = db.session.query(TokenBlocklist).filter_by(jti=jti).first()
        return token is not None

    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(courses_bp)
    app.register_blueprint(course_sem_bp)
    app.register_blueprint(coursework_bp)
    app.register_blueprint(department_bp)
    app.register_blueprint(exam_bp)
    app.register_blueprint(faculty_bp)
    app.register_blueprint(lecturer_bp)
    app.register_blueprint(lecturer_unit_bp)
    app.register_blueprint(semester_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(student_course_bp)
    app.register_blueprint(unit_bp)
    app.register_blueprint(enrollment_bp)
    app.register_blueprint(fees_bp)

    CORS(app, resources={r"*": {"origins": "*"}})
    return app


app = create_app()
