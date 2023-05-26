import os
import pickle
filename='score.bin'

def get_integer(prompt):
    return int(input(prompt))

def get_average(s):
    total=sum(s)
    return total/len(s)

def input_scores():
    s=[]
    print('[점수 입력]')
    i=1
    while True:
        score=get_integer(f'#{i}? ')
        if score>=0:
            s.append(score)
            i+=1
        else: break
    print()
    return s

def show_scores(s):
    print('[점수 출력]')   
    print('개인 점수:',end=' ')
    for i in range(0,len(s)):
        print(s[i],end=' ')
    print()
    print(f'평균:{get_average(s):.1f}')
    print()

def search(s,n):
    if n in s:
        print(f'{n}점은 {s.index(n)+1}번 학생의 점수입니다.')
    else: print(f'{n}점을 받은 학생은 없습니다.')
    print()

def save_data(fp):
    with open(fp,'wb') as file:
        pickle.dump(scores, file)

def load_data(fp):
    with open(fp,'rb') as file:
        scores=pickle.load(file)
        return scores

def main():
    scores=[]
    if os.path.exists(filename):
        scores=load_data(filename)
        print('[파일 읽기]')
        print()
    else:
        scores=input_scores()
    
    show_scores(scores)
    save_data(filename)

# 주 프로그램부
if __name__ == '__main__':
    main()
