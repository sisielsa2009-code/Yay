# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default persistent.endings=[]
label ending_1:
    "Congrats! Ruby learns to cope by finding another friend!"
    if "1" not in persistent.endings:
        $ persistent.endings.append("1")
    return
label ending_2:
    "Welp...Ruby lost the chance of finding another friend..."
    if "2" not in persistent.endings:
        $ persistent.endings.append("2")
    return
label ending_3:
    "Yay! Ruby was able to get a pet to be her new best friend!"
    if "3" not in persistent.endings:
        $ persistent.endings.append("3")
    return
label ending_4:
    "If you can't make them, break them."
    if "4" not in persistent.endings:
        $ persistent.endings.append("4")
    return
label ending_5:
    "Just get over it."
    if "5" not in persistent.endings:
        $ persistent.endings.append("5")
    return
define e = Character("Ruby", color='#FF0000')
image Ruby happy = "Ruby happy.png"
define f = Character("Emerald", color='#008000')
image Emerald angry = "Emerald angry.png"
image Ruby crying = "Ruby crying.png"
image Pearl worried = "Pearl worried.png"
define g = Character("Pearl", color='#FFC0CB')
image Pearl number = "Pearl number.png"
image Black cat = "Black cat.png"
define h = Character("Black cat", color='#808080')
image Ruby smirking = "Ruby smirking.png"
image Ruby neutral = "Ruby neutral.png"
transform big:
    align (0.5, 0.5)
    zoom 2
image rainydaybig: 
    "rainyday.jpg" 
    xysize (config.screen_width, config.screen_height)
    fit 'cover'
image parkbenchbig:
    "parkbench.jpg"
    xysize (config.screen_width, config.screen_height)
    fit 'cover'
image coffeeshopbig:
    "coffeeshop.jpg"
    xysize (config.screen_width, config.screen_height)
    fit 'cover'
image catstorebig:
    "catstore.jpg"
    xysize (config.screen_width, config.screen_height)
    fit 'cover'
image housebig:
    "house.avif"
    xysize (config.screen_width, config.screen_height)
    fit 'cover'
image houseonfirebig:
    "houseonfire.jpg"
    xysize (config.screen_width, config.screen_height)
    fit 'cover'
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
    play music "audio/happysound.mp3"
    e "Hello! My name is Ruby, and I go to Bonita High School!"
    e "Come with me and dive into my bonita world!"
    jump place

label place:
    scene schoolhallway
    with fade
    show Ruby happy at truecenter
    e "I was happily walking in the school hallway one day when suddenly..."
    show Emerald angry at right
    f "Ruby, we can't be friends anymore. You're too sensitive."
    play music "audio/cryingsound.mp3"
    menu:
        "Insult her and walk away like a diva":
            play music "audio/ohhsound.mp3"
            e "That's cool. You were an eye sore anyway! If I looked at you any longer, I was sure by bonita eyes were going to burn away anytime soon."
            f "This is exactly what I mean! So sensitive all the time! Good riddance and I hope we never cross paths ever again!"
        "Beg her not to leave and look like a total loser":
            play music "audio/cryingsound.mp3"
            e "Please don't leave me! You're my only friend!"
            f "Just get lost Ruby. I don't even wanna see you again."
label outside:
    play music "audio/sadsound.mp3"
    scene rainydaybig
    with fade
    show Ruby crying at truecenter
    e "{i}I walk out, trying hard to not cry, but the tears eventually spill over. I can't believe Emerald just did that to me.{i}"
label other:
    scene parkbenchbig
    with fade
    show Ruby crying at truecenter
    e "{i}I sit down, trying to process my emotions. There is no way that just happened...Emerald...I thought she liked me for who I truly was.{i}"
    show Pearl worried at left
    g "Are you okay?"
    e "{i}I look up and see a girl my age.{i}"
    e "No. My best friend just unfriended me, and now I don't know what to do."
    g "I'm so sorry to hear that. My name is Pearl, by the way. Come on, let's go somewhere warm."
    menu:
        "Accept her offer":
            g "Let's go to coffee shop nearby."
            label kindness:
                play music "audio/rainlofisound.mp3"
                scene coffeeshopbig
                with fade
                show Ruby neutral at center
                show Pearl worried at left
                e "Thank you for your kindness. I never knew someone could be this kind willingly."
                g "No problem. It seemed like you needed it."
                e "Why did you choose to be kind to me? You could've just left me in the rain."
                g "This world can be cruel, especially after what you told me about Emerald. This world could always use small acts of kindness."
                e "{i}I just stared at her, a spark of warmth flickering in me.{i}"
                hide Pearl worried at left
                show Pearl number at left
                g "Here's my number if you ever need someone to talk to."
                menu:
                    "Accept b/c u don't have friends":
                        g "Great! Have a great rest of your evening."
                        label great:
                            scene housebig
                            with fade
                            show Ruby happy at truecenter
                            e "Pearl was like an angel sent from heaven. She really is nothing like Emerald. I guess this world isn't that cruel after all."
                            $ renpy.save("1-1", extra_info="Ending 1: Such an angel.")
                            return
                    "Decline b/c u don't want friends":
                        e "I'm sorry. There's no need for that."
                        g "*Smiles.* That's alright. I understand."
                        label amazing:
                            scene housebig
                            with fade
                            show Ruby crying at truecenter
                            e "Why did I not accept her number? She was so kind to me and I was being a pick me."
                            hide Ruby crying at truecenter
                            show Ruby neutral at truecenter
                            e "Oh well, what happened happened. I can't change anything about except look forward to tomorrow."
                            $ renpy.save("1-2", extra_info="Ending 2: Oh well.")
                            return
        "Reject her offer":
            e "No thank you. I appreciate the offer tho."
            g "I understand. I hope you feel better soon."
            label store:
                play music "audio/meowsound.mp3"
                scene catstorebig
                with fade
                show Ruby neutral at left
                e "{i}So many cute cats. How nice it would be to own one...{i}"
                show Black cat
                h "Meow."
                hide Ruby neutral at left
                show Ruby happy at left
                e"{i} You're so cute. How about I just adopt you?{i}"
                menu:
                    "Adopt? Yes b/c IT'S SO CUTE!":
                        label home:
                            play music "audio/rainlofisound.mp3"
                            scene housebig
                            with fade
                            show Ruby happy at truecenter
                            show Black cat at center
                            play music "audio/happysound.mp3"
                            e "{i} Why am I feeling happy just looking at him? Maybe he was the light I needed in this dark world."
                            $ renpy.save("1-3", extra_info="Ending 3: Happy human, happy animal.")
                            return
                    "Adopt? No b/c it's ugly":
                        label gohome:
                            play music "audio/rainlofisound.mp3"
                            scene housebig
                            with fade
                            show Ruby neutral at truecenter
                            e "Aw shucks! What should I do now? Adopting a cat didn't work out..."
                            menu:
                                "Sleep":
                                    e "Yeah I should sleep. I actually going fricking insane."
                                    $ renpy.save ("1-5", extra_info="Ending 5: Just sleep over it.")
                                    return
                                "Go to Emerald's house":
                                    label Emeraldhouse:
                                        play sound "audio/firesound.mp3"
                                        scene houseonfirebig
                                        with fade
                                        show Ruby smirking at truecenter
                                        e "{i}HEHEHEHEH! This is what you get for dumping your best friend, Emerald!{i}"
                                        $ renpy.save("1-4", extra_info="Ending 4: I'd let the world burn.")
                                        return
screen endings_gallery():
    tag menu
    frame:
        vbox:
            text "Endings Unlocked."
            if "1" in persistent.endings:
                text "Ending 1: Such an angel."
            else:
                text "???"
            if "2" in persistent.endings:
                text "Ending 2: Oh well."
            else:
                text "???"
            if "3" in persistent.endings:
                text "Ending 3: Happy human, happy animal."
            else:
                text "???"
            if "4" in persistent.endings:
                text "Ending 4: I'd let the world burn."
            else:
                text "???"
            if "5" in persistent.endings:
                text "Ending 5: Just sleep over it."
            else:
                text "???"  
            textbutton "Return" action Return()                                
                                



