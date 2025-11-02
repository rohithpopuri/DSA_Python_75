class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s={}
        dict_t={}
        if len(s)!=len(t):
            return False
        for c in s :
            if c not in dict_s :
                dict_s[c]=1
            else:
                dict_s[c]=dict_s[c]+1
           
        for ch in t :
            if ch not in dict_t :
                dict_t[ch]=1
            else:
                dict_t[ch]+=1
        if dict_s==dict_t:
            return True 
        return False
        
        