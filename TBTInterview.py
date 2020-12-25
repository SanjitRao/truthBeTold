a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

def TBTproblem(a): #where "a" is a 2D array
    storage = 0
    currentColumn =0
    for r in range(len(a)):
        for c in range(currentColumn , len(a[r])):
            storage = a[r][c]
            a[r][c] = a[c][r]
            a[c][r] = storage
        currentColumn+=1
    for r in range(len(a)):
        for i in range(int(len(a[r])/2)):
            storage = a[r][i]
            a[r][i] = a[r][len(a[r])-1-i]
            a[r][len(a[r])-1-i] = storage

    return a

ans = TBTproblem(a)
for row in ans:
    print (row)

