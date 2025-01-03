from faker import Faker
from models.sql.User import User

fake = Faker()

def generate_fake_user():
    return User(
        name=fake.name(),
        email=fake.email(),
    )

def generate_fake_users(num: int):
    return [generate_fake_user() for _ in range(num)]
