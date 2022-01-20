msg = "Hello World"

for x in range(4):
    print(msg)
    print('Goodbye')

print('Done')


def sayhello5times():
    msg = "Why hello there."
    x = 1
    for x in range (1, 8):
        if x > 2:
            print(msg)
            print(x)

sayhello5times()

f = open("c://users//kcewe//dev//temp//demofile.txt", "a")
f.write ("Hey look I did a thing!")