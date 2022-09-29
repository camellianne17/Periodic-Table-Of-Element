import random

def main():
    """Start a fruit guessing game."""
    print("Guess the Periodic Table Element  !")
    print("Fe,Ai,Ca,In,Os,Ti,Hg")

    Periodic_Table_Element = [
        "Fe",
        "AI",
        "CA",
        "In",
        "Os",
        "Ti",
        "Hg"
         ]
    x = random.choice(Periodic_Table_Element)
    "FE"=Iron is too reactive to exist alone, so it only occurs naturally in the Earth's crust as iron ores, such as hematite, magnetite, and siderite.
    "AI"=the symbol ‘ Al ‘ and the third most common element of the crust of our planet
    "CA"=cal­ci­um is a met­al with a sil­very-white col­or.
    "IN"=metal that conducts heat and electricity well.
    "OS"=has the highest abrasion resistance of any material.
    "Ti"=titaniam are know for their high strenght,low weight, and exceptional corrosion resistance
    "Hg"=planet with attractive features for lovers of science and astronomy.
    guess = None

    while x != guess:

        guess = str(input("What  Periodic Table Element am I thinking of? "))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))

main()
