from task_2 import logger

@logger('path.log')
def flat_generator(list_of_lists):
    list_1 = sum(list_of_lists, [])
    cursor = 0
    while cursor < len(list_1):
        yield list_1[cursor]
        cursor += 1


if __name__ == '__main__':
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    for i in flat_generator(list_of_lists_1):
        print(i)
