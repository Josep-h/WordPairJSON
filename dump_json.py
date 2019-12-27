import json

dict_ = {'name': "foo.bar", "sex": "non"}

file = open('fake.json', 'w')
json.dump(dict_, file)
file.close()
