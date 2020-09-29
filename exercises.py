def is_multiple(n, m):
    """True if n is a multiple of m"""
    return not n % m


def is_even(k):
    return not k % 2


def minmax(data):
    min = max = data[0]
    for d in data:
        min = d if d < min else min
        max = d if d > max else max
    return min, max


def minmax(data):
    """copyed from site https://codeleading.com/article/83702969426/"""
    data.sort()
    return data[0], data[-1]


def sum_squares(n):
    result = 0
    for i in range(n):
        result += i ** 2
    return result


def comprehension_sum_squares(n):
    return sum([i ** 2 for i in range(n)])


def sum_odd_squares(n):
    result = 0
    for i in range(n):
        if bool(i % 2):
            result += i ** 2
    return result


def sum_odd_squares_v2(n):
    result = 0
    for i in range(1, n, 2):
        result += i ** 2
    return result


def comprehension_sum_odd_squares(n):
    return sum([i ** 2 for i in range(n) if bool(i % 2)])


# Python list comprehension syntax to produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256]
a = [2 ** x for x in range(9)]


def par_product_odd(int_sequence):
    s = 0
    odd_numbers = []
    for x in int_sequence:
        if bool(x % 2) and x not in odd_numbers:
            s += 1
            odd_numbers.append(x)
        if s == 2:
            return True
    return False


def is_distinct(int_sequence):
    int_sequence.sort()
    for i in range(1, len(int_sequence)):
        if int_sequence[i] == int_sequence[i - 1]:
            return False
    return True


def scale(data, factor):
    """esta versao nao funciona pois os numeros sao imataveis
        ao multiplicar cria nova instancia do numero resultando"""
    for val in data:
        val *= factor


def scale_v2(data, factor):
    for i in range(len(data)):
        data[i] *= factor


# list comprehension syntax to produce the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
[sum(2 * i for i in range(n)) for n in range(1, 11)]

# list comprehension syntax to produce the list [ a , b , c , ..., z ]
[chr(x) for x in range(97, 123)]


def readLineFromConsole():
    record = []
    try:
        item = input()
        while item != 'ctrl-D':
            record.append(item)
            item = input()
    except EOFError:
        print('EOFError')

    for i in range(len(record) - 1, -1, -1):
        print(record[i])


def dot_product(list_a, list_b):
    result = []
    for i in range(len(list_a)):
        result.append(list_a[i] * list_b[i])
    return result


def dot_product_v2(list_a, list_b):
    return [list_a[i] * list_b[i] for i in range(len(la))]


def write_on_list(list_a, index, value):
    try:
        list_a[index] = value
    except IndexError:
        print('Don’t try buffer overflow attacks in Python!')


def num_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = 0
    for c in s:
        if c.lower() in vowels:
            result += 1
    return result


def rem_punctuation(s):
    punctuation = ['!', '?', '.', ',', '\'', ':']
    result = ''
    for c in s:
        if c not in punctuation:
            result += c
    return result


def correct_arithmetic():
    numbers = input('please type in three integers separeted by space:')
    a, b, c = numbers.split()
    a = int(a)
    b = int(b)
    c = int(c)
    if a + b == c or a == b - c or a * b == c:
        return True
    return False


def factors(n):
    pending = []
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            pending.append(n // k)
        k += 1
    if k * k == n:
        yield k
    for i in range(len(pending) - 1, 0, -1):
        yield pending[i]


def norm(v, p=2):
    import math
    result = 0
    for n in v:
        result += pow(n, p)
    return pow(result, 1.0 / float(p))


def input_words():
    words_in = input("words separated by white-space")
    words = words_in.split()
    d = dict()
    for word in words:
        if word not in d.keys():
            d[word] = 1
        else:
            d[word] += 1
    for k, v in d.items():
        print("word {} appears {} times.".format(k, v))
