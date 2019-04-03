def number_level(password):
    text_number=False
    for x in password:
        if x.isnumeric():
            text_number= True
            break

    return text_number
def alpha_level(password):
    text_alpha=False
    for x in password:

        if x.isalpha():
            text_alpha=True
            break

    return text_alpha

def main():
    
    time=5
    while time>0:
        time -=1
        password = input()
        strength_level =0
        print type(password)
        if len(password)>=8:
            strength_level +=1
        else:
            print("")
        if number_level(password):
            strength_level +=1
        else:
            print("")
        if alpha_level(password):
            strength_level +=1
        else:
            print("")

        strength_level_str=str(strength_level)
        f = open('password03.txt','a')
        f.write('input{}'.format(password))
        f.close()


        
        if strength_level >= 3:
            print("")
            break
        else:
            print("")
            continue

    if time== 0:

        print("")
if __name__ == '__main__':
    main()