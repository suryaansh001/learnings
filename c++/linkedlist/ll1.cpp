#include<iostream>
using namespace std;

class node{
    public:
    int data;
    node* next; 
    node(int val) {
        data = val;
        next = NULL;
    }
};
void insertnode(node* &head,int val){
    node* n = new node(val);
    if (head==NULL){
        head=n;
        return;
    }
    else{
        node* temp=head;
        while(temp->next=NULL){
            temp=temp->next;
                        
        }
    }