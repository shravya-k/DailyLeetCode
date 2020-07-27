class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        table= [[0 for i in range(len(s)+1)] for j in range(len(s)+1)]
        res=""
        if not s:
            return res
        res=s[0]
        for i in range(1,len(s)+1):
            table[i][i]=1
            
        k=1
        for j in range(2,len(s)+1):
            i=1
            k+=1
            while j<=len(s):
                if k==2:
                    if s[i-1]==s[j-1]:
                        table[i][j]=1
                        res=s[i-1:j]
                else:
                    if s[i-1]==s[j-1] and table[i+1][j-1]:
                        table[i][j]=1
                        res=s[i-1:j]
                j+=1
                i+=1
                
        return(res)    
                
            
        
