"""dsadsadas"""
def main():
    """dsadsadas"""
    push = int(input())
    sit = int(input())
    up = int(input())
    run = int(input())
    c_push = int(input())
    c_sit = int(input())
    c_up = int(input())
    c_run = int(input())
    if push/c_push >= sit/c_sit and push/c_push >= up/c_up and push/c_push >= run/c_run :
        print(f"{push/c_push:.0f}")
    elif sit/c_sit >= up/c_up and sit/c_sit >= run/c_run :
        print(f"{sit/c_sit:.0f}")
    elif up/c_up >= run/c_run :
        print(f"{up/c_up:.0f}")
    else:
        print(f"{run/c_run:.0f}")

main()
