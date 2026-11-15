# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Ruby")
image Ruby happy = "Ruby happy.png"
define f = Character("Emerald (best friend)")
image Emerald angry = "Emerald angry.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene schoolbuilding

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Ruby happy at truecenter
    # These display lines of dialogue.

    e "Hello! My name is Ruby, and I go to Glimmer High School!"

    e "Come with me and dive into my glimmering world!"
    jump place

label place:
    scene schoolhallway
    show Ruby happy at truecenter
    e "I was happily walking in the school hallway one day when suddenly..."
    show Emerald angry at right
    f "Ruby, we can't be friends anymore. You're too sensitive."
    menu:
        "Accept it and walk away":
            e "That's cool. I never liked you anyway either."
            f "Good I hope we never cross paths again!"
        "Beg and ask her not to leave her.":
            e "Please don't leave me! You're my only friend!"
            f "Just get lost Ruby. I don't even wanna see you again."
