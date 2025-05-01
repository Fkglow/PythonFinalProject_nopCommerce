import random
import re
import string

from faker import Faker

class DataGenerator(Faker):
    email_regex = r'^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@&"]+)*)|(&quot;.+&quot;))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
    email_pattern = re.compile(email_regex)
    valid_password_length = random.randint(6,64)

    def generate_valid_firstName(self):
        return self.first_name()

    def generate_valid_lastName(self):
        return self.last_name()

    def generate_random_company_name(self):
        return self.company()

    #PASSWORD
    def generate_valid_password(self):
        return self.password(length=self.valid_password_length, special_chars=True, upper_case=True, lower_case=True)

    def generate_invalid_password(self):
        #Different approach for short as Faker has password min_length, which can throw AssertionError for short (~1-5 chars)
        if random.choice(['short', 'long']) == 'short':
            password_length = random.randint(1,5)
            chars = string.ascii_letters
            invalid_password = ''.join(random.choice(chars) for _ in range(password_length))
        else:
            password_length = random.randint(65, 100)
            invalid_password = self.password(length=password_length)
        return invalid_password

    # EMAIL
    def generate_valid_email(self):
        # wouldn't it be better to just use rstr.xeger???? check docs TODO:
        while True:
            email = self.email()
            if self.email_pattern.fullmatch(email):
                return email

    def generate_invalid_email(self):
        improperCharacters = ['<', '>', '(', ')', '[', ']', '.', ',', ';', ':', ' ', '"']
        domain = self.domain_name()
        proper_mail_part = self.generate_random_6_letters()

        invalid_mail = proper_mail_part + random.choice(improperCharacters) + "@" + domain
        return invalid_mail

    def generate_email_that_fails_regex(self):
        text = self.generate_random_6_letters()
        mail = text + "@" + text
        return mail

    @staticmethod
    def generate_random_6_letters():
        text = ''.join(random.choices(string.ascii_letters, k=6))
        return text

