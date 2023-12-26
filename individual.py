#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_after_positive(*args):
    found_positive = False
    result_sum = 0

    for arg in args:
        if found_positive:
            result_sum += arg
        elif arg > 0:
            found_positive = True

    if found_positive:
        return result_sum
    else:
        return None


if __name__ == "__main__":
    user_input = list(map(float, input("Введите числа через пробел: ").split()))

    result = sum_after_positive(*user_input)
    print(result)
