import random 

PWD_LEN = 8

symbols = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L',
           'M','N','O','P','Q','R','S','T','U','V', 'W','X','Y','Z',
           '1','2','3','4','5','6','7','8','9','0',
           '~','!','@','#','$','%','^','&','*','(',')','-','='
          ]

pass_list = []
for i in range(PWD_LEN):
    pass_list.append(random.choice(symbols))

password = "".join(pass_list)

print(password)
input("\nНажмите Enter для выхода")
