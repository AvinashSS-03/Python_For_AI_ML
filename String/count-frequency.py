a=input()
freq={}
for ch in a:
    freq[ch]=freq.get(ch,0)+1
print(freq)