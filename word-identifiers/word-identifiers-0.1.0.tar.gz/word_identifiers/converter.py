from .wordlist import wordlist

reverse_wordlist = {w: i for i, w in enumerate(wordlist)}


def words_to_id(words):
    if not isinstance(words, list) or not all(isinstance(word, str) for word in words) or not words:
        raise ValueError("words_to_id must be called on a nonempty list of strings")
    if words[0] == wordlist[0]:
        raise ValueError("cannot start with the first word in the wordlist")
    result = 0
    for word in words:
        result *= len(wordlist)
        if word not in reverse_wordlist:
            raise ValueError("Word not in standard wordlist {word}".format(word=word))
        result += reverse_wordlist[word]
    return result - 1

def id_to_words(identifier):
    if not isinstance(identifier, int):
        raise ValueError("id_to_words must be called on an integer")
    identifier += 1
    words = []
    while identifier:
        words.append(wordlist[identifier % len(wordlist)])
        identifier //= len(wordlist)
    return words[::-1]
