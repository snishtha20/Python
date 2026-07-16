def palin(str):
    if len(str)<=1: # <=1 isiliye kiya because if string has even letters then it will become null 
        print('palindrome')
    else:
        if str[0] == str[-1]:
            palin(str[1:-1])
        else:
            print('not palindrome')

palin('madam')
palin('malayalam')
palin('nishtha')
palin('jaipur')
palin('abba' )
