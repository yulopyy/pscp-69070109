"""dasasadd"""
def main():
    """dsadasasda"""
    month = int(input())
    day = int(input())
    winter = [1,2,3]
    spring = [4,5,6]
    summer = [7,8,9]
    fall = [10,11,12]

    if not month % 3 and day >= 21:
        if month in winter:
            print("spring")
        elif month in spring:
            print("summer")
        elif month in summer:
            print("fall")
        elif month in fall:
            print("winter")
    else:
        if month in winter:
            print("winter")
        elif month in spring:
            print("spring")
        elif month in summer:
            print("summer")
        elif month in fall:
            print("fall")
main()
