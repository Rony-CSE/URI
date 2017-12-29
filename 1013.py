a,b,c = input().split()
a=int(a)
b=int(b)
c=int(c)

maiorAB=(a+b+abs(a-b))/2 # find max from a & b
maiorAC=(a+c+abs(a-c))/2 # find max from a & c
if maiorAB > maiorAC:
     maior=maiorAB
else:
     maior=maiorAC
	
print("%d eh o maior"%maior)
