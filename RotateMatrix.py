'''
You are given a n x n 2D matrix A representing an image.
Rotate the image by 90 degrees (clockwise).

PS: You aren't allowed to create an additional array

Input
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
 ]

Output
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
 ]
'''

row = int(input("Enter the number of rows : "))
col = int(input("Enter the number of colomns : "))
mat = [[int(input()) for x in range (col)] for y in range(row)]

# transpose matrix
for i in range(0, row):
    for j in range(0, i):
        mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

# reverse the row
for i in range(0,row):
    for j in range(0,col//2):
        mat[i][j], mat[i][col-j-1] = mat[i][col-j-1],mat[i][j]

for i in range(row):
    for j in range(col):
        print(mat[i][j], end = " ")
    print()
