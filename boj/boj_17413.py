import sys
input = sys.stdin.readline

S = input().rstrip()

result = []
temp_str = ''
in_tag = False

for char in S:
    if char == '<':  # 태그의 시작을 만났을 때
        if temp_str:  # 만약 그 전에 단어가 있으면 뒤집어서 결과에 추가
            result.append(temp_str[::-1])
            temp_str = ''  # 단어 초기화
        in_tag = True  # 태그 안에 있다는 표시
        result.append(char)  # '<' 문자 그대로 추가
    elif char == '>':  # 태그의 끝을 만났을 때
        in_tag = False  # 태그가 끝났으므로 표시 제거
        result.append(char)  # '>' 문자 그대로 추가
    elif in_tag:  # 태그 안에 있는 동안에는
        result.append(char)  # 태그 안의 문자는 그대로 추가
    elif char == ' ':  # 공백을 만나면
        result.append(temp_str[::-1])  # 지금까지의 단어를 뒤집어서 추가
        result.append(' ')  # 공백 그대로 추가
        temp_str = ''  # 단어 초기화
    else:  # 태그 밖에서 단어를 만났을 때
        temp_str += char  # 단어를 계속 저장

if temp_str:
    result.append(temp_str[::-1])

print(''.join(result))