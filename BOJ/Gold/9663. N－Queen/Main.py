n = int(input())
board = [-1 for _ in range(n)]
answer = 0

# 배치가 가능한지 체크하는 함수
def is_can(y, x):
    # 만약 맨 윗층이라면 묻지도 말고 패스
    if y == 0:
        return True

    # y가 1층 이상일 때, 순회하며 배치 불가능한지 테스트
    for i in range(y): 
        # 같은 x값이거나 대각선이면 False
        if x == board[i] or abs(board[i] - x) == abs(y - i): 
            return False
    
    return True

# 퀸을 배치하는 함수
def queen(y):
    global answer

    if y == n: # 모두 착수가 끝남
        answer += 1
        return

    for x in range(n):
        if is_can(y, x): # y, x에 착수 가능?
            board[y] = x # y층의 x에 착수
            queen(y+1) # 다음 층으로 넘어감

queen(0)
print(answer)