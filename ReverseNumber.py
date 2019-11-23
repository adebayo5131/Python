##class Solution:
##
##    self.x =231
##
##    def __init__(self, x):
##        self.x = 123
##        
##    def reverse(self, x: int) -> int:
##        if str(x).startswith("-"):
##            x = x[1:]
##            return("-{0}".format(int(str(x)[::-1])))
##        else:
##            return(int(str(x)[::-1]))

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

        
