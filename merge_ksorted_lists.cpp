#include<iostream>
#include<vector>
using namespace std;
//template class vector<int>;


vector<int> sortedmerge(vector<int> &l1, vector<int> &l2); 

vector<int> sortedmerge(vector<int> &l1, vector<int> &l2) {
    if (l1.size() == 0)
        return l2;
    if (l2.size() == 0)
        return l1;

    vector<int> res;
    vector<int> temp;
    if (l1.front() <= l2.front()) {
        res.push_back(l1.front());
        l1.erase(l1.begin());
        temp = sortedmerge(l1, l2);
    }
    else {
        res.push_back(l2.front());
        l2.erase(l2.begin());
        temp = sortedmerge(l1, l2);
    }
    for (auto i : temp) 
        res.push_back(i);
    
    return res;
}

vector<int> merge(vector<vector<int>> nums, int start, int end) {
    int i = start;
    int j = end;
    while (i < end) {
        nums[i] = sortedmerge(nums[i], nums[j]);
        i += 1;
        j -= 1;
        if (i >= j) {
            i = 0;
            end = j;
        }
    }

    return nums[0];

}


int main()
{
    vector<vector<int>> nums = {{1,2,3,4}, {10,11,12}, {5,6,7}, {-1,8,9,15,20}};
    vector<int> res = merge(nums, 0, nums.size()-1);
    for (auto i: res) {
        cout << i << "\t";
    }
    return 0;
}
