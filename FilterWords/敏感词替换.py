# 将filterwords.txt转成列表形式
filterwords = []
f = open('filterwords.txt', 'r')
for line in f:
    filterwords.append(line.strip('\n'))
f.close()

SentenceInput = input('请输入一段话：')
NewSentence = SentenceInput
input('如果你的输入中有敏感词，敏感词将会被替换。')

# 替换敏感词
for w in filterwords:
    if w in SentenceInput:
        NewSentence = SentenceInput.replace(w, '**')
print(NewSentence)
