"""

"QAQ" is a word to denote an expression of crying. Imagine "Q" as eyes with tears and "A" as a mouth.

Now Diamond has given Bort a string consisting of only uppercase English letters of length n. There is a great number of "QAQ" in the string (Diamond is so cute!).

Bort wants to know how many subsequences "QAQ" are in the string Diamond has given. Note that the letters "QAQ" don't have to be consecutive, but the order of letters should be exact.

"""

word = input()

def QAQs(word):
    Qs = [i for i in range(len(word)) if word[i] == 'Q']
    As = [i for i in range(len(word)) if word[i] == 'A']
    qaqs = 0
    for q in Qs:
        for a in As:
            if a > q:
                qaqs += len([i for i in Qs if i > a])

    return qaqs


print(QAQs(word))
