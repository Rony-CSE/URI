#include <stdio.h>
int main()
{
	double N;
	int taka,hundred,fifty,twenty,ten,five,two,one;
	int rest100,rest50,rest20,rest10,rest5,rest2,p50,rp50,p25,rp25,p10,rp10,p5,rp5,p1,paisa;
	scanf("%lf",&N);
	taka=N;
	hundred=taka/100;
	rest100=taka%100;
	fifty=rest100/50;
	rest50=rest100%50;
	twenty=rest50/20;
	rest20=rest50%20;
	ten=rest20/10;
	rest10=rest20%10;
	five=rest10/5;
	rest5=rest10%5;
	two=rest5/2;
	rest2=rest5%2;
	one=rest2;
	paisa=100*N-taka*100;
	p50=paisa/50;
	rp50=paisa%50;
	p25=rp50/25;
	rp25=rp50%25;
	p10=rp25/10;
	rp10=rp25%10;
	p5=rp10/5;
	rp5=rp10%5;
	p1=rp5;
	printf("NOTAS:\n%d nota(s) de R$ 100.00\n%d nota(s) de R$ 50.00\n%d nota(s) de R$ 20.00\n%d nota(s) de R$ 10.00\n%d nota(s) de R$ 5.00\n%d nota(s) de R$ 2.00\nMOEDAS:\n%d moeda(s) de R$ 1.00\n%d moeda(s) de R$ 0.50\n%d moeda(s) de R$ 0.25\n%d moeda(s) de R$ 0.10\n%d moeda(s) de R$ 0.05\n%d moeda(s) de R$ 0.01\n",hundred,fifty,twenty,ten,five,two,one,p50,p25,p10,p5,p1);
	return 0;
}