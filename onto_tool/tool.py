from  owlready2 import *

class Onto:
    def __init__(self, name_ontology, uri_onto):
        # __init__ é o construtor: inicializa os atributos
        self.nome = name_ontology
        self.uri_onto = uri_onto

    @property
    def load_onto(self):
        onto = owlready2.get_ontology(self.uri_onto).load()
        out =[]
        def  maker(prop):
            aux = []
            for c in prop:
                  aux.append(c)
            return aux

        out.append(maker(onto.classes()))
        out.append(maker(onto.individuals()))
        out.append(maker(onto.properties()))
        out.append(maker( onto.object_properties()))
        out.append(maker(onto.data_properties()))
        out.append(maker(onto.annotation_properties()))
        out.append(maker(onto.disjoint_classes()))
        out.append(maker(onto.disjoints()))
        out.append(maker(onto.disjoint_properties()))
        out.append(maker(onto.rules()))
        out.append(maker(onto.variables()))
        out.append(maker(onto.general_class_axioms()))

        return out



      # onto.individuals()

       # return  , onto.individuals(), ,\
          # , ,\
           # , ,\
           #,,\
          #,,,\
          #


