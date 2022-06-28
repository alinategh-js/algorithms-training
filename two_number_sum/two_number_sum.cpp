#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

// O(n^2) time | O(1) space
vector<int> twoNumberSum1(vector<int> array, int targetSum){
    int arrayLength = array.size();
    for(int i=0; i < arrayLength - 1; i++){
        int firstNumber = array[i];
        for(int j=i+1; j < arrayLength; j++){
            int secondNumber = array[j];
            if(firstNumber + secondNumber == targetSum)
                return {firstNumber, secondNumber};
        }
    }
    return {};
}

// O(n) time | O(n) space
vector<int> twoNumberSum2(vector<int> array, int targetSum){
    unordered_set<int> numbers; // it's a hash table
    for (int num : array){
        int targetNumber = targetSum - num;
        if (numbers.find(targetNumber) != numbers.end()) // if targetNumber is found in numbers
            return {targetNumber, num};
        else
            numbers.insert(num);
    }
    return {};
}

// O(nlog(n)) time | O(1) space
vector<int> twoNumberSum3(vector<int> array, int targetSum){
    sort(array.begin(), array.end());
    int leftPointer = 0;
    int rightPointer = array.size() - 1;
    while (leftPointer < rightPointer){
        int sum = array[leftPointer] + array[rightPointer];
        if (sum == targetSum)
            return {array[leftPointer], array[rightPointer]};
        else if (sum > targetSum)
            rightPointer--;
        else
            leftPointer++;
    }
    return {};
}

int main() 
{
    vector<int> array = {3, 5, -4, 8, 11, 1, -1, 6};
    vector<int> result = twoNumberSum3(array, 10);
    for (int i: result)
        cout << i << ", ";
}