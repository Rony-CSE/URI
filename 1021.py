coins = {0.01 : 0 , 0.05 : 0 , 0.10 : 0 , 0.25 : 0 , 0.50 : 0 , 1 : 0}
notes = {2 : 0 , 5 : 0 , 10 : 0 , 20 : 0 , 50 : 0 , 100 : 0}
amount = 0
N=float(input())
while amount <= N <= 1000000.00:
    if amount + 100 <= N:
        amount += 100
        notes[100] += 1
    elif amount + 50 <= N:
        amount += 50
        notes[50] += 1
    elif amount + 20 <= N:
        amount += 20
        notes[20] += 1
    elif amount + 10 <= N:
        amount += 10
        notes[10] += 1
    elif amount + 5 <= N:
        amount += 5
        notes[5] += 1
    elif amount + 2 <= N:
        amount += 2
        notes[2] += 1
    elif amount + 1 <= N:
        amount += 1
        coins[1] += 1
    elif amount + 0.50 <= N:
        amount += 0.50
        coins[0.50] += 1
    elif amount + 0.25 <= N:
        amount += 0.25
        coins[0.25] += 1
    elif amount + 0.10 <= N:
        amount += 0.10
        coins[0.10] += 1
    elif amount + 0.05 <= N:
        amount += 0.05
        coins[0.05] += 1
    elif amount + 0.01 <= N:
        amount += 0.01
        coins[0.01] += 1
    else:
        break
print("NOTAS:")
print("%d nota(s) de R$ 100.00" % notes[100])
print("%d nota(s) de R$ 50.00" % notes[50])
print("%d nota(s) de R$ 20.00" % notes[20])
print("%d nota(s) de R$ 10.00" % notes[10])
print("%d nota(s) de R$ 5.00" % notes[5])
print("%d nota(s) de R$ 2.00" % notes[2])
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % coins[1])
print("%d moeda(s) de R$ 0.50" % coins[0.50])
print("%d moeda(s) de R$ 0.25" % coins[0.25])
print("%d moeda(s) de R$ 0.10" % coins[0.10])
print("%d moeda(s) de R$ 0.05" % coins[0.05])
print("%d moeda(s) de R$ 0.01" % coins[0.01])
