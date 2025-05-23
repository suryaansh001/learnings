#include<iostream>
using namespace std;

// int main(){
//     int j=1;
//     for (int i =1;i<=3;i++){
//         int count=0;
//         for(int count=0;count<3;count++){
//             cout<<j<<" ";
//             j++;
//         }
//         cout<<endl;

        
//     }
// }

//=============triangle pattern===================
int main(){
    int line;
    cout<<"enter number of lines";
    cin>>line;



    // for(int i=1;i<line;i++){
    //     char s='*'*i;
    //     cout<<s<<endl;
    // }

    for(int i=1;i<line;i++){
        for(int j=1;j<=i;j++){
            cout<<i;
        }
        cout<<endl;
    }

    //Floyds triangle
    for(int i=1;i<=line;i++){
        for(int j=1;j<=i;j++){
            cout<<j;

        }
        cout<<endl;
    }
}