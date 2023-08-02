import os
class AUV:
    def __init__(self, num_thrusters, name, sensors, year, team_size):
        self.num_thrusters = num_thrusters
        self.name = name
        self.sensors = sensors
        self.year = year
        self.team_size = team_size

    def showTable(AUVs):    # método que mostra os AUVs em uma tabela
        print("-------------------------------------------------------------------------------------------------------------------")
        print("{:<8} {:<15} {:<10} {:<50} {:<20}".format('Nome','Num. de Thr.','Ano', 'Sensores','Tamanho do Time'))
        for k in AUVs:
            sensores_print = ''.join(str(a + ', ') for a in k.sensors)
            print("{:<8} {:<15} {:<10} {:<50} {:<20}".format(k.name, k.num_thrusters, k.year, sensores_print, k.team_size)) #substituir 1 por k.sensores
        print("-------------------------------------------------------------------------------------------------------------------")

    def showIndiv(self):    # mostra os AUVs individualmente
        print("--------------------------------------------")
        print("Nome:", self.name)
        print("Sensores:", self.sensors)
        print("Ano de Fabricacao:", self.year)
        print("Numero de Thrusters:", self.num_thrusters)
        print("--------------------------------------------")

    def rankNewToOld(AUVs):     # ranqueia os AUVs do mais velho para o mais novo
        lista_decr = sorted(AUVs, key=lambda i: i.year , reverse=True)
        print("Lista por ano de fabricacao:")
        for i in lista_decr:
            print("----------------------------------------")
            print(f"Nome: {i.name}")
            print(f"Ano : {i.year}")
            print("----------------------------------------")

    def rankTeamSize(AUVs):     # ranqueia os AUVs do mais velho para o mais novo
        lista_cres = sorted(AUVs, key=lambda i: i.team_size)
        print("Lista por tamanho de time:")
        for i in lista_cres:
            print("----------------------------------------")
            print(f"Nome: {i.name}")
            print(f"Tamanho do Time : {i.team_size}")
            print("----------------------------------------")

sensoresBrHUE = ["Cameras", "Profundidade", "Sonoro", "IMU"]
sensoresLua = ["Cameras", "Profundidade", "Bussola", "DVL", "IMU"]

brhue = AUV(6, "BrHUE", sensoresBrHUE, 2017, 35)
lua = AUV(8, "Lua", sensoresLua, 2020, 42)

AUVs = [brhue, lua] # informações exemplo TODO: pegar informações verdadeiras

while 1:
    os.system('clear')
    print('Bem vindo a interface! O que voce deseja exibir?')
    print('1 - Tabela de AUVs')
    print('2 - Exibir BrHUE')
    print('3 - Exibir Lua')
    print('4 - Ranking por Ano')
    print('5 - Ranking por Tamanho do Time')
    print('6 - Sair')
    choice = input()
    if choice == '1':
        os.system('clear')
        AUV.showTable(AUVs)
    elif choice == '2':
        os.system('clear')
        brhue.showIndiv()
    elif choice == '3':
        os.system('clear')
        lua.showIndiv()
    elif choice == '4':
        os.system('clear')
        AUV.rankNewToOld(AUVs)
    elif choice == '5':
        os.system('clear')
        AUV.rankTeamSize(AUVs)
    elif choice == '6':
        os.system('clear')
        break
    else:
        print("Opcao invalida, por favor tente novamente...")

    input("Aperte enter para continuar...")

