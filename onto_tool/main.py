import rdflib
from pyshacl import validate
from owlready2 import *


onto = get_ontology("https://protege.stanford.edu/ontologies/pizza/pizza.owl").load()

cls = []
cls = onto.classes()
ind= onto.individuals()
print(list(cls))
print(list(ind))
