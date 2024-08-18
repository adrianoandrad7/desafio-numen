from enum import Enum, auto
import random
import os
import time

class Resultado(Enum):
    VITORIA = auto()
    DERROTA = auto()
    EMPATE = auto()

class Escolha(Enum):
    PEDRA = 1
    PAPEL = 2
    TESOURA = 3
    
class Opcoes(Enum):
    MELHOR_DE_3 = 1
    MELHOR_DE_5 = 2
    MELHOR_DE_7 = 3

class Jokenpo:
    
    def __init__(self):
        self.numero_de_partidas = 0
        self.numero_de_vitorias = 0
        self.numero_de_derrotas = 0
        self.numero_de_empates = 0
        self.nome_jogador = ""
        
        self.resultados = {
            (Escolha.PEDRA, Escolha.PEDRA): Resultado.EMPATE,
            (Escolha.PEDRA, Escolha.PAPEL): Resultado.DERROTA,
            (Escolha.PEDRA, Escolha.TESOURA): Resultado.VITORIA,
            (Escolha.PAPEL, Escolha.PEDRA): Resultado.VITORIA,
            (Escolha.PAPEL, Escolha.PAPEL): Resultado.EMPATE,
            (Escolha.PAPEL, Escolha.TESOURA): Resultado.DERROTA,
            (Escolha.TESOURA, Escolha.PEDRA): Resultado.DERROTA,
            (Escolha.TESOURA, Escolha.PAPEL): Resultado.VITORIA,
            (Escolha.TESOURA, Escolha.TESOURA): Resultado.EMPATE
        }

    def calcular_percentual(self, numero_de_ocorrencias):
        if self.numero_de_partidas == 0:
            return 0.0
        return (numero_de_ocorrencias / self.numero_de_partidas) * 100

    def verificar_resultado_da_partida(self, opcao_jogador, opcao_maquina):
        
        resultado = self.resultados[(opcao_jogador, opcao_maquina)]

        if resultado == Resultado.VITORIA:
            self.numero_de_vitorias += 1
        elif resultado == Resultado.DERROTA:
            self.numero_de_derrotas  += 1
        elif resultado == Resultado.EMPATE:
            self.numero_de_empates += 1

        return resultado

    def exibir_placar(self, resultado):
        
        print("--------------------------------------------------")
        print(f"PLACAR - {self.nome_jogador}: {self.numero_de_vitorias} X  MAQUINA: {self.numero_de_derrotas}")
        print(f"Número de vitórias: {self.numero_de_vitorias}")
        print(f"Número de derrotas: {self.numero_de_derrotas}")
        print(f"Número de empates: {self.numero_de_empates}")
        
        if resultado == Resultado.VITORIA:
            print("--------------------------------------------------")
            print("Você venceu - Boa escolha!!")
        elif resultado == Resultado.DERROTA:
            print("--------------------------------------------------")
            print("Você perdeu, tente outra estratégia na próxima!")
        else:
            print("--------------------------------------------------")
            print("Empate! melhore sua estratégia!")
        print("--------------------------------------------------")

    def escolher_opcao_jogador(self):
        escolhas = {"pedra": Escolha.PEDRA, "papel": Escolha.PAPEL, "tesoura": Escolha.TESOURA}
        while True:
            print("--------------------------------------------------")
            print("Digite uma opção: Pedra - Papel - Tesoura: ", end='')
            escolha = input().strip().lower()
            print("--------------------------------------------------")
            self.limpar_tela()
            if escolha in escolhas:
                return escolhas[escolha]
            else:
                print("Entrada inválida. Por favor, escolha uma opção válida: Pedra - Papel - Tesoura")

    def escolher_opcao_aleatoria_maquina(self):
        opcao = random.choice([Escolha.PEDRA, Escolha.PAPEL, Escolha.TESOURA])
        return opcao

    def exibir_escolhas(self, escolha_jogador, escolha_maquina):
        escolhas = {
            Escolha.PEDRA: "Pedra",
            Escolha.PAPEL: "Papel",
            Escolha.TESOURA: "Tesoura"
        }
        
        print("--------------------------------------------------")
        print(f"Você escolheu: {escolhas[escolha_jogador]}")
        time.sleep(1)
        print(f"Máquina escolheu: {escolhas[escolha_maquina]}")
            
    def exibir_estatisticas(self):
        titulo = "Estatísticas do jogo"
        print("--------------------------------------------------")
        estatisticas = [
            f"Número de partidas: {self.numero_de_partidas}\n",
            f"Percentual de vitórias: {self.calcular_percentual(self.numero_de_vitorias):.2f}%\n",
            f"Percentual de derrotas: {self.calcular_percentual(self.numero_de_derrotas):.2f}%\n",
            f"Percentual de empates: {self.calcular_percentual(self.numero_de_empates):.2f}%\n"
        ]
        
        print(titulo)
        print("--------------------------------------------------")
        for estatistica in estatisticas:
            print(estatistica, end='')
        print("--------------------------------------------------")

    def exibir_resultado(self, resultado):
        if resultado == Resultado.VITORIA:
            print("Boa escolha!")
        elif resultado == Resultado.DERROTA:
            print("Tente outra estratégia na próxima!")
        else:
            print("Empate! Vamos para a próxima!")

    def perguntar_continuacao(self):
        while True:
            print("Deseja continuar o jogo até a ultima partida? (sim/não): ", end='')
            resposta = input().strip().lower()
            if resposta in ["sim", "não","nao"]:
                return resposta == "sim"
            else:
                print("Entrada inválida. Por favor, responda com 'sim' ou 'não'.")
                
    def limpar_tela(self):
        if os.name == 'nt':#Windows
            os.system('cls')
        else:#Linux
            os.system('clear')
            
    def perguntar_opcao_jogo(self):
        print("Escolha o modo do jogo: ")
        print("Opção 1 Melhor de 3")
        print("Opção 2 Melhor de 5")
        print("Opção 3 Melhor de 7")
        print("Opção escolhida: ", end='')

        while True:
            try:
                escolha = int(input())
                if escolha in [opcao.value for opcao in Opcoes]:
                    return Opcoes(escolha)
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida: 1 Melhor de 3, 2 Melhor de 5, 3 Melhor de 7: ", end='')
            except ValueError:
                print("Entrada inválida. Por favor, escolha uma opção válida: 1 Melhor de 3, 2 Melhor de 5, 3 Melhor de 7: ", end='')
    
    def exibir_resultado_final(self):
        print(f"PLACAR - {self.nome_jogador} {self.numero_de_vitorias} X MAQUINA {self.numero_de_derrotas}")
        if self.numero_de_vitorias > self.numero_de_derrotas:
            print("--------------------------------------------------")
            print("Jogo Finalizado - Você Venceu o Jogo!!")
        elif self.numero_de_derrotas > self.numero_de_vitorias:
            print("--------------------------------------------------")
            print("Jogo Finalizado - A Máquina Venceu o Jogo!!")
        else:
            print("--------------------------------------------------")
            print("Jogo Finalizado  - O Jogo Terminou Empatado!") 
            
    def verifica_fim_jogo(self, opcao_jogo, numero_de_vitorias, numero_de_derrotas):
        
        fim_jogo = False 
        
        if opcao_jogo == Opcoes.MELHOR_DE_3:
            if numero_de_vitorias == 2 or numero_de_derrotas == 2:
                fim_jogo = True
        elif opcao_jogo == Opcoes.MELHOR_DE_5:
            if numero_de_vitorias == 3 or numero_de_derrotas == 3:
                fim_jogo = True
        elif opcao_jogo == Opcoes.MELHOR_DE_7:
            if numero_de_vitorias == 4 or numero_de_derrotas == 4:
                fim_jogo = True

        return fim_jogo
    
    def iniciar_jogo(self):
        print("----------------------------------------")
        print("---------------JOKENPO------------------")
        print("----------------------------------------")

        self.nome_jogador = input("Digite seu nome: ")

        while True: 
            opcao_jogo = self.perguntar_opcao_jogo()
            
            self.numero_de_vitorias = 0
            self.numero_de_derrotas = 0
            self.numero_de_empates = 0
            
            while True:
                opcao_jogador = self.escolher_opcao_jogador()
                opcao_maquina = self.escolher_opcao_aleatoria_maquina()
                self.numero_de_partidas += 1

                self.exibir_escolhas(opcao_jogador, opcao_maquina)
                resultado = self.verificar_resultado_da_partida(opcao_jogador, opcao_maquina)
                self.exibir_placar(resultado)

                # Verifica se o jogo já foi vencido ou perdido, ignorando empates
                ja_venceu = self.verifica_fim_jogo(opcao_jogo, self.numero_de_vitorias, self.numero_de_derrotas)
                
                if ja_venceu:
                    time.sleep(5)
                    break
                
                if not self.perguntar_continuacao():
                    break

            self.limpar_tela()
            self.exibir_resultado_final()
            self.exibir_estatisticas()

            print("Deseja jogar novamente? (sim/não): ", end='')
            resposta = input().strip().lower()
            if resposta != "sim":
                print("Obrigado por jogar! Até a próxima!")
                break  

if __name__ == "__main__":
    jogo = Jokenpo()
    jogo.iniciar_jogo()
