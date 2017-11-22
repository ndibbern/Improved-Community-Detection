import networkx as nx
import matplotlib.pyplot as plt

'''
# Description
Use this module for plotting and saving plots of clusters

# More information
https://networkx.github.io/documentation/stable/tutorial.html#nodes
'''

def plot_G(G, coordinates, classes):
    '''
    # Inputs
    G: an nx graph to be plotted
    coordinates: a map that specifies the coordinates of each node in G
    classes: a list that with the classes of the nodes, to give each class a unique color
    '''
    plt.plot()
    nx.draw(G, coordinates, with_labels=True, node_color=classes)
    plt.show()

def save_G(G, file_name):
    '''
    # Inputs
    file_name: the name of the image to hold the plot
    '''
    plt.plot()
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.savefig("{}.png".format(file_name))

if __name__ == '__main__':
    G = nx.Graph()
    G.add_node(1)
    G.add_nodes_from([2, 3, 4, 5])
    G.add_edge(1, 2)
    G.add_edges_from([(3, 4), (4, 5), (3, 5)])
    plot_G(G)
