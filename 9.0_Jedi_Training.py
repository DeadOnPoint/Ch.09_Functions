#Sign your name: Will Jacobson


#1.) Correct the following code: (The user's number should be increased by 1 and printed.)

def increase(x):
    return x + 1

x = int(input("Enter a number: "))
x = increase(x)
print("Your number has been increased to", x)




#2.) Correct the following code to print 1-10:

def count_to_ten():
    for i in range(0,10):
        print(i)

count_to_ten()



#3.) Correct the following code to sum the list:

def sum_list(list):
    sum = 0
    for i in list:
        sum = i + sum
    return sum

sum = sum_list([45, 2, 10, -5, 100])
print(sum)




#4.) Correct the following code which should reverse the sentence that is entered.

def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(1,text_length + 1):
        result = result + text[i * -1]
    return result

text = input("Enter a sentence: ")
text = reverse(text)
print(text)



#5.) Correct the following code: (if one of the options is not entered it should print the statements)

def get_user_choice():
    while True:
        command = input("Command: ")
        if command == "f" or command == "m" or command == "s" or command == "d" or command == "q":
            return command
        else:
            print("Hey, that's not a command. Here are your options:" )
            print("f - Full speed ahead")
            print("m - Moderate speed")
            print("s - Status")
            print("d - Drink")
            print("q - Quit")

command = get_user_choice()
print("You entered:", command)

