GRID = [
    [10, 20, 30, 40],
    [5,  1,  2,  10],
    [4,  2,  1,  5 ],
    [1,  20, 30, 2 ]
]
dp=[[0]*4 for _ in range(4)]
dp[0][0]=GRID[0][0]
for j in range(1, 4):
    dp[0][j]=dp[0][j-1]+GRID[0][j]
for i in range(1, 4):
    dp[i][0]=dp[i-1][0]+GRID[i][0]
for i in range(1, 4):
    for j in range(1, 4):
        dp[i][j]=GRID[i][j]+min(dp[i-1][j], dp[i][j-1])
print(dp[3][3])
