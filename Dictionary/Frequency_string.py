#This programming is used to check the frequency of the word
n="AABBCCccdda"
freq={}

for ch in n:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)

