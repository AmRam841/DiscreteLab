import pandas as pd 
from pyvis.network import Network
import networkx as nx
import pickle
import json
import heapq
import sys
import random
class Graph:
    
    class GraphVisualizer:
        
        def Visualizer():
            
            #data Loading 
            data = pd.read_csv("facebook_combined.txt" , sep=" " , header=None)
            data.columns =  ["person1" , "person2"]
            sample = data.sample(1000 , random_state=1)
            sample.head(10)

            #Constructing network graph 
            net = Network(notebook = True, cdn_resources = "remote",
                            bgcolor = "#222222",
                            font_color = "white",
                            height = "750px",
                            width = "100%",
                            select_menu = True,
                            filter_menu = True,
            )
            nodes = list(set([*sample.person1,*sample.person2]))
            edges = sample.values.tolist()
            # physics tweaks
            net.show_buttons(filter_="physics")
            net.add_nodes(nodes)
            net.add_edges(edges)
            net.show("graph_with_menu.html")
        
        
    class ShortestPath:
        
        def Random_Creat_Graph(nodes_num: int , edge_prob:float = 0.3):
            G  = nx.DiGraph()
            for i in range(nodes_num):
                G.add_node(i, weight=random.randint(1,20))
            for i in range(nodes_num):
                for j in range(nodes_num):
                    if i != j and random.random() < edge_prob:
                        G.add_edge(i,j , weight=random.randint(1,20))
            return G
           
            
            
        
        def BFS():
            
            
        
            return True
        
        def Dijkstra():
            
            
            return True
        
        
        def Bellman_Ford():
            
            
            return True
        
        
        def Floyd_Warshall():
            
            
            return True
        
        
        def johnson():
            
            
            
            return True
    class ChooseAlgoMenu:
        def ChooseAlgo():
            print("choose shortest path algo")
            algos = ["1. Dijkstra", "2. Bellman-Ford", "3. BFS (unweighted)", "4. Floyd-Warshall"]      
            for a in algos:
                print(a)
            choice = input("Enter choice number :(just a number) ").strip()
        
            return choice
    
        def run_algo(G , choice , start , end):
            # match choice:
            #     case "1":
            #         length , path = nx.single_source_dijkstra(G,start , end)
            #     case "2":
            #         length , path = nx.single_source_bellman_ford(G,start , end)
            #     case "3":
            #         length , path = nx.shortest_path(G,start , end)
            #         length = len(path) - 1
            #     case "4":
            #         all_pairs = dict(nx.floyd_warshall(G))
            #         length = all_pairs[start][end]
            #         path = nx.reconstruct_path(start, end, all_pairs) 
            #     case _ :
            #         print("invalid choice")
            #         return None , None
            
        # return length , path
            
        
            try:
                match choice:
                    case "1":
                        return nx.single_source_dijkstra(G, start, end)
                    case "2":
                        return nx.single_source_bellman_ford(G, start, end)
                    case "3":
                        path = nx.shortest_path(G, start, end)
                        return len(path) - 1, path
                    case "4":
                        dist, pred = nx.floyd_warshall_predecessor_and_distance(G)
                        return dist[start][end], nx.reconstruct_path(start, end, pred)
                    case _:
                        print("Invalid choice")
                        return None, None
            except nx.NetworkXNoPath:
                print("No path exists.")
                return None, None
    
    # says that 

