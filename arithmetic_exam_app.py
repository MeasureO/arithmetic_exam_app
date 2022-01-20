import random


print("Which level do you want? Enter a number:")
print("1 - simple operations with numbers 2-9")
print("2 - integral squares of 11-29")
while True:
    try:
        level = int(input())
        assert level in [1, 2]
    except ValueError:
        print("Incorrect format.")
        continue
    except AssertionError:
        print("Incorrect format.")
        continue
    else:
        break
right_answers = 0
if level == 1:
    for i in range(5):
        task = f"{random.randint(2, 9)} {random.choice('+-*')} {random.randint(2, 9)}"
        print(task)
        while True:
            try:
                answer = int(input())
            except ValueError:
                print("Incorrect format.")
                continue
            else:
                break
        # print("Right!" if eval(task) == answer else "Wrong!")
        if eval(task) == answer:
            print("Right!")
            right_answers += 1
        else:
            print("Wrong!")
elif level == 2:
    for i in range(5):
        task = random.randint(11, 29)
        print(task)
        while True:
            try:
                answer = int(input())
            except ValueError:
                print("Wrong format! Try again.")
                continue
            else:
                break
        # print("Right!" if eval(task) == answer else "Wrong!")
        if task ** 2 == answer:
            print("Right!")
            right_answers += 1
        else:
            print("Wrong!")
#print(f"Your mark is {right_answers}/5.")
print(f"Your mark is {right_answers}/5. Would you like to save the result? Enter yes or no.")
command = input()
if command in ['yes', 'YES', 'y', 'Yes']:
    print("What is your name?")
    name = input()
    with open("results.txt", 'a') as file:
        if level == 1:
            file.write(f"{name}: {right_answers}/5 in level {level} (simple operations with numbers 2-9).")
        elif level == 2:
            file.write(f"{name}: {right_answers}/5 in level {level} (integral squares of 11-29).")
    print('The results are saved in "results.txt".')


