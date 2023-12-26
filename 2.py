#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def harmonic_mean(*args):
    if len(args) == 0:
        return None

    reciprocal_sum = sum(1 / x for x in args)
    harmonic_mean_value = len(args) / reciprocal_sum

    return harmonic_mean_value


if __name__ == "__main__":
    numbers = list(map(int, input("Введите значения через пробел: ").split()))
    print(f"Среднее гармоническое чисел {numbers}: {harmonic_mean(*numbers)}")
