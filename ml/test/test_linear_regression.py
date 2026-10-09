import numpy as np
from ml.src.linear_regression import (predict, compute_cost, gradient_descent)

def test_predict():
    X=np.array([100,200,300])

    predictions = predict(X, w=0.08, b=0.0)

    expected= np.array([8,16,24])

    assert np.allclose(predictions, expected)


def test_cost_is_zero_for_perfect_predictions():
    X = np.array([100, 200, 300])
    y = np.array([8, 16, 24])
    w = 0.08
    b = 0.0

    cost = compute_cost(X, y, w, b)

    assert np.isclose(cost, 0.0)

def test_gradient_descent_reduces_cost():
    X = np.array([1,2,3,4,5],dtype=float)
    y = np.array([2,4,6,8,10],dtype=float)
    initial_cost = compute_cost(X, y, w=0.0, b=0.0)

    w,b,_ = gradient_descent(X, y, w=0.0, b=0.0, learning_rate=0.01, iterations=1000)

    final_cost = compute_cost(X, y, w, b)

    assert final_cost < initial_cost