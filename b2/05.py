class Carro:
    def __init__(self, consumo_km_por_litro):
        self.consumo_km_por_litro = consumo_km_por_litro
        self.nivel_combustivel = 0

    def andar(self, distancia):
        consumo = distancia / self.consumo_km_por_litro
        if consumo <= self.nivel_combustivel:
            self.nivel_combustivel -= consumo
            print(f"Carro percorreu {distancia} km.")
        else:
            print("Opaaa: Menos de 10 de gasoza eu não ando,poh.")

    def obter_gasolina(self):
        return self.nivel_combustivel

    def adicionar_gasolina(self, quantidade):
        self.nivel_combustivel += quantidade
        print(f"Foram adicionados {quantidade} litros de gasoza. Da pra ir até a esquina com esse nível de gasoza: {self.nivel_combustivel} .")

def main():
    consumo_km_por_litro = float(input("Informe o consumo do carro em km por litro: "))
    carro = Carro(consumo_km_por_litro)

    while True:
        print("\nEscolha uma opção aí tio:")
        print("1. Andar")
        print("2. Verificar nível de gasoza")
        print("3. Abastecer")
        print("4. Sair")

        opcao = input("Escolha uma das opções: ")

        if opcao == "1":
            distancia = float(input("Vai andar quanto ai em km? "))
            carro.andar(distancia)
        elif opcao == "2":
            print(f"Nível atual de gasoza: {carro.obter_gasolina()} litros.")
        elif opcao == "3":
            quantidade = float(input("Tá caro né? vai abastecer: "))
            carro.adicionar_gasolina(quantidade)
        elif opcao == "4":
            print("Saindo do programa, eheheheheheeee.")
            break
        else:
            print("Opção inválida. faz o L.")

if __name__ == "__main__":
    main()