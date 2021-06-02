import requests
import re

class Book:    

    def __init__(self, book_url, local_filename):

        def read_file(filename):
            """
            Read local file and return the 
            """
            with open(filename) as f:
                content = f.read().splitlines()
            return content

        def download_book(book_url, local_filename):
            """Download a book from Gutenberg

            book_url - String representing the Gutenberg file to be downloaded
            local_filename - What you want to call the file on your local machine.
            """
            r = requests.get(book_url)
            open(local_filename, 'wb').write(r.content)

        def get_word_data(text):
            word_counts = {}
            list_word_counts = []
            count = 0
            
            for line in text:
                for word in re.findall(r'\w+', line):
                    count += 1
                    lower_case_word = word.lower()
                    if not word_counts.get(lower_case_word, None):
                        word_and_count = {
                            'count': 0,
                            'word': lower_case_word
                        }
                        word_counts[lower_case_word] = word_and_count
                        list_word_counts.append(word_and_count)
                    word_counts[lower_case_word]['count'] += 1

            unique_words = []
            
            # descending_sorted_list = sorted(list_word_counts, key=lambda k: k['count'], reverse=True) 
            # ascending_sorted_list = sorted(list_word_counts, key=lambda k: k['count'])

            for word in list_word_counts:
                unique_words.append(word['word'])

            return {
                'total_words': count,
                'unique_words': unique_words,
                'word_counts': list_word_counts
            }

        def seperate_metadata_and_body(text):
            """
            Returns metadata of a gutenberg .txt file
            """
            index = 0
            while text[index][:3] != '***':
                index += 1
            return {
                'metadata': text[:index],
                'body': text[index + 1:]
            }

        def get_metadatum(metadata_fragment, attribute):
            """
            Returns the value of a specified metadata attribute
            """
            return metadata_fragment.split(attribute)[1].strip()

        download_book(book_url, local_filename)
        self.text = read_file(local_filename)

        metadata_and_body = seperate_metadata_and_body(self.text)
        self.metadata = metadata_and_body['metadata']
        self.body = metadata_and_body['body']
        
        attributes = ['Title', 'Author']
        values = {}
        for attribute in attributes:
            for line in self.metadata:
                sym = attribute + ':'
                if sym in line:
                    values[attribute.lower()] = get_metadatum(line, sym)
        
        self.title = values['title']
        self.author = values['author']
        
        word_info = get_word_data(self.body)
        word_info_with_metadata = get_word_data(self.text)
        self.unique_words = word_info['unique_words']
        self.total_words = word_info['total_words']
        self.number_of_unique_words = len(self.unique_words)
        self.word_counts = word_info['word_counts']
        self.unique_words_with_metadata = word_info_with_metadata['unique_words']
        self.total_words_with_metadata = word_info_with_metadata['total_words']
        self.number_of_unique_words_with_metadata = len(self.unique_words_with_metadata)
        self.word_counts_with_metadata = word_info_with_metadata['word_counts']

    def get_words_from_user(self):
            word = 'let us go'
            words = []
            while word != '':
                word = input("Enter your word: ")
                words.append(word)
            return words[:-1]

    def print_twenty_most_common_words(self, include_metadata=False):
        desired_list = self.word_counts
        if include_metadata:
            desired_list = self.word_counts_with_metadata
        descending_sorted_list = sorted(desired_list, key=lambda k: k['count'], reverse=True)
        message = 'Twenty Most Common Words:'
        if include_metadata:
            message = 'Twenty Most Common Words (Including MetaData):' 
        print(message)
        for word in descending_sorted_list[:20]:
            display_word = word['word']
            display_count = word['count']
            print(f'{display_word}: {display_count}')
        print()

    def print_twenty_rarest_words(self, include_metadata=False):
        desired_list = self.word_counts
        if include_metadata:
            desired_list = self.word_counts_with_metadata
        ascending_sorted_list = sorted(desired_list, key=lambda k: k['count'])
        message = 'Twenty Rarest Words:'
        if include_metadata:
            message = 'Twenty Rarest Words (Including MetaData):' 
        print(message)
        for word in ascending_sorted_list[:20]:
            display_word = word['word']
            display_count = word['count']
            print(f'{display_word}: {display_count}')
        print()

    def common_words(self, book_instance):
        words = []
        for word in self.unique_words:
            if word in book_instance.unique_words:
                words.append(word)

        return words

    def print_comparison(self):
        print('With Metadata:')
        print(f'Number of unique words: {self.number_of_unique_words_with_metadata}')
        self.print_twenty_most_common_words(True)
        self.print_twenty_rarest_words(True)
        print('Without Metadata:')
        print(f'Number of unique words: {self.number_of_unique_words}')
        self.print_twenty_most_common_words()
        self.print_twenty_rarest_words()

    def get_words_from_user_and_compare(self):
        words = self.get_words_from_user()
        words_in_text = []
        for word in words:
            if word in self.unique_words:
                words_in_text.append(word)
        print(words_in_text)

    def print_summary(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Number of unique words: {self.number_of_unique_words}')
        print(f'Number of total words: {self.total_words}')


dorian_gray = Book('https://www.gutenberg.org/files/174/174-0.txt', 'DorianGray.txt')
moby_dick = Book('https://www.gutenberg.org/files/2701/2701-0.txt', 'Moby.txt')
dollhouse = Book('https://www.gutenberg.org/files/2542/2542-0.txt', 'Dollhouse.txt')

dorian_gray.print_comparison()
moby_dick.print_comparison()
dollhouse.print_comparison()

dorian_gray.get_words_from_user_and_compare()
moby_dick.get_words_from_user_and_compare()
dollhouse.get_words_from_user_and_compare()

dorian_gray.print_summary()
moby_dick.print_summary()
dollhouse.print_summary()

dorian_gray.common_words(dollhouse)
