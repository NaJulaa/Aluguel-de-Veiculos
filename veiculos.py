from veiculo import Veiculo

veiculos = {}
class Veiculos:

    def __init__(self, lista):
        self.lista = lista


    def newVeiculo(self):
        marcaTemp = str(input('Marca: '))
        modeloTemp = str(input('Modelo: '))
        versaoTemp = str(input('Versao: '))
        motorTemp = str(input('Motor: '))
        corTemp = str(input('Cor: '))

        veiculoTemp = Veiculo(marcaTemp, modeloTemp, versaoTemp, motorTemp, corTemp)

        self.lista.append(veiculoTemp)


    def showVeiculos(self):
        v = 0
        for cliente in self.lista:
            v = v + 1
            print(f"{v} - {cliente}")


    def editVeiculo(self):
        self.showVeiculos()
        id = int(input('Numero do Veiculo a Ser Editado: '))
        id -= 1
        newMarca = str(input('Marca do Modelo: '))
        newModelo = str(input('Modelo do Veiculo: '))
        newVersao = str(input('Versao do Veiculo: '))
        newMotor = str(input('Motor do Veiculo: '))
        newCor = str(input('Cor do Veiculo: '))

        # self.lista[id].setVeiculo(newMarca, newModelo, newVersao, newMotor, newCor)
        temp = self.lista[id]
        temp.setCliente(newMarca, newModelo, newVersao, newMotor, newCor)


    def delVeiculo(self):
        self.showClientes()
        id = int(input('Numero do Veiculo a ser Deletado: '))
        id -= 1
        del (self.lista[id])
