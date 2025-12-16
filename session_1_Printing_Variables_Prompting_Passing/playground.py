
marks = int(input("Enter your marks : ")) # 87, 66, 59, 45, 18, 71

if marks >= 0 and marks <= 100 :
    if marks >= 90 :
        print('A+')
    elif marks >= 80 :
        print('A')
    elif marks >= 70 :
        print('B')
    elif marks >= 60 :
        print('C')
    elif marks >= 50 :
        print('D')
    elif marks >= 35 :
        print('E')
    else :
        print('F')
else :
    print("Please enter a valid marks")

