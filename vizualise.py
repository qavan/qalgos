import matplotlib.pyplot as plt
import networkx as nx
import random


# noinspection DuplicatedCode
def vizualise_0(w):
    qg = nx.Graph()
    for elem, value in w.items():
        if value is []:
            qg.add_edge(str(elem), str(random.randint(1, len(w))), weight=0)
            continue
        for xvalue in value:
            qg.add_edge(str(elem), str(xvalue), weight=1)
    connected = [(u, v) for (u, v, d) in qg.edges(data=True) if d['weight'] == 1]
    isolated = [(u, v) for (u, v, d) in qg.edges(data=True) if d['weight'] == 0]
    pos = nx.spring_layout(qg)
    nx.draw_networkx_nodes(qg, pos, node_size=440, node_color='orange')
    nx.draw_networkx_edges(qg, pos, width=len(list(w.keys())), edge_color='b', edgelist=connected, alpha=1)
    nx.draw_networkx_edges(qg, pos, width=len(list(w.keys())), edge_color='b', edgelist=isolated, alpha=0)
    nx.draw_networkx_labels(qg, pos, font_size=16, font_family='sans-serif', font_weight='bold')
    plt.axis('on')
    plt.show()
    return True
