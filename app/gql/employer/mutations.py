from graphene import Mutation, String, Field, Int, Boolean
from app.gql.types import EmployerObject
from app.db.models import Employer
from app.db.database import Session


class AddEmployer(Mutation):
    class Arguments:
        name = String(required=True)
        email = String(required=True)
        industry = String(required=True)

    employer = Field(lambda: EmployerObject)

    @staticmethod
    def mutate(root, info, name, email, industry):
        session = Session()
        employer = Employer(name=name, email=email, industry=industry)
        session.add(employer)
        session.commit()
        session.refresh(employer)
        return AddEmployer(employer)


class UpdateEmployer(Mutation):
    class Arguments:
        id = Int(required=True)
        name = String()
        email = String()
        industry = String()

    employer = Field(lambda: EmployerObject)

    @staticmethod
    def mutate(root, info, id, name=None, email=None, industry=None):
        session = Session()
        employer = session.query(Employer).filter(
            Employer.id == id).first()

        if not employer:
            raise Exception("no employer found")

        if name is not None:
            employer.name = name
        if email is not None:
            employer.email = email
        if industry is not None:
            employer.industry = industry

        session.commit()
        session.refresh(employer)
        session.close()
        return UpdateEmployer(employer)


class DeleteEmployer(Mutation):
    class Arguments:
        id = Int(required=True)

    success = Boolean()

    @staticmethod
    def mutate(root, info, id):
        session = Session()
        employer = session.query(Employer).filter(Employer.id == id).first()
        if not employer:
            raise Exception("Employer not found")

        session.delete(employer)
        session.commit()
        session.close()
        return DeleteEmployer(success=True)
