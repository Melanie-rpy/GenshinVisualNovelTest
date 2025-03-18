# the letter after define is the shortcut for when i call upon it
# within quotations put the name that appears.


define M = Character("Mualani", color="#FF69B4", window_background="gui/textbox_mualani.png")

# images s
image bg natlan = "bg_natlan.png"
image bg natlan_shop = "bg_natlan_shop.png"
image mualani chibi = "mualani_chibi.png"
image mualani chibi surfboard = "mualani_chibi_surfboard.png"

# LINK START

label start:
    # FADE FROM BLACK
    # OST
    play music "genshin_ost_tribe.mp3"

    scene bg natlan with fade


    show mualani chibi at center with dissolve

    # Mualani introduction
    M "Yooo! My name is Mualani, a member of the people of the springs!"
    M "I don't think you've met me before!"
    M "."

   
    hide mualani chibi with dissolve
    show mualani chibi surfboard at center with moveinleft

    M "Let me tell you about my super sharky surfboard. It's not just any surfboard, it's the fastest and coolest one in the entire tribe!"
    M "With it, I can ride the biggest waves and explore the vast ocean like no one else."

    hide mualani chibi surfboard with dissolve

    show mualani chibi at center with dissolve

    M "Now, let me take you to my shop where I work.. sometimes!"

    play music "genshin_ost_shop.mp3"
    scene bg natlan_shop with wipeleft

    show mualani chibi at center with dissolve

    M "Welcome to my shop! Here, you can find all sorts of amazing items and gear for your adventures."


    return
