file1 = "/home/agoyal/Desktop/diff/server1.txt"
clean1 = "/home/agoyal/Desktop/diff/clean1.txt"
clean2 = "/home/agoyal/Desktop/diff/clean2.txt"
file2 = "/home/agoyal/Desktop/diff/server2.txt"

with open(file2, "r") as f, open(clean2, "a") as c:
    for line in f:
        if "|" in line:
           line = line.split("|")[1]
        c.write(line)
c.close()
f.close()

