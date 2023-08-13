from graphene import ObjectType, List, Field, Int
from app.gql.types import JobObject, EmployerObject, UserObject, ApplicationObject
from app.db.database import Session
from app.db.models import Job, Employer, User, Application
from sqlalchemy.orm import joinedload


class Query(ObjectType):
    job = Field(JobObject, id=Int(required=True))
    jobs = List(JobObject)
    employer = Field(EmployerObject, id=Int(required=True))
    employers = List(EmployerObject)
    user = Field(UserObject, id=Int(required=True))
    users = List(UserObject)
    application = Field(ApplicationObject, id=Int(required=True))
    applications = List(ApplicationObject)

    @staticmethod
    def resolve_job(root, info, id):
        return Session().query(Job).filter(Job.id == id).first()

    @staticmethod
    def resolve_jobs(root, info):
        return Session().query(Job).all()

    @staticmethod
    def resolve_employer(root, info, id):
        return Session().query(Employer).filter(Employer.id == id).first()

    @staticmethod
    def resolve_employers(root, info):
        return Session().query(Employer).all()

    @staticmethod
    def resolve_user(root, info, id):
        return Session().query(User).filter(User.id == id).first()

    @staticmethod
    def resolve_users(root, info):
        return Session().query(User).all()

    @staticmethod
    def resolve_application(root, info, id):
        return Session().query(Application).filter(Application.id == id).first()

    @staticmethod
    def resolve_applications(root, info):
        return Session().query(Application).all()
