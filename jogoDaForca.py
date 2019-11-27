from random import randint

#recebendo arquivo
arquivo = open('listaDeAnimais.txt', 'r').read()

#tratamento dos dados
arquivo = arquivo.replace(";", "")
arquivo = arquivo.replace("á", "a")
arquivo = arquivo.replace("é", "e")
arquivo = arquivo.replace("í", "i")
arquivo = arquivo.replace("ó", "o")
arquivo = arquivo.replace("ú", "u")
arquivo = arquivo.replace("â", "a")
arquivo = arquivo.replace("ê", "e")
arquivo = arquivo.replace("î", "i")
arquivo = arquivo.replace("ô", "o")
arquivo = arquivo.replace("û", "u")
arquivo = arquivo.replace("ã", "a")
arquivo = arquivo.replace("ç", "c")
arquivo = arquivo.replace(":", "")
animais = arquivo.split()

print("                                                                        ")
print("                             -|             |-")
print("         -|                  [-_-_-_-_-_-_-_-]                  |-")
print("         [-_-_-_-_-]          |             |          [-_-_-_-_-]")
print("          | o   o |           [  0   0   0  ]           | o   o |")
print("           |     |    -|       |           |       |-    |     |")
print("           |     |_-___-___-___-|         |-___-___-___-_|     |")
print("           |  o  ]              [    0    ]              [  o  |")
print("           |     ]   o   o   o  [ _______ ]  o   o   o   [     | ----__________")
print("_____----- |     ]              [ ||||||| ]              [     |")
print("           |     ]              [ ||||||| ]              [     |")
print("       _-_-|_____]--------------[_|||||||_]--------------[_____|-_-_")
print("      ( (__________------------_____________-------------_________) )")
print("\n--------------------------*Bem vindo ao Jogo*----------------------------------")
print("---------------------------Adivinhe o animal-----------------------------------")

jogarDeNovo = 1
while(jogarDeNovo == 1):
    
    #escolhendo animal da lista
    posicao = randint(0, len(animais)-1)
    animalSecreto = list(animais[posicao])

    #ocultando o resultado
    adivinhadoAteAgora = []
    for i in range(len(animalSecreto)):
        if animalSecreto[i] == '-':
            adivinhadoAteAgora.append('-')
        else:
            adivinhadoAteAgora.append('*')

    print("")
    print("O animal contém %d letras" %len(animalSecreto))
    print(adivinhadoAteAgora, "\n")

    i = 1
    ganhou = 0
    acertou = 0
    tentativa = 5
    while tentativa > 0:
        
        #verifica se tem a letra do chute
        chute = input("%dº tentativa: " %i)
        for j in range(len(animalSecreto)):
            if chute == animalSecreto[j]:
                acertou = 1
                adivinhadoAteAgora[j] = chute
        print(adivinhadoAteAgora)
        
        #verifica se usuário gastou uma tentativa
        if acertou:
            acertou = 0
        else:
            acertou = 0
            tentativa -= 1

        #verifica se o usuário ganhou o perdeu
        if '*' in adivinhadoAteAgora:
            pass
        else:
            ganhou = 1
            break

        i += 1

    if ganhou:

        print("                                                |>>> ")
        print("                                                | ")
        print("                                            _  _|_  _ ")
        print("                                           |;|_|;|_|;| ")
        print("                                           \\.    .   / ")
        print("                                            \\:  .   / ")
        print("                                             ||:   | ")
        print("                                             ||:.  | ")
        print("                 Você Ganhou                 ||:  .| ")
        print("                                             ||:   | ")
        print("                                             ||: , | ")
        print("                                             ||:   | ")
        print("                                             ||: . | ")
        print("              __                            _||_   | ")
        print("     ____--`~    '--~~__            __ ----~    ~`---,              ___ ")
        print("-~--~                   ~---__ ,--~'                  ~~----_____-~'   `~----~~ ")
    else:

        print("")
        print("  / \\\\              / \\\\ ")
        print(" /   \\\\            /   \\\\ ")
        print("(_____)           (_____) ")
        print(" |   |  _   _   _  |   | ")
        print(" | O |_| |_| |_| |_| O | ")
        print(" |-  |          _  | - | ")
        print(" |   |   - _^_     |   | ")
        print(" |  _|    //|\\\\\\  -|   | ")
        print(" |   |   ///|\\\\\\   |  -| ")
        print(" |-  |_  |||||||   |   | ")
        print(" |   |   |||||||   |-  | ")
        print(" |___|___|||||||___|___| ")
        print("         (      ( ")
        print("         \\      \\ ")
        print("         )      ) ")
        print("         |      |                 Game Over ")
        print("         (      ( ")
        print("         \\      \\          O animal era", animais[posicao])
  
    jogarDeNovo = int(input("Jogar Novamente?: Sim = 1 || Não = 0 "))