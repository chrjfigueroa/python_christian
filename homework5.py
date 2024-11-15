import numpy as np

"""
 1. The Odd Ones Out
"""

cluster_magnitudes = np.array([[1,2,3],[5,7,9],[2,4,6],[7,7,7]])

def odd_clusters(magnitudes):
    # Returns an 2d array of magnitudes in a cluster which are all odd.
    odd_magnitudes = []

    for cluster in magnitudes:
        total_odds = 0

        for magnitude in cluster:
            if magnitude % 2 == 1:
                total_odds += 1
        
        if total_odds == len(cluster):
            odd_magnitudes.append(cluster)
    
    return np.array(odd_magnitudes)

odd_magnitudes = odd_clusters(cluster_magnitudes)

print(odd_magnitudes)


"""
2. Let's Play Checker's
"""

def checkers():

    # 2.1: create an 8 by 8 matrix
    grid = []
    for i in range(8):
        row=[]
        for j in range(8):
            row.append(0)
        grid.append(row)

    # 2.2: 1's on the odd rows/columns
    for i in range(4):
        for j in range(4):
            grid[2*i][2*j] = 1

    # 2.3: 1's on the even rows/columns
    for i in range(4):
        for j in range(4):
            grid[2*i+1][2*j+1] = 1

    return np.array(grid)

checkerboard = checkers()
print(checkerboard)

# 2.4

def reverse_checkers():

    grid = []
    for i in range(8):
        row=[]
        for j in range(8):
            row.append(1)
        grid.append(row)

    for i in range(4):
        for j in range(4):
            grid[2*i][2*j] = 0

    for i in range(4):
        for j in range(4):
            grid[2*i+1][2*j+1] = 0

    return np.array(grid)

reverse_checkerboard = reverse_checkers()
print(reverse_checkerboard)


"""
3. The Expanding Universe
"""
universe = np.array(['galaxy','clusters'])
def expansion(words, space):
    # Returns array with number (space) of space between each letter in original array.""
    expanded = []

    for word in words:
        letters = list(word)

        for i in range(len(letters)-1):
            for j in range(space):
                letters[i] += " "

            expanded_letters = "".join(letters)
        expanded.append([expanded_letters])

    return np.array(expanded)
        
expanded_letters = expansion(universe, 11)
print(expanded_letters)


"""
4. While studying exoplanets, you decide to identify only the second-largest planet
in each system. Write a function that takes a 2D numpy array and returns an
array containing only the second-largest value in each column (system).
"""

planet_sizes = np.random.randint(100,1000,(5,5))

def second_largest(array_2D):
    second_large = []
    
    for system in array_2D:

        max = np.max(system)
        index = np.argwhere(system == max)
        new_system = np.delete(system,index)
        
        np.sort(new_system)
        
        new_max = new_system[-1]
        second_large.append([new_max])
    
    return np.array(second_large)

second_largest_planets = second_largest(planet_sizes)
print(second_largest_planets)