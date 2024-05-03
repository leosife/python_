class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando


    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JA esta filmando')
            return
        
        print(f'{self.nome} esta filmando')
        self.filmando = True

    def fotografar(self):
        if self.filmando:
            print('A camera não pode fotografar enquanto filma')
            return
        
        print(f'{self.nome} esta fotografando')

    def parar_filmar(self):
        if not self.filmando:
            print('A camera não esta filmando')
            return


        self.filmando = False
        print('A camera parou de filmar')



c1 = Camera('Canon')
c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()
c1.filmar()
c1.parar_filmar()
c1.parar_filmar()