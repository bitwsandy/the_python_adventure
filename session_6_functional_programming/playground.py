
def coffee_next_button(total_coffee) :
    count = 0
    while total_coffee > 50:
        coffee_out = 50
        total_coffee = total_coffee - coffee_out
        count = count + 1
        yield count


next_button = coffee_next_button(500)

for i in range(1,11):
    print(next(next_button))













