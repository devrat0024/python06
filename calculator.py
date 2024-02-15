name_1= input(" What is your name :")
name_2= input ("What is his/her name?")
combine_string = name_1+name_2
lower_case_string =combine_string.lower()
t = lower_case_string.count ('t')
r = lower_case_string.count ('r')
u = lower_case_string.count ('u')
e = lower_case_string.count ('e')
true = t + r + u + e

l = lower_case_string.count ('l')
o = lower_case_string.count ('o')
v = lower_case_string.count ('v')
e = lower_case_string.count ('e')
love = l + o + v + e

Love_score = int(str(true) + str(love))
if Love_score < 10  or Love_score > 90:
    print(f"your score is {Love_score}and you go together go like coke and mentos ")
elif Love_score>= 40 and Love_score <=50:
    print(f"your score is {Love_score}and you are alright together")
else :
    print(f"your score is {Love_score} ")