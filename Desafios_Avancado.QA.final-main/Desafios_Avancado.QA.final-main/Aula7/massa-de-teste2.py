from faker import Faker
import csv
fake = Faker()
fake = Faker('pt_BR')
print("Nome: ", fake.name())
print("Email: ", fake.email())
print("Cidade: ", fake.city())

