filterwords = []
f = open('filterwords.txt', 'r')
for line in f:
    filterwords.append(line.strip('\n'))
f.close()

WordInput = input('请输入一个词：')
Result = "不是敏感词~"

for w in filterwords:
    if w in WordInput:
        Result = "是敏感词！"

print(WordInput+Result)
