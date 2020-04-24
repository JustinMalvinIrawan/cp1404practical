def main():
    words_to_be_counted = {}
    input_text = input("Text:")
    words = input_text.split()
    for word in words:
        words_frequency = words_to_be_counted.get(word,0)
        words_to_be_counted[word] = words_frequency + 1

    words = list(words_to_be_counted.keys())
    words.sort()

    max_length = max((len(word) for word in words))
    for word in words:
        print("{:{}} : {}".format(word, max_length, words_to_be_counted[word]))


if __name__ == '__main__':
    main()