# Description
# The third stage brings new abilities for your software: 
# it will be able to recognize the number of a specific habitat 
# from the input and show the animals living there.

# Add all variables with images from the template 
# to a variable with the type list. 
# The order of variables matters: 
# they must be in the order they're defined in the code. 
# The list must contain all of them with no duplicates.


# Objectives
# In this stage, your program should:
# Ask for a number of the habitat using the following phrase: 
# Which habitat # do you need?.
# Use the input number as an index of your habitat to print its content.
# End with the following phrase:
# ---
# The end of the program. To check another habitat restart the watcher please.


# Examples
# The greater-than symbol followed by a space (> ) represents the user input. 
# Notice that it's not part of the input.

# Example 1

# Which habitat # do you need? > 5
 
# Switching on camera from the habitat with rabbits...
#         ,
#        /|      __
#       / |   ,-~ /
#      Y :|  //  /
#      | jj /( .^
#      >-"~"-v"
#     /       Y
#    jo  o    |
#   ( ~T~     j
#    >._-' _./
#   /   "~"  |
#  Y     _,  |
# /| ;-"~ _  l
#/ l/ ,-"~    \
#\//\/      .- \
# Y        /    Y
# l       I     !
# ]\      _\    /"\
#(" ~----( ~   Y.  )
# It seems there will be more rabbits soon!
# ---
# The end of the program. To check another habitat restart the watcher please.

# Example 2

# Which habitat # do you need? > 4
 
#Switching on camera from the habitat with bats...
#_________________               _________________
# ~-.              \  |\___/|  /              .-~
#     ~-.           \ / o o \ /           .-~
#        >           \\  W  //           <
#       /             /~---~\             \
#      /_            |       |            _\
#         ~-.        |       |        .-~
#            ;        \     /        i
#           /___      /\   /\      ___\
#                ~-. /  \_/  \ .-~
#                   V         V
# It looks like this bat is fine.
# ---
# The end of the program. To check another habitat restart the watcher please.


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


habitats = [camel, lion, deer, goose, bat, rabbit]
print(habitats[int(input("Which habitat # do you need?"))])
print("""---
The end of the program. To check another habitat restart the watcher please.""")
