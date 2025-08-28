#include <iostream>
using namespace std;

void print_vector(int size, int vector[10]){
    for (int i=0;i<size;i++)
    {
        cout << vector[i] << " ";
    }
    cout << endl; 
}

void add_vectors(int size, int vector1[10], int vector2[10]){
    for (int i=0;i<size;i++)
    {
        cout << vector1[i] + vector2[i]<< " ";
    }
    cout << endl;
}

void subtract_vectors(int size, int vector1[10], int vector2[10]){
    for (int i=0;i<size;i++)
    {
        cout << vector1[i] - vector2[i]<< " ";
    }
    cout << endl;
}

void input_vectors(int size, int vector1[10], int vector2[10]){
    for (int i=0;i<size;i++)
    {
        cin>>vector1[i];
    }
    for (int i=0;i<size;i++)
    {
        cin>>vector2[i];
    }
    cout << endl;
}

void check_vectors(int size, int vector1[10],int vector2[10],bool check){
    for (int i=0;i<size;i++){ 
    if (vector1[i]!=vector2[i]){
        check=false;
    }
    else {
        check=true;
    }
    }
    if (check==true){
        cout << "True";
    }
    else{
        cout << "False";
    }
    cout << endl;
}

int main() {

    int size;
    int vector1[10];
    int vector2[10];
    char op;
    bool check=true;
    cin>> size;

    input_vectors(size, vector1,vector2);
    print_vector(size, vector1);
    cin >> op;

    if (op =='+'){
        add_vectors(size, vector1, vector2);
    }
    else if (op == '-' ){
        subtract_vectors(size, vector1, vector2);
    }
    else if (op == '=' ){
        check_vectors(size, vector1, vector2, check);
    }

    return 0;
}