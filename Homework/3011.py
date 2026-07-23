"""dadadsad"""
def main():
    """dsadasd"""
    colour1 = str(input())
    colour2 = str(input())
    if colour1 not in ["Red", "Yellow", "Blue"] or colour2 not in ["Red", "Yellow", "Blue"]:
        print("Error")
    else:
        if colour1 == "Red" and colour2 == "Yellow" or colour1 == "Yellow" and colour2 == "Red":
            print("Orange")
        elif colour1 == "Red" and colour2 == "Blue" or colour1 == "Blue" and colour2 == "Red":
            print("Violet")
        elif colour1 == "Yellow" and colour2 == "Blue" or colour1 == "Blue" and colour2 == "Yellow":
            print("Green")
        elif colour1 == colour2:
            print(colour1)
        else:
            print("Error")

main()
