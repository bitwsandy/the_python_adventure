limit = int(input("Enter the upper limit for prime numbers: "))
print("Prime numbers up to", limit, ":")
for number in range(2, limit + 1):
    prime = True
    if number < 2:
        prime = False
    else:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                prime = False
                break
    if prime:
        print(number, end=" ")