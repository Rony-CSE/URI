currency = {1 : 0,
                2 : 0,
                5 : 0,
               10 : 0,
               20 : 0,
               50 : 0,
               100 : 0}

amount = 0
total=int(input())
print(total)
while amount < total:

    if amount + 100 <= total:
        amount += 100
        currency[100] += 1
    elif amount + 50 <= total:
        amount += 50
        currency[50] += 1
    elif amount + 20 <= total:
        amount += 20
        currency[20] += 1
    elif amount + 10 <= total:
        amount += 10
        currency[10] += 1
    elif amount + 5 <= total:
        amount += 5
        currency[5] += 1
    elif amount + 2 <= total:
        amount += 2
        currency[2] += 1
    else:
        amount += 1
        currency[1] += 1
print(currency[100]+currency[50]+currency[20]+currency[10]+currency[5]+currency[2]+currency[1],'notes needed minimum ')
print("%d note(s) of TK 100.00" % currency[100])
print("%d note(s) of TK 50.00" % currency[50])
print("%d note(s) of TK 20.00" % currency[20])
print("%d note(s) of TK 10.00" % currency[10])
print("%d note(s) of TK 5.00" % currency[5])
print("%d note(s) of TK 2.00" % currency[2])
print("%d note(s) of TK 1.00" % currency[1])
