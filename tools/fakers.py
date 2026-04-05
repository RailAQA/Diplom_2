from faker import Faker

from tools.data.ingredients import get_ingrendient

class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    def email(self) -> str:
        return self.faker.email(domain="testyandex.ru")
    
    def name(self) -> str:
        return self.faker.name_female()
    
    def password(self) -> str:
        return self.faker.password(length=10)
    
    def ingrendient(self) -> str:
        return self.faker.random_element(elements=get_ingrendient())
    
    def bad_ingredient(self) -> str:
        return self.faker.pystr(max_chars=12, min_chars=7)
    
fake = Fake(faker=Faker())