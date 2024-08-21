import json
from os.path import exists  

def lerVeiculo():
    with open('veiculos.json', 'r') as file:
        veiculo = json.load(file)
    
    return veiculo

def Motorista_criar_arquivo():
    ''''''
    import json
    veiculos = {}
    with open('veiculos.json', 'w') as veiculosjson:
        json.dump(veiculos, veiculosjson, indent=3)
    #return veiculos  

def Motorista_verificar_arquivo():
    ''''''
    from os.path import exists
    existencia = exists('veiculos.json')
    return existencia

def Motorista_manipular_arquivo():
    ''''''
    if Motorista_verificar_arquivo():
        print ("Existe")
    else:
        print("n existe")


#veiculos = lerVeiculo()

# Novo veículo a ser adicionado ou atualizado
novoVeiculo = {
    "marca": "marca",
    "modelo": "modelo",
    "versao": "versao",
    "motor": "motor",
    "cor": "cor"
}

# Atualizar o dicionário veiculos com o novo veículo
#veiculos.update(novoVeiculo)

# Sobrescrever o arquivo com os novos dados
#with open('veiculos.json', 'w') as file:
#    json.dump(veiculos, file, indent=4)

Motorista_manipular_arquivo()
Motorista_criar_arquivo()
Motorista_manipular_arquivo()