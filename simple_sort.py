import words

def sort(wordlist):
    sorted = []
    for word in wordlist:
        if len(sorted) == 0:
            sorted.insert(0, word)
        else:
            pos = 0
            for i, sword in enumerate(sorted):
                if word > sword:
                    pos += 1
                    continue
                else:
                    break
            sorted.insert(pos,word)
    return sorted


def main():
    print(sort(words.word_list))


if __name__ == "__main__":
    main()