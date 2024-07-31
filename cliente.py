

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def getCliente(self):
        return Cliente(self.nome, self.cpf)

    def setCliente(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

