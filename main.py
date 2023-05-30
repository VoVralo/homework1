presidents = ['Леонід Кравчук', 'Леонід Кучма', 'Віктор Ющенко', 'Віктор Янукович', 'Петро Порошенко',
              'Володимир Зеленський']


def structure_names(presidents: list) -> str:
    yield from presidents


n = structure_names(presidents)
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
