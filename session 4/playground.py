import re
text = "The quick brown fox jumps oversss the lazy dog. fox is lazy abcde pqr"

grouping_pattern = r'(\b\w{5}\b).*?(\b\w{3}\b)'
grouping_match = re.search(grouping_pattern, text)
grouping_matches = re.findall(grouping_pattern, text)
# If a match is found, print the captured groups
if grouping_match:
    print("Grouping match found:")
    print("Group 1:", grouping_match.group(1))
    print("Group 2:", grouping_match.group(2))

print(grouping_matches)
