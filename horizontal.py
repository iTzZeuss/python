user_nums = []
first_addend = []
second_addend = []
results = []
dash_lines = []

print("Welcome to the mathematical arranger. This script takes numbers from user and prints the results in a horizontal formula.")

inp = int(input("How many operations do you want? (up to 5)"))
for num in range(int(inp)):
    if range(inp) == 1:
        inp2 = input("Give your first operation (in x + y or x - y form)")
        user_nums.append(inp2)
    elif range(inp) == 2:
        inp2 = input("Give your second operation (in x + y or x - y form)")
        user_nums.append(inp2)
    elif range(inp) == 3:
        inp2 = input("Give your third operation (in x + y or x - y form)")
        user_nums.append(inp2)
    elif range(inp) == 4:
        inp2 = input("Give your fourth operation (in x + y or x - y form)")
        user_nums.append(inp2)
    elif range(inp) == 5:
        inp2 = input("Give your second operation (in x + y or x - y form)")
        user_nums.append(inp2)
        user_nums.append(inp2)

def arithmetic_arranger(problems, show_answers=True): 
    for problem in problems:
        parts = problem.split()
    return problems

def first_row(problems):
    for problem in problems:
        parts = problem.split()
        one = parts[0]
        first_addend.append(one)

def second_row(problems):
    for problem in problems:
        parts = problem.split()    
        second_addend.append(parts[1])
        second_addend.append(parts[2])
     
def calculate(problems):    #calculating results
    for problem in problems:
        parts = problem.split()
        if parts[1] == '+':
            sum1 = int(parts[0]) + int(parts[2])
            results.append(sum1)
        elif parts[1] == '-':
            sum1 = int(parts[0]) - int(parts[2])
            results.append(sum1)
arithmetic_arranger(user_nums)
text = arithmetic_arranger(user_nums)
first_row(text)
second_row(text)
calculate(text)
for num in range(len(text)):    
    length = max(len(first_addend[num]), len(second_addend[num])) + 2
    line = length*'-'
    dash_lines.append(line)
def printer(first_row, second_row, answers=True):
    #checking how many times it will print
    if len(first_addend) == 1:
        print("    ".join(str(num).rjust(6) for num in first_addend))
        print(second_row[0], second_row[1].rjust(length - 1), "\n",length*'-')
        print(" ","     ".join(dash_lines))
        res = str(results[0])
        if answers == True:
            print("    ".join(str(res).rjust(6) for res in results))

    elif len(first_addend) == 2:
        print("    ".join(str(num).rjust(6) for num in first_addend))
        print(second_row[0], second_row[1].rjust(length - 1),"  ",second_row[2], second_row[3].rjust(length - 1))
        print(" ","     ".join(dash_lines))
        res = str(results[0])
        if answers == True:
            print("    ".join(str(res).rjust(6) for res in results))

    elif len(first_addend) == 3:
        print("    ".join(str(num).rjust(6) for num in first_addend))
        print(first_row[0].rjust(length + 1),"  ",first_row[1].rjust(length + 1),"  ",first_row[2].rjust(length + 1),"  ",first_row[3].rjust(length + 1),"  ",first_row[4].rjust(length + 1))
        print(" ","     ".join(dash_lines))
        res = str(results[0])
        if answers == True:
            print("    ".join(str(res).rjust(6) for res in results))

    elif len(first_addend) == 4:
        print("    ".join(str(num).rjust(6) for num in first_addend))
        print(second_row[0], second_row[1].rjust(length - 1),"  ",second_row[2], second_row[3].rjust(length - 1),"  ",second_row[4], second_row[5].rjust(length - 1),"  ",second_row[6], second_row[7].rjust(length - 1))
        print(" ","     ".join(dash_lines))
        res = str(results[0])
        if answers == True:
            print("    ".join(str(res).rjust(6) for res in results))


    elif len(first_addend) == 5:
        print("    ".join(str(num).rjust(6) for num in first_addend))
        print(second_row[0], second_row[1].rjust(length - 1),"  ",second_row[2], second_row[3].rjust(length - 1),"  ",second_row[4], second_row[5].rjust(length - 1),"  ",second_row[6], second_row[7].rjust(length - 1),"  ",second_row[8], second_row[9].rjust(length - 1))
        print(" ","     ".join(dash_lines))
        res = str(results[0])
        if answers == True:
            print("    ".join(str(res).rjust(6) for res in results))
           
printer(first_addend, second_addend, answers=True)