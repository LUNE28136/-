def read_single_digit(n):
    n=int(n)
    if n==1: return '일'
    elif n==2: return '이'
    elif n==3: return '삼'
    elif n==4: return '사'
    elif n==5: return '오'
    elif n==6: return '육'
    elif n==7: return '칠'
    elif n==8: return '팔'
    elif n==9: return '구'
    else: return '영'

def read_number(n):
    n=str(n)
    n1=read_single_digit(n[0])
    n2=read_single_digit(n[1])
    n3=read_single_digit(n[2])
    return n1, n2, n3

def main():
    n=num=int(input('세 자리 정수 입력: '))
    read1, read2, read3=read_number(num)
    print(read1, read2, read3)

if __name__=='__main__':
    main()
