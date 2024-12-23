from collections import defaultdict

from parsers.input_parser import InputParser

test_mode = False

parser = InputParser(test_mode)
parser.parse()

pairs = [item.split('-') for item in parser.get_input_lines()]

connections = defaultdict(set)

for item1, item2 in pairs:
    connections[item1].add(item2)
    connections[item2].add(item1)


def bron_kerbosch(R, P, X):
    if not P and not X:
        # Found a maximal clique
        cliques.append(list(R))
        return
    for node in list(P):
        bron_kerbosch(
            R.union([node]),
            P.intersection(connections[node]),
            X.intersection(connections[node])
        )
        P.remove(node)
        X.add(node)


cliques = []
nodes = set(connections.keys())
bron_kerbosch(set(), nodes, set())
print(cliques)

mex_len_item = max(cliques, key=len)
print(','.join(sorted(mex_len_item)))
