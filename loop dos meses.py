from time import sleep
print()
x = 0
while 0 <= x:
    x +=1

    from datetime import datetime, timedelta

    data_atual = datetime.now()
    prox_mes = data_atual + timedelta(days=(30*x))
    mes_proximo = prox_mes.strftime("%B")
    sleep(0.8)

    print("O próximo mês é:", mes_proximo)