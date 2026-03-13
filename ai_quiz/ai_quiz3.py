def count_fruits(quiz_list): #ai 퀴즈 어려엉
    quiz_dict = {}
    for n in quiz_list:
        if n in quiz_dict:
                quiz_dict[n] += 1
        else:
                quiz_dict[n] = 1
    return quiz_dict

def find_most_frequent(quiz_dict):
    max_fruit = None
    max_count = 0

    for key,value in quiz_dict.items():
        if value > max_count:
             max_count = value
             max_fruit = key
    return max_fruit

quiz_list = ["apple","banana","apple","orange","banana","apple"]
result = find_most_frequent(count_fruits(quiz_list))
print("Most frequent fruit is :",result)