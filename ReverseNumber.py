
class Solution(object):
    
    def __init__(self,x):
        self.x= x
        
    def reverse(self, x: int) -> int:
        if str(x).startswith("-"):
            print(format(-1 * int(str(x*-1)[::-1])))
        else:
            print(int(str(x)[::-1]))

x= 9646324351      
c=Solution(x)
c.reverse(x)

        
