import random

class Jokenpo:
    def __init__(self):
        self.opcoes = ["Pedra", "Papel", "Tesoura"]

    def opcao(self):
        escolha_p1 = input("P1 faça uma escolha entre Papel, Pedra ou Tesoura: ").capitalize()
        if escolha_p1 not in self.opcoes:
            print("Opção inválida, Digite Papel, Pedra ou Tesoura: ")
            return self.opcao()
        return escolha_p1

    def escolha_p2(self):

        return random.choice(self.opcoes)

    def vencedor(self, jogador, computador):

        if jogador == computador:
            return 'Empate'
        elif (jogador == "Pedra" and computador == "Tesoura") or \
             (jogador == "Papel" and computador == "Pedra") or \
             (jogador == "Tesoura" and computador == "Papel"):
            return "P1 venceu! :)"
        else:
            return "P2 venceu!"

    def Start(self):

        jogador = self.opcao()
        P2 = self.escolha_p2()
        print(f'P1 escolheu: {jogador}')
        print(f'P2 escolheu: {P2}')
        resultado = self.vencedor(jogador, P2)
        print(resultado)

#j = Jokenpo()
#j.Start()
