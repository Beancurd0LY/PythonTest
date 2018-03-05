#!/bin/env python
# coding=utf-8
import json
filename = 'json.json'
with open(filename) as f:
    pop_data = json.load(f)
    for pop_dict in pop_data:
        name = pop_dict['name']
        print '%s,'%(name)


