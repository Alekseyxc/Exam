import sys


def normalize(word):
    return ''.join(filter(lambda x: x.isalpha(), word)).lower()


def split_words(buffer):
    words = []
    for line in buffer:
        words.extend(normalize(i) for i in line.strip().split())
    return words



def prepare_index(buffer, index):
    for idx, paragraph in enumerate(buffer):
        words = split_words(paragraph)
        for word in words:
            if word not in index:
                index[word] = []
            index[word].append(idx)


def main(text):
    index = {}
    buffer = []
    temp_buffer = []
    with open(text) as f:
        for line in f:
            stripped = line.strip()
            if not stripped:
                buffer.append(tuple(temp_buffer[:]))
                temp_buffer = []
                continue
            temp_buffer.append(line)
    prepare_index(buffer, index)

    word = input("Введить слово для пошуку: ")
    normalized_word = normalize(word)
    if normalized_word not in index:
        print(f"Слово {word} не існує в тексті")
        sys.exit(0)
    for idx in index[normalized_word]:
        print(''.join(buffer[idx]))

if __name__ == '__main__':
    text = "text.txt"
    if len(sys.argv) > 1:
        text = sys.argv[1]
    main(text)
