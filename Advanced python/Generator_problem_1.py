#It can be used for long datasets

def w():
    with open("test.txt") as f:
        for line in f:
            yield line

for i in w():
    print(i)