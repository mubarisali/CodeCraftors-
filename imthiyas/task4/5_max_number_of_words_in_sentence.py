#A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

#You are given an array of strings sentences, where each sentences[i] represents a single sentence.

#Return the maximum number of words that appear in a single sentence.

sentence=("monu","salim","salman bob","manu minu kunju")
words=0
for i in sentence:
    count=len(i.split())
    if count>words:
        words=count
    print(words)
