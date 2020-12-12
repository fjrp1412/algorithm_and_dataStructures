# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    indexes = list(range(len(weights)))
    partial_values = [val/wht for val,wht in zip(values, weights)]
    indexes = sorted(indexes, reverse=True, key= lambda i: partial_values[i])

    for i in indexes:
        if(capacity == 0):
            return value
        a = min(weights[i], capacity)
        value += a * partial_values[i]
        weights[i] -= a
        capacity -= a




    return value




if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
