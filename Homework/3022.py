"""dsadasdas"""
def main():
    """dsadasdasd"""
    temp = float(input())
    now = input()
    change = input()

    if now == "C":
        celsius = temp
    elif now == "F":
        celsius = (temp - 32) * 5 / 9
    elif now == "K":
        celsius = temp - 273.15
    else:
        celsius = (temp - 491.67) * 5 / 9

    if change == "C":
        result = celsius
    elif change == "F":
        result = celsius * 9 / 5 + 32
    elif change == "K":
        result = celsius + 273.15
    else:
        result = (celsius + 273.15) * 9 / 5

    print(f"{result:.2f}")

main()
