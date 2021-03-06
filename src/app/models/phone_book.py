class PhoneBook:
  def __init__(self):
    self.collection = []

  def add_person(self, person):
    self.collection.append(person)
    return True

  def remove_person(self, person):
    if person in self.collection:
      self.collection.remove(person)
      return True
    return False

  def find_by(self, attr, value):
    try:
      person = [person for person in self.collection if person[attr]==value] 
      return person
    except AttributeError:
      print("Error")
