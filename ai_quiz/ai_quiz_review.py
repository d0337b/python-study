#2번: 점수 평균 & 합격 여부
#사용자에게 국어, 영어, 수학 점수를 입력받고
#평균을 계산해서 출력
#평균이 60점 이상이면 합격, 아니면 불합격 출력
#힌트:

#input() 3번
#정수 변환 → 합 → 나누기 3 → if문

korea = int(input("국어 점수 입력해주세요"))
eng = int(input("영어 점수 입력해주세요"))
math = int(input("수학 점수 입력해주세요"))
totalav = (korea + eng + math) / 3
print("평균 점수는", totalav, "입니다.")
if totalav >= 60:
    print("합격")
else:
    print("불합격")
