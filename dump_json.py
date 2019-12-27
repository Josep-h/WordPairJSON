import json

dict_ = {'name': "foo.bar", "sex": "non", "anything": 2}

file = open('new_fake.json', 'w')
json.dump(dict_, file)
file.close()
