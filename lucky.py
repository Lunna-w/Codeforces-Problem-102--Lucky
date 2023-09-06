t = int(input())

for i in range(t):
    n = input()

 
    begin = sum(int(char) for char in n[:3])
    end = sum(int(char) for char in n[-3:])

    if begin == end:
        print("YES")
    else:
        print("NO")
