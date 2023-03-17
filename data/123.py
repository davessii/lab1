f=open('app1.txt', 'w')
a = str(input())
b = str(input())
c = str(input())
f.write(a + " " + b+ " "+ c)
f.close()

line = open('app.txt')
line = line.readline()
a,b,c = line.split(" ")
a,b,c, = int(a), int(b), int(c)
print (a,b,c)
arr= []
for i in range(a):
    arr.append(b*i+c)
print (arr)

f=open('result.txt', 'w')
f.write(str(arr))
f.close()
