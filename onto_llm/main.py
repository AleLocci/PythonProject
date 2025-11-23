from rdflib import Graph, RDF, RDFS, OWL

# Carrega a ontologia
g = Graph()
g.parse("/home/alexandre/Documents/Ontologies/Person/people.rdf", format="xml")

# Listar classes
def listar_classes():
    return [str(s) for s in g.subjects(RDF.type, OWL.Class)]

# Listar propriedades
def listar_propriedades():
    return [str(s) for s in g.subjects(RDF.type, OWL.ObjectProperty)] + \
           [str(s) for s in g.subjects(RDF.type, OWL.DatatypeProperty)]

# Listar indivíduos
def listar_individuos():
    return [str(s) for s in g.subjects(RDF.type, None)
            if s not in listar_classes() and s not in listar_propriedades()]

# Buscar rótulo (label) de uma entidade
def obter_label(entidade):
    label = g.value(entidade, RDFS.label)
    return str(label) if label else entidade

# Exemplo de uso
print("Classes:")
for c in listar_classes():
    print(" -", obter_label(c))

print("\nPropriedades:")
for p in listar_propriedades():
    print(" -", obter_label(p))

print("\nIndivíduos:")
for i in listar_individuos():
    print(" -", obter_label(i))
