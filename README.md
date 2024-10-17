# CGT Assignment

 degree_sequence = [3, 3, 3, 3, 2, 2]

## Havel Hakimi Algorithm : 
 ```
[3, 3, 3, 3, 2, 2] --sort--> [3, 3, 3, 3, 2, 2]
[3, 3, 3, 3, 2, 2] --alg-->[2, 2, 2, 2, 2]
[2, 2, 2, 2, 2] --sort--> [2, 2, 2, 2, 2]
[2, 2, 2, 2, 2] --alg-->[1, 1, 2, 2]
[1, 1, 2, 2] --sort--> [2, 2, 1, 1]
[2, 2, 1, 1] --alg-->[1, 0, 1]
[1, 0, 1] --sort--> [1, 1, 0]
[1, 1, 0] --alg-->[0, 0]
Finished! Graph IS constructable with Havel Hakimi algorithm.
```
## Graph 
![Graph Drawing](graph.png)

## Checking Eulerian Graph and hence finding Euler path using Fluery Algorithm

```
The graph is not Eulerian. The vertices with odd degrees are: [0, 1, 2, 3]
``` 
###Weighted Graph 
![Weighted Graph](weighted.png)

##Dijkstra Algorithm Result
```
Enter the starting node for Dijkstra's algorithm: 0
{3: 8, 2: 7, 1: 14, 0: 0, 5: 15, 4: 9}
```

##Min Spanning Tree
![Min spanning Tree Diagram](min_spanning.png)


## Edge-Vertex-K-connectivity
```
Vertex Connectivity: 5
Vertices to remove to disconnect the graph: []
Edge Connectivity: 3
Edges to remove to disconnect the graph: [(3, 2), (1, 5), (0, 4)]
The graph is 5-connected.
```