def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


i = iter(fibonacci())

# python -i teste_generator.py
# next(i)
