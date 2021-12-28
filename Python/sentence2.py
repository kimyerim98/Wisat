#단어 갯수 새기 위치 단어 빼기
sentence='The regret after not doing something is bigger than that of doing something'
l_sentence=sentence.lower()
print(l_sentence)
list_st=l_sentence.split(' ')
print(len(list_st))
i=0
x=['the','is','that','of']
while(i!=len(list_st)):
    if list_st[i] in x:
        i=i+1
        pass
    else:
        print(list_st[i],' ',end='')
        i+=1
