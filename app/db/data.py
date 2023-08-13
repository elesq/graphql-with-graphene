# sample data collections

employer_data = [
    {"name": "meta", "email": "ed@ed.io", "industry": "Tech"},
    {"name": "tla", "email": "ida@ida.io", "industry": "automotive"},
    {"name": "msf", "email": "iris@iris.io", "industry": "entertainment"},
    {"name": "ggl", "email": "meg@meg.io", "industry": "advertising"}
]

jobs_data = [
    {"title": "software engineer",
        "description": "dev stuff", "employer_id": 1},
    {"title": "Senior Data Analyst",
        "description": "analyse stuff", "employer_id": 1},
    {"title": "marketing director",
        "description": "sell stuff", "employer_id": 3},
    {"title": "Advertising consultant",
        "description": "promote stuff", "employer_id": 4}
]

user_data = [
    {"username": "ed", "email": "ed@ward.io", "password": "1234", "role": "lead"},
    {"username": "ida", "email": "ida@ward.io",
        "password": "1234", "role": "star"},
    {"username": "iris", "email": "iris@ward.io",
        "password": "1234", "role": "boss"},
    {"username": "meg", "email": "meg@ward.io",
        "password": "1234", "role": "commander"},
]

applications_data = [
    {"user_id": 1, "job_id": 1},
    {"user_id": 2, "job_id": 1},
    {"user_id": 4, "job_id": 1},
    {"user_id": 3, "job_id": 2},
    {"user_id": 2, "job_id": 2},
    {"user_id": 4, "job_id": 3}
]
