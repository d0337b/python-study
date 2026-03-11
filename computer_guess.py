low = 1
high = 100
print("1부터 100 사이의 숫자를 하나 생각하세요")
while True:
    gu = (low + high) // 2
    print("당신이 생각한 숫자는", gu, "입니까?")
    answer = input("맞으면 c, 더 작으면 l, 더 크면 h를 입력하세요")
    if answer == "c":
        print("맞췃지롱")
        break
    elif answer == "l":
        high = gu - 1
    elif answer == "h":
        low = gu + 1
