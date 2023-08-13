from graphene import Mutation, String, Int, Field, Boolean
from graphql import GraphQLError
from app.db.database import Session
from app.db.models import User


class LoginUser(Mutation):
    class Arguments:
        email = String(required=True)
        pasword = String(required=True)

    token = String()

    @staticmethod
    def mutate(root, info, email, password):
        session = Session()
        user = session.query(User).filter(User.email == email).first()

        if not user or user.password != password:
            raise GraphQLError("Invaliud email or password")
