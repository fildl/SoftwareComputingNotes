def add_1(n):
    return(n + 1)

functions = [str.strip,
             float,
             round,
             add_1,
             str
             ]

def pipe(functions_list, obj):
    for func in functions_list:
        obj = func(obj)
    return obj

def pipe(functions_list):
    def _inner_(obj):
        for func in functions_list:
            obj = func(obj)
        return obj
    return _inner_

print(pipe(functions, " 2.12 "))
assert pipe(functions, " 2.12 ") == "3"