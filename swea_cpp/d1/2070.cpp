#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    
    for(int tc = 1; tc<=T; tc++) {
        int A, B;
        cin >> A >> B;
        if (A > B) {
            cout << "#" << tc << " >" << endl;
        } else if (A < B) {
            cout << "#" << tc << " <" << endl;
        } else {
            cout << "#" << tc << " =" << endl;
        }
    }
    
    return 0;
}