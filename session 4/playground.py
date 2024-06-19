import re

text = "quickest The brown fox arfsgdhetd jumps overr The lazy dog. the fox."
grouping_pattern = r'(\b\w{5}\b)\s(\b\w{3}\b)'

grouping_match = re.finditer(grouping_pattern, text)
for i in grouping_match:
    print(i)
# If a match is found, print the captured groups
# if grouping_match:
#     print("Grouping match found:")
#     print("Group 1:", grouping_match.group(1))
#     print("Group 2:", grouping_match.group(2))