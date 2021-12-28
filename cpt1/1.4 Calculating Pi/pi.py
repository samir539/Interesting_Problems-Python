def calc_pi(accuracy:int) -> float:
    numerator:float = 4.0
    denominator:float = 1.0
    multiplicative:float = 1.0
    pi_value: float = 0.0

    for _ in range(accuracy):
        pi_value += multiplicative * (numerator/denominator)
        denominator += 2.0
        multiplicative *= -1

    return pi_value

if __name__ == "__main__":
    print(calc_pi(1000000000000000))

