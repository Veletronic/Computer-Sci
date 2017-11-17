myfile = open("Mytext.txt", "w")
myfile.write("The end times are upon us!\n")
myfile.write("----------------------------------------------\n")
myfile.write("Run! RUN FOR IT!\n")
myfile.close()

handle = open ("Mytext.txt", "r")
while True:
    line = handle.readlines()
    if len(line) == 0:
        break
    print (line, end="")
handle.close()

m = open("Mytext.txt","r")
xs = m.readlines()
m.close()

xs.sort()

r = open("Random.txt", "w")
for v in xs:
    r.write(v)
r.close()

myfile = open ("somefile.zip", "w")
myfile.write("Something?\n")
myfile.close()

f = open ("somefile.txt")
content =f.read()
f.close()

words = content.split()
print("there are {0} words in the file.".format(len(words)))

f = open ("somefile.zip","rb")
g = open ("Copy.zip", "wb")
while True:
    buf = f.read(1024)
    if len(buf) == 0:
        break
    g.write(buf)
f.close()
g.close()

