import json

my_dict = { 'Ali': 9, 'Sid': 1, 'Luna': 7, 'Sim': 12, 'Pooja': 4, 'Jen': 2}
with open('data.json', 'w') as fp:
    json.dump(my_dict, fp)