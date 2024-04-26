class Pessoa:
    def __init__(self, nome, sexo, cpf, ativo):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.ativo = ativo

    def desativar(self):
        self.ativo = False
        print("A pessoa foi desativada com sucesso")

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

if __name__ == "__main__":
    pessoa1 = Pessoa("Luiza", "F", "I L0ve YOU", True)
    pessoa1.desativar()
    pessoa1.ativo = True
    print(pessoa1.ativo)

    pessoa1.set_nome("Sunshine")
    print(pessoa1.get_nome())

    pessoa1.nome = "Desligado"
    print(pessoa1.nome)

