"""dasasdasd"""
def main():
    """dasasdasd"""
    num_of_rabbits = int(input())
    list_point = []
    for _ in range(num_of_rabbits):
        point = int(input())
        list_point.append(point)
    print(max(list_point))
    print(list_point.count(max(list_point)))

main()
