def Reverse(n):
    s = ''
    
    for i in n:
       s = i + s
    return s
print(Reverse('adebayo'))


def reverse(n):
    output = [""]*len(n)
    i = len(n) -1
    
    if n == " ":
        return (" ")
    else:
        
        for j in n:
            output[i] = j
            i-=1
        return ''.join(output)
print(reverse(" "))
