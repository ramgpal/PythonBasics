A = [[1, 2, 3], [3, 4, 5], [6, 7, 8]] # A -> 3x3 matrics
B = [[1, 0], [1, 0], [5, 0]]          # B -> 3x2 matrics
C = [[0, 0], [0, 0], [0, 0]]          # resultant C -> 3x2 matrics
for i in range(0, len(C)):
    for j in range (0, len(C[i])):
        for k in range (0, len(B)):
            C[i][j] += A[i][k] * B[i][j]
for i in C:
    print (i)