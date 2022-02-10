def check_score(l):
    new_list=[]

    def expand_list(l):
        for i in l:
            if type(i)==list:
                expand_list(i)
            else:
                new_list.append(i)

    expand_list(l)
    #print(new_list)
    symbol={'#':5,'O':3,'X':1,'!':-1,'!!':-3,'!!!':-5}
    sum=0
    for i in new_list:
        if i in symbol:
            sum+=symbol[i]

    if sum<0:
        return 0
    else:
        return sum           


print(check_score([
    ['#','!'],
    ['!!','X','x']
]))

print(check_score([
    ['!!!','O','!'],
    ['X','#','!!!'],
    ['!!','X','O']
]))