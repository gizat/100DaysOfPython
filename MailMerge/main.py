with open('Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()

with open('Input/Letters/starting_letter.txt') as template:
    content = template.read()
    
    for name in names:
        name = name.strip('\n')   
        letter = content.replace('[name]', name)
        with open(f'Output/ReadyToSend/letter_for_{name}.txt', mode='w') as file:
            file.write(letter)