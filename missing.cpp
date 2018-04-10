
#include<iostream>
#include<vector>

using namespace std;
vector<int> findDisappearedNumbers(vector<int> &);

vector<int> findDisappearedNumbers(vector<int> &nums) {
        int len = nums.size();
        for(int i=0; i<len; i++) {
            int m = abs(nums[i])-1; // index start from 0
            nums[m] = nums[m]>0 ? -nums[m] : nums[m];
        }
        vector<int> res;
        for(int i = 0; i<len; i++) {
            if(nums[i] > 0) res.push_back(i+1);
        }
        return res;
}

int main()
{
    int input[] = {4,3,2,7,8,2,3,1};
    vector<int> nums;
 //  vector<int> nums = {4,3,2,7,8,2,3,1};
    nums.assign(&input[0], &input[0]+7);
    
    vector<int> results = findDisappearedNumbers(nums);    
    for ( auto num : results)
        cout<<num<<endl;
return 0;

}

