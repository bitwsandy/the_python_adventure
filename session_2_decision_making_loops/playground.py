limit = 10
print("Prime numbers up to", limit, ":")
for number in range(2, limit + 1):
    #range(2,11) # 2,3,4,5,6,7,8,9,10
    # number : 9
    prime = True
    if number < 2:
        prime = False
    else:
        for i in range(2, int(number/2)+1):
            # range(2, 5) : number = 9
            if number % i == 0:
                prime = False
                break
    if prime:
        print(number, end=" ")
    # 2 3 5 7


for i in range(2, 4):
    print(i)