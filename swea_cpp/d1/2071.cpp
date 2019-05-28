#include <iostream>

using namespace std;

int main(){
    int T;
    cin >> T;
    int *arr = new int[10];
    for(int tc = 0; tc < T; tc++)
    {
        int sum = 0;
        for(int i = 0; i < 10; i++)
        {
            cin >> arr[i];
            sum += arr[i];
        }
        if(sum%10 > 4){
            sum = sum/10+1;
        } else {
            sum = sum/10;
        }
        cout << "#" << tc+1 << " " << sum << endl;
    }
    
    return 0;
}