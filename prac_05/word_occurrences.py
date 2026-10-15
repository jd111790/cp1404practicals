"""
Word Occurrences
Estimate: 30 minutes
Actual:    minutes
"""

"""
this is a collection of words of nice words this is a fun thing it is
"""
word_count = {}
user_string = input("Text: ")
i = 0
key = ""
while i <= len(user_string):
    try:
        if user_string[i] == " ":
            # print(key)
            if key in word_count.keys():
                word_count[key] += 1
            else:
                word_count[key] = 1
            key = ""
        else:
            key += user_string[i]
        # print(key)
        i += 1
    except IndexError:
        if key in word_count.keys():
            word_count[key] += 1
        else:
            word_count[key] = 1
        key = ""
        i += 1
print(word_count.items())