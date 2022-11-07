# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Susan")
define dd = Character("David Dalton")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene apartment
    play music "audio/narrator.mp3"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show susansample

    # These display lines of dialogue.

    "Coming home from her latest case, Susan Murphy, private eye, opens the door to her apartment."

    "Stepping inside, glancing down, she sees the expected bills and magazines slipped through the mail slot onto the floor."

    "Among the pile is an ornate envelope, with an equally ornate invitation inside an image of the envelope is displayed, reading:"

    "Dear Susan Murphy, you have been cordially invited as a distinguished guest to ring in 1952 in style aboard the USS Neptune. We will be departing at 6:00 P.M. December 30th from Honolulu Harbour, and returning to the same location on January 3rd. I hope to see you there! - Michael McQuaid"

    stop music

    s "McQuaid, McQuaid, where have I heard that name before? Oh right, I did a case for him. Well, I could use a vacation after today…Sure, why the heck not!"

    s "Once you add a story, pictures, and music, you can release it to the world!"

    scene ship

    "A couple of weeks later, Susan readies to board the Neptune, admiring the lavish yacht."

    scene susancabin

    "As Susan sorts through her luggage, there is a knock at the door."

    dd "There will be a dinner for all the guests in the dining hall in 30 minutes."

    s "Okay, thanks for the information."

    s " (Thoughts): Okay, time for me to get dolled up for dinner. I hope the food is going to be good."
    # This ends the game.

    return
