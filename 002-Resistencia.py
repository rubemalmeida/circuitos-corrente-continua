print "O circuito está em série ou paralelo?"
while True:
    try:
        fResult = int(raw_input("Digite 1 se em série, ou 2 em paralelo: "))
        if fResult in (1, 2):
            break
        print "Numero invalido. Tente novamente.."
    except ValueError:
        print "Oops! Resposta invalida. Tente novamente..."
while True:
    try:
        sResult = int(raw_input("Qual a quantidade de resistores associados? "))
        if sResult > 0:
            break
        print "Informe a quantidade. Tente novamente.."
    except ValueError:
        print "Oops! Valor invalido. Tente novamente..."
while True:
    try:
        tResult = float(raw_input("Qual a tensao da fonte em V? "))
        break
    except ValueError:
        print "Oops! Valor invalido. Tente novamente..."
lista=[]
for i in range(sResult):
    while True:
        try:
            valor = int(raw_input('Qual o valor do ' + str(i+1) + 'o resistor? '))
            lista.append(valor)
            break
        except ValueError:
            print "Oops! Valor invalido. Tente novamente..."
req=0
if fResult == 1:
    req = sum(lista)
else:
    for i in range(sResult):
        req += 1.0/lista[i]
    req = 1.0/req
    
result = (tResult*1.0)/req    
print 'A resistência equivalente é de ' + str(req) + ' Ohms'
print 'A corrente é de ' + str(result) + ' A'​