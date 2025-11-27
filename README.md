# Ontology Explorer Tool

A simple Python tool for exploring ontologies using [Owlready2](https://owlready2.readthedocs.io/).  
It loads an ontology from a given URI and generates lists of its main properties, such as classes, individuals, and axioms.

---

## 🚀 Features
- Load an ontology from a URI.
- Extract and list:
  - Classes
  - Individuals
  - Properties (object, data, annotation)
  - Disjoint classes and properties
  - Rules and variables
  - General class axioms

---

## 📦 Requirements
- Python 3.8+
- [Owlready2](https://pypi.org/project/Owlready2/)

Install dependencies: 

<pre><code class="language-python">
  pip install owlready2
<pre><code class="language-python">
from tool import Onto

# Load Pizza Ontology
onto = Onto("Pizza Ontology", "https://protege.stanford.edu/ontologies/pizza/pizza.owl")

# Explore ontology
properties = onto.load_onto

# Print results
for section in properties:
    print(section)
</code></pre>

<pre><code class="language-python">
[Pizza, VegetarianPizza, Country, Ingredient, ...]
[Margherita, Americana, Soho, ...]
[hasIngredient, hasBase, isMadeIn, ...]
</code></pre>

...
onto_tool/
│── tool.py        # Onto class definition
│── main.py        # Example usage
│── README.md      # Documentation
