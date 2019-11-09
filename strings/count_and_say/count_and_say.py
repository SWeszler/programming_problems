def count_and_say(n):
    result = '1'

    for _ in range(n - 1):
        temp = ''
        count = 0
        prev = result[0]
        for i in range(len(result)):
            if result[i] != prev:
                temp += str(count) + prev
                prev = result[i]
                count = 1
            else:
                count += 1
        temp += str(count) + result[i]
        result = temp

    return result
