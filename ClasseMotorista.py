class Motorista:
    def __init__(self):
        self._Nome = input("Qual o nome e sobrenome da nova pessoa? ")
        self.Idade = input("Qual a idade dela? ")
        self.EstadoCivil = input("Qual o estado civil dela? ")
        self.NCarteirinha = input("Qual o numero da carteirinha dela? ")

    def __str__(self):
        return f"Motorista {self.Nome} de N° de carteira {self.NCarteirinha}, possui {self.Idade} " \
               f" e é {self.EstadoCivil}."

    @property
    def Nome(self):
        return self._Nome

    def NomeM(self):
        self._Nome = input("Qual será o novo nome e sobrenome? ")

    def IdadeM(self):
        self.Idade = input("Qual será a nova idade? ")

    def EstadoCivilM(self):
        self.EstadoCivil = input("Qual é o novo estado civil? ")

    def NCarteirinhaM(self):
        self.NCarteirinha = input("Qual é o novo N° da carteira? ")
