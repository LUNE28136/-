def get_item(prompt):
    i=input(prompt)
    return i

def get_count(prompt):
    c=int(input(prompt))
    return c

def search_shopping_bag(s):
    i=get_item('장바구니에서 확인하고자하는 상품은? ' )
    if i in s:
        print(f'{i}은(는) {s.get(i)}개 담겨 있습니다.')
    else:
        print(f'{i}은(는) 장바구니에 담겨 있지 않습니다.')

shopping_bag={}
while True:
    item=get_item('상품명? ')
    if item=='': 
        print()
        break
    else:
        count=get_count('수량은? ')
        shopping_bag[item]=count
        print(f'장바구니에 {item} {count}개가 담겼습니다.')
        
print('>>>장바구니 보기:',shopping_bag)
print()

search_shopping_bag(shopping_bag)
