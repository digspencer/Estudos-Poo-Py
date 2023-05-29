class Carro:
    def __init__(self, marca, modelo, cor, combustivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel

        self.desligar = False
        self.ligar = True
        self.velocidade = 0

    def ligarCarro(self):
        if self.ligar:
            print('Você ligou o {}'.format(self.modelo))

    def acelerar(self):
        if self.ligar and self.velocidade >= 0:
            self.velocidade += 1
            print(f'O {self.modelo} está a {self.velocidade} Km/h.')

    def frear(self):
        if self.ligar and self.velocidade >= 1:
            self.velocidade -= 1
            print(f'Você freiou o {self.modelo} e ele agora está em {self.velocidade} Km/h.')
        elif self.ligar and self.velocidade <= 0:
            print(f'Não há como frear {self.modelo} porque ele já está parado.')

    def ligar_esguinchador(self):
        if self.ligar and self.velocidade >= 1:
            print('O esguinchador está ligado, diminua a velocidade.')
        else:
            print('Diminua a velocidade para ligar o esguinchador.')
    def desligar_carro(self):
        self.desligar = True
        self.ligar = False
        print('Você desligou o carro.')