#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys


def y_hat(w, x):
    return w[0] * x[0] + w[1] * x[1]


def cost(w, x, y, m):
    _sum = sum([(y_hat(w, x[i]) - y[i]) ** 2 for i in xrange(m)])
    return _sum / (2 * m)


def gradientdescent(w, x, y, m, alpha, iterations):
    for i in xrange(iterations):
        _w = w[:]
        for j in range(2): # size of dimension
            _sum = sum([(y_hat(w, x[k]) - y[k]) * x[k][j] for k in xrange(m)]) # 최소제곱의 미분한 결과
            _w[j] = _w[j] - alpha * _sum / m
        w = _w[:]
    return w


def main():
    x = []  # List of training example parameters
    y = []  # List of trainign example results

    for line in sys.stdin:
        [a, b] = map(float, line.split(','))
        x.append(a)
        y.append(b)

    m = len(x) # Number of training examples

    x = [[1, i] for i in x]  # 1차 함수이므로 w 0 값은 항상 1

    # Initialize w's
    init_w = [0.0, 0.0]
    learningrate = 0.01
    iterations = 10000

    # Run gradient descent to get our guessed hypothesis
    final_w = gradientdescent(init_w, x, y, m, learningrate, iterations)

    # Evaluate our hypothesis accuracy
    print "Initial cost:", cost(init_w, x, y, m)
    print "Initial weight:", init_w
    print "Final cost:", cost(final_w, x, y, m)
    print "Final weight:", final_w

if __name__ == "__main__":
    main()
