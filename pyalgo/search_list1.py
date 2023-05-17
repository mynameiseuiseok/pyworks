# 순차 탐색
# 리스트의 첫번째 자료부터 하나씩 비교하면서 같은 값이 나오면
# 그 위치를 돌려주고(반환), 못 찾으면 -1을 반환함

def search_list(a, x):
    n = len(v)
    for i in range(0, n):
        if a[i] == x:
            return i
    return -1

def search_list2(a, x):
    same_num = []
    n = len(a)
    for i in range(0, n):
        if a[i] == x:
            same_num.append(i)
    # 리스트에 저장된 값이 없으면
    if len(same_num) == 0:
        # return -1
        return "값을 찾을 수 없습니다."
    else:
        return same_num

v = [60, 5, 33, 5, 12, 97, 24]

# 매개변수 - 리스트, 찾는 값
print(search_list(v, 5))   #1
print(search_list(v, 12))   #3
print(search_list(v, 100))   #3

# 중복값 위치 찾기
print(search_list2(v, 5))    # 1, 6
print(search_list2(v, 20))    # 1, 6

"""
n = len(v)

for i in range(0, n):
    if v[i] == 13:
        print("찾음")
    else:
        print("없음")
"""