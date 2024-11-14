def max_words_in_a_sentence(sentences):
    m=0
    for i in sentences:
        words=i.split()
        l=len(words)
        if m<l:
            m=l
    return m



sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

result = max_words_in_a_sentence(sentences)

print(result)