#!usr/bin/env python

import yaml
import json

yaml_file = 'class1_ex6.yml'
json_file = 'class1_ex6.json'

my_dict = {
    'color':'yellow',
    'number':'4444'
}

my_list = [
    'Hello',
    44,
    my_dict,
    'Bye'
]

with open(yaml_file,"w") as f:
    f.write(yaml.dump(my_list,default_flow_style=False))

with open(json_file,"w") as f:
    json.dump(my_list,f)

