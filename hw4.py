def rep_char(c,n):
    c=str(c)
    print(c*n)

def print_welcome_message(name):
    msg1=f' Hello {name},'
    msg2=' Welcom to Seoul.'
    nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
    rep_char('-',nstr*2)
    print(msg1)
    print(msg2)
    rep_char('-',nstr*2)

name=input('Input his/her name: ')
print_welcome_message(name)
