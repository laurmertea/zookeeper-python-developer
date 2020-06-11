import numpy as np

# Description
# It's time to make your project more convenient and understandable.
# In this final stage, your software will be ready for use by the zoo staff.
# Your program should understand the habitat numbers, show the animals,
# and be able to work infinitely.

# Objectives
# These are your tasks at this point:
# Your program should repeat the behavior from the previous stage,
# now in a loop.
# Do not forget to add an exit opportunity for the program: 
# inputting the word exit must terminate the program.
# At the end of execution, it must print See you!.

# Example
# The greater-than symbol followed by a space (> ) represents the user input. 
# Notice that it's not part of the input.
# The complete program should work this way:
# Which habitat # do you need? > 3
#  
# Switching on camera from the habitat with a lovely goose...
#    
#                                    _
#                                ,-"" "".
#                              ,'  ____  `.
#                            ,'  ,'    `.  `._
#   (`.         _..--.._   ,'  ,'        \    \
#  (`-.\    .-""        ""'   /          (  d _b
# (`._  `-"" ,._             (            `-(   \
# <_  `     (  <`<            \              `-._\
#  <`-       (__< <           :
#   (__        (_<_<          ;
#    `------------------------------------------
# This bird stares intently at you... (Maybe it's time to change the channel?)
# > Which habitat # do you need? > 1
# 
# Switching on camera from the habitat with lions...
#                                               ,w.
#                                             ,YWMMw  ,M  ,
#                        _.---.._   __..---._.'MMMMMw,wMWmW,
#                   _.-""        '''           YP"WMMMMMMMMMb,
#                .-' __.'                   .'     MMMMW^WMMMM;
#    _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
# ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
#,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
#WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
#"^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
#           /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
#          /  .'             /  (       .'  /     Ww._     `.  `"
#         /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
#        (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
# The lion is croaking!
# Which habitat # do you need? > exit
# See you!

camel = r"""
Switching on camera from habitat with camels...
 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;     
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
Yey, our little camel is sunbathing!"""

lion = r"""
Switching on camera from habitat with lions...
                                               ,w.
                                             ,YWMMw  ,M  ,
                        _.---.._   __..---._.'MMMMMw,wMWmW,
                   _.-""        '''           YP"WMMMMMMMMMb,
                .-' __.'                   .'     MMMMW^WMMMM;
    _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
 ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
"^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
           /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
          /  .'             /  (       .'  /     Ww._     `.  `"
         /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
        (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
The lion is croaking!"""

deer = r"""
Switching on camera from habitat with deers...
   /|       |\
`__\\       //__'
   ||      ||
 \__`\     |'__/
   `_\\   //_'
   _.,:---;,._
   \_:     :_/
     |@. .@|
     |     |
     ,\.-./ \
     ;;`-'   `---__________-----.-.
     ;;;                         \_\
     ';;;                         |
      ;    |                      ;
       \   \     \        |      /
        \_, \    /        \     |\
          |';|  |,,,,,,,,/ \    \ \_
          |  |  |           \   /   |
          \  \  |           |  / \  |
           | || |           | |   | |
           | || |           | |   | |
           | || |           | |   | |
           |_||_|           |_|   |_|
          /_//_/           /_/   /_/
Our 'Bambi' looks hungry. Let's go to feed it!"""

goose = r"""
Switching on camera from habitat with lovely goose...

                                    _
                                ,-"" "".
                              ,'  ____  `.
                            ,'  ,'    `.  `._
   (`.         _..--.._   ,'  ,'        \    \
  (`-.\    .-""        ""'   /          (  d _b
 (`._  `-"" ,._             (            `-(   \
 <_  `     (  <`<            \              `-._\
  <`-       (__< <           :
   (__        (_<_<          ;
    `------------------------------------------
This bird stares intently at you... (Maybe it's time to change the channel?)"""

bat = r"""
Switching on camera from habitat with bats...
_________________               _________________
 ~-.              \  |\___/|  /              .-~
     ~-.           \ / o o \ /           .-~
        >           \\  W  //           <
       /             /~---~\             \
      /_            |       |            _\
         ~-.        |       |        .-~
            ;        \     /        i
           /___      /\   /\      ___\
                ~-. /  \_/  \ .-~
                   V         V
It looks like this bat is fine."""

rabbit = r"""
Switching on camera from habitat with rabbits...
         ,
        /|      __
       / |   ,-~ /
      Y :|  //  /
      | jj /( .^
      >-"~"-v"
     /       Y
    jo  o    |
   ( ~T~     j
    >._-' _./
   /   "~"  |
  Y     _,  |
 /| ;-"~ _  l
/ l/ ,-"~    \
\//\/      .- \
 Y        /    Y 
 l       I     !
 ]\      _\    /"\
(" ~----( ~   Y.  )
It seems there will be more rabbits soon!"""

animals_info = ['camel','lion','deer','goose','bat','rabbit']
animals = [camel,lion,deer,goose,bat,rabbit]

print("Which habitat # do you need?")
print("You can type `info` to see which habitats are available for a visit.")
print("You can also type `exit` to leave the zoo!")
user_input = input()

while user_input != "exit":
    if user_input != "info":
        if 0 <= int(user_input) < len(animals):
            print(animals[int(user_input)])
        else:
            print("Habitat " + user_input + " is not available, yet!")
    else:
        index = 0
        while index < len(animals_info):
            print("Type " + str(index) + " to see the " + animals_info[index])
            index += 1

    print("Which habitat # do you need?")
    print("You can type `info` to see which habitats are available for a visit.")
    print("You can also type `exit` to leave the zoo!")
    user_input = input()
print("See you!")
