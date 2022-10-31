MAX = 999999

def TSP(mask, pos, graph, dp,n, visited):
	if mask == visited:
		return graph[pos][0]
	if dp[mask][pos] != -1:
		return dp[mask][pos]
	
	ans = MAX 
	for city in range(0, n):
		if ((mask & (1 << city)) == 0):
			new = graph[pos][city] + TSP(mask|(1<<city),city, graph, dp, n, visited)
			ans = min(ans, new)
	
	dp[mask][pos]=ans
	return dp[mask][pos]




graph = [[0, 1, 9, 8, 1, 4, 8, 3, 10, 7, 10, 8], [5, 0, 8, 6, 1, 3, 4, 1, 10, 3, 4, 10], [2, 6, 0, 6, 4, 10, 7, 5, 4, 10, 9, 10], [7, 6, 10, 0, 6, 3, 6, 6, 8, 10, 2, 8], [10, 7, 2, 5, 0, 9, 7, 2, 8, 8, 5, 8], [4, 2, 1, 3, 7, 0, 3, 9, 7, 10, 10, 1], [7, 6, 8, 6, 9, 1, 0, 10, 9, 7, 9, 10], [9, 6, 10, 9, 9, 7, 8, 0, 7, 3, 4, 10], [9, 3, 9, 4, 2, 6, 3, 3, 0, 10, 6, 5], [6, 4, 10, 8, 7, 2, 6, 10, 1, 0, 2, 9], [9, 9, 3, 1, 6, 8, 9, 8, 7, 6, 0, 2], [5, 2, 7, 8, 3, 3, 8, 4, 7, 8, 1, 0]]
n = 12
visited = (1 << n) - 1
r,c=12,4
dp=[[-1 for j in range(c)]for i in range(r)]
for i in range(0, (1<<n)):
	for j in range(0, n):
		dp[i][j] = -1

print(TSP(1, 0,graph, dp, n, visited))
