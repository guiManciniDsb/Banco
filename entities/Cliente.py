#arquivo para classe cliente
class Cliente:
    def __init__(self, cpf, nome, idade, email):
        self.cpf=cpf
        self.nome=nome
        self.idade=idade
        self.email=email
    
    def __str__(self):
        return f"Nome: {self.nome} | Cpf: {self.cpf} | Idade: {self.idade} | Email: {self.email}"