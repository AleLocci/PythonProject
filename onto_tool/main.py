from owlready2 import *

# 1. Criar uma nova ontologia
onto = get_ontology("http://example.org/onto.owl")

with onto:
    # 2. Definir classes
    class Pessoa(Thing):
        pass

    class Estudante(Pessoa):
        pass

    class Professor(Pessoa):
        pass

    # 3. Definir propriedades
    class ensina(ObjectProperty):
        domain = [Professor]
        range = [Estudante]

    class idade(DataProperty):
        domain = [Pessoa]
        range = [int]

# 4. Criar instâncias
joao = Professor("Joao")
maria = Estudante("Maria")

joao.ensina.append(maria)
joao.idade = [40]
maria.idade = [22]

# 5. Salvar a ontologia em arquivo OWL
onto.save(file="onto.owl", format="rdfxml")

# 6. Consultar
print(f"{joao.name} ensina {joao.ensina[0].name}")
print(f"Idade de {maria.name}: {maria.idade}")
