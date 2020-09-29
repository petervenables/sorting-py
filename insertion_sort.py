import words
import random

def sort(unsorted):
    # consume one input element at a time
    # remove 1 element from the input data
    # finds the location it belongs within 
    # the sorted list and inserts it there.
    for i, item in enumerate(unsorted):
        unsorted.pop(i)
        if i == 0:
            unsorted.insert(i, item)
            continue
        else:
            sorted = unsorted[:i]
            j = len(sorted)-1
            while j >= 0:
                if item > sorted[j]:
                    unsorted.insert(j+1, item)
                    break
                if j == 0:
                    unsorted.insert(j, item)
                    break
                j -= 1
    return unsorted


def main():
    print(sort(words.letter_list))
    print(sort(words.word_list))
    print(sort(words.number_list))
    print(sort(random.sample(range(1, 10000), 1000)))

if __name__ == "__main__":
    main()