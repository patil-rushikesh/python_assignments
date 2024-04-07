stop_words = {'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'herself', 'it', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that'}

def remove_stop_words(text):
    words = text.split()
    result = []
    for word in words:
        if word.lower() not in stop_words:
            result.append(word)
    return ' '.join(result)

def main():
    paragraph = input("Enter a paragraph: ")

    with open("input.txt", "w") as file:
        file.write(paragraph)

    with open("input.txt", "r") as file:
        text = file.read()

    result = remove_stop_words(text)

    print("Paragraph after removing stop words:")
    print(result)

if __name__ == "__main__":
    main()
