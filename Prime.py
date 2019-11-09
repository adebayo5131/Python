def Integer(first, last):
    for Number in range (first, (last +1)):
        count = 0
        for i in range(2, (Number//2 + 1)):
            if(Number % i == 0):
                count = count + 1
                break

        if (count == 0 and Number != 1):
            print(Number)
     
            

def play():
    print('I can list all prime numbers for you')        
    print("Enter the first Integer")
    first = int(input())
    print("Enter the second Integer")
    second = int(input())
    Integer(first, second)

play()



