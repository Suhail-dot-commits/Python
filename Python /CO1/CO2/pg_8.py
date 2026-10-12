def longestword(word):
    max_length =len(word[0])
    for item in word:
       length=len(item)
       if length >max_length:
          max_length =length
    return max_length
words=input("enter a list of words seperated by spaces:")
word=words.split()
result=longestword(word)
print(f"the length of the longest word is: {result} ")
