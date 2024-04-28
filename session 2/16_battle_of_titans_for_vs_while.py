import time

# Code for measuring time taken by the for loop
start_time_for = time.time()

start = 1
end = 10

for i in range(start, end + 1):
    result = i + i

end_time_for = time.time()
time_taken_for = end_time_for - start_time_for

print("Time taken by for loop:", time_taken_for)

# Code for measuring time taken by the while loop
start_time_while = time.time()

i = start
while i <= end:
    result = i + i
    i += 1

end_time_while = time.time()
time_taken_while = end_time_while - start_time_while

print("Time taken by while loop:", time_taken_while)
