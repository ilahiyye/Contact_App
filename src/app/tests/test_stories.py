import os
import sys
sys.path.append(os.path.join(os.path.dirname( "C:/Users/user/Desktop/Tech_Python/Week4/tirex-contactapp/src/app/models")))
#modulu tanimirdi deye path elave edirik
from models.person import Person
from models.phone_book import PhoneBook
from stories.list_user_story import ListUserStory

import unittest

class TestUserStories(unittest.TestCase):
    def setUp(self):
        self.pb = PhoneBook()
        

    def test_list_user_story(self):
        person_1 = Person("Ilahiya", "Musayeva", '123421')  
        person_2 = Person("Amar", "Musayev", "265571")
        pb = PhoneBook()
        pb.add_person(person_1)
        pb.add_person(person_2)
        keyword = "show_list"
        List = ListUserStory(pb)        
        resualt = List.run(keyword)
        return self.assertTrue([person_1, person_2], resualt)

if __name__ == "__main__":
   
    unittest.main()





