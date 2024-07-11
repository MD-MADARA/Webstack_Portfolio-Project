#!/usr/bin/python3
from backend.models.user import User
from faker import Faker


fake = Faker()

for i in range(10):
    name = fake.name().split()
    data = {
        "address": fake.address(),
        "email": fake.email(),
        "first_name": name[0],
        "last_name": name[1],
        "password": fake.password(),
        "phone": fake.phone_number()
    }
    new = User(**data)
    new.save()
