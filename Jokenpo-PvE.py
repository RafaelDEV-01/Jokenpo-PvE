import random

class Jokenpo:
    def __init__(self):
        self.opcoes = ["Pedra", "Papel", "Tesoura"]

    def opcao(self):
        escolha_p1 = input("Player faça uma escolha entre Papel, Pedra ou Tesoura: ").capitalize()
        if escolha_p1 not in self.opcoes:
            print("Opção inválida, Digite Papel, Pedra ou Tesoura: ")
            return self.opcao()
        return escolha_p1

    def escolha_p2(self):

        return random.choice(self.opcoes)

    def vencedor(self, player, bot):

        if player == bot:
            return 'Empate!'
        elif (player == "Pedra" and bot == "Tesoura") or \
             (player == "Papel" and bot == "Pedra") or \
             (player == "Tesoura" and bot == "Papel"):
            return "Player venceu!"
        else:
            return "Bot venceu!"

    def Start(self):

        jogador = self.opcao()
        P2 = self.escolha_p2()
        print(f'Player escolheu: {jogador}')
        print(f'Bot escolheu: {P2}')
        resultado = self.vencedor(jogador, P2)
        print(resultado)

s = Jokenpo()
s.Start()
