import sqlite3

class Agenda:
    def __init__(self, db_path='agenda.db'):
        self.conn = sqlite3.connect(db_path)
        self.criar_tabela_contatos()

    def criar_tabela_contatos(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contatos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                telefone TEXT
            )
        ''')
        self.conn.commit()

    def adicionar_contato(self, nome, telefone):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO contatos (nome, telefone) VALUES (?, ?)', (nome, telefone))
        self.conn.commit()
        print(f"Contato {nome} adicionado com sucesso.")

    def remover_contato(self, nome):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM contatos WHERE nome = ?', (nome,))
        self.conn.commit()
        print(f"Ue ja enjoou do(a) {nome}, blz então eu removi.")

    def exibir_lista_contatos(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM contatos')
        contatos = cursor.fetchall()
        if not contatos:
            print("Você não tem amigos!.")
        else:
            print("Pega a lista de Contatos dos cornos:")
            for contato in contatos:
                print(f"{contato[0]}. Nome: {contato[1]}, Telefone: {contato[2]}")

    def __del__(self):
        self.conn.close()

def menu():
    print("\nMenu:")
    print("1. Visualizar Lista de Contatinhos")
    print("2. Adicionar Contatinhos rsrs")
    print("3. Remover os otarios")
    print("4. Sair")

if __name__ == "__main__":
    agenda = Agenda()

    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            agenda.exibir_lista_contatos()
        elif escolha == "2":
            nome = input("Digite o nome do contatinho, masss se eu fosse tu colocava apelido rsrs: ")
            telefone = input("Digite o telefone do contatinho: ")
            agenda.adicionar_contato(nome, telefone)
        elif escolha == "3":
            nome = input("Digite o nome do contatinho que vc deseja remover: ")
            agenda.remover_contato(nome)
        elif escolha == "4":
            print("Saindo do programa. Rlx! vou contar pra tua muier rsrs")
            break
        else:
            print("Opção inválida. faça o L, bem lentamente.")