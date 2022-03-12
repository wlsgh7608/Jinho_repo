## 탐색이란?

많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
그래프, 트리 등의 자료구조 안에서 탐색을 하는 문제를 자주 다룸
대표적인 알고리즘 - DFS(깊이우선 탐색),BFS(너비우선 탐색)

## 자료구조란?
데이터를 표현하고 관리하고 처리하기 위한 구조
대표적인 자료구조인 스택과 큐는 다음 두 핵심 함수로 구성됨
 - 삽입(Push) : 데이터를 삽입한다.
 - 삭제(Pop) : 데이터를 삭제한다.

## 스택(Stack)
스택은 FILO, LIFO 구조
  - append() : 리스트의 가장 뒤쪽에 데이터 삽입
  - pop() : 리스트의 가장 뒤쪽에서 데이터 꺼냄


## 큐(Queue)
FIFO 구조
collections 모듈에서 제공하는 deque 자료구조 활용
 - append() : 데큐의 가장 뒤쪽에 데이터 삽입
 - popleft() : 데큐의 가장 앞쪽의 데이터 꺼냄
list() - deque 객체 -> 리스트 객체

## 재귀 함수(Recursive Function)
- 자기 자신을 다시 호출하는 함수
- 컴퓨터 내부에서 재귀 함수의 수행은 스택 자료구조 이용
 - 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료 되기 때문
- 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수가 언제 끝날지, 종료 조건을 꼭 명시
ex) 팩토리얼


## DFS(Depth-First Search)
- 깊이 우선 탐색
- 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
- 스택 자료구조 이용

그래프의 기본구조
 - 노드(Node)와 간선(Edge)로 구성
그래프 표현방식
 - 인접 행렬(Adjacency Matrix) : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
 - 인접 리스트(Adjacency List) : 리스트로 그래프의 연결 관계를 표현하는 방식

인접 행렬(Adjacency Matrix)
 - 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식
 - 연결이 되어 있지 않은 노드끼리는 무한(Inf)의 비용이라고 작성
 - 모든 관계를 저장하므로 노드 개수가 많을수록 메모리 불필요하게 낭비
 - 두 노드가 연결되어 있는지 확인하는 속도가 빠름
``` python
INF = 999999

G = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]
print(G)
```
인접 리스트(Adjacency List)
 - 리스트 자료형 이용
 - 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장
 - 노드 개수가 많을수록 메모리를 효율적으로 사용
 - 두 노드가 연결되어 있는지 확인하는 속도가 느림
``` python
G = [[] for _ in range(3)] 

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
G[0].append((1,7))
G[0].append((2,5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
G[1].append((0,7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
G[2].append((0,5))

print(G)
```

## DFS 동작 과정
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드 꺼냄


# BFS(Breadth First Search)
- 너비 우선 탐색
- 가까운 노드부터 탐색하는 알고리즘
- 큐 자료구조 이용
- deque 라이브러리를 이용하는것이 바람직하다 
- 일반적으로 dfs 보다 실행속도가 빠름
## BFS 동작 과정
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리


bfs, dfs 정리
| | DFS | BFS |
|------|----|-----|
|동작 원리|스택|큐|
|구현 방법|재귀 함수 이용| 큐 자료구조 이용|