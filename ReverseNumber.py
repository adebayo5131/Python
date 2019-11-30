class Solution(object):
    def reverse(self,x): 
        if x > 0:
            reverse = 0
            while(x > 0):
                reminder =x %10
                reverse = (reverse *10) + reminder
                x = x //10
            reverse
        elif x <= 0:
            x*= -1
            reverse = 0
            while(x > 0):
                reminder =x %10
                reverse = (reverse *10) + reminder
                x = x //10
            reverse = reverse*-1
          #Handle integer overflow
        minX = -2**31  
        maxX = 2**31 - 1  
        if reverse < maxX and reverse > minX:  
            return reverse  
        else:
            return 0

x= -123      
c=Solution()
print(c.reverse(x))

        
