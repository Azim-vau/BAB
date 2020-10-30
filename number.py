import time,os
os.system('clear')

#####logo#####
logo = '''
\033[1;92m                        
                      .~#########%%;~. 
                     @############%%;`@
                    @######/~\/~\%%;,;,@
                   |#######\    /;;;;.,.|
                   |#########\/%;;;;;.,.|
          XX       |##/~~\####%;;;/~~\;,|       XX
        XX..X      |#|  o  \##%;/  o  |.|      X..XX
      XX.....X     |##\____/##%;\____/.,|     X.....XX
 XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX
X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X
X |.....X  @#%,.@     |######%%;;;;,.|     @#%,.@  X.....| X
X  \...X     @#%,.@   |# # # % ; ; ;,|   @#%,.@     X.../  X
 X# \.X        @#%,.@       \033[1;91mB.A.B \033[1;92m    @#%,.@        X./  #
  ##  X          @#%,.@              @#%,.@          X   #
, "# #X            @#%,.@          @#%,.@            X ##
   `###X             @#%,.@      @#%,.@             ####'
  . ' ###              @#%.,@  @#%,.@              ###`"
    . ";"                @#%.@#%,.@                ;"` ' .
      '                    @#%,.@                   ,.
      ` ,                @#%,.@  @@                `
                          @@@  @@@     
\033[1;93m MR. ERROR \033[1;96mB.A.B
\033[1;97m--------------------------------------------------
\033[1;96m \033[1m
 AUTHOR     : AZIM MAHMUD 
 FACEBOOK   : FACEBOOK.COM/MR.AZIM.VAU
 YOUTUBE    : YOUTUBE.COM/MR.ERROR
 GITHUB     : GITHUB.COM/AZIM-VAU
\033[1;93m
--------------------------------------------------
\033[1;94m
                                '''
print(logo)
CorrectUsername = "BAB"
CorrectPassword = "AZIM"
loop = 'true'
while (loop == 'true'):
    username = raw_input('\nUSERNAME: ')
    if (username == CorrectUsername):
        password = raw_input('\nPASSWORD: ')
        if (password == CorrectPassword):
            print("\nAPPROVED!")
            time.sleep(2)
            loop = 'false'
        else:
            print("wrong password")
            os.system('xdg-open https://www.facebook.com/123548648342413')
    else:
        print("wrong username")
        os.system('xdg-open https://www.facebook.com/123548648342413')
os.system('clear')
choser = '''
\033[1;95m  Select Your Option: \n
\033[1;92m  [1] 6-Digit
\033[1;93m  [2] 7-Digit
\033[1;96m  [3] 8-Digit
\033[1;95m  [4] 11-Digit
'''
def input():
    print(logo)
    print(choser)
    v= raw_input("\n\033[1;96m Chose digit ==>")
    if v=="1":
        os.system('clear')
        os.system('python2 A')
    elif v=="2":
        os.system('clear')
        os.system('python2 B')
    elif v=="3":
        os.system('clear')
        os.system('python2 C')
    elif v=="4":
        os.system('clear')
        os.system('python2 D')


input()
