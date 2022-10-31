# Python3 implementation of the approach
V = 4
answer = []

# Function to find the minimum weight
# Hamiltonian Cycle
def tsp(graph, v, currPos, n, count, cost):

	# If last node is reached and it has
	# a link to the starting node i.e
	# the source then keep the minimum
	# value out of the total cost of
	# traversal and "ans"
	# Finally return to check for
	# more possible values
	if (count == n and graph[currPos][0]):
		answer.append(cost + graph[currPos][0])
		return

	# BACKTRACKING STEP
	# Loop to traverse the adjacency list
	# of currPos node and increasing the count
	# by 1 and cost by graph[currPos][i] value
	for i in range(n):
		if (v[i] == False and graph[currPos][i]):
			
			# Mark as visited
			v[i] = True
			tsp(graph, v, i, n, count + 1,
				cost + graph[currPos][i])
			
			# Mark ith node as unvisited
			v[i] = False

# Driver code

# n is the number of nodes i.e. V
if __name__ == '__main__':
	n = 12
	graph= [[0, 1, 9, 8, 1, 4, 8, 3, 10, 7, 10, 8], [5, 0, 8, 6, 1, 3, 4, 1, 10, 3, 4, 10], [2, 6, 0, 6, 4, 10, 7, 5, 4, 10, 9, 10], [7, 6, 10, 0, 6, 3, 6, 6, 8, 10, 2, 8], [10, 7, 2, 5, 0, 9, 7, 2, 8, 8, 5, 8], [4, 2, 1, 3, 7, 0, 3, 9, 7, 10, 10, 1], [7, 6, 8, 6, 9, 1, 0, 10, 9, 7, 9, 10], [9, 6, 10, 9, 9, 7, 8, 0, 7, 3, 4, 10], [9, 3, 9, 4, 2, 6, 3, 3, 0, 10, 6, 5], [6, 4, 10, 8, 7, 2, 6, 10, 1, 0, 2, 9], [9, 9, 3, 1, 6, 8, 9, 8, 7, 6, 0, 2], [5, 2, 7, 8, 3, 3, 8, 4, 7, 8, 1, 0]]
   

    # Boolean array to check if a node
	# has been visited or not
	v = [False for i in range(n)]
	
	# Mark 0th node as visited
	v[0] = True

	# Find the minimum weight Hamiltonian Cycle
	tsp(graph, v, 0, n, 1, 0)

	# ans is the minimum weight Hamiltonian Cycle
	print(min(answer))

# This code is contributed by mohit kumar

