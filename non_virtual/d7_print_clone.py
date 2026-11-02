from typing import Any

def custom_print(*values: Any,
                 sep: str | None= '', 
                 end: str | None= '\n',
                 caps: bool = False,
                 include_types: bool = False,
                 count: bool = False) -> None:
    
    new_values: list[Any] = []
    for value in values:
        if isinstance(value, str) and caps:
            new_values.append(value.upper())
        else:
            new_values.append(value)

    values_with_types: list[Any] = []
    if include_types:
        for value in new_values:
            values_with_types.append((value, type(value)))
        
        print(*values_with_types, sep = sep, end = end)
    else:
        print(*new_values, sep = sep, end= end)


    counts: int = 0
    if count:
        for value in values:
            counts += 1
        print(f'counts: {counts}')


# custom_print('Bob', 'James', 10, caps= True, sep = ', ')
# custom_print('Bob', 'James', 10, caps= True, include_types=True, sep = ', ')
custom_print('Bob', 'James', 10, caps= True, count=True, sep = ', ')