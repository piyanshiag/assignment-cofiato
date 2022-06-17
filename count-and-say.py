def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        s=self.countAndSay(n-1)
        ans=""
        c=0
        for i in range(len(s)):
            c+=1
            if i==len(s)-1 or s[i]!=s[i+1]:
                ans=ans+str(c)+s[i]
                c=0
        return ans