class JogoDaVelha:

    tabuleiro = {'7': ' ', '8': ' ','9': ' ',
                 '4': ' ', '5': ' ','6': ' ',
                 '1': ' ', '2': ' ','3': ' '}
    
    def __init__(self,jogador='X'):
        self.turno = jogador

    
    def Exibirtabuleiro(self):
        print("┌───┬───┬───┐")
        print(f'| {self.tabuleiro['7']} | {self.tabuleiro['8']} | {self.tabuleiro['9']} |')
        print('|───|───|───|')
        print(f'| {self.tabuleiro['4']} | {self.tabuleiro['5']} | {self.tabuleiro['6']} |')
        print('|───|───|───|')
        print(f'| {self.tabuleiro['1']} | {self.tabuleiro['2']} | {self.tabuleiro['3']} |')
        print("└───┴───┴───┘")
    
    def ChecarGanhador(self):
        if self.tabuleiro['7'] == self.tabuleiro['8'] == self.tabuleiro['9'] != ' ':
            return self.tabuleiro['7']
        elif self.tabuleiro['4'] == self.tabuleiro['5'] == self.tabuleiro['6'] != ' ':
            return self.tabuleiro['4']
        elif self.tabuleiro['1'] == self.tabuleiro['2'] == self.tabuleiro['3'] != ' ':
            return self.tabuleiro['1']
        
        elif self.tabuleiro['7'] == self.tabuleiro['4'] == self.tabuleiro['1'] != ' ':
            return self.tabuleiro['7']
        elif self.tabuleiro['8'] == self.tabuleiro['5'] == self.tabuleiro['2'] != ' ':
            return self.tabuleiro['8']
        elif self.tabuleiro['9'] == self.tabuleiro['6'] == self.tabuleiro['3'] != ' ':
            return self.tabuleiro['9']
        
        elif self.tabuleiro['7'] == self.tabuleiro['5'] == self.tabuleiro['3'] != ' ':
            return self.tabuleiro['7']
        elif self.tabuleiro['1'] == self.tabuleiro['5'] == self.tabuleiro['9'] != ' ':
            return self.tabuleiro['1']
    
    def verificarJogada(self,jogada):
        if j in jogo.tabuleiro.keys():
            if self.tabuleiro[jogada] == ' ':
                return True
        return False
    
    def mudarTurno(self):
        
        if self.turno == 'X':
            self.turno = 'O'
        else:
            self.turno = 'X'
    


jogo = JogoDaVelha()   
while True:
    
    jogo.Exibirtabuleiro()
    estado = jogo.ChecarGanhador()
    if estado == 'X':
        print(f'O jogador X ganhou')
        break
    elif estado == 'O':
        print(f'O jogador O ganhou')
        break

    while True:
        j = input('Qual sua jogada?: ')
        if jogo.verificarJogada(j): # Se a jogada for válida...
                break # Encerra o loop
        else:
            print(f"jogada do {jogo.turno} inválida, jogue novamente.")
    jogo.tabuleiro[j] = jogo.turno
    jogo.mudarTurno()