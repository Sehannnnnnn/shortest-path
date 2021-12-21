## Project : Solving TSP Using Reinforcement learning
solving TSP using simple Reinforcement learning (DQN)
+ Initially, this project was intended to solve the problem of courier delivery.
+ See test.ipynb for all implementations (colab).
+ [TSP?](https://en.wikipedia.org/wiki/Travelling_salesman_problem)

## Environment description 
+ The environment acts as a simulator.
1) Define the TSP problem by creating random coordinates.  
2) It starts from the starting point and ends when all points are visited.
3) object : What is the shortest path to visit all the points from the starting point?
4) Given 20 nodes, the number of possible paths is 20!(2.432902e+18); if the number of nodes increases, the number of possible paths increases exponentially.
5) **Try to find the best approximation solution through reinforcement learning.**



## Random Mover --version[1]
1) Early in the project, it was created to establish a comparison target.
2) it has a random visit strategy among 0-20 nodes at the current node.
3) One day the random agent will visit all nodes, but it is not the best route.

![random Mover](https://github.com/bongseokkim/shortest-path/blob/main/random_mover.gif)


## Random Mover --version[2]
1) It is similar to v[1], but it is not always randomly visited among 0-20 nodes; it randomly visits among the nodes that have not been visited.
2) But it's not a reasonable optimal path either

![random Mover 2](https://github.com/bongseokkim/shortest-path/blob/main/random_mover_version%5B2%5D/random_mover.gif)

## Reinforcement learning Approach (DQN)
It is already known that the TSP problem is impossible to obtain a clear solution within polynomial time.
so there are many algorithms that calculate a good enough approximation 
**This project used a simple reinforcement learning algorithm, DQN.**

## MDP 
It's very simple, and there's probably a better way to construct the MDP.

### State 
 1) example : [1.0, 1.0, 1.0, -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0, 1.0, -1.0, 1.0]
 2) Represented in vector form, 1 represents the node that has not visited -1.

### Action 
1) Where will the agent visit from current node to else [0–20]

### Reward
1) Defines as a simple Euclidean distance.

### Note
+ We have had many trial and error.
+ The agent first visits the node with the highest Q-value value among the nodes to visit.
+ It was advantageous to explore other nodes with low probability.
+ Sets the initial start node to random; lets the agent solve the problem in a variety of ways.

### Training result 
+ We tried to solve the problem as simply as possible, episode :3000 
+ RL-agents find an approximate optimal path in a short time; it takes about two to three minutes to train.
+ If you increase the episode and apply various additional techniques, you can expect better results.
![random Mover 2](https://github.com/bongseokkim/shortest-path/blob/main/DQN_agent/performence_curve.png)

### result example 
![random Mover 2](https://github.com/bongseokkim/shortest-path/blob/main/DQN_agent/DQN_agent.gif)


## Reference
+ https://github.com/seungeunrho/minimalRL , DQN implementation
+ https://github.com/kairess/traveling-salesman-problem, TSP Environment Implementation
+ https://ita9naiwa.github.io/reinforcement%20learning/2019/08/27/CombOpt.html, TSP background


## Dependency
+ train.ipynb is implemented using colab
+ pytorch 1.10.0+cu111
+ numpy 1.19.5
