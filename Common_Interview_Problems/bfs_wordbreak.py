def word_break(words):
    broken_words = []
    def recurse(word):
        results = []
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            #keep prefix, recurse suffix
            # print(prefix)
            # print(suffix)
            if prefix in words:
                if len(suffix) != 0:
                    results += ([prefix] + recurse(suffix))
                else:
                    results += ([prefix])
        if word in words:
            results += ([word])
        return results
    for word in words:
        result = recurse(word)
        result.remove(word)
        broken_words.append(result)
    return broken_words
print(word_break(["superhighway", "super", "high", "way", "highway"]))