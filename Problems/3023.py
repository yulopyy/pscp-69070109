"""dsadasdas"""
def main():
    """dsadasdas"""
    n = int(input())

    if n == 1:
        print(1)
    else:
        total_press = 0
        for i in range(1, n + 1):
            total_press += len(str(i)) + 1
        print(total_press)

main()
