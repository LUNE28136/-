def get_integer(prompt):
    return int(input(prompt))

def get_fixed_price(price):
    return price/((100-sale_rate)/100)
    
def main():
    global sale_rate
    sale_rate=get_integer('할인율은? ')
    priceA=get_integer('A상품의 할인된 가격은? ')
    priceB=get_integer('B상품의 할인된 가격은? ')
    print('A상품의 정가는',get_fixed_price(priceA),'원')
    print('B상품의 정가는',get_fixed_price(priceB),'원')

if __name__=='__main__':
    main()
