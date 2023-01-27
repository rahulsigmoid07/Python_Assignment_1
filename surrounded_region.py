#taking input row number and column number
m=int(input("Enter row length for matrix: "))
n=int(input("Enter column length for matrix: "))

matrix=[]

#taking matrix as input
for i in range(0,m):
    new_list=[]
    for j in range(0,n):
        new_list.append(input())
    matrix.append(new_list)


#taking x and y as direction
x=[0,1,-1,0]
y=[-1,0,0,1]

#dfs call for recusrive call
def dfs(matrix,i,j):

    if(i>=m or j>=n or i<0 or j<0 or matrix[i][j]!='O'):
        return

    matrix[i][j]='p'
    
    for k in range(0,4):
        dfs(matrix,i+x[k],j+y[k])


#calling dfs call at boundary
for i in range(0,m):
    dfs(matrix,i,0)
    dfs(matrix,i,n-1)
for j in range(0,n):
    dfs(matrix,0,j)
    dfs(matrix,m-1,j)

#replacing '0' with 'X' and connected boundary 'P' with 'O'
for i in range(0,m):
    for j in range(0,n):
        if(matrix[i][j]=='O'):
            matrix[i][j]='X'

for i in range(0,m):
    for j in range(0,n):
        if(matrix[i][j]=='p'):
            matrix[i][j]='O'            
        
    
print(f"final Matrix: {matrix}")
