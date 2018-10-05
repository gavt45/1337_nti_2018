#include <iostream>

using namespace std;

int main(){
    freopen("input.txt", "r", stdin);
    int n,m,k,h;
    cin >> n >> m >> k >> h;
    n-=m*k;
    if ((n < h) || (n < 0)) {
        cout << "No";
        return 0;
    }else if (n==h){
        cout << "Yes";
        return 0;
    }else{
        //cout << "Yes";
        if((n%h)==0){
                cout << "Yes";
        }else cout << "No";
    }

    return 0;
}

