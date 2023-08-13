from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.settings.config import DB_URL
from app.db.models import Base, Employer, Job, User, Application
from app.db.data import employer_data, jobs_data, user_data, applications_data

# create and bind the Session factory. We then
# create an actual session by invocation.
engine = create_engine(DB_URL, echo=True)
Session = sessionmaker(bind=engine)


# emp1 = Employer(id=1, name="meta", email="ed@ed.io", industry="tech")


def prepare_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session = Session()

    # unpack the employer values into an Employer structure, the
    # jobs value into a JOb structure and call commit on the
    # session we created
    for employer in employer_data:
        session.add(Employer(**employer))

    for job in jobs_data:
        session.add(Job(**job))

    for user in user_data:
        session.add(User(**user))

    for application in applications_data:
        session.add(Application(**application))

    session.commit()
    session.close()
