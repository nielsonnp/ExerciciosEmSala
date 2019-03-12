class CarroDePasseio:
    def __init__(self, motor_inicial, cor, modelo, ano):
        self.motor = motor_inicial
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return "Modelo: {}, Ano: {}, Cor: {}, Motor: {}".format(self.modelo,self.ano,self.cor,self.motor)

    def get_motor(self):
        return self.motor

    def set_motor(self, novo_motor):
        self.motor = novo_motor

motor_inicial = input("Digite a potência do motor: ")
cor = input("Digite a cor: ")
modelo = input("Digite o modelo: ")
ano = input("Digite o ano: ")

c1 = CarroDePasseio(motor_inicial, cor, modelo, ano)
print(c1)
