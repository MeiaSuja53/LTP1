def fazer_pergunta(pergunta):
    resposta = input(pergunta + " (Sim/Não): ").strip().lower()
    while resposta not in ['sim', 'não']:
        print("Por favor, responda com 'Sim' ou 'Não'.")
        resposta = input(pergunta + " (Sim/Não): ").strip().lower()
    return resposta == 'sim'

def main():
    print("Responde às perguntas aí!!!!:")
    
    respostas = []
    respostas.append(fazer_pergunta("Telefonou para a vítima?"))
    respostas.append(fazer_pergunta("Esteve no local do crime?"))
    respostas.append(fazer_pergunta("Mora perto da vítima?"))
    respostas.append(fazer_pergunta("Devia o malote neh?"))
    respostas.append(fazer_pergunta("Trabalhou com o assassino?"))
    
    num_respostas_positivas = sum(respostas)
    
    resultado = classificar_participacao(num_respostas_positivas)
    
    print(f"\nClassificação: {resultado}")


def classificar_participacao(respostas_positivas):
    if respostas_positivas == 5:
        return "Sai que tu pode ser o assassino"
    elif 3 <= respostas_positivas <= 4:
        return "Cúmplice?👀"
    elif respostas_positivas == 2:
        return "Suspeito tu ehnn"
    else:
        return "Inocente? ou está mentindo?"


if __name__ == "__main__":
    main()