a = [[1,2,3],
     [4,5,6],
     [6,8,9]]

def TBTproblem(a): #where "a" is a SQUARE 2D array
                   #(Hint: This being square is really important for this working properly)
    storage = 0
    currentColumn =0
    for r in range(len(a)):
        for c in range(currentColumn , len(a[r])):
            storage = a[r][c]
            a[r][c] = a[c][r]
            a[c][r] = storage
        currentColumn+=1
    for r in range(len(a)):
        for i in range(len(a[r])):
            storage = a[r][i]
            a[r][i] = a[r][len(a[r])-1-i]
            a[r][len(a[r])-1-i] = storage

    return a

ans = TBTproblem(a)
for row in ans:
    print(row)

