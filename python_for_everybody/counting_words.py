file_name = input('Enter a file: ')
try:
    handle = open(file_name)
except:
    quit()

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

max = 0
big_word = None
for word, count in counts.items():
    if count > max:
        max = count
        big_word = word

print(big_word, max)