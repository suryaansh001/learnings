#include<iostream>
using namespace std;

int sum(int a,int b){
    return a+b;
}


int sumofDgts(int num){
    int sum=0;

    while(num>0){
        sum+=num%10;
        num=int(num/10);
    }
    return sum;
}
// int main(){
//     // int x,y;

//     // cout<<"enter values of x and y";
//     cout<<"enter the values of number";
//     int num;
//     cin>>num;
//     //cin>>x>>y;//**************************imp it is space seprated  */
//     //cout<<"the sum of "<<x<<"+"<<y<<"is "<<sum(x,y)<<endl;
//     cout<<"the sum of digits is "<<sumofDgts(num)<<endl;
int factorial(int num){
    int prod=1;
    for(int i=1;i<num;i++){
        prod=prod*i;
    }
    return prod;
}
int ncr(int n,int r){
    int f1=factorial(n);
    int f2=factorial(r);
    return f1/f2;

}

int main(){

    int n,r;
    cout<<"insert values of n and r in ncr";
    cin>>n>>r;
    cout<<"the result"<<ncr(n,r)<<endl;
}
