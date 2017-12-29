ui = float(input())
if ui<=0 or ui>100 :
    print("Fora de intervalo")
elif ui<=25.00:
    print("Intervalo [0,25]")
elif ui<=50.0:
    print("Intervalo (25,50]")
elif ui<=75.0:
    print("Intervalo (50,75]")
elif ui<=100.0:
    print("Intervalo (75,100]")