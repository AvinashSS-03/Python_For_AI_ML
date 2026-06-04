a=input()
words=a.split()
longest=max(words, key=len)
print(longest)