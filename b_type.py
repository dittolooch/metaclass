# b_type.py

#create a class with normal python syntax
class User:
    name = 'warren'

user_one = User()

#create a class with type
#type(class_name, base_classes, class_attributes_dict)
User2 = type("User", (object,), {'name':'warren'})
user_two = User2()

from django.db import models
class User(models.Model):
    first_name = models.CharField(max_length=30)
    age = models.IntegerField()