def find_anagrams(word, candidates):
    dic = {}
    n = len(word)
    out = []
    for letter in word.lower():
        if letter in dic:
            dic[letter] += 1
        else:
            dic[letter] = 0


    for option in candidates:
        d = dic.copy()
        if len(option) == n and option.lower() != word.lower():
            for letter in option.lower():
                if letter in d:
                    if d[letter] == 0:
                        d.pop(letter)
                    else:
                        d[letter] -= 1
        if len(d) == 0:
            out.append(option)

    return out