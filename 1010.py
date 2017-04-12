cop1,nouop1,uprice1 = input().split()

cop2,nouop2,uprice2 = input().split()

pp1=int(nouop1)*float(uprice1)
pp2=int(nouop2)*float(uprice2)

total=pp1+pp2

print("VALOR A PAGAR: R$ %.2f"%total)
