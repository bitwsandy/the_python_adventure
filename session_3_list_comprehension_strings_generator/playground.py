paragraph = "spark hadoop spark spark kafka hadoop kafka"
words = paragraph.split(" ")
word_freq = {}
print(words)
# ['spark', 'hadoop', 'spark', 'spark', 'kafka', 'hadoop', 'kafka']
for word in words:
    word = word.lower()
    word_freq[word] = word_freq.get(word, 0) + 1
# Ist Iteration Start :  wf = {}
# spark
# word_freq['spark'] = word_freq.get('spark', 0) + 1
# word_freq['spark'] = 0 + 1
# word_freq['spark'] = 1
# Ist Iteration End :  wf = {'spark':1}

# 2nd Iteration Start :  wf = {'spark':1}
# hadoop
# word_freq['hadoop'] = word_freq.get('hadoop', 0) + 1
# word_freq['hadoop'] = 0 + 1
# word_freq['hadoop'] = 1
# 2nd Iteration End :  wf = {'spark':1, hadoop: 1}

# 3rd Iteration Start :  wf = {'spark':1, hadoop: 1}
# hadoop
# word_freq['spark'] = word_freq.get('spark', 0) + 1
# word_freq['spark'] = 1 + 1
# word_freq['spark'] = 2
# 2nd Iteration End :  wf = {'spark':2, hadoop: 1}


# sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
# for word, freq in sorted_word_freq:
#     print(f"{word}: {freq}")
