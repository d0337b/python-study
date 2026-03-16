scores = {
    "철수": 85,
    "영희": 92,
    "민수": 78
}
for name, score in scores.items():
    print(f"{name}: {score}점")

max_score = max(scores.values())

for name, score in scores.items():
    if score == max_score:
        print(name, "가 가장 높은 점수입니다:", score)