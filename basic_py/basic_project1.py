scores = []

while True:
    print("======= 점수관리 program =======")
    print(" 1. 점수 추가")
    print(" 2. 점수 목록 보기")
    print(" 3. 평균 점수 보기")
    print(" 4. 종료")

    choice = int(input("메뉴를 선택하세요: "))

    if choice == 1:
        score = int(input("추가할 점수를 입력하세요"))
        scores.append(score)
        print("점수가 추가되었습니다. \n")
    elif choice == 2:
        if len(scores) == 0:
            print("점수가 없습니다. \n")
        else:
            print("현재 점수 목록:", scores, "\n")
    elif choice == 3:
        if len(scores) == 0:
            print("현재 점수가 없습니다. \n")
        else:
            average = sum(scores) / len(scores)
            print("평균 점수:", average, "\n")
    elif choice == 4:
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 선택입니다. \n")
