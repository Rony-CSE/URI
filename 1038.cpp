#include <bits/stdc++.h>
using namespace std;
int main(void)
{
    int x,y;
    float a;
    cin >> x >> y;
    if(x==1){
        a=4.00;
    }
    else if(x==2){
        a=4.50;
    }
    else if(x==3){
        a=5.00;
    }
    else if(x==4){
        a=2.00;
    }
    else if(x==5){
        a=1.50;
    }
    float total=y*a;
    cout<<fixed<<setprecision(2)<<"Total: R$ "<<total<<endl;
}
