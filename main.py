#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will hel/p you: https://www.w3schools.com/python/ref_string_strip.asp

real_names = []

with open("./Input/Names/invited_names.txt") as names:
    content_names = names.readlines()
    for i in content_names:
        new_name = i.strip("\n")
        real_names.append(new_name)
    print(real_names)

with open("./Input/Letters/starting_letter.txt") as enter:
    letter_template = enter.readlines()

first_line = letter_template[0]

for i in range(0, len(real_names)):
    actual_line = first_line.replace("[name]", str(real_names[i]))
    letter_template[0] = actual_line
    # print(letter_template)
    new_letter = open(f"./Output/ReadyToSend/letter_{real_names[i]}.txt", "w")
    for j in letter_template:
        new_letter.write(j)



