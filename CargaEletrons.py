print "A carga ganhou ou perdeu eletrons?"
while True:
    try:
        fResult = int(raw_input("Digite 1 se ganhou, ou 2 se perdeu: "))
        if fResult in (1, 2):
            break
        print "Numero invalido. Tente novamente.."
    except ValueError:
        print "Oops! Resposta invalida. Tente novamente..."
while True:
    try:
        if fResult == 1:
            sResult = int(raw_input("Qual a quantidade de eletrons que o corpo ganhou? "))
            break
        sResult = int(raw_input("Qual a quantidade de eletrons perdidos? "))
        break
    except ValueError:
        print "Oops! Valor invalido. Tente novamente..."

result = (sResult*1.6*10e-19)
if fResult == 1:
    print "O corpo possui carga positiva {0}C".format(result)
elif fResult == 2:
    print "O corpo possui carga negativa {0}C".format(result)
