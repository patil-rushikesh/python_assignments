def count_words_chars_lines(f):
    total_chars = 0
    total_words = 0
    total_lines = 0
    word_frequency = {}

    with open(f, 'r') as file:
        lines = file.readlines()

    for line in lines:
        total_lines += 1
        total_chars += len(line)
        total_words += len(line.split())
        for word in line.split():
            if word not in word_frequency:
                word_frequency[word] = 1
            else:
                word_frequency[word] += 1

    print("Total characters:", total_chars)
    print("Total words:", total_words)
    print("Total lines:", total_lines)
    print("Word frequencies:")
    for word, freq in word_frequency.items():
        print(f"{word}: {freq}")

file = "xyz.txt"
count_words_chars_lines(file)
