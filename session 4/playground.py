import re

text = """Alice was born on 1990-05-20 in New York.
Bob's email is bob@example.com.
The project deadline is approaching: 2024-07-31.
John's phone numbers are 321-555-4321, 123.555.1234
, 123*555*1234
, 800#555#1234
, 900.555.1234.
cat
mat
pat
bat
Mr. John200
Mr James
Mr Sunder
Mr. Satya
Ms Dibya
Mrs. Ashwini
Mr. A

emails = 
thisIsSample@gmail.com
IamStudent@university.edu
my-117-business@my-work.net

https://www.google.com
http://technologicalgeeks.in
https://youtube.com
https://www.nasa.gov

"""
#thisIsSample@gmail.com

sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'\w+@\w+\.[a-z]{2,5}')
matches = pattern.finditer(text)

for match in matches :
    print(match)

# Study Drills :
# 1. Match all three digits : r'\d\d\d'
# 2. Match all phone numbers : r'\d\d\d.\d\d\d.\d\d\d\d'
# 3. Match all phone numbers with . and - as separator : r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d'
# 4. Match all phone numbers starting with 800 or 900 : r'[89]00[-.]\d\d\d[-.]\d\d\d\d'
# 5. Match all numbers in range 1 to 5 : r[1-5]
# 6. Match all lowercase a to z : r[a-z]
# 7. Match all lowercase and uppercase a to z : r[a-zA-Z]
# 8. Match everything which is not lowercase or uppercase a to z : r'[^a-zA-Z]' | caret here works like negation
# 9. Write Regular Expression to match cat,pat except bat : r'[^b]at'
# 10. Use {} quantifier to match the phone numbers : r'\d{3}.\d{3}.\d{4}'
# 11. Match all Mr. in the text : r'Mr\.'
# 12. Match all Mr and Mr. in the text : r'Mr\.?'
# 13. Match all Mr, Mr. and Initial capital letter in front of it : r'Mr\.?\s[A-Z]'
# 14. Match all Mr, Mr. and name in front of it (except single char name) : r'Mr.\?\s[A-Z]\w+'
# 15. Match all Mr, Mr. and name in front of it (Include single char name) : r'Mr.\?\s[A-Z]\w*'
# 16. Match all Mr, Mr., Mrs., Mrs, Ms, Ms. and name in front of it : r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*'
# 17. Match all emails with small and capital letters , @ , letters , .com : r'[a-zA-Z]+@[a-zA-Z]+\.com'
# 18. Allow . in first part of email : r'[a-zA-Z.]+@[a-zA-Z]+\.com'
# 19. Allow .edu as the last part of email : r'[a-zA-Z.]+@[a-zA-Z]+\.(\w{3}|edu)'
# 20. Allow 0-9 digits and - in first part of email and domain and .net as extension: r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)'

# 21. Write regular expression to match the URLs : r'https?://(www\.)?(\w+)(\.\w+)'
# 22. Print group(0), group(1), group(2), group(3)

