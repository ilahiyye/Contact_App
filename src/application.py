import os
from config import app
from app.models import Person, PhoneBook
from app.stories import *



phone_book = PhoneBook()

keyword = input("Enter keyword: ")




class Application:
    def __init__(self, conf):
        self.conf = conf

    def run(self):
        print(f'[x] Starting contact app')




env = os.getenv('ENVIRONMENT')
application = Application(app[env])
application.run()
