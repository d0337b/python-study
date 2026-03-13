def counter_numbers(numbers): #빈도수 구하기
    count = {}
    for n in numbers:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    return count

def find_most_frequent(count): #최빈값 구하기
    max_number = None
    max_count = 0

    for key in count: #value 빈도수
        if count[key] > max_count:
            max_count = count[key]
            max_number = key
    return max_number

numbers = [3,7,2,9,4,10,15,7,3,7]
result = find_most_frequent(counter_numbers(numbers))
print("Most frequent number is :", result)
