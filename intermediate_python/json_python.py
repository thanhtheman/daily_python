import json

person = {
    'name': 'thanh quach',
    'age': 33,
    'city': 'Toronto',
    'hasChildren': False,
    'title': ['Entrepreneur', 'Founder', 'Risk-Taker', {'personality': ['generous', 'talented', 'kind']}]
}

#conver a dict into JSON
personJSON = json.dumps(person, indent=2)
# print(personJSON)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=3)

#convert json to dict
person = json.loads(personJSON)
# print(person)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)

#we can't convert directly from an object of a class, we have to encode.
#this is a custom encoder
def encode_user(i):
    if isinstance(i, User):
        return {'name': i.name, 'age': i.age, i.__class__.__name__: True}
    else:
        raise Exception

userJSON = json.dumps(user, default=encode_user)
print(type(userJSON))
# please notice that, this conversion method will give us a json string, which means it is a string, not an object like in JS
# we can't access its key-value pair
# print(userJSON['name']) -- this will show error
userDict = json.loads(userJSON)

print(userDict['name'])

