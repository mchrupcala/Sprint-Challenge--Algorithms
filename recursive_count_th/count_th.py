'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def new_word(word, count=0, i=0):
    if i+1 == len(word) or len(word) < 2:
        return count
    elif word[i] + word[i+1] == "th":
        count += 1
    i += 1
    return new_word(word, count, i)


def count_th(word):
    return new_word(word, count=0, i=0)