white = 0
blue = 0

n = int(input())  
paper = [list(map(int, input().split())) for _ in range(n)] 

def count_color(x, y, size):
    global white, blue

    color = paper[x][y]  # 기준이 될 첫 번째 칸 색

    # 전체가 같은 색인지 검사
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                new_size = size // 2
                count_color(x, y, new_size)  # 왼쪽 위
                count_color(x, y + new_size, new_size)  # 오른쪽 위
                count_color(x + new_size, y, new_size)  # 왼쪽 아래
                count_color(x + new_size, y + new_size, new_size)  # 오른쪽 아래
                return 

    # 모두 같은 색이면 해당 색 종이 개수 증가
    if color == 0:
        white += 1
    else:
        blue += 1

count_color(0, 0, n)

print(white)
print(blue)