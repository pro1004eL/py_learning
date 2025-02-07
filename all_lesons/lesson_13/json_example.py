
import json

users_data = [
    {'id': 1, 'is_active': True, 'friends': None, 'name': 'Ivan'},
    {'id': 1, 'is_active': True, 'friends': None, 'name': 'Ivan'},
    {'id': 1, 'is_active': True, 'friends': [
        {'id': 1, 'is_active': True, 'friends': None, 'name': 'Ivan'},
    ], 'name': 'Ivan'},
]


users_data_json = json.dumps(users_data) # створення json формату поповертає str

# with open('json_as_str.txt', 'w') as json_as_str:
#     json_as_str.write(users_data_json)


# with open('json_as_json.json', 'w') as file:
#     json.dump(users_data, file, indent=4)

with open('json_as_str.txt') as f:
   # data = json.loads(f.read())
    data = json.load(f)

print(data)