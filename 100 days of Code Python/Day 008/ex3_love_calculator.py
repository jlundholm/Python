true_list = ["t", "r", "u", "e"]
love_list = ["l", "o", "v", "e"]

def calculate_love_score(name1, name2):
    count1 = 0
    count2 = 0
    for letter in name1:
        if letter in true_list:
            count1 += 1
    for letter in name2:
        if letter in true_list:
            count1 += 1
    for letter in name1:
        if letter in love_list:
            count2 += 1
    for letter in name2:
        if letter in love_list:
            count2 += 1
    print(f"{count1}{count2}")


calculate_love_score("Angela Yu", "Jack Bauer")
