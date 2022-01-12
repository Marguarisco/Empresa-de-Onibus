class Parada:
    def __init__(self):
        self._Nome = input("Qual vai ser o nome da nova parada? ")
        self.Rua = input("Em que rua ela vai estar localizada? ")
        self.Bairro = input("E em que bairro? ")
        self.Cidade = input("Em que cidade? ")
        self.Estado = input("Em que estado? ")

    def __str__(self):
        return f"Parada chamada de {self.Nome}, localizado na rua {self.Rua}, bairro {self.Bairro} da " \
               f"cidade {self.Cidade} no estado {self.Estado}."

    @property
    def Nome(self):
        return self._Nome

    def NomeM(self):
        self._Nome = input("Qual será o novo nome? ")

    def RuaM(self):
        self._Rua = input("Qual será a nova rua? ")

    def BairroM(self):
        self._Bairro = input("Qual será o novo bairro? ")

    def CidadeM(self):
        self._Cidade = input("Qual será a nova cidade? ")

    def EstadoM(self):
        self._Estado = input("Qual será o novo estado? ")
