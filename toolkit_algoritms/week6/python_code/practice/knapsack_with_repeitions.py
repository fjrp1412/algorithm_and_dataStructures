
def knpasack(weights, values, max_capacity):
    value = [0]

    for w in range(1,max_capacity ):
        value.append(0)

        for i in range(1, len(weights)):

            if(weights[i] <= w):
                val = value[w - weights[i]] + values[i]
                if(val > value[w]):
                    value[w] = val
    return value[max_capacity]


if __name__ == "__main__":
    W = 10
    weights = [30,14,16,9]
    values = [6,3,4,2]
    print(knpasack(weights, values, W))
