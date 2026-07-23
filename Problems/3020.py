"""dasasadd"""
def main():
    """dsadasasda"""
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_d = int(input())
    
    result = num_a + ((num_a*(num_b-1)+num_c)*((num_d-1) // num_b)) + (((num_d-1) % num_b)*num_a)
    print(result)
main()
