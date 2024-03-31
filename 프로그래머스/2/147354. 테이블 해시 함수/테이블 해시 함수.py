from functools import *

def solution(data, col, row_begin, row_end):
    data.sort(reverse = True)
    data.sort(key = lambda x: x[col-1])
    return reduce(lambda x, y: x^y, [sum([d%(i+1) for d in data[i]]) for i in range(row_begin-1, row_end)])