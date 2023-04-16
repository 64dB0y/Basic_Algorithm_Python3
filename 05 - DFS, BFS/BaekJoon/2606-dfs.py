'''
1. 입력값으로 컴퓨터 개수 n과 네트워크 상 연결된 컴퓨터 쌍의 수 m을 입력받는다. 이어서 각 컴퓨터와 연결된 컴퓨터 정보를 담을 이차원 리스트 graph를 초기화한다.
2. 컴퓨터 간 연결 정보를 입력받아 graph 리스트에 저장한다. 이 때, 양방향 그래프이므로 입력받은 정보를 양쪽으로 모두 추가해준다.
3. DFS 함수를 정의한다. 현재 노드를 방문 처리하고, 바이러스 감염된 컴퓨터 수를 증가시킨다. 그리고 현재 노드와 연결된 다른 노드들에 대해 재귀적으로 DFS를 수행한다.
4. 1번 컴퓨터부터 DFS를 수행하여 바이러스 감염된 컴퓨터 수를 계산하고 출력한다. 이 때, 1번 컴퓨터 자체는 바이러스에 감염되지 않아서, 결과에서 1을 빼주어야 한다.
'''
# 컴퓨터 개수와 네트워크 상 연결된 컴퓨터 쌍의 수 입력
n = int(input())
m = int(input())

# 각 컴퓨터와 연결된 컴퓨터 정보를 담을 리스트 초기화
graph = [[] for _ in range(n+1)]

# 컴퓨터 간 연결 정보 입력
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 함수 정의
def dfs(v):
    global count
    visited[v] = True  # 현재 노드를 방문 처리
    count += 1  # 바이러스 감염된 컴퓨터 수 증가
    for i in graph[v]:  # 현재 노드와 연결된 다른 노드들에 대해
        if not visited[i]:  # 방문하지 않은 노드인 경우
            dfs(i)  # 재귀적으로 DFS 수행

# 1번 컴퓨터부터 DFS 수행
visited = [False] * (n+1)  # 각 노드의 방문 여부
count = 0  # 바이러스 감염된 컴퓨터 수
dfs(1)

# 1번 컴퓨터를 통해 감염된 컴퓨터 수 출력
print(count-1)