

class Veiculo:
    def __init__(self, marca, modelo, versao, motor, cor):
        self.marca = marca
        self.modelo = modelo
        self.versao = versao
        self.motor = motor
        self.cor = cor


    def getVeiculo(self):
        return self.marca, self.modelo, self.versao, self.motor, self.cor


    def setVeiculo(self, marca, modelo, versao, motor, cor):
        self.marca = marca
        self.modelo = modelo
        self.versao = versao
        self.motor = motor
        self.cor = cor

