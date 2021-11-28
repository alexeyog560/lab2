import matplotlib.pyplot as plt

a = []
b = []
text =[]

file = open("DS2.txt")
with file as f:
    for line in f:
            text.append([int(x) for x in line.split()])

for i in range(len(text)):
    for j in range(1):
        a.append(text[i][0])
        b.append(960 - text[i][1])

plt.scatter(a, b)
plt.show()
plt.close()
file.close()
