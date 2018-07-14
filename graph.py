import json
import networkx as nx

links = [
    ["链得得", "来源", "哈希世界研究院"],
    ["巴比特资讯", "来源", "哈希未来"],
    ["哈希世界研究院", "子品牌", "哈希未来"],
    ["腾讯网", "来源", "链得得"],
    ["搜狐", "来源", "哈希未来"],
    ["链++", "来源", "哈希未来"],
    ["火球财经", "来源", "巴比特资讯"]
]

nodes = []
edges = []

G = nx.Graph()

for link in links:
    if not link[0] in nodes:
        nodes.append(link[0])

    if not link[2] in nodes:
        nodes.append(link[2])

    edges.append((link[2], link[0]))


G.add_nodes_from(nodes)
G.add_edges_from(edges)
pos = nx.spring_layout(G, random_state=0)

nodes = [{
    "id": node,
    "name": node,
    "x": pos[node][0],
    "y": pos[node][1],
} for node in nodes]

edges = [{
    "source": link[2],
    "target": link[0],
    "meta": link[1]
} for link in links]

graph = {
    "nodes": nodes,
    "links": edges
}


print(json.dumps(graph, ensure_ascii=False, indent=4))

print(json.dumps(edges, ensure_ascii=False, indent=4))

print(graph)