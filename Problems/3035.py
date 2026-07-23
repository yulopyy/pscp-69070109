"""dsadsada"""
def main():
    """dsadsadas"""
    var = input().split()
    r = int(var[0])
    x = int(var[1])
    y = int(var[2])
    if (x**2)+(y**2) == r**2:
        print("ON")
    elif (x**2)+(y**2) < r**2:
        print("IN")
    else:
        print("OUT")

main()
