class Camera:
    def __init__(self, nome, filmando = False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'A Câmera {self.nome} já está filmando.')
            return
        
        print(f'{self.nome} está filmando')
        self.filmando = True
    
    def fotografar(self):
        if self.filmando:
            print('Não é possível fotografar filmando.')
        else:
            print('Foto registrada.')

    def desligar(self):
        if self.filmando:
            print('A camera está desligando.')
            self.filmando = False

c1 = Camera ('Canon')
c2 = Camera ('Sony')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.desligar()
c1.fotografar()