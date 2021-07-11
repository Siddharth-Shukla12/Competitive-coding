class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count=0
        for i in zip(*strs):
            if len(set(i))==1:
                
                count+=1
            else:
                break
        
        return strs[0][:count]