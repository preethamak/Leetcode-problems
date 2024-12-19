#include <iostream>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        
        long long reversed = 0;
        long long temp = x;
        
        while (temp != 0) {
            int digit = temp % 10;
            reversed = reversed * 10 + digit;
            temp /= 10;
        }
        
        return (reversed == x);
    }
};

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;

    Solution solution;
    bool result = solution.isPalindrome(num);

    if (result) {
        cout << num << " is a palindrome." << endl;
    } else {
        cout << num << " is not a palindrome." << endl;
    }

    return 0;
}
