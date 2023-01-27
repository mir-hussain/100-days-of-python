print("Highest score finder.")

# Not using For loop

score_list = input("Enter scores in a comma separated way (eg. 15, 25, 45, 32) : \n").replace(
    " ", "").split(",")

highest_score = max(list(map(int, score_list)))

print(f"Highest score is {highest_score}")


# Using for loop

# score_list = input("Enter scores in a comma separated way (eg. 15, 25, 45, 32) : \n").replace(
#     " ", "").split(",")

# highest_score = 0

# for score in score_list:
#     if int(score) > highest_score:
#         highest_score = int(score)

# print(f"Highest score is {highest_score}")
