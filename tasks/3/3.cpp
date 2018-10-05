#include <iostream>
#include <malloc.h>
#include <math.h>
#include <iomanip>

using namespace std;

int main(){
    freopen("input.txt", "r", stdin);
    float a,b,c,p,s;
    int** mat = (int**)malloc(3*sizeof(int*));
    for (int i = 0; i<3; i++){
        mat[i] = (int*)malloc(3*sizeof(int));
        cin >> mat[i][0] >> mat[i][1] >> mat[i][2];
    }
    a = sqrt( pow((mat[1][0] - mat[0][0]), 2) + pow((mat[1][1] - mat[0][1]), 2) +pow((mat[1][2] - mat[0][2]), 2) ); // 1 2
    b = sqrt( pow((mat[2][0] - mat[1][0]), 2) + pow((mat[2][1] - mat[1][1]), 2) +pow((mat[2][2] - mat[1][2]), 2) ); // 1 3
    c = sqrt( pow((mat[2][0] - mat[0][0]), 2) + pow((mat[2][1] - mat[0][1]), 2) +pow((mat[2][2] - mat[0][2]), 2) ); // 3 2
    p = (a+b+c)/2;
    s=sqrt(p * (p-a) * (p-b) * (p-c));
    int i = 0;
    int digit = (int) s;
    for(;digit>0;i++){
                digit/=10;
        }
    cout << setprecision(i+25) << s;
    //cout << "AAA";
    return 0;
}

