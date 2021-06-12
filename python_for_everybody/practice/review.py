import os

file = None

course_1_menu = {
    'a': 'list.txt',
    'b': 'dictionary.txt',
    'c': 'tuples.txt',
    'd': 'objects.txt',
    'e': 'handle.txt',
    'i': 'text_processing.txt',
    'f': 'browser.txt',
    'g': 'urllib.txt',
    'h': 'networking.txt',
    'i': 'regex.txt',
    'j': 'api.txt',
    'k': 'scraping.txt',
    'l': 'sqlite.txt',
    'm': 'web_services.txt',
    'n': 'xml.txt',
    'o': 'json.txt'
}

while True:
    while not file:
        os.system('cls' if os.name == 'nt' else 'clear')
        for k, v in course_1_menu.items():
            print(f'{k}: {v}')
        print()
        choice = input('choose file\n')
        if choice == 'q':
            quit()
        file = course_1_menu[choice]
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
