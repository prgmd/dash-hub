from collections import deque

r, c = map(int, input().split())
world = [input() for _ in range(r)]
visited = [['#'] * c for _ in range(r)]
y, x = map(int, input().split())
cmds = input()
moveness = {'U':(-1, 0), 'R':(0, 1), 'L':(0, -1), 'D':(1, 0)}
q = deque()
y -= 1
x -= 1

for cmd in cmds:
    if cmd == 'W':
        q.append((y, x))
        visited[y][x] = '.'
        now = world[y][x]

        while q:
            ty, tx = q.popleft()
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = ty + dy, tx + dx
                if 0 <= ny < r and 0 <= nx < c and visited[ny][nx] == '#' and world[ny][nx] == now:
                    q.append((ny, nx))
                    visited[ny][nx] = '.'
    else:
        dy, dx = moveness[cmd]
        y, x = y + dy, x + dx

visited[y][x] = '.'
for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    ny, nx = y + dy, x + dx
    if 0 <= ny < r and 0 <= nx < c and visited[ny][nx] == '#':
        visited[ny][nx] = '.'

for v in visited:
    print(''.join(v))