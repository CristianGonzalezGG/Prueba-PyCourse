print("""

       __,-----._                       ,-. 
     ,'   ,-.    \`---.          ,-----<._/ 
    (,.-. o:.`    )),"\\-._    ,'         `. 
   ('"-` .\       \`:_ )\  `-;'-._          \ 
  ,,-.    \` ;  :  \( `-'     ) -._     :   `: 
 (    \ `._\\ ` ;             ;    `    :    ) 
  \`.  `-.    __   ,         /  \        ;, ( 
   `.`-.___--'  `-          /    ;     | :   | 
     `-' `-.`--._          '           ;     | 
           (`--._`.                ;   /\    | 
            \     '                \  ,  )   : 
            |  `--::----            \'   ;  ;| 
            \    .__,-      (        )   :  :| 
             \    : `------; \      |    |   ; 
              \   :       / , )     |    |  ( 
     -hrr-     \   \      `-^-|     |   / , ,\ 
                )  )          | -^- ;   `-^-^' 
             _,' _ ;          |    | 
            / , , ,'         /---. : 
            `-^-^'          (  :  :,' 
                             `-^--' 
""")
print("Welcome to the James Play")
print("James is a Dog who is lost in a neighborhood he has 3 door in front of him..")
print("Help him to choose the best and come back at home")
step1 = input("Fisrt u need to Choose a boat.. Left or Right? (L) (R)")

try:
  if step1 == "L":
    step2 = input("Well done! Now you need to wait for another boat. Swim or wait?")
    if step2.lower() == "wait":
      print("Nice u arrive to the doors")
      print("Now choose a door, There are 3, first one Yellow(Y) Red(R) Blue(B)")
      step3 = input("Choose 1")
      if step3 == "r":
        print("""James is at home Well Done Take it.. 
                        .-"'"-.
                      |       |
                    (`-._____.-')
                  ..  `-._____.-'  ..
                .', :./'.== ==.`\.: ,`.
              : (  :   ___ ___   :  ) ;
              '._.:    |0| |0|    :._.'
                  /     `-'_`-'     \
                _.|       / \       |._
              .'.-|      (   )      |-.`.
            //'  |  .-"`"`-'"`"-.  |  `\\
            ||    |  `~":-...-:"~`  |    ||
            ||     \.    `---'    ./     ||
            ||       '-._     _.-'       ||
          /  \       _/ `~:~` \_       /  \
          ||||\)   .-'    / \    `-.   (/||||
          \|||    (`.___.')-(`.___.')    |||/
          '"' jgs `-----'   `-----'     
          '"'""")
      else: print("Game Over!")
    else: print("GAME OVER!! James drowned..")
    
  elif step1 == "R":
    print("GAME OVER!! ")
      
  else:
    print("Choose (L) or (R)")

except Exception as e:
  print(f"Choose (L) or (R)")
