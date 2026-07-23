"""dasdadaw"""
def main():
    """dasdawdasda"""
    N = int(input())
    if N**0.5 == int(N**0.5):
        n = int((N**0.5) - 1)
    else:
        n = int(N**0.5)
    if N%2 == n%2 :
        print(2*n-1)
    else:
        print(2*n)

main()
