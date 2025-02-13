class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        op = 0
        y = 0
        x = list()
      
        for k in allowed:
            x.append(k)
          
        for i in words:
            for j in i:
                if j in x:
                    y+=1
                else:
                    break
            if y==len(i):
                op+=1
            y=0
          
        return op
