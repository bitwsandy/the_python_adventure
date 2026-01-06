

nums = [1,5,8,2,4,6,2,4,2,5,6,2,1,2,6,3,4]

# print("Sum of nums : ", sum(nums))
# print("Min of nums : ", min(nums))
# print("Max of nums : ", max(nums))
# print("Length of nums : ", len(nums))
# print("Sorted order of nums : ", sorted(nums))
# print("Reversed order of nums : ", list(reversed(nums)))


sentence = "The quick brown fox jumps over the lazy dog"
# [The, quick, brown.....................]
results = [sum(1 for char in word if char in 'aeiou')
           for word in sentence.split(" ")]

print(sentence)
print(sentence.split(' '))


vowel_count = []

for word in sentence.split(" "): # ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
    count = 0
    for char in word:
        if char in 'aeiou':
            count += 1
    vowel_count.append(count)

print(vowel_count)






