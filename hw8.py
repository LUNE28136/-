def get_item(prompt):
    i=input(prompt)
    return i

def get_count(prompt):
    c=int(input(prompt))
    return c

def buy(s):
    print('[구입]')
    i=get_item('상품명? ')
    if i=='': 
         print()
         return False
    else:
        c=get_count('수량은? ')
        s[i]=c
        print(f'장바구니에 {i} {c}개가 담겼습니다.')
        print()

def show(s):
    print('>>>장바구니 보기:',s)

def find(s):
    i=get_item('장바구니에서 확인하고자하는 상품은? ' )
    if i=='':
         print()
         return False
    else:
        if i in s:
            print(f'{i}은(는) {s.get(i)}개 담겨 있습니다.')
            print()
        else:
            print(f'장바구니에 {i}은(는) 없습니다.')
            print()
        find(s)

def main():
    shopping_bag = {}
    while True:
        if buy(shopping_bag) == False:
            break
    show(shopping_bag)
    find(shopping_bag)

if __name__ == "__main__":
    main()
