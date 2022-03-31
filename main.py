# 1 realizar a instalação do pymongo: python -m pip install pymongo
# 2 instalar dnspython para acesso ao host do banco: python -m pip install dnspython
# 3 cria banco mongo utilizando o script:
from pymongo import MongoClient

# função em python é declarada utilizando a key word def : define
# vai conectar no banco mongo que for passado como parâmetro
# e vai devolver o banco como resposta
def get_database(database):
    # var cliente recebe o objeto cliente mongoDb
    client = MongoClient("mongodb://localhost:27017")
    # client = MongoClient(database="localhost", port="27017")
    return client[database]

def insert_farm(farm): # insere uma nova fazenda
    db = get_database("class_19004") # conectando no banco e salvando a conexao na var db
    #     con.collection.funcao
    ret = db.farms.insert_one(farm)
    return ret.inserted_id

# bloco que inicia um programa em python
if __name__ == "__main__":
    #python listas, tuplas, dicionários
    #mongo JSONs { "key": "value" }

    #dictionary in python newFarm
    newFarm ={
        "name": "Farm's Python 1",
        "manager": "João Quebra Toco"
    }
    # arm. na var id o último id inserido
    id = insert_farm(newFarm)

    #imprimindo a mensagem com o ID da fazenda gerado pelo mongoDB
    print(f"Fazenda inserida. ID:[ {id} ]")