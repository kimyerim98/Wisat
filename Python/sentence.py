#단어 빼기 및 원하는 곳에 붙여 넣기
sentence='The regret after not doing something is bigger than that of doing something'

list_st=sentence.split(' ')
i=0
x=['the','is','that','of','The']
while(i!=13):
    if list_st[i] in x:
        i=i+1
        pass
    else:
        print(list_st[i],' ',end='')
        i+=1


sen='the sdfsdsdgsadfdasfsad is dsfasdfsad that of dadfadsfsad'
set=sen.split()
set.remove('the')
set.remove('that')
print(' '.join(set))
