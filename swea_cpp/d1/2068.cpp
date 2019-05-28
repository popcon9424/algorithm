#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    
    for(int tc = 1; tc <= T; tc++) {
        int *arr = new int[10];
        int max = 0;
        for(int i = 0; i < 10; i++) {
            cin >> arr[i];
            if(arr[i] > max) {
                max = arr[i];
            }
        }
        cout << "#" << tc << " " << max << endl;
    }
    
    return 0;
}