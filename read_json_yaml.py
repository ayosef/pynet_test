#!/usr/bin/env python

import yaml
import json

from pprint import pprint

yaml_file = 'class1_ex6.yml'
json_file = 'class1_ex6.json'

with open(yaml_file) as f:
    yaml_list = yaml.load(f)

with open(json_file) as f:
    json_list = json.load(f)

print "YAML file:"
print '\n'
pprint(yaml_list)
print '\n'
print "JSON file:"
print '\n'
pprint(json_list)
print '\n'

