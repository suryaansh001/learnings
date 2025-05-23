
#include<iostream>
#include<string>
using namespace std;
int main(){
    // int a=25444;
    // cout<<sizeof(a);

    // char a='a';
    // cout<<sizeof(a);
    // string a="Helllllllo";`
    // cout<<sizeof(a);



//incorrect output 
    string f[3]={"hi","hello","bye"};
    // for(int i=0;i<f->length();i++){
    //     cout<<f[i]<<endl;
    //     cout<<i<<endl;
    // }
    //an use methods like .length() on each individual string. However, since you're only interested in printing the string and the index


    // cout<<f[0].length()<<endl;
    // cout<<f[1].length()<<endl;
    // cout<<f[2].length()<<endl;
    
    
    ///=========================================================
    //typecasting
    // double l= 3.14;
    // int k= (int)l;
    // cout<<k<<endl;
    
    //===============================================
    //input
    int a;
    cout<<"Enter ur  age";
    cin>>a;
    cout<<"the age   u entered is "<<a<<endl;
    if (a>18){
        cout<<"u can vote";
        }
    else{
        cout<<"u cannot vote"<<endl;
    }
    
    
    
    
    return 0;




}