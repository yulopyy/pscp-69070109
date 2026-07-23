"""dsaada"""
def main():
    """"sadsadda"""
    price = int(input())
    if 500 <= price <= 10000:
        price += (price*10)/100
        price += (price*7)/100
        print (f"{price:.2f}")
    elif price < 500:
        price += 50
        price += (price*7)/100
        print (f"{price:.2f}")
    elif price > 10000:
        price += 1000
        price += (price*7)/100
        print (f"{price:.2f}")

main()
