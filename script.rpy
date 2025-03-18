# the letter after define is the shortcut for when i call upon it
# within quotations put the name that appears.

# Notes:
# - Defined Mualani with custom color and textbox background
# - Added dissolve and moveinleft effects for sprite transitions
# - Used wipeleft for background transition
# - Ensured Mualani's chibi sprite is shown in the shop
# - Built-in visual effects: dissolve, fade, move, zoom, pan, wipe, slide, shake, flash
# - Custom transitions: Transform and ATL (Animation and Transformation Language)
# - Particle effects: renpy.show_particles
# - Third-party plugins: Ren'Py Particle System, Ren'Py Live2D, Ren'Py Spine

define M = Character("Mualani", color="#FF69B4", window_background="gui/textbox_mualani.png")

# Define images
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

    # Show Mualani's chibi sprite with a fade-in effect
    show mualani chibi at center with dissolve

    # Mualani introduction
    M "Yooo! My name is Mualani, a member of the people of the springs!"
    M "I don't think you've met me before!"
    M "I come from the vibrant and lively tribe of the people of the springs, where the waves are as wild as our spirits."

    # Change Mualani's chibi sprite to one showing her surfboard with a move-in effect
    hide mualani chibi with dissolve
    show mualani chibi surfboard at center with moveinleft

    M "Let me tell you about my super sharky surfboard. It's not just any surfboard, it's the fastest and coolest one in the entire tribe!"
    M "With it, I can ride the biggest waves and explore the vast ocean like no one else. It's my trusty companion on all my adventures."

    # Hide Mualani's chibi sprite with surfboard with a fade-out effect
    hide mualani chibi surfboard with dissolve

    # Show Mualani's initial chibi sprite again with a fade-in effect
    show mualani chibi at center with dissolve

    # Transition to her shop with a wipe effect
    M "Now, let me take you to my shop where I work.. sometimes!"

    # Change background to her shop and switch OST with a fade effect
    play music "genshin_ost_shop.mp3"
    scene bg natlan_shop with wipeleft

    # Show Mualani's chibi sprite again in the shop
    show mualani chibi at center with dissolve

    M "Welcome to my shop! Here, you can find all sorts of amazing items and gear for your adventures."

    # Continue with the rest of the script
    # ...

    return