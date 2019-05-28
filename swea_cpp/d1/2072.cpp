#include <iostream>

using namespace std;

int main() {
    int count;
    cin >> count;
    for(int cnt = 0; cnt < count; cnt++)
    {
        int *arr = new int[10];
        int sum = 0;
        for(int i = 0; i < 10; i++)
        {
            cin >> arr[i];
            if(arr[i]%2 == 1)
                sum = sum + arr[i];
        }
        cout << "#" << cnt+1 << " " << sum << endl;
    }
    return 0;
}