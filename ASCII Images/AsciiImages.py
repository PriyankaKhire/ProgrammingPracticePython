class AsciiImages(object):
    def __init__(self):
        self.images = {
            "WindowsLogo" : self.windowsLogo(),
            "Toucan" : self.toucan(),
            "SailingMan" : self.sailingMan(),
            "Ruler"  : self.ruler(),
            "PizzaSlice" : self.pizzaSlice(),
            "Pig" : self.pig(),
            "Owl" : self.owl(),
            "OpenBook" : self.openBook(),
            "LittleBird" : self.littleBird(),
            "Key" : self.key(),
            "Igloo" : self.igloo(),
            "GenieLamp" : self.genieLamp(),
            "Dog" : self.dog(),
            "Clover" : self.clover(),
            "AtmCar" : self.atmCar(),
            "Arrow" : self.arrow()
            }

    def arrow(self):
        return ("""
Arrow

   >>>>>>>_____________________\`-._
   >>>>>>>                                              /.-'
   """)


    def atmCar(self):
        return ("""
Car going to ATM
                                      ___
                 .--.              [ATM]
          .----'   '---.            |
          '-()-----()-'           |

""")


    def clover(self):
        return ("""

Clover
                                      .-.
                                     ( . )
                                   .-.':'.-. 
                                  (  =,!,=  )
                                   '-' | '-'
 """)


    def dog(self):
        return ("""
Dog

                .-"-.
             /|6 6|\\
           {/(_0_)\\}
             _/ ^ \_
           (/_/^\_\\)-'

           """)


    def genieLamp(self):
        return ("""
Genie's Lamp

                {}       _,
       ___/__\_//
      (__\_____/
           -' `) (`
               ~""~
               """)


    def igloo(self):
        return ("""
Igloo
                               _..-.._           *
                        *  .'_/ _ \_'.      
                        /_ _| __|_ _\___  *
                      | _ |_ _| _ |__|     /\ 
                      |___|___|___|__\/
                      """)


    def key(self):
        return ("""

Key
                        .--.
                    /  .-. '----------.
                    \ '-' .--"--""-"-'
                     '--'
""")


    def littleBird(self):
        return ("""
Little bird
                       __
                      ('v')     
                      ((   ))  
                 ------"-------
                 """)


    def openBook(self):
        return ("""
Open Book
      __...--~~~~~-._   _.-~~~~~--...__
    //                      `V'                      \\
   //                          |                         \\
  //__...--~~~~~~-._ |  _.-~~~~~~--..._\\
 //__.....----~~~~._\ | /_.~~~~----.....__\\
================\\|//================
                               `---`
                """)


    def owl(self):
        return ("""
Owl
___/|
\o.O|
(___)
  U
  """)


    def pig(self):
        return ("""
Pig

            .-~~-. |\\_
     @_/        /  oo\_
          |    \   \   _ (")
          \    /-| ||'-'
           \_\  \_\\
           """)


    def pizzaSlice(self):
        return("""\
Pizza Slice

               // ""--.._
              ||  (_)  _ "-._
              ||     _ (_)       '-.
              ||   (_)       __ ..-'
               \\__..--""

""")


    def ruler(self):
        return ("""
Ruler
          ________________________________________________
         |'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|'|
         |___1___2___3___4___5___6___7___8___9__10__11__12_|
""")


    def sailingMan(self):
        return ("""
Man Sailing
                            |\\
                            |  \\
                            |     \\
                            |       \\
                            |         \\
                         o |           \\
                       \\|-|______\\
                       _|\\|___
                       \\_____/
                       """)


    def toucan(self):
        return ("""

         __,---.
        /__|o\  )
           `-\ / /
                ,) (,
              //   \\
              {(     )}
  =======""===""===============
                 |||||
                  |||
                   |
""")

    def windowsLogo(self):
        return("""\
Windows Logo
                    
                 _.-;;-._
          '-..-'|   ||   |
         '-..-'|_.-;;-._|
          '-..-'|   ||   |
        '-..-'|_.-''-._|

                    """)
