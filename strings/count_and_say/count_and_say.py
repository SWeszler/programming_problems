def count_and_say(n):
    elem = '1'

    for i in range(1, n):
        prev = elem[0]
        count = 0
        new_elem = ''
        for j in range(len(elem)):
            if elem[j] == prev:
                count += 1
            else:
                new_elem += str(count) + prev
                count = 1
            prev = elem[j]

        new_elem += str(count) + prev
        elem = new_elem

    return elem