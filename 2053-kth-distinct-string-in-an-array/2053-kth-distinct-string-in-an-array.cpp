class Solution {
private:
    vector<string> findDistinct(vector<string> &arr){
        vector<string> ans;
        unordered_map<string,int> freq;
        for(auto &s: arr){
            freq[s]++;
        }
        for(auto &s: arr){
            if(freq[s]==1){
                ans.push_back(s);
            }
        }
        return ans;
    }
public:
    string kthDistinct(vector<string>& arr, int k) {
        vector<string> res = findDistinct(arr);
        if(k>0 && k<=res.size()){
            return res[k-1];
        }
        return "";
    }
};