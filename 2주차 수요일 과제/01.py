def compare_two(first, second):
    i = 0
    while i < len(first) and i < len(second):
        if first[i] != second[i]:
            break
        i += 1
    common_word = first[0:i]
    return common_word


#words = list(map(str, input().split()))
words = ["apple", "apps", "ape"]
common_word = compare_two(words[0], words[1])
for i in range(2, len(words)):
    if common_word == "":
        break
    common_word = compare_two(common_word, words[i])
print(common_word)