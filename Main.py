from ClasseOnibus import *
from ClasseParada import *
from ClasseMotorista import *
from ClasseFiscal import *
import time

DicOnibus = {}
DicParadas = {}
DicMotoristas = {}
DicFiscais = {}

DicEmpresa = {}



"__________________________________________"
"FUNÇÔES ÔNIBUS"

def CriandoOnibus():
    Condicao = True
    while Condicao == True:
        NovoOnibus = Onibus()
        Linha = NovoOnibus.Linha
        if Linha in DicOnibus:
            print("Linha de ônibus já criada, coloque outra linha\n")
        else:
            DicOnibus[Linha] = NovoOnibus
            DicEmpresa[Linha] = [[], "", "N", 0]
            print(f"Ônibus de linha {Linha} criado com sucesso!\n\n")
            print("Voltando ao menu......\n\n")
            Condicao = False

def AssignandoAdicionando():
    while True:
        Linha = input("Qual é a linha do ônibus escolhido? (S para voltar)\n ")

        if Linha == "S":
            print("Voltando......\n\n")
            break

        if Linha not in DicOnibus:
            print("Linha de ônibus não existente, coloque outro\n")

        else:
            while True:
                NumeroMenuTres = int(input("O que deseja fazer?\n"
                                           "1- Assignar motorista ao ônibus\n"
                                           "2- Assignar fiscal ao ônibus\n"
                                           "3- Adicionar ponto de parada ao ônibus\n"
                                           "4- Voltar\n"))

                if NumeroMenuTres == 1:  # motorista
                    Condicao = True
                    while Condicao == True:
                        NomeMotorista = input("Qual o nome do motorista? (Para sair digite S)\n ")
                        if NomeMotorista == 'S':
                            print("Voltando......\n\n")
                            Condicao = False

                        elif NomeMotorista not in DicMotoristas:
                            print("Motorista não encontrado! Selecione um motorista existente"
                                  " ou crie um novo:\n")
                        else:
                            if DicMotoristas[NomeMotorista][1] == "N":
                                pass
                            else:
                                LinhaAntiga =  DicMotoristas[NomeMotorista][1]
                                print(f"Motorista assignado ao ônibus {LinhaAntiga}, mudando ele para a linha {Linha}\n")
                                DicEmpresa[LinhaAntiga][1] = ""
                            if DicEmpresa[Linha][1] != "":
                                AntigoMotorista = DicEmpresa[Linha][1]
                                DicMotoristas[AntigoMotorista][1] = "N"
                            DicMotoristas[NomeMotorista][1] = Linha
                            DicEmpresa[Linha][1] = NomeMotorista
                            Condicao = False
                            print(f"Motorista {NomeMotorista} assignado ao ônibus de linha {Linha}\n\n")
                            print("Voltando......\n\n")

                elif NumeroMenuTres == 2:  # fiscal
                    Condicao = True
                    while Condicao == True:
                        NomeFiscal = input("Qual o nome fiscal? (Para sair digite S)\n ")
                        if NomeFiscal == 'S':
                            print("Voltando......\n\n")
                            Condicao = False

                        elif NomeFiscal not in DicFiscais:
                            print("Fiscal não encontrado! Selecione um fiscal existente"
                                  " ou crie um novo:\n")
                        else:
                            if DicFiscais[NomeFiscal][1] == "N":
                                pass
                            else:
                                LinhaAntiga =  DicFiscais[NomeFiscal][1]
                                print(f"Fiscal assignado ao ônibus {LinhaAntiga}, mudando ele para a linha {Linha}\n")
                                DicEmpresa[LinhaAntiga][2] = "N"

                            if DicEmpresa[Linha][2] != "N":
                                AntigoFiscal = DicEmpresa[Linha][2]
                                DicFiscais[AntigoFiscal][1] = "N"

                            DicFiscais[NomeFiscal][1] = Linha
                            Condicao = False
                            DicEmpresa[Linha][2] = NomeFiscal
                            print(f"Fiscal {NomeFiscal} assignado ao ônibus de linha {Linha}\n\n")
                            print("Voltando......\n\n")

                elif NumeroMenuTres == 3:  # parada
                    Condicao = True
                    while Condicao == True:
                        NomeParada = input("Qual o nome da nova parada? (Para sair digite S)\n ")

                        if NomeParada == 'S':
                            Condicao = False
                            print("Voltando......\n\n")
                        elif NomeParada not in DicParadas:
                            print("Parada não encontrada! Selecione uma parada existente"
                                  " ou crie uma nova:\n")
                        elif NomeParada in DicEmpresa[Linha][0]:
                            print("Parada já se encontra dentro da rota desse ônibus. \n")
                        else:
                            Condicao = False
                            Lista = DicEmpresa[Linha][0]
                            Lista += [NomeParada]
                            DicEmpresa[Linha][0] = Lista
                            Tamanho = len(Lista)
                            DicEmpresa[Linha][3] = Tamanho * Passagem
                            LinhasdaParada = DicParadas[NomeParada][1]
                            LinhasdaParada += Linha
                            DicParadas[NomeParada][1] = LinhasdaParada
                            print(f'Parada {NomeParada} adicionada a rota do ônibus de linha {Linha}\n\n')
                            print("Voltando......\n\n")

                elif NumeroMenuTres == 4:
                    break

                else:
                    print("Número inexistente. Selecione um número na lista.\n")

def AlterarDadosOnibus():
    while True:
        Linha = input("Qual é a linha do ônibus?(Coloque S para voltar) \n")

        if Linha == "S":
            print("Voltando......\n\n")
            break

        if Linha not in DicOnibus:
            print("Linha de ônibus não existente, coloque outro\n")

        else:
            while True:
                OnibusM = DicOnibus[Linha]
                NumeroMenuQuatroUm = int(input("Qual você deseja?\n"
                                               "1- Alterar dados do ônibus\n"
                                               "2- Alterar rota do ônibus\n"
                                               "3- Voltar \n"))
                if NumeroMenuQuatroUm == 1:
                    while True:
                        NumeroMenuQuatro = int(input("Qual você deseja?\n"
                                                     "1- Linha\n"
                                                     "2- Cor\n"
                                                     "3- Quantidade de Bancos\n"
                                                     "4- Ano que foi fabricado\n"
                                                     "5- Voltar\n "))
                        if NumeroMenuQuatro == 1:
                            Condicao = True
                            while Condicao == True:
                                OnibusM.LinhaM()
                                LinhaNova = OnibusM.Linha
                                if LinhaNova in DicOnibus:
                                    print("Linha de ônibus já criada, coloque outra linha\n")
                                else:
                                    InformacoesAntigas = DicEmpresa[Linha]
                                    del DicEmpresa[Linha]
                                    DicEmpresa[LinhaNova] = InformacoesAntigas
                                    InformacoesAntigas = DicOnibus[Linha]
                                    del DicOnibus[Linha]
                                    DicOnibus[LinhaNova] = InformacoesAntigas
                                    Condicao = False
                                    print("Linha Alterada!\n")
                                    Linha = LinhaNova
                        elif NumeroMenuQuatro == 2:
                            OnibusM.CorM()
                            print("Cor do Onibus alterada!\n")
                        elif NumeroMenuQuatro == 3:
                            OnibusM.QuantBancosM()
                            print("Quantidade de banco alterada!\n")
                        elif NumeroMenuQuatro == 4:
                            OnibusM.AnoM()
                            print("Ano alterado!\n")
                        elif NumeroMenuQuatro == 5:
                            print("Voltando......\n\n")
                            break
                        else:
                            print("Número inexistente, selecione outro. \n\n")
                elif NumeroMenuQuatroUm == 2:
                    while True:
                        ListaAux = DicEmpresa[Linha][0]
                        print(ListaAux)
                        print("Selecione a parada que deseja modificar:\n")
                        for i in range(len(ListaAux)):
                            print(f'{i + 1}- {ListaAux[i]}')
                        NParada = int(input('Qual número? (S para sair)')) - 1

                        if NParada == "S":
                            break

                        NAcao = int(input("O que deseja fazer com essa parada?\n"
                                          "1- Deletar\n"
                                          "2- Mudar de lugar\n"
                                          "3- Acrescentar outra no lugar\n"
                                          "4- Volta\n "))

                        if NAcao == 1:
                            del ListaAux[NParada]
                            Tamanho =  len(ListaAux)
                            DicEmpresa[Linha][3] = Tamanho * Passagem

                        elif NAcao == 2:
                            ParadaSelecionada = ListaAux[NParada]
                            del ListaAux[NParada]
                            for i in range(len(ListaAux)):
                                print(f'{i + 1}- {ListaAux[i]}')
                            Posicao = int(input("Depois de qual deseja colocar? \n"
                                                "Caso queira que seja o primeiro, selecione -1\n"
                                                "")) + 1
                            ListaAux.insert(Posicao, ParadaSelecionada)
                            print("Realocado com sucesso!\n A ordem de paradas agora se encontra como:\n")
                            for i in range(len(ListaAux)):
                                print(f'{i + 1}- {ListaAux[i]}')

                        elif NAcao == 3:
                            Condicao = True
                            while Condicao == True:
                                NomeParada = input("Qual o nome da nova parada? (S para sair)\n ")
                                if NomeParada == "S":
                                    break
                                if NomeParada not in DicParadas:
                                    print("Parada não encontrada! Selecione uma parada existente"
                                          " ou crie uma nova:\n")
                                else:
                                    if NomeParada in ListaAux:
                                        print("Parada escolhida ja se encontra na rota desse ônibus! Selecione outra\n")
                                    else:
                                        Condicao = False
                                        print(f"Nova parada adicionada na posição da antiga no ônibus de {Linha}\n")
                                        ListaAux[NParada] = NomeParada

                        elif NAcao == 4:
                            print("Voltando......\n\n")
                            break

                        else:
                            print("Número escolhido não existe! Selecione um número da lista\n")

                        DicEmpresa[Linha][0] = ListaAux
                elif NumeroMenuQuatroUm == 3:
                    print("Voltando......\n\n")
                    break
                else:
                    print("Número escolhido não existe! Selecione um número da lista\n")

def DeletarOnibus():
    Linha = input("Qual é a linha do ônibus que deseja deletar?\n ")
    ListaParadas, NomeMoto, NomeFiscal = DicEmpresa[Linha][0], DicEmpresa[Linha][1], DicEmpresa[Linha][2]
    for i in ListaParadas:
        for j in range(len(DicParadas[i][1])):
            if Linha == DicParadas[i][1][j]:
                ListaAux = DicParadas[i][1]
                del ListaAux[j]
                DicParadas[i][1] = ListaAux
    if NomeMoto =="":
        pass
    else:
        DicMotoristas[NomeMoto][1] = ""
    if NomeFiscal =="N":
        pass
    else:
        DicFiscais[NomeFiscal][1] = "N"
    del DicOnibus[Linha],
    del DicEmpresa[Linha]
    print("Onibus deletado e retirado de todo os sistema!\n")
    print("Voltando ao menu......\n\n")


"__________________________________________"
"FUNÇÔES PARADAS"

def CriandoParada():
    Condicao = True
    while Condicao == True:
        NovaParada = Parada()
        Nome = NovaParada.Nome
        if Nome in DicParadas:
            print("Parada com nome já existente, coloque outro nome\n")
        else:
            DicParadas[Nome] = [NovaParada,[]]
            print(f"Parada {Nome} criada com sucesso!\n")
            Condicao = False
            print("Voltando ao menu......\n\n")

def AlterarDadosParada():
    while True:
        Nome = input("Qual é o nome da parada que deseja modificar? (Para sair digite S)\n ")

        if Nome == "S":
            print("Voltando.....\n\n")
            break

        if Nome not in DicParadas:
            print("Parada não existente, coloque outra\n")

        else:
            ParadaM = DicParadas[Nome][0]
            NumeroMenuQuatro = int(input("Qual você deseja?\n"
                                         "1- Nome\n"
                                         "2- Rua\n"
                                         "3- Bairro\n"
                                         "4- Cidade\n"
                                         "5- Estado\n"
                                         "6- Sair\n"))
            if NumeroMenuQuatro == 1:
                Condicao = True
                while Condicao == True:
                    ParadaM.NomeM()
                    NomeNovo = ParadaM.Nome
                    if NomeNovo in DicParadas:
                        print("Nome de parada já criada, coloque outro nome\n")
                    else:
                        Linhas = DicParadas[Nome][1]
                        if Linhas == []:
                            pass
                        else:
                            for i in Linhas:
                                LinhasOnibus = DicEmpresa[i][0]
                                for j in range(len(LinhasOnibus)):
                                    if Nome == LinhasOnibus[j]:
                                        LinhasOnibus[j] = NomeNovo
                                        print(f"Ponto de parada da linha {i} mudou de nome de {Nome} para {NomeNovo}\n")
                                DicEmpresa[i][0]= LinhasOnibus
                        InformacoesAntigas = DicParadas[Nome]
                        del DicParadas[Nome]
                        DicParadas[NomeNovo] = InformacoesAntigas
                    Condicao = False
                    print("Voltando......\n\n")
            elif NumeroMenuQuatro == 2:
                ParadaM.RuaM()
                print("Rua modificada com sucesso!\n")
            elif NumeroMenuQuatro == 3:
                ParadaM.BairroM()
                print("Bairro modificado com sucesso!\n")
            elif NumeroMenuQuatro == 4:
                ParadaM.CidadeM()
                print("Cidade modificada com sucesso!\n")
            elif NumeroMenuQuatro == 5:
                ParadaM.EstadoM()
                print("Estado modoficado com sucesso!\n")
            elif NumeroMenuQuatro == 6:
                print("Voltando......\n\n")
                break
            else:
                print("Número não encontrado! Selecione outro")

def DeletarParada():
    Nome = input("Qual é o nome da parada que deseja deletar?\n ")
    del DicParadas[Nome]
    Chaves = list(DicEmpresa.keys())
    for i in Chaves:
        ListaAux = DicEmpresa[i][0]
        for j in range(len(ListaAux)):
            if Nome == ListaAux[j]:
                del (ListaAux[j])
                DicEmpresa[i][0] = ListaAux
                Tamanho = len(ListaAux)
                DicEmpresa[i][3] = Tamanho * Passagem
    print("Parada deletada com sucesso!\n")
    print("Voltando....\n\n")

"__________________________________________"
"FUNÇÔES MOTORISTA"

def CriandoMotorista():
    Condicao = True
    while Condicao == True:
        NovoMotorista = Motorista()
        Nome = NovoMotorista.Nome
        if Nome in DicMotoristas:
            print("Motorista com o mesmo nome e sobrenome já criado, coloque outro\n")
        else:
            DicMotoristas[Nome] = [NovoMotorista, 'N']
            print(f"Motorista {Nome} criado com sucesso!\n")
            Condicao = False
            print("Voltando....\n\n")

def AlterarDadosMotorista():
    while True:
        Nome = input("Qual é o nome do motorista que deseja modificar? (Digite S para sair)\n ")
        if Nome == "S":
            print("Voltando.....\n\n")
            break
        if Nome not in DicMotoristas:
            print("Motorista não existente, coloque outro\n")

        else:
            MotoristaM = DicMotoristas[Nome][0]
            while True:
                NumeroMenuQuatro = int(input("Qual você deseja?\n"
                                             "1- Nome\n"
                                             "2- Idade\n"
                                             "3- Estado Civil\n"
                                             "4- Número da Carteira\n"
                                             "5- Voltar\n"))
                if NumeroMenuQuatro == 1:
                    Condicao = True
                    while Condicao == True:
                        MotoristaM.NomeM()
                        NomeNovo = MotoristaM.Nome
                        if NomeNovo in DicMotoristas:
                            print("Nome de motorista já criado, coloque outro nome\n")
                        else:
                            Linha = DicMotoristas[Nome][1]
                            if Linha == "N":
                                pass
                            else:
                                DicEmpresa[Linha][1] = NomeNovo
                            InformacoesAntigas = DicMotoristas[Nome]
                            del DicMotoristas[Nome]
                            DicMotoristas[NomeNovo] = InformacoesAntigas
                            print("Nome modificado com sucesso!\n")
                            Condicao = False
                elif NumeroMenuQuatro == 2:
                    MotoristaM.IdadeM()
                    print("Idade modificada com sucesso!\n")
                elif NumeroMenuQuatro == 3:
                    MotoristaM.EstadoCivilM()
                    print("Estado civil modificado com sucesso!\n")
                elif NumeroMenuQuatro == 4:
                    MotoristaM.NCarteirinhaM()
                    print("Número da Carteira modificada com sucesso!\n")
                elif NumeroMenuQuatro == 5:
                    print("Voltando.....\n\n")
                    break
                else:
                    print("Número inexistente. Escolha outro\n")

def DeletarMotorista():
    Nome = input("Qual é o nome do motorista que deseja deletar?\n ")
    del DicMotoristas[Nome]
    Chaves = list(DicEmpresa.keys())
    for i in Chaves:
        if Nome == DicEmpresa[i][1]:
            DicEmpresa[i][1] = ""
    print("Motorista deletado com sucesso!\n")
    print("Voltando....\n\n")

"__________________________________________"
"FUNÇÔES FISCAIS"

def CriandoFiscal():
    Condicao = True
    while Condicao == True:
        NovoFiscal = Fiscal()
        Nome = NovoFiscal.Nome
        if Nome in DicFiscais:
            print("Fiscal com o mesmo nome e sobrenome já criado, coloque outro\n")
        else:
            DicFiscais[Nome] = [NovoFiscal, 'N']
            print(f"Fiscal {Nome} criado com sucesso!\n")
            Condicao = False
            print("Voltando....\n\n")

def AlterarDadosFiscal():
    while True:
        Nome = input("Qual é o nome do fiscal que deseja modificar? (Digite S para sair)\n ")

        if Nome == "S":
            print("Voltando.....\n\n")
            break

        if Nome not in DicFiscais:
            print("Fiscal não existente, coloque outro\n")

        else:
            FiscalM = DicFiscais[Nome][0]
            while True:
                NumeroMenuQuatro = int(input("Qual você deseja?\n"
                                             "1- Nome\n"
                                             "2- Idade\n"
                                             "3- Estado Civil\n"
                                             "4- Número da Carteira\n"
                                             "5- Voltar \n"))
                if NumeroMenuQuatro == 1:
                    Condicao = True
                    while Condicao == True:
                        FiscalM.NomeM()
                        NomeNovo = FiscalM.Nome
                        if NomeNovo in DicFiscais:
                            print("Nome de fiscal já criado, coloque outro nome\n")
                        else:
                            Linha = DicFiscais[Nome][1]
                            if Linha == "N":
                                pass
                            else:
                                DicEmpresa[Linha] = str(NomeNovo)
                            InformacoesAntigas = DicFiscais[Nome]
                            del DicFiscais[Nome]
                            DicFiscais[NomeNovo] = InformacoesAntigas
                            Condicao = False
                            print("Nome modificado com sucesso!\n")
                elif NumeroMenuQuatro == 2:
                    FiscalM.IdadeM()
                    print("Idade modificada com sucesso!\n")
                elif NumeroMenuQuatro == 3:
                    FiscalM.EstadoCivilM()
                    print("Estado civil modificado com sucesso!\n")
                elif NumeroMenuQuatro == 4:
                    FiscalM.NCarteirinhaM()
                    print("Número da Carteira modificada com sucesso!\n")
                elif NumeroMenuQuatro ==5:
                    print("Voltando.....\n\n")
                    break
                else:
                    print("Número inexistente. Escolha outro\n")

def DeletarFiscal():
    Nome = input("Qual é o nome do fiscal que deseja deletar?\n ")
    del DicFiscais[Nome]
    Chaves = list(DicEmpresa.keys())
    for i in Chaves:
        if Nome == DicEmpresa[i][2]:
            DicEmpresa[i][2] = "Não"
    print("Fiscal deletado com sucesso!\n")
    print("Voltando....\n\n")


"___________________________________________"
"FUNÇÃO MAIN"

def main():
    global Passagem
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n")
    print("    .---------------------------.\n"
          "   /,--..---..---..---..---..--. `.\n"
          "  //___||___||___||___||___||___\_|\n"
          "  [j__ ######################## [_|\n"
          "     \============================|\n"
          '  .==|  |"""||"""||"""||"""| |"""||\n'
          ' /======"---""---""---""---"=|  =||\n'
          " |____    []*          ____  | ==||\n"
          ' //  \\               //  \\ |===||\n'
          ' "\__/"---------------"\__/"-+---+\n\n')
    time.sleep(0.5)
    print("Bem vindo ao sistema de gerenciamento de rede de transportes!")
    Passagem = float(input("Defina um valor em real para o preço da passagem por parada\n"
                           ""))
    while True:
        time.sleep(0.5)

        NumeroMenuUm= int(input("\n_________________________________________________\n"
                                "Selecione um número para a ação que deseja fazer \n"
                                 "1- Criar\n"
                                 "2- Mostrar\n"
                                 "3- Assignar ou Adicionar\n"
                                 "4- Alterar dados\n"
                                 "5- Deletar\n"
                                 "6- Sair\n"))
        print("_________________________________________________\n")
        if NumeroMenuUm not in [3,6]:
            NumeroMenuDois = int(input("Deseja fazer essa ação com qual?\n"  # Definir um nome
                                       "1- Ônibus\n"
                                       "2- Ponto de Parada\n"
                                       "3- Motorista\n"
                                       "4- Fiscal\n"))
        elif NumeroMenuUm== 3:
            NumeroMenuDois= 1

        elif NumeroMenuUm== 6:
            print("Obrigado por usar! Até logo!")
            print("Saindo do programa.........")
            break

        else:
            pass


        if NumeroMenuDois== 1: #Onibus
            if NumeroMenuUm == 1: CriandoOnibus()

            elif NumeroMenuUm == 2:
                for i in DicOnibus.keys():
                    Rotas = DicEmpresa[i][0]
                    NomeMoto = DicEmpresa[i][1]
                    NomeFiscal = DicEmpresa[i][2]
                    Preco = DicEmpresa[i][3]
                    print(DicOnibus[i])
                    if NomeMoto =="":
                        NomeMoto = 'não tem'
                    if NomeFiscal == "N":
                        NomeFiscal = 'não tem'
                    Rotas = ", ".join(Rotas)
                    if Rotas == "":
                        Rotas = 0
                    print(f"Com rota {Rotas}, Motorista {NomeMoto}, Fiscal {NomeFiscal} e preço da passagem {Preco}\n")

            elif NumeroMenuUm == 3: AssignandoAdicionando()

            elif NumeroMenuUm == 4: AlterarDadosOnibus()

            elif NumeroMenuUm == 5: DeletarOnibus()


        elif NumeroMenuDois== 2: #Parada
            if NumeroMenuUm== 1: CriandoParada()

            elif NumeroMenuUm== 2:
                for i in DicParadas.keys():
                    print(DicParadas[i][0])
                    OnibusPassa = DicParadas[i][1]
                    OnibusPassa = ", ".join(OnibusPassa)
                    if OnibusPassa == "":
                        OnibusPassa = "nenhum"
                    print(f'Os ônibus que passam por essa linha é {OnibusPassa}\n')

            elif NumeroMenuUm == 4: AlterarDadosParada()

            elif NumeroMenuUm == 5: DeletarParada()


        elif NumeroMenuDois == 3: #Motorista
            if NumeroMenuUm == 1: CriandoMotorista()

            elif NumeroMenuUm == 2:
                for i in DicMotoristas.keys():
                    print(DicMotoristas[i][0])
                    if DicMotoristas[i][1] == "N":
                        print("Esse motorista não está alocado a um ônibus\n")
                    else:
                        print(f'O ônibus que esse motorista dirige é {DicMotoristas[i][1]}\n')

            elif NumeroMenuUm == 4: AlterarDadosMotorista()

            elif NumeroMenuUm == 5: DeletarMotorista()


        elif NumeroMenuDois == 4: #Fiscal
            if NumeroMenuUm == 1: CriandoFiscal()

            elif NumeroMenuUm == 2:
                for i in DicFiscais.keys():
                    print(DicFiscais[i][0])
                    if DicFiscais[i][1] == 'N':
                        print("Esse fiscal não está alocado a nenhum ônibus\n")
                    else:
                        print(f'O ônibus que esse fiscal trabalha é {DicFiscais[i][1]}\n')

            elif NumeroMenuUm == 4: AlterarDadosFiscal()

            elif NumeroMenuUm == 5: DeletarFiscal()


        else:
            print("Número não está na lista. Selecione outro.")

if __name__ == "__main__":
    main()



