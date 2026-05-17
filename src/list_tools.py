import sys


def parse_args():
    return [int(arg) for arg in sys.argv[1:]]

def list_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def list_min(numbers):
    smallest = numbers[0]
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
    return smallest

def list_max(numbers):
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

def unique_items(numbers):
    items = []
    for num in numbers:
        if num not in items:
            items.append(num)
    return items


def compute_stats(numbers):
    count = len(numbers)

    if count == 0:
        print('No numbers provided.')
        return

    total = list_sum(numbers)

    print('count: ', count)
    print('sum: ', total)
    print('mean: ', total/count)
    print('min: ', list_min(numbers))
    print('max: ', list_max(numbers))
    print('sorted: ', sorted(numbers))
    print('unique: ', unique_items(numbers))


def main():
    numbers = parse_args()
    compute_stats(numbers)


if __name__ == "__main__":
    main()
