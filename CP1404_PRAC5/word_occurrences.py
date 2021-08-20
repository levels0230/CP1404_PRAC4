count_word = {}
Text = input("Enter the text: ")
word = Text.split()
words = Text.split()

for word in words:
    frequent = count_word.get(word, 0)
    count_word[word] = frequent + 1
words = list(count_word.keys())
words.sort()
max = max((len(word) for word in words))

for word in words:
    print("{:{}} : {}".format(word, max, count_word[word]))