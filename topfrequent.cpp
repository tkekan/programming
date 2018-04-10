#include<vector>
#include<iostream>
#include<unordered_map>
using namespace std;

vector<int> topKFrequent(int [], int, int);

vector<int> topKFrequent(int nums[], int k, int size) {
        unordered_map<int, int> m;
        for (int i = 0; i < size; i++) {
            printf("Map-%d\n", m[nums[i]]);
            ++m[nums[i]];
       }
        
        vector<vector<int> > buckets(size + 1); 
        for (auto p : m) {
            printf("\n%d - %d",p.first,p.second);
            buckets[p.second].push_back(p.first);
        }
        
        for (int num : buckets[0] )
            cout << endl << "val: " << num;

        vector<int> ans;
        printf("Bucket size is %d",buckets.size());
        for (int i = buckets.size() - 1; i >= 0 && ans.size() < k; --i) {
            for (int num : buckets[i]) {
                ans.push_back(num);
                if (ans.size() == k)
                    break;
            }
        }
        return ans;
    }

int main()
{
    int  nums[] =  { 4,104,104,104,4,1,-1,2,-1,2,3 };
    int size =  sizeof(nums) / sizeof(nums[0]);
    vector<int> ans = topKFrequent(nums, 2, size);
    cout <<"Final answer is :" << endl;
    for (int num : ans)
        cout << num << endl;
    return 0;
}
