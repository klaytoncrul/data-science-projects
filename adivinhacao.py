import random
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("defina o nivel:"))

    if(nivel== 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1,total_de_tentativas +1):
        print ("Tentativa, {} de {}".format(rodada, total_de_tentativas) )
        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou: {} ".format( chute_str))
        chute = int(chute_str)

        if chute <1 or chute >100:
            print ("O numero digitado deve ser entre 1 e 100!")
            continue


        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {}!".format(pontos))
            break
        else:
            if (chute_maior):
                print("O número secreto é menor que o número digitado")
            elif (chute_menor):
                print("O número secreto é maior que o número digitado")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos



                print("Você errou!")
    print("O numero secreto é ", numero_secreto)
    print("Fim do jogo")
