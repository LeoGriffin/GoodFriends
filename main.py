from Classes.Personne import Person
from Classes.Transaction import Transaction
from Classes.Dettes import Dette
import os
import simplejson as json
person_file = open("data/person.json", "+w")

leo = Person(1, "Griffin", "Léo", "FR76", "hotmail.fr", "0769")
nico = Person(2, "Fruit", "Nicolas", "FR76", "hotmail.fr", "0769")

#person_file.write(leo)
leo.save()
nico.modify()