# 1 realizar a instalação do pymongo: python -m pip install pymongo
# 2 instalar dnspython para acesso ao host do banco: python -m pip install dnspython
# 3 cria banco mongo utilizando o script:
from pymongo import MongoClient
import pprint

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
    ret = db.farms.insert_one(farm) # inserindo um documento
    # 2a forma de conectar-se a uma collection
    # ret = db['farms'].insert_one(farm)
    return ret.inserted_id

def insert_farms(farms):
    db = get_database("class_19004")
    ret = db.farms.insert_many(farms) # inserindo vários documentos
    return ret.inserted_ids # retornando os últimos ids inseridos (ids dos docs)

def delete_one_farm(conditions):
    col = get_database("class_19004").farms
    return col.delete_one(conditions)

def delete_many_farms(conditions):
    get_database("class_19004").farms.delete_many(conditions)

def find_one_farm(conditions):
    # pprint.pprint( get_database("class_19004").farms.find(conditions)  )
    db = get_database("class_19004")
    col = db.farms
    pprint.pprint(col.find_one(conditions))

def find_farms(conditions):
    col = get_database("class_19004").farms
    #   var  |-lista------------|
    for f in col.find(conditions):
        pprint.pprint(f)

# bloco que inicia um programa em python
if __name__ == "__main__":
    #criando índice para o atributo manager
    try: #tente executar os código abaixo
        col_farms = get_database("class_19004").farms
        index_manager = col_farms.create_index("manager")
        print(f"Índice {index_manager} criado com sucesso!")
    except:
        print(f"Falha ao criar índice {index_manager}")