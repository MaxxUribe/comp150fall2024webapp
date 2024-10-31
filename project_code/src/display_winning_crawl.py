import time

def display_winning_crawl(speed=0.05):
    winning_crawl_ascii = r"""
            .         .      .         .      .         .
        .      .     .   .   .       .   .    .  .   .      .      .
                 .        .  *       .         *          .
          *    .     .    .        .     *       .       .
        .        .         *       .      *       .     .
        .     .         .        .     *     .      .
         .    *       .  *  .    .      .    .    *     .    *  
       .    .        .     .   .        .   .     .     .    .
              .      .  .       .     .  .    .     .      .
                .        .  .    .  *      .  .        .
          .     .  *    .  .    .        .     .   *     .
              .  .        .  .   .     .         .       .
    .         .       .     .    .       .  *         .      *
          .    .  *    .       .       .     .    .     .
           .     .      .        .  .      .        * .     .
          *  .    .  *     . .    .      *  .  .     .    .
        .        .         .        .     *       .         .
         .    .       .      .     .   *       .    .   *   *
            .         *      .  .         .       .        .
    *        .      .      .    .     .    *        .   .
           .    .         .  .        .    *  .  .  .
        .   *         .    .   *  .      .  .  *       .    *
                    ***********************************
                    *.______      .______     _______ *
                    *|   _  \     |   _  \   /  _____|*
                    *|  |_)  |    |  |_)  | |  |  __  *
                    *|      /     |   ___/  |  | |_ | *
                    *|  |\  \----.|  |      |  |__| | *
                    *| _| `._____|| _|       \______| *
                    ***********************************

                 /       .      .                   .         .    .      .
  .      .      /"@,/ `.               .           ________   ___   ____
               .   /    `.                     .  / __   __| / _ \ |  _ \
               ;          `.                   ___> \ | |   |  _  ||    /__
              :   .         `-._      .       |_____/ |_| . |_| |_||_|\____|
      .       ;     <=,_c.,_.o=-b         .    _  _  _   ___   ____    ____
        .    :      C=\=\;@<""             .  | |/ \| | / _ \ |  _ \. / ___|
        :    ;   _c'l@< :>\@                  |   .   ||  _  ||    /__> \  .
   .    |    \._=-"" \@`"            .         \_/ \_/ |_| |_||_|\______/
        |    `b                 .            .            .
.       #             .                   .         .                   .
        #     . .     __ ..-- ---:::::::::::---.___         . .
    .  .#      __..::::::..::::::::::::::::::::..::""-- ...__         .
....,,o###==-""...::::........::++||#||#+#|+++::::..:::::::::::-._
.     _`%". ........:::.......:::+|||#||||||++:..::::::::::::+++|++-._    .
    -'..   . .......::::......:::+++||##||||||..::...:::::+::::+++|||||-.
.-'. ... ........::::::::.....:::::+++||###|+|+:.::.:++++::++++++||#|#|||#.
  ..  . .::.:::::::::::::::.::.:::::++|||###|||+:+++++++|:+++++||####|#|#|||
.......:+::.:::::::::::::::.:::::::++++||||##+|||++++|#|##++||||######|##|||
:..:.:::|+:::::::::::::::::::::::+++++||||||#:++|#|||####|#|||LS#####|+|##||
:::::::::::::::::::::++++:::::::::+||+|||||||||######@#@#|########@@#||#||||
:::..:.:..:::+:::::+++||++++||::+++||||||||||+||#||||||||||################|
.......::::::++:+:+++|||||##|##++++||||||||||++:+||++++++|#############|####
"""
    
    description = (
        "--------------------------------------------------------------------\n"
        "As the dust settles, the Empire's grip on the galaxy begins to weaken.\n"
        "You and your party have thwarted their sinister plans, and hope has been\n"
        "restored to countless worlds. The Jedi's light shines bright, and the\n"
        "Rebellion's spirit is rekindled.\n\n"
        "With the power of the Kyber Crystals safeguarded, the galaxy unites to\n"
        "celebrate this hard-fought victory. Your bravery will be remembered as\n"
        "a beacon of hope for generations to come.\n\n"
        "Congratulations, you've saved the galaxy from tyranny! May the Force\n"
        "be with you always.\n"
        "--------------------------------------------------------------------"
    )

    print("\n" + "=" * 70 + "\n")  # Adding a line to separate the ASCII art and the description

    for line in winning_crawl_ascii.splitlines():
        print(line)
        time.sleep(speed)  # Use the customizable speed

    print("\n" + description + "\n")
