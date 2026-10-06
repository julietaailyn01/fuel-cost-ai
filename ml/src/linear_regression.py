import numpy as np


def predict(X, w, b):
    return w * X + b


def compute_cost(X, y, w, b):
    m = len(X)

    predictions = predict(X, w, b)
    errors = predictions - y

    cost = np.sum(errors ** 2) / (2 * m)

    return cost


def compute_gradients(X, y, w, b):
    m = len(X)

    predictions = predict(X, w, b)
    errors = predictions - y

    dw = np.sum(errors * X) / m
    db = np.sum(errors) / m

    return dw, db


def gradient_descent(
    X,
    y,
    w,
    b,
    learning_rate,
    iterations
):
    cost_history = []

    for _ in range(iterations):
        dw, db = compute_gradients(X, y, w, b)

        w = w - learning_rate * dw
        b = b - learning_rate * db

        cost = compute_cost(X, y, w, b)
        cost_history.append(cost)

    return w, b, cost_history