from os import walk
import os

clear = lambda: os.system('cls')

def get_user_input(message):
    OPTION = int(input(message))
    return OPTION

def home_screen():
    print('WELCOME TO THE NOTPAD APP')
    print('\nSelect an option below to get started!')
    print('\n1. New Note')
    print('2. Open Note')
    print('3. List Notes')
    print('4. Edit Note')
    print('5. Remove Note\n')
    print('6. Exit\n')

def process_option():
    if OPTION == 1:
        note = input('Creating a new note...\n\n\n')
        clear()
        file_name = input('Chose a name to save your note: ')

        with open('notepad_data/' + file_name + '.notepad', 'w+') as file:
            file.write(note)
            file.close
        
        print('File saved sucessfully!')
    elif OPTION == 2:
        file_name = input('Write the note name to open: ')

        if not os.path.exists('notepad_data/{}.notepad'.format(file_name)):
            print('This note does not exists!')
            exit()
        
        clear()
        with open('notepad_data/' + file_name + '.notepad', 'r+') as file:
            print(file.read())
            file.close
    elif OPTION == 3:
        clear()
        filenames = next(walk('notepad_data'), (None, None, []))[2]
        print('Found {} notes\n'.format(len(filenames)))

        for file in filenames:
            file = ''.join(file.split())[:-8]

            print('- ' + file)
    elif OPTION == 4:
        file_name = input('Chose a note to edit: ')

        if not os.path.exists('notepad_data/{}.notepad'.format(file_name)):
            print('This note does not exists!')
            exit()

        note = input('Editing {}...\n\n\n'.format(file_name))

        with open('notepad_data/' + file_name + '.notepad', 'w+') as file:
            file.write(note)
            file.close
        
        print('File saved sucessfully!')
    elif OPTION == 5:
        file_name = input('What note you want to delete? ')

        if not os.path.exists('notepad_data/{}.notepad'.format(file_name)):
            print('This note does not exists!')
            exit()

        os.remove('notepad_data/{}.notepad'.format(file_name))
    else:
        return exit()

if not os.path.exists('notepad_data'):
    os.mkdir('notepad_data')

home_screen()

OPTION = get_user_input('Select an opion: ')

process_option()