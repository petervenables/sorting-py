import words

def swap(list, left, right):
    temp = list[left]
    list[left] = list[right]
    list[right] = temp


def partition(list, lidx, hidx):
    pivot = lidx
    i = lidx
    while i < hidx:
        if list[i] < list[hidx]:
            swap(list, i, pivot)
            pivot += 1
        i += 1
    swap(list, hidx, pivot)
    return pivot


def sort(list, lidx=0, hidx=None):
    if len(list) == 0:
        return []

    if hidx == None:
        hidx = len(list) - 1

    if lidx < hidx:
        pivot = partition(list, lidx, hidx)
        sort(list, lidx, pivot - 1)
        sort(list, pivot + 1, hidx)

    return list

def main():
    print(sort(words.word_list))

if __name__ == "__main__":
    main()