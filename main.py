import networkx as nx 
import matplotlib.pyplot as plt

# check if colors of the neighbors of node i conflict with selcted color j
def safe_to_color(Graph,colors, i, j):
    # loop thru all the neighbors of node i
    for k in range(len(Graph[i]) - 1):
        # if there is connecting edge and the color is already j
        if Graph[i][k] and colors[k] == j:
            return False
        
    # if no conflict
    return True

# dfs backtrack recursion
def backtracking_dfs_color(Graph, N, colors, i):

    #end of graph
    if i == len(Graph): return True

    # loop thru all the possible colors for each edge
    for j in range(N):
        # check if can color the node with selected color
        if safe_to_color(Graph,colors, i, j):
            colors[i] = j
            # continue to next node
            if backtracking_dfs_color(Graph, N, colors, i+1):
                return True
            # in case of backtrack
            colors[i] = -1
        

# create a graph and color it with the colors from the Backtracking search
def visualize_graph(Graph,colors,colors_map):

    G = nx.Graph()
    node_color = []
    # create a list of colors for the nodes
    for c in colors:
        node_color.append(colors_map[c])
    for i in range(len(Graph)):
        # create and color each node
        G.add_node(i, color='r')

        # add edges to the i node
        for j in range(len(Graph[i])):
            if(Graph[i][j]):
                G.add_edge(i,j)

    # draw the graph
    nx.draw(G, with_labels = True, node_color = node_color)
    # save the graph
    plt.savefig('graph.png')
    return


# function to call to Backtracking and output the solution
def color_graph(Graph, N,colors_map):
    colors = len(Graph) * [-1] # list of colors, init to no color as -1

    # call Backtracking function
    if not backtracking_dfs_color(Graph, N, colors, 0):
        print("No possible solution for N:" + str(N))
        return False
    
    # Print the solution
    print("Solution:")
    for c in colors:
        print(c, end=' ')

    # visualize the graph
    visualize_graph(Graph,colors,colors_map)
    return True



# main function
if __name__== '__main__':
    # example input : Graph, N, colors_map

    Graph = [[0,1,1,1,1],
             [1,0,1,0,0],
             [1,1,0,1,1],
             [1,0,1,0,1],
             [1,0,1,1,0]]
    N = 4
    colors_map = ["r","g","b","y"]
    color_graph(Graph, N,colors_map)