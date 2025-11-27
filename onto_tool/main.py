from tool import Onto   # importa a classe Onto do arquivo tool.py

if __name__ == "__main__":
    onto = Onto("Pizza Ontology", "https://protege.stanford.edu/ontologies/pizza/pizza.owl")
    pizza_onto=[]
    pizza_onto = onto.load_onto

#Test#######
print(pizza_onto[0])
print(pizza_onto[1])
print(pizza_onto[2])

