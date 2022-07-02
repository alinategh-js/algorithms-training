#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

// subsequence (subarray) of a given sequence (array) is any sequence that
// can be derived from the given sequence by deleting some or no elements 
// without changing the order of the remaining elements

// Time complexity: O(n)
// Worst case scenario occurs when we traverse through the whole array
bool validateSubSequence(vector<int> array, vector<int> subsequence){
    int subsequenceIndex = 0;
    int subsequenceLength = subsequence.size();
    for (auto element : array){
        if(subsequence[subsequenceIndex] == element)
            subsequenceIndex++;
        if(subsequenceIndex == subsequenceLength)
            return true;
    }
    return false;
}

int main() 
{
    vector<int> array = {1, 5, 10, -1, -5, 23, 42, 89, -120};
    vector<int> subsequence1 = {5, -1, 23, -120};
    vector<int> subsequence2 = {1, -1, 23, 42};
    vector<int> subsequence3 = {1, -1, 10, 42};
    bool result1 = validateSubSequence(array, subsequence1);
    bool result2 = validateSubSequence(array, subsequence2);
    bool result3 = validateSubSequence(array, subsequence3);
    cout << result1 << endl;
    cout << result2 << endl;
    cout << result3 << endl;
}