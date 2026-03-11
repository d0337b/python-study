import random
secret_number =random.randint(1, 10)
attempt = 0
while True:
    guess = int(input("1 부터 10사이 숫자 맞춰보세요:"))
    attempt += 1
    if guess == secret_number:
        print("축하합니다 숫자를 맞췄습니다.")
        print("시도횟수:", attempt)
        break
    elif guess < secret_number:
        print("숫자가 너무 작습니다. 다시 시도하세요")
    else:
        print("숫자가 너무 큽니다. 다시 시도하세요")