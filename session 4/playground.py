import re

text = """The quick brown fox jumps over the lazysssss dog The fox was also tired lazy133 He had a good time"""

grouping_pattern = r'(\b\w{5}\b).*?(\b\w{3}\b)'
grouping_match = re.search(grouping_pattern, text)
if grouping_match:
    print("Grouping match found:")
    print("Group 1:", grouping_match.group(1))
    print("Group 2:", grouping_match.group(2))
grouping_matches = re.findall(grouping_pattern, text)
print(grouping_matches)