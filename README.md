## Open soruce Project : Solving Shortest path Problem using something



## Environment (env.py)
1) x,y 좌표(0~100)를 random generate, default 20개  
2) 시작점으로 부터 출발해 모든 점을 다 방문하면 종료된다.
3) object : 시작점으로 부터 출발해 모든 점들을 방문하는 최단 경로는? 
4) 단순 search의 경우, 모든 경로 탐색은 20! = 2432902008176640000 이므로 불가능하다 
5) 강화학습을 통해서 최단경로를 찾아보자.



## Random Mover 
1) 비교 대상을 확립하기 위해 Random Mover를 베이스라인으로 정한다
2) 시작점으로 부터 랜덤하게 방문하고, 모든 지점을 방문했으면 종료한다.
3) 하지만 Random mover는 optimal 경로가 아니다.


![random Mover](https://github.com/bongseokkim/shortest-path/blob/main/random_mover.gif)


## Reinforcement learning Approach 

1) something 
2) 





## Chatting log

|  date | name  |  |   |   |
|---|---|---|---|---|
|2021.11.26   | bongseok  | 태양광 발전 예측 문제는 너무 재미없다. 재밌는걸로 주제를 바꾸자             |   |   |
|2021.11.26   | sehan     | 솔직히 맞다. 태양광보다 실생활에 가까운걸 하자.                              |   |   |
|2021.11.26   | bongseok  | 최근에 생각한게 있는데, 택배 너무 늦게온다 이걸 풀어보자 어때                  |   |   |
|2021.11.26   | sehan     | 최단 경로 알고리즘 최근에 배웠는데, 더 좋은 방법 없을까? 고민해보자                |   |   |




## 어떤 걸 할까? 
+ 2021.11.26  : 프로젝트 주제를, 택배 배송 문제 해결로 정함. 



## 어케할까? 
+ 2021.11.26  : 일단 수업시간에 최단경로 알고리즘 배웠는데, 오픈소스를 통해 좋은 방법 할 수있는거 찾아보자 (세한).
                </br> 강화학습 최근에 공부하고 있는데 이거로 해보자 (봉석).

## 계획

|  date | name  | what to do  |   next meeting plan         |        |
|---|---|---|---|---|
|2021.11.26  ~11.29 | bongseok,sehan  |    최적경로 탐색에 대한 레퍼런스 탐색                 | 2021.11.29    |   |
|2021.11.29  ~ | bongseok,sehan  |    최적경로 탐색에 필요한 기본 클래스 구성                  | 2021.12.1    |   |
|2021.12.07   | bongseok     | 강화학습 적용을 위한, 환경 구성                |   |   |
