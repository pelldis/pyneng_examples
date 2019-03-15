import graphviz
from draw_network_graph import draw_topology
from parse_cdp_neighbors import parse_cdp_neighbors

draw_topology(parse_cdp_neighbors('sw1_sh_cdp_neighbors.txt'), 'sw1_sh_cdp_neighbors.svg' )























