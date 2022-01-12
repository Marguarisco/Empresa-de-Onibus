class Onibus:
    def __init__(self):
        self._Linha = input("Qual vai ser a linha do novo ônibus? ")
        self.Cor = input("Qual é a cor dele? ")
        self.QuantBancos = input("Quantos lugares para sentar ele tem? ")
        self.Ano = input("Em que ano ele foi fabricado? ")

    def __str__(self):
        return f"Ônibus de cor {self.Cor} cuja linha é a {self.Linha}, fabricado em {self.Ano} " \
               f"e que possui {self.QuantBancos} lugares."

    @property
    def Linha(self):
        return self._Linha

    def LinhaM(self):
        self._Linha = input("Qual será a nova linha? ")

    def CorM(self):
        self.Cor = input("Qual será a nova cor? ")

    def QuantBancosM(self):
        self.QuantBancos = input("Qual será a nova quantidade de bancos? ")

    def AnoM(self):
        self.Ano = input("Qual será o novo ano do ônibus? ")
