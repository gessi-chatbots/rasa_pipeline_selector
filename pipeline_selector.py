from owlready2 import *
from random import randrange
print(onto_path)

onto = get_ontology("file://ontologies/rasa_pipeline_ontology_instances.owl").load()

individuals_by_class = {}

for ind in onto.individuals():
    for c in ind.is_a:
        if c not in individuals_by_class.keys(): individuals_by_class[c] = []
        individuals_by_class[c].append(ind)

config = []

for c in onto.Component.subclasses():
    subclasses = False

    for sub in c.subclasses():
       subclasses = True
       n = len(individuals_by_class[sub])
       config.append(individuals_by_class[sub][randrange(n)])

    if not subclasses:
        n = len(individuals_by_class[c])
        config.append(individuals_by_class[c][randrange(n)])

output = """
recipe: default.v1

language: en
pipeline:
"""
for c in config:
    output += "- name: " + str(c).split('.')[-1] + "\n"

output += "\npolicies:\n"

with open('./config.yml', 'w') as f:
    f.write(output)