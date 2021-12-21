## Open soruce Project : Solving Shortest path Problem using something



## Environment (env.py)
1) x,y 좌표(0~100)를 random generate, default 20개  
2) 시작점으로 부터 출발해 모든 점을 다 방문하면 종료된다.
3) object : 시작점으로 부터 출발해 모든 점들을 방문하는 최단 경로는? 
4) 단순 search의 경우, 모든 경로 탐색은 20! = 2432902008176640000 이므로 불가능하다 
5) 강화학습을 통해서 최단경로를 찾아보자 (Euclidian Distance).



## Random Mover --version[1]
1) 비교 대상을 확립하기 위해 Random Mover를 베이스라인으로 정한다
2) 시작점으로 부터 랜덤하게 방문하고, 모든 지점을 방문했으면 종료한다.
3) 하지만 Random mover는 optimal 경로가 아니다.

![random Mover](https://github.com/bongseokkim/shortest-path/blob/main/random_mover.gif)


## Random Mover --version[2]
1) Random Mover --version[1]는 모든 가능한 경로을 랜덤해서 방문한다.
2) 하지만 방문하지 않은 경로만 방문하면 되므로 수정함

![random Mover 2](https://github.com/bongseokkim/shortest-path/blob/main/random_mover_version%5B2%5D/random_mover.gif)

## Reinforcement learning Approach (DQN)

### State 
 1) example : [1.0, 1.0, 1.0, -1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0, 1.0, -1.0, 1.0]
 2) -1은 방문하지 않은 노드를 표현, 1은 방문한 노드 

### Action 
1) 현재 노드에서 어디 노드로 방문할 것은가? [0~20] 


### Reward
1) Euclidan distance 


### Training result 
![random Mover 2](https://github.com/bongseokkim/shortest-path/blob/main/DQN_agent/performence_curve.png)

### result example 
![random Mover 2](https://github.com/bongseokkim/shortest-path/blob/main/DQN_agent/DQN_agent.gif)


