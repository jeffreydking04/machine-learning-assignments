import os

file = None

menu = {
    'x': 'indexing.txt',
    'a': 'introduction.txt',
    'b': 'np.txt',
    'c': 'np.2.txt',
    'd': 'pandas.txt',
    'e': 'df.txt',
    'f': 'data_cleaning.txt',
    'g': 'dc2.txt',
    'h': 'dupes.txt',
    'i': 'plotting.txt',
    'j': 'reading.txt',
    'k': 'np_adv.txt',
    'z': 'postgresql.txt'
}

while True:
    while not file:
        os.system('cls' if os.name == 'nt' else 'clear')
        for k, v in menu.items():
            print(f'{k}: {v}')
        print()
        choice = input('choose file\n')
        if choice == 'q':
            quit()
        file = menu[choice]
        try:
            fhand = open(file)
        except:
            print('Invalid choice')
            file = None

    question = True
    for line in fhand:
        if question:
            os.system('cls' if os.name == 'nt' else 'clear')
            answer = input(line + '\n')
            if answer == 'q':
                print()
                break
            question = False
        else:
            print()
            input(line)
            question = True
    file = None
