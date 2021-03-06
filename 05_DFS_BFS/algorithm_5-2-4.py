from collections import deque

# BSF : Breadth First Search
# 너비 우선 탐색이라고도 부르며, 가까운 노드부터 탐색하는 알고리즘
# DFS는 최대한 멀리 있는 노드를 우선으로 탐색하는 방식으로 동작하는데
# BFS는 그 반대다.

# BFS는 큐 자료구조를 이용하며 구체적인 동작 과정은 다음과 같다.
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를
#    모두 큐에 삽입하고 방문 처리를 한다.
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Quequ) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반봅
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)

# DFS와 BFS
# 동작 원리 DFS: 스택, BFS : 큐
# 구현 방법 DFS: 재귀 함수 이용 BFS: 큐 자료구조 이용
