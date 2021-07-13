# Contagem Regressiva

from time import sleep 

print("Let's count it!")

print()

print("Deseja realizar à contagem regressiva de hora [H] / minuto [M] / segundo [S]?")
escolha = input("->> ");

# while not (escolha != 'h') or not (escolha != 'm') or not(escolha != 's') :
#     print("Opção inválida, escolha novamente...")
#     print("Hora [H] / Minuto [M] / Segundo [S]")
#     escolha = input("->> ");

if escolha == 'h' :
    print("Quantas horas de contagem regressiva?")
    hora = int(input("->> "))

    print()

    pH = ''
    pM = ''
    pS = ''
    
    for countH in range(hora, 0, -1) :
        for countM in range(59, -1, -1) :
            for countS in range(59, -1, -1) :
                if countH < 10 :
                    pH = f"0{countH}"
                else :
                    ph = str(countH)
                if countM < 10 :
                    pM = f"0{countM}"
                else :
                    pM = str(countM)
                if countS < 10 :
                    pS = f"0{countS}"
                else :
                    pS = str(countS)
                if countM == 59 and countS == 59 and countH == hora:
                    print(f"{pH}:00:00")
                    countH = countH - 1
                    pH = f"0{countH}"
                print(f"{pH}:{pM}:{pS}")
                sleep(1);

elif escolha == 'm' :
    print("Quantos minutos de contagem regressiva?")
    minuto = int(input("->> "))

    print()

    pH = ''
    pM = ''
    pS = ''

    for countH in range(1, 0, -1) :
        for countM in range(minuto, 0, -1) :
            for countS in range(59, -1, -1) :
                countH = countH - 1
                if countM < 10 :
                    pM = f"0{countM}"
                else :
                    pM = str(countM)
                if countS < 10 :
                    pS = f"0{countS}"
                else :
                    pS = str(countS)
                if countM == minuto and countS == 59:
                    print(f"00:{pM}:00")
                pM = f"0{countM - 1}"
                print(f"00:{pM}:{pS}")
                sleep(1);
                
elif escolha == 's' :
    print("Quantos segundos de contagem regressiva?")
    segundo = int(input("->> "))

    print()

    pH = ''
    pM = ''
    pS = ''

    for countH in range(1, 0, -1) :
        for countM in range(1, 0, -1) :
            for countS in range(segundo, -1, -1) :
                countH = countH - 1
                countM = countM - 1
                if countS < 10 :
                    pS = f"0{countS}"
                else :
                    pS = str(countS)
                pM = f"0{countM - 1}"
                print(f"00:00:{pS}")
                sleep(1);

print()
 

