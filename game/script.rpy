# You can place the script of your game in this file.

# Declare characters used by this game.
init:
    # Define backgrounds here.
    image bg academy = "images/bg_academy.jpg"
    image bg bombshelter = "images/bg_bombshelter.jpg"
    image bg cafeteria = "images/bg_cafeteria.jpg"
    image bg classroom = "images/bg_classroom.jpg"
    image bg dorm = "images/bg_dorm.jpg"
    image bg dorm2 = "images/bg_dorm2.jpg"
    image bg dormhall = "images/bg_dormhall.jpg"
    image bg dormhall1 = "images/bg_dormhall1.jpg"
    image bg dormhall2 = "images/bg_dormhall2.jpg"
    image bg dormhall3 = "images/bg_dormhall3.jpg"
    image bg dormroom = "images/bg_dormroom.jpg"
    image bg dormroom2 = "images/bg_dormroom2.jpg"
    image bg dormroom3 = "images/bg_dormroom3.jpg"
    image bg email1 = "images/bg_email1.png"
    image bg flashback1 = "images/bg_flashback1.jpg"
    image bg flashback2 = "images/bg_flashback2.jpg"
    image bg flashback3 = "images/bg_flashback3.jpg"
    image bg language = "images/bg_language.jpg"
    image bg sunrise = "images/bg_sunrise.jpg"
    image bg newdormroom1 = "images/bg_newdormroom1.jpg"

    image white = "images/ambient_white.png"
    image yellow = "images/ambient_yellow.png"
    image yellowrotate = "images/ambient_yellowrotate.png"
    image kanagoodbye = "images/bg_kanagoodbye.jpg"
    image snowblossom = SnowBlossom(anim.Filmstrip("images/prop_sakura.png", (20, 20), (2, 1), .15), fast=True)
    image angelicblossom = SnowBlossom("images/prop_sparkle.png",count=35,border=0,xspeed=(0,0),yspeed=(-50,-100),start=10, horizontal=False)
    image lotsoflove = SnowBlossom("images/prop_heart.png",count=10,border=20,xspeed=(50,100),yspeed=(-50,-100),start=10, horizontal=True)
    image lotsoflove2 = SnowBlossom("images/prop_heart.png",count=20,border=20,xspeed=(20,30),yspeed=(-100,-150),start=10, horizontal=False)

    # Declare text styles here.
    $ style.create("narrated", "default", u"(text) Narrated")
    $ style.narrated.font = "fonts/DejaVuSerif-BoldItalic.ttf"
    $ style.narrated.size = 18
    $ style.narrated.color = "#EED583"
    $ style.create("emailed", "default", u"(text) Emailed")
    $ style.emailed.color = "#D6EEAA"
    $ style.emailed.font = "fonts/DejaVuSansMono-Bold.ttf"
    $ style.emailed.size = 18
    $ style.create("whispered", "default", u"(text) Whispered")
    $ style.whispered.color = "#B0B0B0"
    $ style.whispered.italic = True
    $ style.create("rollingcredits1", "default", u"(text) Rollingcredits1")
    $ style.rollingcredits1.font = "fonts/DejaVuSansMono-Bold.ttf"
    $ style.rollingcredits1.size = 9
    $ style.rollingcredits1.drop_shadow = (1, 1)
    $ style.rollingcredits1.drop_shadow_color = "#303030"
    $ style.create("rollingcredits2", "default", u"(text) Rollingcredits2")
    $ style.rollingcredits2.font = "fonts/DejaVuSansMono-Bold.ttf"
    $ style.rollingcredits2.size = 9
    $ style.rollingcredits2.drop_shadow = (1, 1)
    $ style.rollingcredits2.drop_shadow_color = "#303030"
    $ style.rollingcredits2.text_align = 0.5
    $ style.create("credits", "default", u"(text) Credits")
    $ style.credits.font = "fonts/DejaVuSansMono-Bold.ttf"
    $ style.credits.size = 18
    $ style.credits.color = "#FFFFFF"
    $ style.credits.outlines = [(2, "#000000", 0, 0)]
    $ style.create("emailedcyllia", "default", u"(text) EmailedCyllia")
    $ style.emailedcyllia.color = "#74EECC"
    $ style.emailedcyllia.font = "fonts/DejaVuSansMono-Bold.ttf"
    $ style.emailedcyllia.size = 18

    # Declare characters used by this game.

    #### kana ####
    $ k = Character(None)

    $ k_angry = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-angry.png", (0,0), "character/kana_mouth-gasp.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-angrytwitch.png",xalign=0.0,yalign=1.0))
    $ k_annoyed = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-angry.png", (0,0), "character/kana_eyes-annoyed.png", (0,0), "character/kana_mouth-pursed.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))
    $ k_baka = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-beady.png", (0,0), "character/kana_mouth-baka.png", (0,0), "character/kana_special-sweatdrop1.png",xalign=0.0,yalign=1.0))
    $ k_bewildered = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-surprised.png", (0,0), "character/kana_mouth-smaller.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))
    $ k_creepy = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_mouth-happy.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-evil.png",xalign=0.0,yalign=1.0))
    $ k_dream = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-sighing.png", (0,0), "character/kana_mouth-happy.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))
    $ k_ehhh = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-nervous.png", (0,0), "character/kana_mouth-nervous.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-sweatdrop1.png", (0,0), "character/kana_special-sweatdrop2.png",xalign=0.0,yalign=1.0))
    $ k_evil = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-angry.png", (0,0), "character/kana_eyes-evil.png", (0,0), "character/kana_mouth-happy.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))
    $ k_furious = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-angry.png", (0,0), "character/kana_eyes-annoyed.png", (0,0), "character/kana_mouth-gasp.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-angrytwitch.png",xalign=0.0,yalign=1.0))
    $ k_gasp = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-beady.png", (0,0), "character/kana_mouth-gasp.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-sweatdrop1.png",xalign=0.0,yalign=1.0))
    $ k_genki = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-arches.png", (0,0), "character/kana_mouth-happy.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))
    $ k_glad = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-normal.png", (0,0), "character/kana_mouth-smile.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))
    $ k_happy = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-normal.png", (0,0), "character/kana_mouth-happy.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))
    $ k_incredulous = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-surprised.png", (0,0), "character/kana_mouth-gasp.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))
    $ k_nervous = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-arches.png", (0,0), "character/kana_mouth-small.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-sweatdrop1.png", (0,0), "character/kana_special-sweatdrop2.png",xalign=0.0,yalign=1.0))
    $ k_omg = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-surprised.png", (0,0), "character/kana_mouth-wide.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-sweatdrop1.png", (0,0), "character/kana_special-sweatdrop2.png",xalign=0.0,yalign=1.0))
    $ k_oops = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-beady.png", (0,0), "character/kana_mouth-smaller.png", (0,0), "character/kana_special-sweatdrop1.png",xalign=0.0,yalign=1.0))
    $ k_painful = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-quirky.png", (0,0), "character/kana_eyes-squealing.png", (0,0), "character/kana_mouth-baka.png", (0,0), "character/kana_special-sweatdrop1.png",xalign=0.0,yalign=1.0))
    $ k_panic = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-sad.png", (0,0), "character/kana_eyes-shocked.png", (0,0), "character/kana_mouth-gasp.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-sweatdrop1.png", (0,0), "character/kana_special-sweatdrop2.png",xalign=0.0,yalign=1.0))
    $ k_relieved = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal-low.png", (0,0), "character/kana_eyes-smug.png", (0,0), "character/kana_mouth-happy.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))
    $ k_reprimand = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-angry.png", (0,0), "character/kana_eyes-evil.png", (0,0), "character/kana_mouth-smaller.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))
    $ k_sad = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-normal.png", (0,0), "character/kana_mouth-small.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))
    $ k_sarcastic = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-unamused.png", (0,0), "character/kana_mouth-smaller.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-sweatdrop1.png",xalign=0.0,yalign=1.0))
    $ k_scary = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_mouth-nervous.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-evil.png", (0,0), "character/kana_special-sweatdrop1.png", (0,0), "character/kana_special-sweatdrop2.png",xalign=0.0,yalign=1.0))
    $ k_scheme = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-angry.png", (0,0), "character/kana_eyes-evil.png", (0,0), "character/kana_mouth-smug.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))
    $ k_shock = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-quirky.png", (0,0), "character/kana_eyes-shocked.png", (0,0), "character/kana_mouth-shocked.png", (0,0), "character/kana_special-shockcrown.png",xalign=0.0,yalign=1.0))
    $ k_shout = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-angry.png", (0,0), "character/kana_eyes-squealing.png", (0,0), "character/kana_mouth-gasp.png", (0,0), "character/kana_special-angrytwitch.png",xalign=0.0,yalign=1.0))
    $ k_sigh = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-sighing.png", (0,0), "character/kana_mouth-smaller.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))
    $ k_smile = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-arches.png", (0,0), "character/kana_mouth-smile.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))
    $ k_smug = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal-low.png", (0,0), "character/kana_eyes-smug.png", (0,0), "character/kana_mouth-smug.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))
    $ k_sneaky = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-sneaky.png", (0,0), "character/kana_mouth-happy.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-sweatdrop1.png",xalign=0.0,yalign=1.0))
    $ k_squeal = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-squealing.png", (0,0), "character/kana_mouth-happy.png",xalign=0.0,yalign=1.0))
    $ k_stare = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-angry.png", (0,0), "character/kana_eyes-evil.png", (0,0), "character/kana_mouth-pursed.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))
    $ k_swirl = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-swirly.png", (0,0), "character/kana_mouth-happy.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-sweatdrop1.png", (0,0), "character/kana_special-sweatdrop2.png",xalign=0.0,yalign=1.0))
    $ k_tired = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal-low.png", (0,0), "character/kana_eyes-smug.png", (0,0), "character/kana_mouth-smaller.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))
    $ k_treacherous = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-angry.png", (0,0), "character/kana_eyes-evil.png", (0,0), "character/kana_mouth-smile.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))
    $ k_unamused = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal-low.png", (0,0), "character/kana_eyes-unamused.png", (0,0), "character/kana_mouth-pursed.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))
    $ k_villainous = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-angry.png", (0,0), "character/kana_eyes-evil.png", (0,0), "character/kana_mouth-small.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))
    $ k_waterfall = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-sad.png", (0,0), "character/kana_eyes-waterfalltears.png", (0,0), "character/kana_mouth-smaller.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))
    $ k_weird = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-sneaky.png", (0,0), "character/kana_mouth-pursed.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-sweatdrop1.png",xalign=0.0,yalign=1.0))
    $ k_worried = Character(None, window_top_padding=40, window_left_padding=160, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-nervous.png", (0,0), "character/kana_mouth-small.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0))

    ## Do not add until version 6.12.1
    #$ k_angry = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-angry.png", (0,0), "character/kana_mouth-gasp.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-angrytwitch.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_annoyed = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-angry.png", (0,0), "character/kana_eyes-annoyed.png", (0,0), "character/kana_mouth-pursed.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_baka = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-beady.png", (0,0), "character/kana_mouth-baka.png", (0,0), "character/kana_special-sweatdrop1.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_bewildered = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-surprised.png", (0,0), "character/kana_mouth-smaller.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_creepy = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_mouth-happy.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-evil.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_dream = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-sighing.png", (0,0), "character/kana_mouth-happy.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_ehhh = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-nervous.png", (0,0), "character/kana_mouth-nervous.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-sweatdrop1.png", (0,0), "character/kana_special-sweatdrop2.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_evil = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-angry.png", (0,0), "character/kana_eyes-evil.png", (0,0), "character/kana_mouth-happy.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_furious = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-angry.png", (0,0), "character/kana_eyes-annoyed.png", (0,0), "character/kana_mouth-gasp.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-angrytwitch.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_gasp = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-beady.png", (0,0), "character/kana_mouth-gasp.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-sweatdrop1.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_genki = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-arches.png", (0,0), "character/kana_mouth-happy.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_glad = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-normal.png", (0,0), "character/kana_mouth-smile.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_happy = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-normal.png", (0,0), "character/kana_mouth-happy.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_incredulous = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-surprised.png", (0,0), "character/kana_mouth-gasp.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_nervous = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-arches.png", (0,0), "character/kana_mouth-small.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-sweatdrop1.png", (0,0), "character/kana_special-sweatdrop2.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_omg = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-surprised.png", (0,0), "character/kana_mouth-wide.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-sweatdrop1.png", (0,0), "character/kana_special-sweatdrop2.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_oops = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-beady.png", (0,0), "character/kana_mouth-smaller.png", (0,0), "character/kana_special-sweatdrop1.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_painful = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-quirky.png", (0,0), "character/kana_eyes-squealing.png", (0,0), "character/kana_mouth-baka.png", (0,0), "character/kana_special-sweatdrop1.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_panic = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-sad.png", (0,0), "character/kana_eyes-shocked.png", (0,0), "character/kana_mouth-gasp.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-sweatdrop1.png", (0,0), "character/kana_special-sweatdrop2.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_relieved = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal-low.png", (0,0), "character/kana_eyes-smug.png", (0,0), "character/kana_mouth-happy.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_reprimand = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-angry.png", (0,0), "character/kana_eyes-evil.png", (0,0), "character/kana_mouth-smaller.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_sad = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-normal.png", (0,0), "character/kana_mouth-small.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_sarcastic = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-unamused.png", (0,0), "character/kana_mouth-smaller.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-sweatdrop1.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_scary = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_mouth-nervous.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-evil.png", (0,0), "character/kana_special-sweatdrop1.png", (0,0), "character/kana_special-sweatdrop2.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_scheme = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-angry.png", (0,0), "character/kana_eyes-evil.png", (0,0), "character/kana_mouth-smug.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_shock = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-quirky.png", (0,0), "character/kana_eyes-shocked.png", (0,0), "character/kana_mouth-shocked.png", (0,0), "character/kana_special-shockcrown.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_shout = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-angry.png", (0,0), "character/kana_eyes-squealing.png", (0,0), "character/kana_mouth-gasp.png", (0,0), "character/kana_special-angrytwitch.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_sigh = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-sighing.png", (0,0), "character/kana_mouth-smaller.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_smile = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-arches.png", (0,0), "character/kana_mouth-smile.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_smug = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal-low.png", (0,0), "character/kana_eyes-smug.png", (0,0), "character/kana_mouth-smug.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_sneaky = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-sneaky.png", (0,0), "character/kana_mouth-happy.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-sweatdrop1.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_squeal = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-squealing.png", (0,0), "character/kana_mouth-happy.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_stare = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-angry.png", (0,0), "character/kana_eyes-evil.png", (0,0), "character/kana_mouth-pursed.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_swirl = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-happy.png", (0,0), "character/kana_eyes-swirly.png", (0,0), "character/kana_mouth-happy.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-sweatdrop1.png", (0,0), "character/kana_special-sweatdrop2.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_tired = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal-low.png", (0,0), "character/kana_eyes-smug.png", (0,0), "character/kana_mouth-smaller.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_treacherous = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-angry.png", (0,0), "character/kana_eyes-evil.png", (0,0), "character/kana_mouth-smile.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_unamused = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal-low.png", (0,0), "character/kana_eyes-unamused.png", (0,0), "character/kana_mouth-pursed.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_villainous = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-angry.png", (0,0), "character/kana_eyes-evil.png", (0,0), "character/kana_mouth-small.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_waterfall = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-sad.png", (0,0), "character/kana_eyes-waterfalltears.png", (0,0), "character/kana_mouth-smaller.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_weird = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-sneaky.png", (0,0), "character/kana_mouth-pursed.png", (0,0), "character/kana_special-nose.png", (0,0), "character/kana_special-sweatdrop1.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")
    #$ k_worried = Character(None, show_side_image=im.Composite(None, (0,0), "character/kana_body.png", (0,0), "character/kana_eyebrows-normal.png", (0,0), "character/kana_eyes-nervous.png", (0,0), "character/kana_mouth-small.png", (0,0), "character/kana_special-nose.png",xalign=0.0,yalign=1.0), ctc="ctc_arrow", ctc_position="fixed")

    #### miharu ####
    image miharu calm = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-happy-low.png", (0,0), "character/miharu_eyes-narrow.png", (0,0), "character/miharu_mouth-smile.png")
    image miharu cautious = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-normal.png", (0,0), "character/miharu_eyes-widen.png", (0,0), "character/miharu_mouth-calm.png")
    image miharu concern = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-sad.png", (0,0), "character/miharu_eyes-widen.png", (0,0), "character/miharu_mouth-calm.png")
    image miharu confused = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-sad.png", (0,0), "character/miharu_eyes-constrict.png", (0,0), "character/miharu_mouth-awe.png")
    image miharu curious = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-normal.png", (0,0), "character/miharu_eyes-widen.png", (0,0), "character/miharu_mouth-awe.png")
    image miharu cute = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-happy.png", (0,0), "character/miharu_eyes-widen.png", (0,0), "character/miharu_mouth-smile.png")
    image miharu doubt = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-sad.png", (0,0), "character/miharu_eyes-widen.png", (0,0), "character/miharu_mouth-smile.png")
    image miharu dread = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-sad.png", (0,0), "character/miharu_eyes-constrict.png", (0,0), "character/miharu_mouth-calm.png")
    image miharu excited = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-happy.png", (0,0), "character/miharu_eyes-widen.png", (0,0), "character/miharu_mouth-genki.png")
    image miharu genki = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-happy-low.png", (0,0), "character/miharu_eyes-arches.png", (0,0), "character/miharu_mouth-genki.png")
    image miharu glad = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-happy-low.png", (0,0), "character/miharu_eyes-arches.png", (0,0), "character/miharu_mouth-pleasant.png")
    image miharu grief = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-sad-low.png", (0,0), "character/miharu_eyes-arches.png", (0,0), "character/miharu_mouth-calm.png")
    image miharu happy = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-happy.png", (0,0), "character/miharu_eyes-widen.png", (0,0), "character/miharu_mouth-pleasant.png")
    image miharu nervous = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-sad.png", (0,0), "character/miharu_eyes-constrict.png", (0,0), "character/miharu_mouth-smile.png")
    image miharu relieved = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-happy-low.png", (0,0), "character/miharu_eyes-narrow.png", (0,0), "character/miharu_mouth-pleasant.png")
    image miharu sad = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-sad-low.png", (0,0), "character/miharu_eyes-narrow.png", (0,0), "character/miharu_mouth-awe.png")
    image miharu sigh = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-happy-low.png", (0,0), "character/miharu_eyes-arches.png", (0,0), "character/miharu_mouth-awe.png")
    image miharu smile = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-happy-low.png", (0,0), "character/miharu_eyes-arches.png", (0,0), "character/miharu_mouth-smile.png")
    image miharu smug = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-normal.png", (0,0), "character/miharu_eyes-widen.png", (0,0), "character/miharu_mouth-smile.png")
    image miharu tired = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-happy-low.png", (0,0), "character/miharu_eyes-narrow.png", (0,0), "character/miharu_mouth-calm.png")
    image miharu uncomfortable = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-sad.png", (0,0), "character/miharu_eyes-constrict.png", (0,0), "character/miharu_mouth-pleasant.png")
    image miharu whimper = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-sad-low.png", (0,0), "character/miharu_eyes-arches.png", (0,0), "character/miharu_mouth-awe.png")
    image miharu wonder = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-happy.png", (0,0), "character/miharu_eyes-constrict.png", (0,0), "character/miharu_mouth-awe.png")
    image miharu worried = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-sad.png", (0,0), "character/miharu_eyes-widen.png", (0,0), "character/miharu_mouth-awe.png")
    image miharu chibi1 = "character/miharu_chibi1.png"
    image miharu chibi2 = "character/miharu_chibi2.png"
    image miharu chibi3 = "character/miharu_chibi3.png"
    # ad-hoc expressions
    image miharu curiousbandage = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-normal.png", (0,0), "character/miharu_eyes-widen.png", (0,0), "character/miharu_mouth-awe.png", (0,0), "character/miharu_special-bandage.png")
    image miharu cutebandage = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-happy.png", (0,0), "character/miharu_eyes-widen.png", (0,0), "character/miharu_mouth-smile.png", (0,0), "character/miharu_special-bandage.png")
    image miharu dreadbandage = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-sad.png", (0,0), "character/miharu_eyes-constrict.png", (0,0), "character/miharu_mouth-calm.png", (0,0), "character/miharu_special-bandage.png")
    image miharu excitedbandage = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-happy.png", (0,0), "character/miharu_eyes-widen.png", (0,0), "character/miharu_mouth-genki.png", (0,0), "character/miharu_special-bandage.png")
    image miharu griefbandage = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-sad-low.png", (0,0), "character/miharu_eyes-arches.png", (0,0), "character/miharu_mouth-calm.png", (0,0), "character/miharu_special-bandage.png")
    image miharu happybandage = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-happy.png", (0,0), "character/miharu_eyes-widen.png", (0,0), "character/miharu_mouth-pleasant.png", (0,0), "character/miharu_special-bandage.png")
    image miharu relievedbandage = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-happy-low.png", (0,0), "character/miharu_eyes-narrow.png", (0,0), "character/miharu_mouth-pleasant.png", (0,0), "character/miharu_special-bandage.png")
    image miharu smilebandage = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-happy-low.png", (0,0), "character/miharu_eyes-arches.png", (0,0), "character/miharu_mouth-smile.png", (0,0), "character/miharu_special-bandage.png")
    image miharu uncomfortablebandage = im.Composite(None, (0,0), "character/miharu_body.png", (0,0), "character/miharu_eyebrows-sad.png", (0,0), "character/miharu_eyes-constrict.png", (0,0), "character/miharu_mouth-pleasant.png", (0,0), "character/miharu_special-bandage.png")
    image miharu casual_confused = im.Composite(None, (0,0), "character/miharu_body_casual.png", (0,0), "character/miharu_eyebrows-sad.png", (0,0), "character/miharu_eyes-constrict.png", (0,0), "character/miharu_mouth-awe.png")
    image miharu casual_nervous = im.Composite(None, (0,0), "character/miharu_body_casual.png", (0,0), "character/miharu_eyebrows-sad.png", (0,0), "character/miharu_eyes-constrict.png", (0,0), "character/miharu_mouth-smile.png")
    image miharu casual_grief = im.Composite(None, (0,0), "character/miharu_body_casual.png", (0,0), "character/miharu_eyebrows-sad-low.png", (0,0), "character/miharu_eyes-arches.png", (0,0), "character/miharu_mouth-calm.png")
    image miharu casual_whimper = im.Composite(None, (0,0), "character/miharu_body_casual.png", (0,0), "character/miharu_eyebrows-sad-low.png", (0,0), "character/miharu_eyes-arches.png", (0,0), "character/miharu_mouth-awe.png")
    image miharu casual_uncomfortable = im.Composite(None, (0,0), "character/miharu_body_casual.png", (0,0), "character/miharu_eyebrows-sad.png", (0,0), "character/miharu_eyes-constrict.png", (0,0), "character/miharu_mouth-pleasant.png")
    image miharu casual_glad = im.Composite(None, (0,0), "character/miharu_body_casual.png", (0,0), "character/miharu_eyebrows-happy-low.png", (0,0), "character/miharu_eyes-arches.png", (0,0), "character/miharu_mouth-pleasant.png")

    #### aizawa ####
    image aizawa accuse = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal.png", (0,0), "character/aizawa_eyes-furious.png", (0,0), "character/aizawa_mouth-awe.png")
    image aizawa aho = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy-low.png", (0,0), "character/aizawa_eyes-shock.png", (0,0), "character/aizawa_mouth-genki.png", (0,0), "character/aizawa_special-sweatdrop.png")
    image aizawa amused = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy-low.png", (0,0), "character/aizawa_eyes-tired.png", (0,0), "character/aizawa_mouth-smile.png")
    image aizawa anxious = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy.png", (0,0), "character/aizawa_eyes-happy.png", (0,0), "character/aizawa_mouth-normal.png")
    image aizawa astound = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal.png", (0,0), "character/aizawa_eyes-surprise.png", (0,0), "character/aizawa_mouth-pursed.png")
    image aizawa awesome = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal.png", (0,0), "character/aizawa_eyes-normal.png", (0,0), "character/aizawa_mouth-pleasant.png")
    image aizawa baka = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-sad-low.png", (0,0), "character/aizawa_eyes-beady.png", (0,0), "character/aizawa_mouth-baka.png", (0,0), "character/aizawa_special-sweatdrop.png")
    image aizawa beg = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-sad-low.png", (0,0), "character/aizawa_eyes-tired.png", (0,0), "character/aizawa_mouth-gasp.png")
    image aizawa calm = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy-low.png", (0,0), "character/aizawa_eyes-tired.png", (0,0), "character/aizawa_mouth-normal.png")
    image aizawa chastisecenter = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal-low.png", (0,0), "character/aizawa_eyes-sneaky-center.png", (0,0), "character/aizawa_mouth-awe.png")
    image aizawa chastiseleft = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal-low.png", (0,0), "character/aizawa_eyes-sneaky-left.png", (0,0), "character/aizawa_mouth-awe.png")
    image aizawa chastiseright = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal-low.png", (0,0), "character/aizawa_eyes-sneaky-right.png", (0,0), "character/aizawa_mouth-awe.png")
    image aizawa chortlecenter = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal-low.png", (0,0), "character/aizawa_eyes-sneaky-center.png", (0,0), "character/aizawa_mouth-pleasant.png")
    image aizawa chortleleft = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal-low.png", (0,0), "character/aizawa_eyes-sneaky-left.png", (0,0), "character/aizawa_mouth-pleasant.png")
    image aizawa chortleright = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal-low.png", (0,0), "character/aizawa_eyes-sneaky-right.png", (0,0), "character/aizawa_mouth-pleasant.png")
    image aizawa complain = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-sad-low.png", (0,0), "character/aizawa_eyes-dream.png", (0,0), "character/aizawa_mouth-gasp.png")
    image aizawa confused = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-sad-low.png", (0,0), "character/aizawa_eyes-beady.png", (0,0), "character/aizawa_mouth-pursed.png", (0,0), "character/aizawa_special-sweatdrop.png")
    image aizawa confuzzled = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-sad-low.png", (0,0), "character/aizawa_eyes-beady.png", (0,0), "character/aizawa_mouth-awe.png", (0,0), "character/aizawa_special-sweatdrop.png")
    image aizawa cool = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal.png", (0,0), "character/aizawa_eyes-normal.png", (0,0), "character/aizawa_mouth-normal.png")
    image aizawa cry = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-sad-low.png", (0,0), "character/aizawa_eyes-waterfall.png", (0,0), "character/aizawa_mouth-gasp.png")
    image aizawa cute = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy-low.png", (0,0), "character/aizawa_eyes-arches.png", (0,0), "character/aizawa_mouth-pleasant.png")
    image aizawa dream = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy-low.png", (0,0), "character/aizawa_eyes-dream.png", (0,0), "character/aizawa_mouth-smile.png")
    image aizawa drunksmile = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy-low.png", (0,0), "character/aizawa_eyes-arches.png", (0,0), "character/aizawa_mouth-smile.png", (0,0), "character/aizawa_special-blush.png")
    image aizawa dumbfounded = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy.png", (0,0), "character/aizawa_eyes-surprise.png", (0,0), "character/aizawa_mouth-genki.png", (0,0), "character/aizawa_special-sweatdrop.png")
    image aizawa evilchuckle = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal.png", (0,0), "character/aizawa_eyes-angry.png", (0,0), "character/aizawa_mouth-pleasant.png")
    image aizawa evilcool = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal.png", (0,0), "character/aizawa_eyes-angry.png", (0,0), "character/aizawa_mouth-normal.png")
    image aizawa evilsmile = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal.png", (0,0), "character/aizawa_eyes-angry.png", (0,0), "character/aizawa_mouth-smile.png")
    image aizawa evilsmug = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal.png", (0,0), "character/aizawa_eyes-angry.png", (0,0), "character/aizawa_mouth-smug.png")
    image aizawa fatigue = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-sad-low.png", (0,0), "character/aizawa_eyes-dream.png", (0,0), "character/aizawa_mouth-pursed.png")
    image aizawa frustrated = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal-low.png", (0,0), "character/aizawa_eyes-squeal.png", (0,0), "character/aizawa_mouth-gasp.png")
    image aizawa gasp = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy-low.png", (0,0), "character/aizawa_eyes-shock.png", (0,0), "character/aizawa_mouth-gasp.png", (0,0), "character/aizawa_special-sweatdrop.png")
    image aizawa genki = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy-low.png", (0,0), "character/aizawa_eyes-arches.png", (0,0), "character/aizawa_mouth-genki.png")
    image aizawa glad = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy.png", (0,0), "character/aizawa_eyes-normal.png", (0,0), "character/aizawa_mouth-pleasant.png")
    image aizawa grateful = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy-low.png", (0,0), "character/aizawa_eyes-tired.png", (0,0), "character/aizawa_mouth-pleasant.png")
    image aizawa happy = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy.png", (0,0), "character/aizawa_eyes-normal.png", (0,0), "character/aizawa_mouth-genki.png")
    image aizawa hungry = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-sad-low.png", (0,0), "character/aizawa_eyes-arches.png", (0,0), "character/aizawa_mouth-pout.png")
    image aizawa hurt = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-sad-low.png", (0,0), "character/aizawa_eyes-arches.png", (0,0), "character/aizawa_mouth-normal.png")
    image aizawa impatient = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal-low.png", (0,0), "character/aizawa_eyes-arches.png", (0,0), "character/aizawa_mouth-pursed.png")
    image aizawa impressed = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy.png", (0,0), "character/aizawa_eyes-surprise.png", (0,0), "character/aizawa_mouth-pleasant.png")
    image aizawa inquisitive = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal.png", (0,0), "character/aizawa_eyes-normal.png", (0,0), "character/aizawa_mouth-pursed.png")
    image aizawa joyful = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy.png", (0,0), "character/aizawa_eyes-happy.png", (0,0), "character/aizawa_mouth-pleasant.png", (0,0), "character/aizawa_special-blush.png")
    image aizawa lecture = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy-low.png", (0,0), "character/aizawa_eyes-wise.png", (0,0), "character/aizawa_mouth-pleasant.png")
    image aizawa love = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy.png", (0,0), "character/aizawa_eyes-happy.png", (0,0), "character/aizawa_mouth-genki.png", (0,0), "character/aizawa_special-blush.png")
    image aizawa maniac = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal.png", (0,0), "character/aizawa_eyes-surprise.png", (0,0), "character/aizawa_mouth-stupidgrin.png")
    image aizawa meditate = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy-low.png", (0,0), "character/aizawa_eyes-wise.png", (0,0), "character/aizawa_mouth-pursed.png")
    image aizawa megasigh = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-sad-low.png", (0,0), "character/aizawa_eyes-dream.png", (0,0), "character/aizawa_mouth-wide.png", (0,0), "character/aizawa_special-sweatdrop.png", (0,0), "character/aizawa_special-hidenose.png")
    image aizawa moronic = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-sad-low.png", (0,0), "character/aizawa_eyes-beady.png", (0,0), "character/aizawa_mouth-wide.png", (0,0), "character/aizawa_special-sweatdrop.png", (0,0), "character/aizawa_special-hidenose.png")
    image aizawa naive = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy.png", (0,0), "character/aizawa_eyes-happy.png", (0,0), "character/aizawa_mouth-awe.png")
    image aizawa nervous = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy-low.png", (0,0), "character/aizawa_eyes-arches.png", (0,0), "character/aizawa_mouth-smile.png", (0,0), "character/aizawa_special-sweatdrop.png")
    image aizawa obsessed = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy.png", (0,0), "character/aizawa_eyes-happy.png", (0,0), "character/aizawa_mouth-stupidgrin.png")
    image aizawa oops = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-sad-low.png", (0,0), "character/aizawa_eyes-beady.png", (0,0), "character/aizawa_mouth-gasp.png", (0,0), "character/aizawa_special-sweatdrop.png")
    image aizawa orly = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy.png", (0,0), "character/aizawa_eyes-mocking.png", (0,0), "character/aizawa_mouth-stupidgrin.png")
    image aizawa pity = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-sad.png", (0,0), "character/aizawa_eyes-normal.png", (0,0), "character/aizawa_mouth-awe.png")
    image aizawa pleasantdream = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy-low.png", (0,0), "character/aizawa_eyes-dream.png", (0,0), "character/aizawa_mouth-pleasant.png")
    image aizawa reel = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-sad-low.png", (0,0), "character/aizawa_eyes-squeal.png", (0,0), "character/aizawa_mouth-pursed.png")
    image aizawa reprimand = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal.png", (0,0), "character/aizawa_eyes-furious.png", (0,0), "character/aizawa_mouth-gasp.png")
    image aizawa resign = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-sad-low.png", (0,0), "character/aizawa_eyes-dream.png", (0,0), "character/aizawa_mouth-pout.png")
    image aizawa revenge = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal.png", (0,0), "character/aizawa_eyes-furious.png", (0,0), "character/aizawa_mouth-smile.png")
    image aizawa sad = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-sad-low.png", (0,0), "character/aizawa_eyes-tired.png", (0,0), "character/aizawa_mouth-awe.png")
    image aizawa sadistic = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal.png", (0,0), "character/aizawa_eyes-furious.png", (0,0), "character/aizawa_mouth-stupidgrin.png")
    image aizawa savor = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal-low.png", (0,0), "character/aizawa_eyes-squeal.png", (0,0), "character/aizawa_mouth-smile.png")
    image aizawa scared = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal.png", (0,0), "character/aizawa_eyes-surprise.png", (0,0), "character/aizawa_mouth-gasp.png", (0,0), "character/aizawa_special-sweatdrop.png")
    image aizawa schemecenter = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal-low.png", (0,0), "character/aizawa_eyes-sneaky-center.png", (0,0), "character/aizawa_mouth-smile.png")
    image aizawa schemeleft = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal-low.png", (0,0), "character/aizawa_eyes-sneaky-left.png", (0,0), "character/aizawa_mouth-smile.png")
    image aizawa schemeright = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal-low.png", (0,0), "character/aizawa_eyes-sneaky-right.png", (0,0), "character/aizawa_mouth-smile.png")
    image aizawa scold = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal.png", (0,0), "character/aizawa_eyes-angry.png", (0,0), "character/aizawa_mouth-gasp.png")
    image aizawa scream = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal-low.png", (0,0), "character/aizawa_eyes-squeal.png", (0,0), "character/aizawa_mouth-wide.png", (0,0), "character/aizawa_special-hidenose.png")
    image aizawa shock = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy-low.png", (0,0), "character/aizawa_eyes-shock.png", (0,0), "character/aizawa_mouth-wide.png", (0,0), "character/aizawa_special-sweatdrop.png", (0,0), "character/aizawa_special-hidenose.png")
    image aizawa sigh = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-sad-low.png", (0,0), "character/aizawa_eyes-dream.png", (0,0), "character/aizawa_mouth-awe.png")
    image aizawa smile = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy-low.png", (0,0), "character/aizawa_eyes-arches.png", (0,0), "character/aizawa_mouth-smile.png")
    image aizawa smug = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy-low.png", (0,0), "character/aizawa_eyes-arches.png", (0,0), "character/aizawa_mouth-smug.png")
    image aizawa snicker = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy.png", (0,0), "character/aizawa_eyes-mocking.png", (0,0), "character/aizawa_mouth-smug.png")
    image aizawa snide = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal.png", (0,0), "character/aizawa_eyes-normal.png", (0,0), "character/aizawa_mouth-smile.png")
    image aizawa speechlesscenter = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal-low.png", (0,0), "character/aizawa_eyes-sneaky-center.png", (0,0), "character/aizawa_mouth-pursed.png")
    image aizawa speechlessleft = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal-low.png", (0,0), "character/aizawa_eyes-sneaky-left.png", (0,0), "character/aizawa_mouth-pursed.png")
    image aizawa speechlessright = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal-low.png", (0,0), "character/aizawa_eyes-sneaky-right.png", (0,0), "character/aizawa_mouth-pursed.png")
    image aizawa squeal = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal-low.png", (0,0), "character/aizawa_eyes-squeal.png", (0,0), "character/aizawa_mouth-genki.png")
    image aizawa stare = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal.png", (0,0), "character/aizawa_eyes-furious.png", (0,0), "character/aizawa_mouth-pursed.png")
    image aizawa sweetdream = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy-low.png", (0,0), "character/aizawa_eyes-dream.png", (0,0), "character/aizawa_mouth-normal.png")
    image aizawa tearsofpride = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy-low.png", (0,0), "character/aizawa_eyes-waterfall.png", (0,0), "character/aizawa_mouth-pleasant.png")
    image aizawa tearsofjoy = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-happy-low.png", (0,0), "character/aizawa_eyes-waterfall.png", (0,0), "character/aizawa_mouth-genki.png")
    image aizawa tired = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-sad-low.png", (0,0), "character/aizawa_eyes-tired.png", (0,0), "character/aizawa_mouth-pursed.png")
    image aizawa unamused = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-normal.png", (0,0), "character/aizawa_eyes-angry.png", (0,0), "character/aizawa_mouth-pursed.png")
    image aizawa weep = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-sad-low.png", (0,0), "character/aizawa_eyes-waterfall.png", (0,0), "character/aizawa_mouth-baka.png")
    image aizawa whimper = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-sad-low.png", (0,0), "character/aizawa_eyes-waterfall.png", (0,0), "character/aizawa_mouth-pout.png")
    image aizawa yelp = im.Composite(None, (0,0), "character/aizawa_body.png", (0,0), "character/aizawa_eyebrows-sad-low.png", (0,0), "character/aizawa_eyes-squeal.png", (0,0), "character/aizawa_mouth-pout.png")

    #### freya ####
    image freya angry = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry.png", (0,0), "character/freya_eyes-surprise.png", (0,0), "character/freya_mouth-frown.png")
    image freya annoyed = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry-low.png", (0,0), "character/freya_eyes-dream.png", (0,0), "character/freya_mouth-bitelip.png")
    image freya bashful = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-happy-low.png", (0,0), "character/freya_eyes-sad-away.png", (0,0), "character/freya_mouth-smile.png")
    image freya berate = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry-low.png", (0,0), "character/freya_eyes-leer.png", (0,0), "character/freya_mouth-shout.png")
    image freya blankstare = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-straight-low.png", (0,0), "character/freya_eyes-deadpan.png", (0,0), "character/freya_mouth-pursed.png")
    image freya bloodlust = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry.png", (0,0), "character/freya_eyes-angry.png", (0,0), "character/freya_mouth-grin.png")
    image freya bored = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-happy-low.png", (0,0), "character/freya_eyes-leer.png", (0,0), "character/freya_mouth-frown.png")
    image freya breakdown = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-happy-low.png", (0,0), "character/freya_eyes-deadpan.png", (0,0), "character/freya_mouth-grin.png")
    image freya calm = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-normal.png", (0,0), "character/freya_eyes-normal.png", (0,0), "character/freya_mouth-smile.png")
    image freya chide = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry-low.png", (0,0), "character/freya_eyes-dream.png", (0,0), "character/freya_mouth-reprimand.png")
    image freya coldstare = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-normal.png", (0,0), "character/freya_eyes-angry.png", (0,0), "character/freya_mouth-frown.png")
    image freya complain = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-normal-low.png", (0,0), "character/freya_eyes-arches.png", (0,0), "character/freya_mouth-gasp.png")
    image freya cool = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry.png", (0,0), "character/freya_eyes-normal.png", (0,0), "character/freya_mouth-smile.png")
    image freya covet = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-happy-low.png", (0,0), "character/freya_eyes-sad-away.png", (0,0), "character/freya_mouth-pleasant.png")
    image freya crazy = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-straight.png", (0,0), "character/freya_eyes-madness.png", (0,0), "character/freya_mouth-grin.png")
    image freya cry = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-sad-low.png", (0,0), "character/freya_eyes-sad-away.png", (0,0), "character/freya_mouth-frown.png")
    image freya curious = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-normal.png", (0,0), "character/freya_eyes-normal.png", (0,0), "character/freya_mouth-normal.png")
    image freya cute = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-happy.png", (0,0), "character/freya_eyes-normal.png", (0,0), "character/freya_mouth-pleasant.png")
    image freya cynical = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-normal-low.png", (0,0), "character/freya_eyes-leer.png", (0,0), "character/freya_mouth-crazygrin.png")
    image freya defensive = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry.png", (0,0), "character/freya_eyes-surprise.png", (0,0), "character/freya_mouth-grin.png")
    image freya depressed = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-sad.png", (0,0), "character/freya_eyes-deadpan.png", (0,0), "character/freya_mouth-frown.png")
    image freya deranged = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry.png", (0,0), "character/freya_eyes-madness.png", (0,0), "character/freya_mouth-crazygrin.png")
    image freya despair = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-sad-low.png", (0,0), "character/freya_eyes-sad-away.png", (0,0), "character/freya_mouth-awe.png")
    image freya disapprove = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry-low.png", (0,0), "character/freya_eyes-angry.png", (0,0), "character/freya_mouth-pursed.png")
    image freya disturbed = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-happy.png", (0,0), "character/freya_eyes-madness.png", (0,0), "character/freya_mouth-pursed.png")
    image freya dread = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-sad.png", (0,0), "character/freya_eyes-surprise.png", (0,0), "character/freya_mouth-gasp.png")
    image freya dream = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-straight-low.png", (0,0), "character/freya_eyes-dream.png", (0,0), "character/freya_mouth-normal.png")
    image freya evil = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry-low.png", (0,0), "character/freya_eyes-leer.png", (0,0), "character/freya_mouth-grin.png")
    image freya evildream = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry-low.png", (0,0), "character/freya_eyes-dream.png", (0,0), "character/freya_mouth-crazygrin.png")
    image freya frustrated = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-straight-low.png", (0,0), "character/freya_eyes-sad-away.png", (0,0), "character/freya_mouth-bitelip.png")
    image freya fury = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry.png", (0,0), "character/freya_eyes-angry.png", (0,0), "character/freya_mouth-bitelip.png")
    image freya gasp = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-happy.png", (0,0), "character/freya_eyes-normal.png", (0,0), "character/freya_mouth-gasp.png")
    image freya glad = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-happy-low.png", (0,0), "character/freya_eyes-arches.png", (0,0), "character/freya_mouth-pleasant.png")
    image freya glare = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry-low.png", (0,0), "character/freya_eyes-leer.png", (0,0), "character/freya_mouth-frown.png")
    image freya impressed = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-happy.png", (0,0), "character/freya_eyes-surprise.png", (0,0), "character/freya_mouth-reprimand.png")
    image freya intimidated = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-sad.png", (0,0), "character/freya_eyes-surprise.png", (0,0), "character/freya_mouth-pleasant.png", (0,0), "character/freya_special-sweatdrop.png")
    image freya irked = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry-low.png", (0,0), "character/freya_eyes-sad-away.png", (0,0), "character/freya_mouth-awe.png")
    image freya irritated = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry-low.png", (0,0), "character/freya_eyes-leer.png", (0,0), "character/freya_mouth-bitelip.png")
    image freya lecture = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry-low.png", (0,0), "character/freya_eyes-leer.png", (0,0), "character/freya_mouth-reprimand.png")
    image freya leer = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-straight-low.png", (0,0), "character/freya_eyes-leer.png", (0,0), "character/freya_mouth-pursed.png")
    image freya love = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-straight-low.png", (0,0), "character/freya_eyes-sad.png", (0,0), "character/freya_mouth-pleasant.png")
    image freya madness = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-happy.png", (0,0), "character/freya_eyes-madness.png", (0,0), "character/freya_mouth-madness.png")
    image freya meditate = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-straight-low.png", (0,0), "character/freya_eyes-dream.png", (0,0), "character/freya_mouth-pursed.png")
    image freya melancholy = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-happy-low.png", (0,0), "character/freya_eyes-deadpan.png", (0,0), "character/freya_mouth-awe.png")
    image freya mock = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-normal-low.png", (0,0), "character/freya_eyes-sad.png", (0,0), "character/freya_mouth-grin.png")
    image freya nag = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry.png", (0,0), "character/freya_eyes-normal.png", (0,0), "character/freya_mouth-wide.png")
    image freya nervous = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-sad-low.png", (0,0), "character/freya_eyes-arches.png", (0,0), "character/freya_mouth-smile.png")
    image freya nervouschuckle = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-sad-low.png", (0,0), "character/freya_eyes-arches.png", (0,0), "character/freya_mouth-grin.png")
    image freya obligated = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry-low.png", (0,0), "character/freya_eyes-sad.png", (0,0), "character/freya_mouth-frown.png")
    image freya omg = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-normal.png", (0,0), "character/freya_eyes-surprise.png", (0,0), "character/freya_mouth-wide.png", (0,0), "character/freya_special-sweatdrop.png")
    image freya perturbed = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-normal-low.png", (0,0), "character/freya_eyes-sad-away.png", (0,0), "character/freya_mouth-pursed.png", (0,0), "character/freya_special-sweatdrop.png")
    image freya pity = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-sad.png", (0,0), "character/freya_eyes-normal.png", (0,0), "character/freya_mouth-awe.png")
    image freya pleasantdream = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-happy-low.png", (0,0), "character/freya_eyes-dream.png", (0,0), "character/freya_mouth-pleasant.png")
    image freya ponder = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-straight-low.png", (0,0), "character/freya_eyes-dream.png", (0,0), "character/freya_mouth-frown.png")
    image freya pout = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry.png", (0,0), "character/freya_eyes-normal.png", (0,0), "character/freya_mouth-bitelip.png")
    image freya psycho = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry.png", (0,0), "character/freya_eyes-madness.png", (0,0), "character/freya_mouth-madness.png")
    image freya reprimand = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry-low.png", (0,0), "character/freya_eyes-angry.png", (0,0), "character/freya_mouth-reprimand.png")
    image freya sad = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-sad-low.png", (0,0), "character/freya_eyes-sad.png", (0,0), "character/freya_mouth-awe.png")
    image freya saddream = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-sad-low.png", (0,0), "character/freya_eyes-dream.png", (0,0), "character/freya_mouth-frown.png")
    image freya sarcastic = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-normal-low.png", (0,0), "character/freya_eyes-sad-away.png", (0,0), "character/freya_mouth-reprimand.png")
    image freya scheme = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry-low.png", (0,0), "character/freya_eyes-angry.png", (0,0), "character/freya_mouth-pleasant.png")
    image freya scold = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry.png", (0,0), "character/freya_eyes-angry.png", (0,0), "character/freya_mouth-gasp.png")
    image freya scowl = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry-low.png", (0,0), "character/freya_eyes-angry.png", (0,0), "character/freya_mouth-normal.png")
    image freya shock = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-happy.png", (0,0), "character/freya_eyes-surprise.png", (0,0), "character/freya_mouth-shout.png")
    image freya shout = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry.png", (0,0), "character/freya_eyes-angry.png", (0,0), "character/freya_mouth-shout.png")
    image freya sigh = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-straight-low.png", (0,0), "character/freya_eyes-dream.png", (0,0), "character/freya_mouth-awe.png")
    image freya sinister = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry-low.png", (0,0), "character/freya_eyes-angry.png", (0,0), "character/freya_mouth-smile.png")
    image freya smile = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-happy-low.png", (0,0), "character/freya_eyes-arches.png", (0,0), "character/freya_mouth-smile.png")
    image freya snicker = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-normal-low.png", (0,0), "character/freya_eyes-sad.png", (0,0), "character/freya_mouth-smile.png")
    image freya snide = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-normal-low.png", (0,0), "character/freya_eyes-leer.png", (0,0), "character/freya_mouth-smile.png")
    image freya stare = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-normal.png", (0,0), "character/freya_eyes-normal.png", (0,0), "character/freya_mouth-pursed.png")
    image freya surprised = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-straight.png", (0,0), "character/freya_eyes-surprise.png", (0,0), "character/freya_mouth-normal.png")
    image freya suspicious = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-normal-low.png", (0,0), "character/freya_eyes-leer.png", (0,0), "character/freya_mouth-awe.png")
    image freya sweetdream = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-happy-low.png", (0,0), "character/freya_eyes-dream.png", (0,0), "character/freya_mouth-smile.png")
    image freya tender = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-happy-low.png", (0,0), "character/freya_eyes-sad.png", (0,0), "character/freya_mouth-smile.png")
    image freya threaten = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry-low.png", (0,0), "character/freya_eyes-leer.png", (0,0), "character/freya_mouth-gasp.png")
    image freya tired = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-sad-low.png", (0,0), "character/freya_eyes-dream.png", (0,0), "character/freya_mouth-awe.png")
    image freya upset = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry.png", (0,0), "character/freya_eyes-normal.png", (0,0), "character/freya_mouth-frown.png")
    image freya weary = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-happy-low.png", (0,0), "character/freya_eyes-sad.png", (0,0), "character/freya_mouth-pursed.png")
    image freya worried = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-sad.png", (0,0), "character/freya_eyes-surprise.png", (0,0), "character/freya_mouth-awe.png")
    image freya yawn = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-happy-low.png", (0,0), "character/freya_eyes-arches.png", (0,0), "character/freya_mouth-reprimand.png")
    image freya yearn = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-happy-low.png", (0,0), "character/freya_eyes-sad.png", (0,0), "character/freya_mouth-normal.png")
    # ad-hoc expressions
    image freya grimace = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry-low.png", (0,0), "character/freya_eyes-leer.png", (0,0), "character/freya_mouth-pursed.png")
    image freya keen = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry.png", (0,0), "character/freya_eyes-normal.png", (0,0), "character/freya_mouth-pleasant.png")
    image freya mocksideways = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-normal-low.png", (0,0), "character/freya_eyes-sad-away.png", (0,0), "character/freya_mouth-grin.png")
    image freya perplexed = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-normal-low.png", (0,0), "character/freya_eyes-sad.png", (0,0), "character/freya_mouth-pursed.png", (0,0), "character/freya_special-sweatdrop.png")
    image freya troubled = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-angry-low.png", (0,0), "character/freya_eyes-sad-away.png", (0,0), "character/freya_mouth-pursed.png")
    image freya uneasy = im.Composite(None, (0,0), "character/freya_body.png", (0,0), "character/freya_eyebrows-normal-low.png", (0,0), "character/freya_eyes-sad-away.png", (0,0), "character/freya_mouth-pursed.png")

    #### reina ####
    image reina angry = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-frown.png", (0,0), "character/reina_eyes-angry.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry-low.png")
    image reina apologize = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-gasp.png", (0,0), "character/reina_eyes-sad.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-sad.png")
    image reina awkward = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-grin.png", (0,0), "character/reina_eyes-nervous.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-sad.png", (0,0), "character/reina_special-blush.png", (0,0), "character/reina_special-sweatdrop.png")
    image reina bashful = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-normal.png", (0,0), "character/reina_eyes-angry-right.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png", (0,0), "character/reina_special-blush.png")
    image reina bliss = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-cute.png", (0,0), "character/reina_eyes-glad.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy.png", (0,0), "character/reina_special-blush.png")
    image reina blush = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_special-red.png", (0,0), "character/reina_mouth-pursed.png", (0,0), "character/reina_eyes-surprise.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-normal.png", (0,0), "character/reina_special-blush.png")
    image reina bored = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pursed.png", (0,0), "character/reina_eyes-bored.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-straight-low.png")
    image reina calm = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-smile.png", (0,0), "character/reina_eyes-normal.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-normal.png")
    image reina chastise = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pout.png", (0,0), "character/reina_eyes-weird.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-wink-left.png")
    image reina chide = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pout.png", (0,0), "character/reina_eyes-bored.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry-low.png")
    image reina complain = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-gasp.png", (0,0), "character/reina_eyes-dream.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry-low.png")
    image reina coo = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-cute.png", (0,0), "character/reina_eyes-arches.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy.png", (0,0), "character/reina_special-blush.png")
    image reina cool = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pleasant.png", (0,0), "character/reina_eyes-angry.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-normal-low.png")
    image reina coolsmile = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-smile.png", (0,0), "character/reina_eyes-angry.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-normal-low.png")
    image reina coolstare = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pursed.png", (0,0), "character/reina_eyes-angry.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-normal-low.png")
    image reina curious = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-normal.png", (0,0), "character/reina_eyes-normal.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-normal.png")
    image reina delight = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-cute.png", (0,0), "character/reina_eyes-mellow.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png", (0,0), "character/reina_special-blush.png")
    image reina depressed = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-frown.png", (0,0), "character/reina_mouth-normal.png", (0,0), "character/reina_eyes-sad-right.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-sad-low.png")
    image reina desire = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pout.png", (0,0), "character/reina_eyes-mellow.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-sad.png", (0,0), "character/reina_special-blush.png")
    image reina dream = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-normal.png", (0,0), "character/reina_eyes-dream.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-normal-low.png")
    image reina drool = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-lecher.png", (0,0), "character/reina_eyes-arches.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png", (0,0), "character/reina_special-blush.png")
    image reina eager = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-lecher.png", (0,0), "character/reina_eyes-surprise.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy.png", (0,0), "character/reina_special-blush.png")
    image reina embarrassed = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-gasp.png", (0,0), "character/reina_eyes-surprise.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry.png", (0,0), "character/reina_special-blush.png", (0,0), "character/reina_special-sweatdrop.png")
    image reina enchanted = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-cute.png", (0,0), "character/reina_eyes-fuzzy.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png", (0,0), "character/reina_special-blush.png")
    image reina evil = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-grin.png", (0,0), "character/reina_eyes-angry.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-normal-low.png")
    image reina excuse = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pleasant.png", (0,0), "character/reina_eyes-nervous.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-sad.png", (0,0), "character/reina_special-sweatdrop.png")
    image reina fantasize = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_special-red.png", (0,0), "character/reina_mouth-lecher.png", (0,0), "character/reina_eyes-fuzzy.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png", (0,0), "character/reina_special-blush.png")
    image reina frown = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-frown.png", (0,0), "character/reina_eyes-normal.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry.png")
    image reina frustrated = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-normal.png", (0,0), "character/reina_eyes-angry-right.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry-low.png")
    image reina fufufu = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-grin.png", (0,0), "character/reina_eyes-bored.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_special-brood.png", (0,0), "character/reina_eyebrows-straight-low.png")
    image reina furious = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-frown.png", (0,0), "character/reina_eyes-surprise.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry.png")
    image reina fuss = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-gasp.png", (0,0), "character/reina_eyes-arches.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-sad-low.png", (0,0), "character/reina_special-sweatdrop.png")
    image reina genki = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-genki.png", (0,0), "character/reina_eyes-arches.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png", (0,0), "character/reina_special-blush.png")
    image reina gulp = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-frown.png", (0,0), "character/reina_eyes-surprise.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy.png", (0,0), "character/reina_special-blush.png")
    image reina happy = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pleasant.png", (0,0), "character/reina_eyes-arches.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png", (0,0), "character/reina_special-blush.png")
    image reina happydream = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-smile.png", (0,0), "character/reina_eyes-dream.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png", (0,0), "character/reina_special-blush.png")
    image reina hentai = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_special-red.png", (0,0), "character/reina_mouth-grin.png", (0,0), "character/reina_eyes-sad-left.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png", (0,0), "character/reina_special-blush.png")
    image reina hopeless = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-frown.png", (0,0), "character/reina_eyes-dream.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-sad-low.png")
    image reina huh = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-gasp.png", (0,0), "character/reina_eyes-weird.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-wink-left.png", (0,0), "character/reina_special-sweatdrop.png")
    image reina impatient = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pursed.png", (0,0), "character/reina_eyes-dream.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry-low.png")
    image reina ippenshindemiru = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pout.png", (0,0), "character/reina_eyes-bored.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_special-brood.png", (0,0), "character/reina_eyebrows-angry-low.png")
    image reina joy = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-smile.png", (0,0), "character/reina_eyes-glad.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy.png", (0,0), "character/reina_special-blush.png")
    image reina kawaii = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-cute.png", (0,0), "character/reina_eyes-sad-crosseye.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png", (0,0), "character/reina_special-blush.png")
    image reina lecherous = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_special-red.png", (0,0), "character/reina_mouth-lecher.png", (0,0), "character/reina_eyes-nervous.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy.png")
    image reina love = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-normal.png", (0,0), "character/reina_eyes-mellow.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png", (0,0), "character/reina_special-blush.png")
    image reina lovestarved = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-frown.png", (0,0), "character/reina_eyes-mellow.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-sad.png", (0,0), "character/reina_special-blush.png")
    image reina lovestruck = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-genki.png", (0,0), "character/reina_eyes-glad.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy.png", (0,0), "character/reina_special-blush.png")
    image reina lust = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pout.png", (0,0), "character/reina_eyes-sad-left.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png", (0,0), "character/reina_special-blush.png")
    image reina mesmerized = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pout.png", (0,0), "character/reina_eyes-surprise.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy.png", (0,0), "character/reina_special-blush.png")
    image reina mock = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-grin.png", (0,0), "character/reina_eyes-bored.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-normal-low.png")
    image reina mope = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-frown.png", (0,0), "character/reina_eyes-sad-right.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry-low.png")
    image reina nag = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-gasp.png", (0,0), "character/reina_eyes-bored.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-sad-low.png")
    image reina naughtydream = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_special-red.png", (0,0), "character/reina_mouth-lecher.png", (0,0), "character/reina_eyes-dream.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png", (0,0), "character/reina_special-blush.png")
    image reina nervous = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-smile.png", (0,0), "character/reina_eyes-nervous.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-sad.png", (0,0), "character/reina_special-sweatdrop.png")
    image reina oggle = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-cute.png", (0,0), "character/reina_eyes-bored.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-straight-low.png", (0,0), "character/reina_special-blush.png")
    image reina oops = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-cute.png", (0,0), "character/reina_eyes-surprise.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy.png", (0,0), "character/reina_special-blush.png", (0,0), "character/reina_special-sweatdrop.png")
    image reina oppose = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pout.png", (0,0), "character/reina_eyes-normal.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry.png")
    image reina overprotect = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-shout.png", (0,0), "character/reina_eyes-glad.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-sad-low.png", (0,0), "character/reina_special-blush.png")
    image reina pained = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-frown.png", (0,0), "character/reina_eyes-arches.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-sad-low.png")
    image reina pout = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pout.png", (0,0), "character/reina_eyes-sad-right.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry-low.png")
    image reina relieved = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pleasant.png", (0,0), "character/reina_eyes-sad.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png")
    image reina reluctant = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pout.png", (0,0), "character/reina_eyes-angry-right.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry-low.png")
    image reina reprimand = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-shout.png", (0,0), "character/reina_eyes-surprise.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry.png")
    image reina sad = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-frown.png", (0,0), "character/reina_eyes-sad.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-sad-low.png")
    image reina sarcastic = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-grin.png", (0,0), "character/reina_eyes-normal.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry.png")
    image reina scold = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-gasp.png", (0,0), "character/reina_eyes-angry.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry-low.png")
    image reina scowl = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-frown.png", (0,0), "character/reina_eyes-weird.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-wink-left.png")
    image reina scream = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-shout.png", (0,0), "character/reina_eyes-surprise.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-normal.png", (0,0), "character/reina_special-sweatdrop.png")
    image reina shock = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pout.png", (0,0), "character/reina_eyes-surprise.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-normal.png")
    image reina shoo = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_special-red.png", (0,0), "character/reina_mouth-shout.png", (0,0), "character/reina_eyes-arches.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-normal.png", (0,0), "character/reina_special-sweatdrop.png")
    image reina shout = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-shout.png", (0,0), "character/reina_eyes-angry.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry-low.png")
    image reina sleepy = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-normal.png", (0,0), "character/reina_eyes-sad.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-normal-low.png")
    image reina smile = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-smile.png", (0,0), "character/reina_eyes-arches.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png", (0,0), "character/reina_special-blush.png")
    image reina smirk = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-smile.png", (0,0), "character/reina_eyes-weird.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-wink-left.png")
    image reina smug = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-smile.png", (0,0), "character/reina_eyes-angry.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry-low.png")
    image reina speechless = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pursed.png", (0,0), "character/reina_eyes-angry-right.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-normal-low.png", (0,0), "character/reina_special-sweatdrop.png")
    image reina stare = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pursed.png", (0,0), "character/reina_eyes-normal.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-normal.png")
    image reina stern = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-frown.png", (0,0), "character/reina_eyes-angry.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-normal-low.png")
    image reina stubborn = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-frown.png", (0,0), "character/reina_eyes-angry-right.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry-low.png")
    image reina suspicious = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pout.png", (0,0), "character/reina_eyes-angry.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry-low.png")
    image reina taunt = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-grin.png", (0,0), "character/reina_eyes-dream.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry-low.png")
    image reina tender = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-smile.png", (0,0), "character/reina_eyes-sad.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png")
    image reina tense = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-grin.png", (0,0), "character/reina_eyes-mellow.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-sad.png", (0,0), "character/reina_special-blush.png")
    image reina thankful = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-smile.png", (0,0), "character/reina_eyes-mellow.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png", (0,0), "character/reina_special-blush.png")
    image reina threaten = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-grin.png", (0,0), "character/reina_eyes-surprise.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry.png")
    image reina tired = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pout.png", (0,0), "character/reina_eyes-sad.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png")
    image reina winkleft = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pleasant.png", (0,0), "character/reina_eyes-wink-left.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-wink-left.png")
    image reina winkright = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pleasant.png", (0,0), "character/reina_eyes-wink-right.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-wink-right.png")
    image reina yawn = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-shout.png", (0,0), "character/reina_eyes-arches.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png")
    image reina yearn = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pout.png", (0,0), "character/reina_eyes-fuzzy.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-sad-low.png", (0,0), "character/reina_special-blush.png")
    # ad-hoc expressions
    image reina silhoutte = "character/reina_silhoutte.png"
    image reina relievedblush = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pleasant.png", (0,0), "character/reina_eyes-sad.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png", (0,0), "character/reina_special-blush.png")
    image reina tenderblush = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-smile.png", (0,0), "character/reina_eyes-sad.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png", (0,0), "character/reina_special-blush.png")
    image reina sinister = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-smile.png", (0,0), "character/reina_eyes-bored.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_special-brood.png", (0,0), "character/reina_eyebrows-straight-low.png")
    image reina kawaiismile = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-smile.png", (0,0), "character/reina_eyes-sad-crosseye.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png", (0,0), "character/reina_special-blush.png")
    image reina bashfulleft = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-normal.png", (0,0), "character/reina_eyes-angry-left.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-happy-low.png", (0,0), "character/reina_special-blush.png")
    image reina nervousblush = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-smile.png", (0,0), "character/reina_eyes-nervous.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-sad.png", (0,0), "character/reina_special-sweatdrop.png", (0,0), "character/reina_special-blush.png")
    image reina shameleft = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_special-red.png", (0,0), "character/reina_mouth-pout.png", (0,0), "character/reina_eyes-angry-left.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry-low.png", (0,0), "character/reina_special-blush.png", (0,0), "character/reina_special-sweatdrop.png")
    image reina shameright = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_special-red.png", (0,0), "character/reina_mouth-pout.png", (0,0), "character/reina_eyes-angry-right.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry-low.png", (0,0), "character/reina_special-blush.png", (0,0), "character/reina_special-sweatdrop.png")
    image reina shameshiftleft = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_special-red.png", (0,0), "character/reina_mouth-pursed.png", (0,0), "character/reina_eyes-angry-left.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry-low.png", (0,0), "character/reina_special-blush.png")
    image reina furiousblush = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-frown.png", (0,0), "character/reina_eyes-surprise.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry.png", (0,0), "character/reina_special-blush.png",)
    image reina leer = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_mouth-pursed.png", (0,0), "character/reina_eyes-bored.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-angry-low.png")
    image reina shoofrown = im.Composite(None, (0,0), "character/reina_body.png", (0,0), "character/reina_special-red.png", (0,0), "character/reina_mouth-frown.png", (0,0), "character/reina_eyes-arches.png", (0,0), "character/reina_special-hair.png", (0,0), "character/reina_eyebrows-normal.png", (0,0), "character/reina_special-sweatdrop.png")

    #### queen ####
    image queen talk = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-normal.png", (0,0), "character/queen_eyes-normal.png", (0,0), "character/queen_eyebrows-normal.png")
    image queen calm = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-pursed.png", (0,0), "character/queen_eyes-normal.png", (0,0), "character/queen_eyebrows-normal.png")
    image queen frown = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-frown.png", (0,0), "character/queen_eyes-normal.png", (0,0), "character/queen_eyebrows-angry.png")
    image queen lecture = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-normal.png", (0,0), "character/queen_eyes-normal.png", (0,0), "character/queen_eyebrows-angry.png")
    image queen annoyed = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-frown.png", (0,0), "character/queen_eyes-dream.png", (0,0), "character/queen_eyebrows-angry-low.png")
    image queen rebuke = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-frown.png", (0,0), "character/queen_eyes-dream.png", (0,0), "character/queen_eyebrows-angry-low.png")
    image queen meditate = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-pursed.png", (0,0), "character/queen_eyes-dream.png", (0,0), "character/queen_eyebrows-normal-low.png")
    image queen mumble = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-normal.png", (0,0), "character/queen_eyes-dream.png", (0,0), "character/queen_eyebrows-normal-low.png")
    image queen stare = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-pursed.png", (0,0), "character/queen_eyes-bored.png", (0,0), "character/queen_eyebrows-straight-low.png")
    image queen stareleft = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-pursed.png", (0,0), "character/queen_eyes-bored-left.png", (0,0), "character/queen_eyebrows-straight-low.png")
    image queen stareright = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-pursed.png", (0,0), "character/queen_eyes-bored-right.png", (0,0), "character/queen_eyebrows-straight-low.png")
    image queen comment = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-normal.png", (0,0), "character/queen_eyes-bored.png", (0,0), "character/queen_eyebrows-straight-low.png")
    image queen commentleft = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-normal.png", (0,0), "character/queen_eyes-bored-left.png", (0,0), "character/queen_eyebrows-straight-low.png")
    image queen commentright = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-normal.png", (0,0), "character/queen_eyes-bored-right.png", (0,0), "character/queen_eyebrows-straight-low.png")
    image queen bored = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-frown.png", (0,0), "character/queen_eyes-bored.png", (0,0), "character/queen_eyebrows-angry-low.png")
    image queen boredleft = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-frown.png", (0,0), "character/queen_eyes-bored-left.png", (0,0), "character/queen_eyebrows-angry-low.png")
    image queen boredright = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-frown.png", (0,0), "character/queen_eyes-bored-right.png", (0,0), "character/queen_eyebrows-angry-low.png")
    image queen chide = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-normal.png", (0,0), "character/queen_eyes-bored.png", (0,0), "character/queen_eyebrows-angry-low.png")
    image queen chideleft = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-normal.png", (0,0), "character/queen_eyes-bored-left.png", (0,0), "character/queen_eyebrows-angry-low.png")
    image queen chideright = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-normal.png", (0,0), "character/queen_eyes-bored-right.png", (0,0), "character/queen_eyebrows-angry-low.png")
    # with haku
    image queen hakutalk = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-normal.png", (0,0), "character/queen_eyes-normal.png", (0,0), "character/queen_eyebrows-normal.png", (0,0), "character/queen_special-haku.png")
    image queen hakucalm = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-pursed.png", (0,0), "character/queen_eyes-normal.png", (0,0), "character/queen_eyebrows-normal.png", (0,0), "character/queen_special-haku.png")
    image queen hakufrown = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-frown.png", (0,0), "character/queen_eyes-normal.png", (0,0), "character/queen_eyebrows-angry.png", (0,0), "character/queen_special-haku.png")
    image queen hakulecture = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-normal.png", (0,0), "character/queen_eyes-normal.png", (0,0), "character/queen_eyebrows-angry.png", (0,0), "character/queen_special-haku.png")
    image queen hakuannoyed = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-frown.png", (0,0), "character/queen_eyes-dream.png", (0,0), "character/queen_eyebrows-angry-low.png", (0,0), "character/queen_special-haku.png")
    image queen hakurebuke = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-frown.png", (0,0), "character/queen_eyes-dream.png", (0,0), "character/queen_eyebrows-angry-low.png", (0,0), "character/queen_special-haku.png")
    image queen hakumeditate = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-pursed.png", (0,0), "character/queen_eyes-dream.png", (0,0), "character/queen_eyebrows-normal-low.png", (0,0), "character/queen_special-haku.png")
    image queen hakumumble = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-normal.png", (0,0), "character/queen_eyes-dream.png", (0,0), "character/queen_eyebrows-normal-low.png", (0,0), "character/queen_special-haku.png")
    image queen hakustare = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-pursed.png", (0,0), "character/queen_eyes-bored.png", (0,0), "character/queen_eyebrows-straight-low.png", (0,0), "character/queen_special-haku.png")
    image queen hakustareleft = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-pursed.png", (0,0), "character/queen_eyes-bored-left.png", (0,0), "character/queen_eyebrows-straight-low.png", (0,0), "character/queen_special-haku.png")
    image queen hakustareright = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-pursed.png", (0,0), "character/queen_eyes-bored-right.png", (0,0), "character/queen_eyebrows-straight-low.png", (0,0), "character/queen_special-haku.png")
    image queen hakucomment = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-normal.png", (0,0), "character/queen_eyes-bored.png", (0,0), "character/queen_eyebrows-straight-low.png", (0,0), "character/queen_special-haku.png")
    image queen hakucommentleft = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-normal.png", (0,0), "character/queen_eyes-bored-left.png", (0,0), "character/queen_eyebrows-straight-low.png", (0,0), "character/queen_special-haku.png")
    image queen hakucommentright = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-normal.png", (0,0), "character/queen_eyes-bored-right.png", (0,0), "character/queen_eyebrows-straight-low.png", (0,0), "character/queen_special-haku.png")
    image queen hakubored = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-frown.png", (0,0), "character/queen_eyes-bored.png", (0,0), "character/queen_eyebrows-angry-low.png", (0,0), "character/queen_special-haku.png")
    image queen hakuboredleft = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-frown.png", (0,0), "character/queen_eyes-bored-left.png", (0,0), "character/queen_eyebrows-angry-low.png", (0,0), "character/queen_special-haku.png")
    image queen hakuboredright = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-frown.png", (0,0), "character/queen_eyes-bored-right.png", (0,0), "character/queen_eyebrows-angry-low.png", (0,0), "character/queen_special-haku.png")
    image queen hakuchide = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-normal.png", (0,0), "character/queen_eyes-bored.png", (0,0), "character/queen_eyebrows-angry-low.png", (0,0), "character/queen_special-haku.png")
    image queen hakuchideleft = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-normal.png", (0,0), "character/queen_eyes-bored-left.png", (0,0), "character/queen_eyebrows-angry-low.png", (0,0), "character/queen_special-haku.png")
    image queen hakuchideright = im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-normal.png", (0,0), "character/queen_eyes-bored-right.png", (0,0), "character/queen_eyebrows-angry-low.png", (0,0), "character/queen_special-haku.png")

    #### Other Character Art ###
    image crowd calm = "character/crowd_body.png"
    image crowd nervous = im.Composite(None, (0,0), "character/crowd_body.png", (0,0), "character/crowd_disgust.png")
    image crowd shout = im.Composite(None, (0,0), "character/crowd_body.png", (0,0), "character/crowd_shout.png")
    image crowd angry = im.Composite(None, (0,0), "character/crowd_body.png", (0,0), "character/crowd_angrytwitch.png")


    #### Image Art ###
    image ambient darken = "images/ambient_darken.png"
    image ambient darkenhole = "images/ambient_darkenhole.png"
    image ambient fire = "images/ambient_fire.png"
    image ambient fire = "images/ambient_fire.png"
    image ambient haunted = "images/ambient_haunted.jpg"
    image ambient heaven = "images/ambient_heaven.jpg"
    image ambient icy = "images/ambient_icy.png"
    image ambient reinaglare = "images/ambient_reinaglare.png"
    image ambient zen = "images/ambient_zen.jpg"
    image overlay garbage = "images/ambient_garbage.jpg"
    image overlay hospital = "images/ambient_hospital.jpg"
    image overlay netbook = "images/overlay_netbook.png"
    image overlay kanabed1 = "images/overlay_kanabed1.png"
    image overlay kanabed2 = "images/overlay_kanabed2.png"
    image bihun1 = "images/prop_bihundouble.png"
    image bihun2 = "images/prop_bihundouble.png"
    image bihun3 = "images/prop_bihundouble.png"
    image bihun4 = "images/prop_bihundouble.png"
    image bihun5 = "images/prop_bihundouble.png"
    image prop blackforest1 = "images/prop_blackforest.png"
    image prop blackforest2 = "images/prop_badblackforest.png"
    image prop bookworm = "images/prop_bookworm.png"
    image prop bookworm = "images/prop_bookworm.png"
    image prop chair = "images/prop_chair.png"
    image prop foodbubble1 = "images/prop_foodbubble1.png"
    image prop foodbubble2 = "images/prop_foodbubble2.png"
    image prop foodbubble3 = "images/prop_foodbubble3.png"
    image prop foodbubble4 = "images/prop_foodbubble4.png"
    image prop foodbubble5 = "images/prop_foodbubble5.png"
    image prop hairbrush = "images/prop_hairbrush.png"
    image prop haku = "images/prop_haku.png"
    image prop nasgor = "images/prop_nasgor.png"
    image prop nasgormini = "images/prop_nasgormini.png"
    image prop netbook = "images/prop_netbook.png"
    image prop sparkle = "images/prop_sparkle.png"
    image prop spotlight = "images/prop_spotlight.png"
    image prop unr1 = "images/prop_unr1.jpg"
    image prop unr2 = "images/prop_unr2.jpg"
    image prop unr3 = "images/prop_unr3.jpg"
    image prop unr4 = "images/prop_unr4.jpg"
    image prop unr5 = "images/prop_unr5.jpg"
    image prop unr6 = "images/prop_unr6.jpg"

    $ m  = Character('Miharu', color="#FDD457", ctc="ctc_arrow", ctc_position="fixed")
    $ ta = Character('Ms. Aizawa', color="#FF91C3", ctc="ctc_arrow", ctc_position="fixed")
    $ f  = Character('Freya', color="#A2FEFE", ctc="ctc_arrow", ctc_position="fixed")
    $ r  = Character('Reina', color="#CAE570", ctc="ctc_arrow", ctc_position="fixed")
    $ q  = Character('Q.U.E.E.N', color="#C362E6", ctc="ctc_arrow", ctc_position="fixed")
    $ cy = Character('Cyllia', color="#55FF00", ctc="ctc_arrow", ctc_position="fixed")

    #### NARRATOR-LIKE ####
    $ nar = Character(' ', what_style = "narrated", what_prefix = "(", what_suffix = ")", ctc="ctc_arrow", ctc_position="fixed")
    $ net = NVLCharacter(None, kind=nvl, what_style = "emailed", ctc="ctc_arrow", ctc_position="fixed")
    $ netcyl = NVLCharacter(None, kind=nvl, what_style = "emailedcyllia", ctc="ctc_arrow", ctc_position="fixed")

    $ outline = Character(None, what_size=28,
                          #window_xalign=0.0, window_yalign=1.0,
                          what_prefix="\n",
                          window_background="gameui/bg_blend.png",
                          what_outlines=[(1, "#000000", 0, 0), (2, "#2B2B2B", 0, 0)],
                          what_slow_cps=70
                          )

    #### DYNAMIC CHARACTER NAMES ####
    $ c = DynamicCharacter('classroom', color="#FFCC94", ctc="ctc_arrow", ctc_position="fixed")
    $ t = DynamicCharacter('teacher', color="#CDDEFF", ctc="ctc_arrow", ctc_position="fixed")
    $ u = DynamicCharacter('unknown', color="#FFBABB", ctc="ctc_arrow", ctc_position="fixed")

    # Declare all music here.
    $ music_aizawa1 = "music/Alexandr_Filippov-Friday-1-slow.ogg"
    $ music_aizawa2 = "music/Alexandr_Filippov-Friday-2-slow.ogg"
    $ music_aizawa3 = "music/Alexandr_Filippov-Friday-2.ogg"
    $ music_aizawa4 = "music/Alexandr_Filippov-Friday-3.ogg"
    $ music_aizawa5 = "music/Alexandr_Filippov-Friday-4.ogg"
    $ music_angelic = "music/Handel_44-Hallelujah.ogg"
    $ music_bombshelter1 = "music/Hemiola-Foxtrot-1.ogg"
    $ music_bombshelter2 = "music/Hemiola-Foxtrot-2.ogg"
    $ music_bombshelter3 = "music/Hemiola-Foxtrot-3.ogg"
    $ music_bombshelter4 = "music/Hemiola-Foxtrot-4.ogg"
    $ music_calm1 = "music/Quietness47_-_Yogoreta.ogg"
    $ music_crazyfight1 = "music/Olga_Scotland-KleinJiga1.ogg"
    $ music_crazyfight2 = "music/Olga_Scotland-KleinJiga2.ogg"
    $ music_crazyfight3 = "music/Olga_Scotland-KleinJiga3.ogg"
    $ music_ED1a = "music/Jamie_Rumley_-_Thank-You1.ogg"
    $ music_ED1b = "music/Jamie_Rumley_-_Thank-You2.ogg"
    $ music_freyajingle = "music/St_Adam-Together-jingle.ogg"
    $ music_haku = "music/Ehma_-_L-arrivee.ogg"
    $ music_konobangumiwa1 = "video/konobangumiwa_snippet.ogg"
    $ music_konobangumiwa2 = "video/konobangumiwa_snippet2.ogg"
    $ music_miharu1 = "music/Dale_Rucklos-For_The_First_Time-1.ogg"
    $ music_miharu2 = "music/Dale_Rucklos-For_The_First_Time-2.ogg"
    $ music_miharu3 = "music/Dale_Rucklos-For_The_First_Time-3.ogg"
    $ music_miharujingle = "music/Dale_Rucklos-For_The_First_Time-jingle.ogg"
    $ music_mellow = "music/Lena_Selyanina-Un_petit_poeme.ogg"
    $ music_netbook1 = "music/click_-_After_Winter_Dreams-1.ogg"
    $ music_netbook2 = "music/click_-_After_Winter_Dreams-2.ogg"
    $ music_OP = "music/Autorotation_-_Coils.ogg"
    $ music_pompous1 = "music/Beethoven_9-IV_1.ogg"
    $ music_pompous2 = "music/Beethoven_9-IV_2.ogg"
    $ music_queen1 = "music/Hemiola_-_Street-Organ.ogg"
    $ music_quirky = "music/Renich - To be happy.ogg"
    $ music_reina1 = "music/Hemiola_-_Reversive1.ogg"
    $ music_reina2 = "music/Hemiola_-_Reversive2.ogg"
    $ music_reinajingle = "music/Hemiola_-_Reversive-jingle.ogg"
    $ music_ridiculous = "music/Olga_Scotland-KoshkaGarmoshka.ogg"
    $ music_roughday = "music/Olga_Scotland-Unikum.ogg"
    $ music_royalty = "music/Olga_Scotland-Medieval-Adventure-Game.ogg"
    $ music_flashback1 = "music/Olga_Scotland-KissingGarden.ogg"
    $ music_silence = "music/silence.ogg"
    $ music_yuri1 = "music/Don_Ward-Missing_You_Now.ogg"

    # Declare all sounds here.
    $ sound_airraidsiren = "sound/airraidsiren.ogg"
    $ sound_birdsongs = "sound/birdsongs.ogg"
    $ sound_catfight = "sound/catfight.ogg"
    $ sound_bells = "sound/bells.ogg"
    $ sound_chatter = "sound/chatter.ogg"
    $ sound_collide = "sound/punch.ogg"
    $ sound_doorslam = "sound/doorslam.ogg"
    $ sound_drumroll = "sound/drumroll.ogg"
    $ sound_drumtada = "sound/drumtada.ogg"
    $ sound_deadsilence = "sound/cricket.ogg"
    $ sound_embarrass = "sound/wauwau.ogg"
    $ sound_gong = "sound/gong.ogg"
    $ sound_lightswitch = "sound/lightswitch.ogg"
    $ sound_mouseclicks = "sound/mouseclicks.ogg"
    $ sound_poison = "sound/poison.ogg"
    $ sound_schoolchime = "sound/schoolchime.ogg"
    $ sound_silence = "sound/silence.ogg"
    $ sound_spotlight = "sound/spotlight.ogg"
    $ sound_stomachgrowl = "sound/stomachgrowl.ogg"
    $ sound_thunder = "sound/thunder.ogg"
    $ sound_thunderstep = "sound/thunderstep.ogg"
    $ sound_typing = "sound/typing.ogg"
    $ sound_war = "sound/war.ogg"
    $ sound_wind = "sound/wind.ogg"
    $ sound_woosh = "sound/woosh.ogg"

    # Special Effects here.

    # Special fade for start of the game
    $ introfade = Fade(3.0, 0, 5.0)
    $ videofade_in = Fade(3.5, 1.5, 0, color="#FFFFFF")
    $ videofade_out = Fade(0, 0, 1.5)
    $ flashbackfade = Fade(1.5, 0, 1.5, color="#FFFFFF")
    $ slowdissolve = Dissolve(2.0)
    $ quickdissolve = Dissolve(0.2)
    $ nodissolve = Dissolve(0.0)
    $ renpy.music.register_channel("countermusic", "music", True)

    # All Video ATL Animations here.
    # mini OP is 6 seconds total
    image miniOP_1:
        "video/OP-placeholder_whitephase.png"
        xpos -0.20 xanchor 0.0 yalign 0.0
        ease 3.0 xpos 1.0

    image miniOP_2:
        "video/OP-placeholder_logo1.png"
        xalign 0.0 yalign 0.0
        time 6.0
        ease 1.0 alpha 0.0

    image miniOP_3:
        "video/OP-placeholder_logo2.png"
        alpha 0.0 xalign 0.0 yalign 0.0
        time 3.0
        ease 1.0 alpha 1.0
        time 6.0
        ease 1.0 alpha 0.0

    # full OP sequence

    # Declare reoccuring graphics files here.
    $ OP_black = "video/OP_bgcolor-black.png"
    $ OP_white = "video/OP_bgcolor-white.png"
    $ OP_spectrum_static01 = "video/OP_spectrum_static01.png"
    $ OP_spectrum_static02 = "video/OP_spectrum_static02.png"
    $ OP_spectrum_static03 = "video/OP_spectrum_static03.png"
    $ OP_spectrum_static04 = "video/OP_spectrum_static04.png"
    $ OP_spectrum_dong01 = "video/OP_spectrum_static01.png"
    $ OP_spectrum_dong02 = "video/OP_spectrum_dong02.png"
    $ OP_spectrum_tock01 = "video/OP_spectrum_tock01.png"
    $ OP_spectrum_tock02 = "video/OP_spectrum_tock02.png"
    $ OP_spectrumstatic = Animation(OP_spectrum_static01, 0.05, OP_spectrum_static02, 0.05, OP_spectrum_static03, 0.05, OP_spectrum_static04, 0.05, im.Flip(OP_spectrum_static01, vertical=True), 0.05, im.Flip(OP_spectrum_static02, vertical=True), 0.05, im.Flip(OP_spectrum_static03, vertical=True), 0.05, im.Flip(OP_spectrum_static04, vertical=True), 0.05, im.Flip(OP_spectrum_static01, horizontal=True), 0.05, im.Flip(OP_spectrum_static02, horizontal=True), 0.05, im.Flip(OP_spectrum_static03, horizontal=True), 0.05, im.Flip(OP_spectrum_static04, horizontal=True), 0.05, im.Flip(OP_spectrum_static01, horizontal=True, vertical=True), 0.05, im.Flip(OP_spectrum_static02, horizontal=True, vertical=True), 0.05, im.Flip(OP_spectrum_static03, horizontal=True, vertical=True), 0.05, im.Flip(OP_spectrum_static04, horizontal=True, vertical=True), 0.05)
    $ OP_filmgrain1 = "video/OP_filmgrain1.png"
    $ OP_filmgrain = Animation(OP_filmgrain1, 0.1, im.Flip(OP_filmgrain1, vertical=True), 0.1, im.Flip(OP_filmgrain1, horizontal=True), 0.1, im.Flip(OP_filmgrain1, horizontal=True, vertical=True), 0.1, im.Flip(OP_filmgrain1, vertical=True), 0.1, OP_filmgrain1, 0.1, im.Flip(OP_filmgrain1, horizontal=True, vertical=True), 0.1, im.Flip(OP_filmgrain1, horizontal=True), 0.1)
    $ OP_interlace = Animation(im.Tile("video/OP_interlace01.png", size=(800,600)), 0.025, im.Tile("video/OP_interlace02.png", size=(800,600)), 0.025, im.Tile("video/OP_interlace03.png", size=(800,600)), 0.025)
    $ OP_circle = "video/OP_circle.png"
    $ OP_light = "video/OP_light2.png"
    $ OP_ripple1 = "video/OP_ripple01.png"
    $ OP_ripple2 = "video/OP_ripple02.png"
    $ OP_cylliapigtails = LiveComposite((800, 600), (0, 0), Animation("video/OP_CyC-Pigtails01.png", 0.07, "video/OP_CyC-Pigtails02.png", 0.07, "video/OP_CyC-Pigtails03.png", 0.07, "video/OP_CyC-Pigtails04.png", 0.07, "video/OP_CyC-Pigtails05.png", 0.07, "video/OP_CyC-Pigtails06.png", 0.07, "video/OP_CyC-Pigtails07.png", 0.07, "video/OP_CyC-Pigtails08.png", 0.07, "video/OP_CyC-Pigtails01.png", 0.07, "video/OP_CyC-Pigtails02.png", 0.07, "video/OP_CyC-Pigtails03.png", 0.07, "video/OP_CyC-Pigtails04.png", 0.07, "video/OP_CyC-Pigtails05.png", 0.07, "video/OP_CyC-Pigtails06.png", 0.07, "video/OP_CyC-Pigtails07.png", 0.07, "video/OP_CyC-Pigtails08.png", 0.07), (0, 0), "video/OP_CyC-Body01.png")
    $ OP_cylliapretear = Animation("video/OP_CyE-Tears03.png", 0.07, "video/OP_CyE-Tears04.png", 0.07, "video/OP_CyE-Tears05.png", 0.07, "video/OP_CyE-Tears03.png", 0.07, "video/OP_CyE-Tears05.png", 0.07, "video/OP_CyE-Tears04.png", 0.07)
    $ OP_cylliasparkle = Animation("video/OP_CyE-Sparkle01.png", 0.05, "video/OP_CyE-Sparkle02.png", 0.05, "video/OP_CyE-Sparkle03.png", 0.05, "video/OP_CyE-Sparkle01.png", 0.05, "video/OP_CyE-Sparkle03.png", 0.05, "video/OP_CyE-Sparkle02.png", 0.05)
    $ OP_teardrop = Animation("video/OP_CyE-Teardrop01.png", 0.1, "video/OP_CyE-Teardrop02.png", 0.1, "video/OP_CyE-Teardrop03.png", 0.1, "video/OP_CyE-Teardrop01.png", 0.1, "video/OP_CyE-Teardrop03.png", 0.1, "video/OP_CyE-Teardrop02.png", 0.1)
    $ OP_teardrop2 = Animation("video/OP_rippleteardrop01.png", 0.1, "video/OP_rippleteardrop02.png", 0.1, "video/OP_rippleteardrop03.png", 0.1, "video/OP_rippleteardrop01.png", 0.1, "video/OP_rippleteardrop03.png", 0.1, "video/OP_rippleteardrop02.png", 0.1)
    $ OP_droplets1 = "video/OP_raincity-droplets1.png"
    $ OP_droplets2 = "video/OP_raincity-droplets2.png"
    $ OP_droplets3 = "video/OP_raincity-droplets3.png"
    $ OP_droplets = Animation(OP_droplets1, 0.05, OP_droplets2, 0.05, OP_droplets3, 0.05, im.Flip(OP_droplets1, horizontal=True), 0.05, OP_droplets2, 0.05, im.Flip(OP_droplets2, horizontal=True), 0.05, im.Flip(OP_droplets3, horizontal=True), 0.05, OP_droplets3, 0.05, im.Flip(OP_droplets1, horizontal=True), 0.05, im.Flip(OP_droplets2, horizontal=True), 0.05, OP_droplets2, 0.05)
    $ OP_droplets21 = "video/OP_rainkana-droplets1.png"
    $ OP_droplets22 = "video/OP_rainkana-droplets2.png"
    $ OP_droplets23 = "video/OP_rainkana-droplets3.png"
    $ OP_droplets2 = Animation(OP_droplets21, 0.03, OP_droplets22, 0.05, OP_droplets21, 0.02, OP_droplets22, 0.04, OP_droplets21, 0.01, OP_droplets22, 0.06, OP_droplets21, 0.02, OP_droplets22, 0.05, OP_droplets21, 0.04, OP_droplets22, 0.02)
    $ OP_quickmontage = Animation("video/OP_quickmontage01.jpg", 0.1, "video/OP_quickmontage02.jpg", 0.1, "video/OP_quickmontage03.jpg", 0.1, "video/OP_quickmontage04.jpg", 0.1, "video/OP_quickmontage05.jpg", 0.1, "video/OP_quickmontage06.jpg", 0.1, "video/OP_quickmontage07.jpg", 0.1, "video/OP_quickmontage08.jpg", 0.1, "video/OP_quickmontage09.jpg", 0.1)

    image newOP_1:
        subpixel True
        #Begin Cyllia Twirl Sequence
        OP_black
        alpha 0.0
        time 3.0
        "video/OP_bgmotionA01.jpg"
        alpha 0.15
        time 4.0
        "video/OP_bgmotionA05.jpg" with Dissolve(0.25)
        alpha 0.3
        time 5.0
        "video/OP_bgmotionA10.jpg" with Dissolve(0.25)
        alpha 0.45
        #End Cyllia Twirl Sequence

        #Begin Sad Image Montage
        time 5.5
        "video/OP_bg2.jpg"
        alpha 0.85
        time 6.0
        linear 0.5 alpha 0.0
        time 6.5
        "video/OP_bg3.jpg"
        alpha 0.9
        time 7.0
        linear 0.6 alpha 0.0
        time 7.6
        "video/OP_bg4.jpg"
        alpha 0.95
        time 8.1
        linear 0.6 alpha 0.0
        time 8.7
        "video/OP_bg5.jpg"
        alpha 1.0
        time 11.0
        OP_white
        #End Sad Image Montage

        #Begin Title Sequence
        time 11.25
        "video/OP_title1.png" with Dissolve (3.25)
        time 14.75
        "video/OP_title2.png" with Dissolve (0.5)
        time 16.5
        "video/OP_title3.png" with Dissolve (1.0)
        #End Title Sequence

        #Begin Cyllia Pose Sequence
        time 20.0
        alpha 0.4
        "video/OP_bgmotionB01.jpg"
        time 20.5
        "video/OP_bgmotionB05.jpg" with Dissolve(0.25)
        time 21.5
        "video/OP_bgmotionB09.jpg" with Dissolve(0.25)
        time 22.5
        "video/OP_bgmotionC02.jpg" with Dissolve(0.25)
        time 23.5
        "video/OP_bgmotionC05.jpg" with Dissolve(0.25)
        time 24.5
        "video/OP_bgmotionC07.jpg" with Dissolve(0.25)
        #End Cyllia Pose Sequence

        #Begin Cyllia Tear Sequence
        time 25.0
        OP_white
        alpha 1.0
        time 26.25
        "video/OP_bgcolor-green.png"
        time 27.5
        OP_black
        #End Cyllia Tear Sequence

        #Begin Character Intro Sequence
        time 30.0
        "video/OP_charbackgroundA3.png"
        xpos 1.0 xanchor 0.0 ypos 0.5 yanchor 0.5 alpha 0.5 rotate None
        linear 0.6 xpos 0.0 alpha 1.0
        time 35.0
        "video/OP_charbackgroundB3.png"
        xalign 0.5 ypos 1.0 yanchor 0.5 alpha 0.5 rotate None
        linear 1.0 rotate 180.0 alpha 1.0
        time 40.0
        "video/OP_charbackgroundC4.png"
        xpos 0.0 xanchor 0.5 yalign 0.0 alpha 0.5 rotate None
        linear 0.6 xanchor 0.0 alpha 1.0
        time 41.0
        "video/OP_charbackgroundC6.png"
        time 45.0
        "video/OP_characterFreyaBlack.png"
        xpos -0.5 xanchor 0.5 yalign 1.0 zoom 1.0 alpha 1.0 rotate None
        linear 0.25 xpos 0.45
        linear 1.75 xpos 0.5
        linear 0.25 xpos 1.5
        time 47.75
        "video/OP_characterAizawaBlack.png"
        xpos 1.5 xanchor 0.5 yalign 1.0 zoom 1.0
        linear 0.25 xpos 0.55
        linear 1.75 xpos 0.5
        #End Character Intro Sequence

        #Begin Kana Rain Sequence
        time 49.75
        OP_teardrop2
        zoom 10.0 alpha 1.0 xalign 0.5 yalign 0.5 alpha 1.0  rotate None
        linear 0.35 zoom 0.1
        time 50.1
        alpha 0.0
        time 50.6
        OP_ripple1
        zoom 0.1 alpha 1.0 xalign 0.5 yalign 0.5
        easeout 1.5 zoom 2.0 alpha 0.0
        time 52.25
        "video/OP_raincity.jpg"
        xalign 0.0 yalign 0.0 alpha 0.0 zoom 1.0 rotate None
        linear 1.0 alpha 1.0
        time 54.25
        "video/OP_rainkana.jpg"
        time 56.25
        "video/OP_raindescent.png"
        time 57.25
        linear 0.75 yalign 1.0
        #End Kana Rain Sequence

        #Begin Miharu Water Sequence
        time 58
        OP_teardrop2
        zoom 10.0 xalign 0.5 yalign 0.5 alpha 1.0
        linear 0.5 zoom 0.1
        time 58.5
        OP_ripple2
        zoom 0.1 alpha 1.0 xalign 0.5 yalign 0.5
        easeout 1.5 zoom 2.0 alpha 0.0
        time 60
        "video/OP_miharuwater1.jpg"
        xalign 0.5 ypos 0.5 yanchor 0.3 zoom 1.0 alpha 0.0
        parallel:
            linear 4.0 alpha 0.8 yanchor 0.4 zoom 1.3
        parallel:
            linear 3.0 alpha 1.0
        time 64
        "video/OP_rainascent.png"
        xalign 0.0 yalign 1.0 alpha 1.0 zoom 1.0
        time 65.25
        linear 3.0 yalign 0.0
        #End Miharu Water Sequence

        #Begin Beach Sequence
        time 70.25
        "video/OP_beachreina.jpg"
        xalign 1.0 yalign 0.0 zoom 2.0
        linear 3.0 zoom 1.0
        time 75.25
        "video/OP_beachkanamiharu.jpg"
        xalign 0.5 yalign 0.0 zoom 2.0 rotate None
        linear 3.0 yalign 0.4 zoom 1.0
        time 78.75
        "video/OP_beachkanamiharu.jpg"
        crop (450,60,225,175) size (800, 600)
        xalign 0.8 yalign 0.2 zoom 1.0 rotate None
        linear 1.5 crop (400,60,225,175) size (800, 600)
        #End Beach Sequence

        #Begin Garden Sequence
        time 81
        "video/OP_garden1.jpg"
        alpha 1.0 xalign 1.0 yalign 0.0 zoom 1.0 crop None size None
        linear 5.5 xalign 0.0
        time 86.25
        "video/OP_gardencylliabg.jpg"
        alpha 1.0
        #End Garden Sequence
        subpixel False

    image newOP_2:
        subpixel True
        #Begin Cyllia Twirl Sequence
        "video/OP_spectrum_line.png"
        ypos 0.5 xpos 1.0 xanchor 0.0
        time 0.10
        linear 0.20 xpos -0.05
        time 0.5
        xalign 0.0 yalign 0.0
        OP_spectrum_dong02
        time 0.55
        OP_spectrumstatic
        time 0.6
        OP_spectrum_dong02
        time 0.68
        OP_spectrumstatic
        time 0.73
        OP_spectrum_dong01
        time 0.78
        OP_spectrumstatic
        time 1.38
        OP_spectrum_dong02
        time 1.48
        OP_spectrumstatic
        time 1.68
        OP_spectrum_tock01
        time 1.78
        OP_spectrumstatic
        time 2.48
        OP_spectrum_tock02
        time 2.53
        OP_spectrumstatic
        time 2.63
        OP_spectrum_tock01
        time 2.68
        OP_spectrumstatic
        time 2.78
        OP_spectrum_tock02
        time 2.83
        OP_spectrum_dong02
        time 2.88
        OP_spectrumstatic
        time 2.93
        OP_spectrum_dong02
        time 3.01
        OP_spectrumstatic
        time 3.06
        OP_spectrum_dong01
        time 3.11
        OP_spectrumstatic
        time 3.71
        OP_spectrum_dong02
        time 3.81
        OP_spectrumstatic
        time 4.01
        OP_spectrum_tock01
        time 4.11
        OP_spectrumstatic
        time 4.81
        OP_spectrum_tock02
        time 4.86
        OP_spectrumstatic
        time 4.96
        OP_spectrum_tock01
        time 5.01
        OP_spectrumstatic
        time 5.11
        OP_spectrum_tock02
        time 5.16
        OP_spectrum_dong02,
        time 5.21
        OP_spectrumstatic
        time 5.26
        OP_spectrum_dong02
        time 5.34
        OP_spectrumstatic
        time 5.39
        OP_spectrum_dong01
        time 5.44
        OP_spectrumstatic
        time 5.5
        OP_black
        alpha 0.0
        #End Cyllia Twirl Sequence

        #Begin Sad Image Montage
        time 5.5
        OP_interlace
        alpha 0.6
        time 9.5
        linear 1.0 alpha 0.0
        time 10.5
        OP_black
        #End Sad Image Montage

        #Begin Title Sequence
        time 18.50
        OP_circle
        xpos 0.75 ypos 0.25 xanchor 0.5 yanchor 0.5 alpha 1.0 zoom 0.05
        linear 1.50 zoom 4.0
        #End Title Sequence

        #Begin Cyllia Pose Sequence
        time 20.0
        Text(renpy.file("video/OPTXT_websites.txt").read(), style="emailed")
        xpos -0.1 xanchor 0.0 yalign 0.0 zoom 1.4 alpha 0.0
        linear 15.0 yalign 1.0 alpha 0.3
        #End Cyllia Pose Sequence

        #Begin Cyllia Tear Sequence
        time 25.0
        "video/OP_emailA1.png"
        xpos 1.0 xanchor 1.0 yalign 0.5 alpha 1.0 zoom 1.0 rotate 0.0
        linear 1.25 xanchor 0.75
        time 26.25
        "video/OP_emailB2.png"
        xpos 1.0 xanchor 1.0 yalign 0.5 alpha 0.4 zoom 1.0 rotate 0.0
        linear 2.5 xanchor 0.25
        time 27.5
        "video/OP_emailC1.png"
        xpos 1.0 xanchor 1.0 yalign 0.5 alpha 0.3 zoom 1.0 rotate 0.0
        linear 2.5 xanchor 0.25
        #End Cyllia Tear Sequence

        #Begin Character Intro Sequence
        time 30.0
        "video/OP_characterKana.png"
        xalign 1.0 ypos 1.0 yanchor 1.0 alpha 0.0 zoom 3.0 rotate None
        linear 3.0 zoom 1.0 alpha 1.0 ypos 1.0
        time 35.0
        "video/OP_characterMiharu.png"
        xalign 0.0 ypos 1.0 yanchor 1.0 alpha 0.0 zoom 3.0 rotate None
        linear 3.0 zoom 1.0 alpha 1.0
        time 40.0
        "video/OP_charbackgroundC5.png"
        xpos 1.0 xanchor 0.5 yalign 0.0 alpha 0.5 zoom 1.0 rotate None
        linear 0.6 xanchor 1.0 alpha 1.0
        time 41.0
        alpha 0.0
        time 42.5
        "video/OP_characterQUEEN.png"
        xalign 1.0 ypos 1.0 yanchor 0.0 alpha 0.0 zoom 1.0  rotate None
        linear 1.5 yanchor 1.0 alpha 1.0
        time 45.0
        "video/OP_characterAizawa.png"
        xpos 1.5 xanchor 0.5 yalign 1.0 zoom 1.0 alpha 1.0
        linear 0.25 xpos 0.55
        linear 1.75 xpos 0.5
        linear 0.25 xpos -0.5
        time 47.75
        "video/OP_characterFreya.png"
        xpos -0.5 xanchor 0.5 yalign 1.0 zoom 1.0
        linear 0.25 xpos 0.45
        linear 1.75 xpos 0.5
        time 49.75
        alpha 0.0
        #End Character Intro Sequence

        #Begin Kana Rain Sequence
        time 50.4
        OP_ripple1
        zoom 0.1 alpha 0.75 xalign 0.5 yalign 0.5
        easeout 1.25 zoom 2.0 alpha 0.3
        time 54.25
        "video/OP_rainkana-light.jpg"
        alpha 0.0 xalign 1.0 yalign 1.0 zoom 1.0 rotate None
        linear 0.25 alpha 0.5
        time 54.5
        linear 0.5 alpha 1.0
        time 55
        linear 0.5 alpha 0.4
        time 55.5
        linear 0.35 alpha 0.85
        time 55.9
        linear 0.35 alpha 1.0
        time 56.25
        "video/OP_raindescenthand.png"
        time 57.25
        linear 0.35 ypos -1.0
        #End Kana Rain Sequence

        #Begin Miharu Water Sequence
        time 58.5
        OP_ripple2
        zoom 0.1 alpha 0.75 xalign 0.5 yalign 0.5
        easeout 1.25 zoom 2.0 alpha 0.3
        time 60
        "video/OP_miharuwaterlight1.jpg"
        xalign 0.5 ypos 0.5 yanchor 0.3 zoom 1.0 alpha 0.0
        parallel:
            linear 4.0 yanchor 0.4 zoom 1.3
        parallel:
            linear 0.5 alpha 0.3
            linear 0.5 alpha 0.1
            linear 0.5 alpha 0.5
            linear 0.5 alpha 0.2
            linear 0.5 alpha 0.7
            linear 0.5 alpha 0.4
            linear 0.4 alpha 0.9
            linear 0.4 alpha 0.5
            linear 0.2 alpha 0.9
        time 64
        "video/OP_rainascenthand.png"
        alpha 1.0 xalign 0.0 yalign 0.0 zoom 1.0
        time 65.25
        linear 0.35 ypos 1.0
        time 67.25
        OP_quickmontage
        xalign 0.5 yalign 0.5 zoom 0.8 alpha 0.0
        linear 3.0 alpha 0.9 zoom 2.5
        time 70.25
        alpha 0.0
        #End Miharu Water Sequence

        #Begin Beach Sequence
        time 72.75
        "video/OP_beachqueen.jpg"
        xalign 0.0 yanchor 0.9 ypos 1.0 zoom 2.5 alpha 0.0
        parallel:
            linear 3.0 xalign 1.0 yalign 0.1 zoom 1.3
        parallel:
            linear 1.0 alpha 1.0
            linear 1.5 alpha 1.0
            linear 1.0 alpha 0.0
        time 77.75
        "video/OP_beachkanamiharu.jpg"
        crop (0,225,225,175) size (800, 600)
        xalign 0.0 yalign 0.5 rotate None alpha 0.0
        parallel:
            linear 1.5 crop (75,225,225,175) size (800, 600)
        parallel:
            linear 0.5 alpha 1.0
            linear 0.5 alpha 1.0
            linear 0.5 alpha 0.0
        #End Beach Sequence

        #Begin Garden Sequence
        time 80.25
        OP_white
        xalign 0.0 yalign 0.0 alpha 0.0 zoom 1.0 crop None size None
        linear 0.5 alpha 1.0
        time 81.25
        linear 2.0 alpha 0.0
        time 83.5
        "video/OP_garden2.jpg"
        xalign 1.0 yalign 0.0 zoom 1.0 alpha 0.0
        parallel:
            linear 5.0 xalign 0.0
        parallel:
            linear 1.0 alpha 1.0
        time 86.25
        "video/OP_gardencyllia1.png"
        alpha 1.0 xalign 0.0 yalign 0.0 zoom 1.0
        time 86.75
        "video/OP_gardencyllia2.png"
        time 86.85
        "video/OP_gardencyllia1.png"
        time 86.95
        "video/OP_gardencyllia2.png"
        time 87.05
        "video/OP_gardencyllia1.png"
        time 87.75
        "video/OP_gardencyllia3.png"
        time 88.3
        "video/OP_gardencyllia4.png"
        time 88.45
        "video/OP_gardencyllia5.png"
        time 88.6
        "video/OP_gardencyllia6.png"
        time 88.75
        "video/OP_gardencyllia7.png"
        time 88.9
        "video/OP_gardencyllia8.png"
        time 89.25
        alpha 0.0
        #End Garden Sequence
        subpixel False

    image newOP_3:
        subpixel True
        #Begin Cyllia Twirl Sequence
        "video/OP_CyA01.png"
        alpha 0.0
        time 4.0
        alpha 1.0
        time 4.12
        "video/OP_CyA02.png"
        time 4.24
        "video/OP_CyA03.png"
        time 4.36
        "video/OP_CyA04.png"
        time 4.48
        "video/OP_CyA05.png"
        time 4.6
        "video/OP_CyA06.png"
        time 4.72
        "video/OP_CyA07.png"
        time 4.84
        "video/OP_CyA08.png"
        time 4.96
        "video/OP_CyA09.png"
        time 5.08
        "video/OP_CyA10.png"
        time 5.2
        alpha 0.0
        #End Cyllia Twirl Sequence

        #Begin Sad Image Montage
        time 5.5
        contains OP_lightshow
        alpha 1.0 xalign 0.5 yalign 0.5 zoom 1.5
        linear 4.75 zoom 0.5
        time 9.25
        OP_light
        alpha 1.0 xalign 0.5 yalign 0.5 zoom 0.1
        easeout 1.75  zoom 6.0
        time 11.0
        OP_black
        alpha 0.0
        #End Sad Image Montage

        #Begin Title Sequence
        time 19.0
        OP_circle
        xpos 0.25 ypos 0.5 xanchor 0.5 yanchor 0.5 alpha 1.0 zoom 0.05
        linear 1.0 zoom 3.0
        #End Title Sequence

        #Begin Cyllia Pose Sequence
        time 20.0
        "video/OP_CyB01.png"
        xalign 0.0 yalign 0.0 alpha 0.0 zoom 1.0
        linear 0.5 alpha 1.0
        time 21.0
        "video/OP_CyB02.png"
        alpha 0.0
        linear 0.5 alpha 1.0
        time 22.0
        "video/OP_CyB03.png"
        alpha 0.0
        linear 0.5 alpha 1.0
        time 23.0
        "video/OP_CyB04.png"
        alpha 0.0
        linear 0.5 alpha 1.0
        time 24.0
        "video/OP_CyB05.png"
        alpha 0.0
        linear 0.5 alpha 1.0
        #End Cyllia Pose Sequence

        #Begin Cyllia Tear Sequence
        time 25.0
        OP_cylliapigtails
        alpha 1.0
        time 26.25
        xpos 0.5 ypos 0.5 xanchor 0.4 yanchor 0.30 zoom 1.5
        time 27.5
        xpos 0.5 ypos 0.5 xanchor 0.35 yanchor 0.20 zoom 2.65
        #End Cyllia Tear Sequence

        #Begin Character Intro Sequence
        time 30.0
        OP_black
        alpha 0.0
        time 40.0
        "video/OP_characterReina.png"
        xpos 0.0 xanchor 1.0 ypos 1.0 yanchor 1.0 alpha 0.0 zoom 1.0 rotate None
        linear 1.5 xanchor 0.0 alpha 1.0
        time 45.0
        "video/OP_charbackgroundD4.png"
        xpos 1.7 xanchor 1.0 ypos 0.5 yanchor 0.5
        linear 0.25 xpos 1.2
        linear 1.75 xpos 1.1
        linear 0.25 xpos 0.0
        time 47.75
        "video/OP_charbackgroundD5.png"
        xpos 1.0 xanchor 0.0 ypos 0.75 yanchor 0.5
        linear 0.25 xpos -0.1
        linear 1.75 xpos -0.2
        time 49.75
        alpha 0.0
        #End Character Intro Sequence

        #Begin Kana Rain Sequence
        time 50.2
        OP_ripple1
        zoom 0.1 alpha 0.5 xalign 0.5 yalign 0.5
        easeout 1.1 zoom 2.0 alpha 0.6
        time 51.25
        OP_droplets
        alpha 0.0 xalign 1.0 yalign 1.0 zoom 1.0 rotate None
        xalign 0.0 yalign 0.0 alpha 0.0
        time 52.25
        linear 1.0 alpha 1.0
        time 54.25
        OP_droplets2
        xalign 0.0 yalign 0.0 alpha 1.0
        time 56.25
        OP_teardrop
        xpos 0.5 ypos 0.3 xanchor 0.5 yanchor 0.5 rotate 90
        time 57.25
        linear 0.75 ypos 1.5
        #End Kana Rain Sequence

        #Begin Miharu Water Sequence
        time 58.5
        OP_ripple2
        zoom 0.1 alpha 0.5 xalign 0.5 yalign 0.5 rotate None
        easeout 1.1 zoom 2.0 alpha 0.6
        time 59.75
        contains OP_miharuwatersurface
        zoom 1.0 alpha 0.0
        linear 0.25 alpha 0.05
        time 64
        OP_teardrop
        xalign 0.5 yalign 0.5 rotate 90 alpha 1.0
        time 65.25
        linear 3.0 ypos 0.3
        time 68.25
        alpha 0.7
        time 70.0
        OP_black
        alpha 0.0 zoom 1.0 rotate None
        #End Miharu Water Sequence

        #Begin Garden Sequence
        time 79.75
        "video/OP_foliage.png"
        alpha 1.0 xanchor 1.0 xpos 0.0 yalign 0.0 size (4200, 600)
        linear 1.5 xanchor 0.0 xpos 1.0
        time 83.5
        alpha 0.0 xanchor 1.0 xpos 1.25 yalign 0.5 size None
        "video/OP_gardentreeshade.png"
        parallel:
            linear 1.5 rotate 5.0
            linear 2.5 rotate 0.0
        parallel:
            easein 1.5 ypos 0.47
            easeout 2.5 ypos 0.53
        parallel:
            linear 5.0 xanchor 0.0 xpos -0.25
        parallel:
            linear 1.5 yzoom 1.03
            easeout 2.5 yzoom 0.99 xzoom 1.05
        parallel:
            linear 1.0 alpha 0.25
            linear 1.0 alpha 0.3
            linear 2.0 alpha 0.2
        time 86.25
        OP_black
        alpha 0.0
        #End Garden Sequence
        subpixel False

    image newOP_4:
        subpixel True
        #Begin Cyllia Twirl Sequence
        OP_filmgrain
        alpha 0.3 zoom 1.15
        #End Cyllia Twirl Sequence

        #Begin Sad Image Montage
        time 5.5
        alpha 0.45 zoom 1.5
        time 9.5
        linear 1.0 alpha 0.0 zoom 1.0
        time 10.5
        OP_black
        alpha 0.0
        #End Sad Image Montage

        #Begin Title Sequence
        time 19.25
        OP_circle
        xpos 0.45 ypos 0.95 xanchor 0.5 yanchor 0.5 alpha 1.0 zoom 0.05
        linear 0.5 zoom 2.5
        #End Title Sequence

        #Begin Cyllia Pose Sequence
        time 20
        OP_filmgrain
        alpha 0.3 zoom 1.5
        time 25.0
        alpha 0.0
        #End Cyllia Pose Sequence

        #Begin Cyllia Tear Sequence
        time 27.75
        "video/OP_CyE-Tears01.png"
        xalign 1.0 yalign 1.0 rotate None zoom 1.0
        linear 0.5 alpha 1.0
        time 28.25
        "video/OP_CyE-Tears02.png"
        time 28.5
        OP_cylliapretear
        time 29.0
        OP_cylliasparkle
        xpos 270 ypos 315 xanchor 0.5 yanchor 0.5
        linear 0.4 alpha 1.0
        time 29.6
        linear 0.35 xpos 800
        #End Cyllia Tear Sequence

        #Begin Character Intro Sequence
        time 31.25
        "video/OP_charTextKana2.png"
        xpos 0.2 xanchor 0.0 yalign 0.5 alpha 0.0 zoom 1.0 rotate None
        linear 2.25 alpha 1.0
        time 35.0
        "video/OP_charTextMiharu2.png"
        xalign 0.6 ypos 0.35 yanchor 0.5 alpha 0.0
        time 36.25
        linear 2.25 alpha 1.0
        time 40.0
        "video/OP_charTextReinaQUEEN.png"
        xalign 0.0 yalign 0.0 alpha 0.0
        time 42.5
        linear 2.0 alpha 1.0
        time 45.0
        "video/OP_charTextAizawa2.png"
        xpos 0.95 xanchor 1.0 ypos 0.5 yanchor 0.5 alpha 0.0
        time 45.25
        linear 0.25 alpha 1.0
        time 46.75
        linear 0.25 alpha 0.0
        time 48.0
        "video/OP_charTextFreya2.png"
        xpos 0.05 xanchor 0.0 ypos 0.75 yanchor 0.5 alpha 0.0
        linear 0.25 alpha 1.0
        time 49.5
        linear 0.25 alpha 0.0
        #End Character Intro Sequence

        #Begin Kana Rain Sequence
        time 50.1
        OP_ripple1
        zoom 0.1 alpha 0.25 xalign 0.5 yalign 0.5
        easeout 1.0 zoom 2.0 alpha 1.0
        time 51.75
        SnowBlossom("video/OP_raindrop1.png",count=150, border=0, xspeed=(0,0),yspeed=(2000,3000),start=10, horizontal=False)
        xalign 0.0 yalign 0.0 zoom 1.0 alpha 0.5
        time 56.25
        contains OP_teardropglow
        xpos 0.5 ypos 0.3 xanchor 0.5 yanchor 0.5 alpha 0.8
        time 57.25
        linear 0.75 ypos 1.5
        #End Kana Rain Sequence

        #Begin Miharu Water Sequence
        time 58
        contains OP_teardropglow
        zoom 7.0 xalign 0.5 yalign 0.5 alpha 0.6
        linear 0.5 zoom 0.1
        time 58.5
        OP_black
        alpha 0.0
        time 64.0
        contains OP_teardropglow2
        xalign 0.5 yalign 0.5 alpha 1.0 zoom 1.0
        time 65.25
        linear 3.0 ypos 0.3
        time 68.25
        alpha 0.7
        #End Miharu Water Sequence

        #Begin Beach Sequence
        time 70.25
        OP_white
        xalign 0.0 yalign 0.0 alpha 1.0 zoom 1.0
        linear 1.5 alpha 0.0
        #End Beach Sequence

        #Begin Garden Sequence
        time 79.95
        contains OP_foliagelight
        xanchor 0.5 yanchor 0.5 xpos 0.0 ypos 0.0 zoom 3.5 alpha 1.0
        time 81.15
        OP_light
        alpha 1.0
        time 83.5
        linear 1.0 xpos -0.35 ypos -0.35 zoom 6.0
        time 86.25
        OP_black
        alpha 0.0
        time 89.25
        "video/projectC3.png"
        xanchor 0.5 yanchor 0.0 xpos 0.5 ypos 0.5 zoom 1.0 alpha 0.0
        linear 0.5 alpha 1.0
        #End Garden Sequence
        subpixel False

    image newOP_5:
        #Begin Opening Credits (these have no sequence boundaries)
        Text(OPCredits01, style="credits")
        xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 alpha 0.0
        alpha 0.0
        time 1.5
        linear 0.5 alpha 1.0
        time 5.0
        linear 0.5 alpha 0.0
        time 16.5
        Text(OPCredits02, style="credits")
        xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.95 alpha 0.0
        linear 0.5 alpha 1.0
        time 19.0
        linear 0.5 alpha 0.0
        time 20.5
        Text(OPCredits03, style="credits")
        xanchor 1.0 yanchor 1.0 xpos 0.95 ypos 0.95 alpha 0.0
        linear 0.5 alpha 1.0
        time 24.5
        linear 0.5 alpha 0.0
        #Exception for extended Cyllia Tear Sequence detail
        time 29.0
        OP_teardrop
        xpos 270 ypos 315 xanchor 0.5 yanchor 0.5
        linear 0.4 alpha 1.0
        time 29.5
        linear 0.4 xpos 900
        #End Exception
        time 30.0
        Text(OPCredits04, style="credits")
        xanchor 0.0 yanchor 1.0 xpos 0.05 ypos 0.8 alpha 0.0
        time 30.5
        linear 0.5 alpha 1.0
        time 34.5
        linear 0.5 alpha 0.0
        time 40.5
        Text(OPCredits05, style="credits")
        xanchor 1.0 yanchor 1.0 xpos 0.95 ypos 0.8 alpha 0.0
        linear 0.5 alpha 1.0
        time 44.5
        linear 0.5 alpha 0.0
        time 49.75
        alpha 0.0 xalign 1.0 yalign 1.0 zoom 1.0 rotate None
        time 52.75
        Text(OPCredits06, style="credits")
        xanchor 0.0 yanchor 1.0 xpos 0.05 ypos 0.9 alpha 0.0
        linear 0.5 alpha 1.0
        time 57.25
        linear 0.5 alpha 0.0
        time 60.25
        Text(OPCredits07, style="credits")
        xanchor 1.0 yanchor 1.0 xpos 0.95 ypos 0.95 alpha 0.0
        linear 0.5 alpha 1.0
        time 64.75
        linear 0.5 alpha 0.0
        #Exception for Miharu Water Sequence detail
        time 69
        OP_light
        alpha 1.0 xalign 0.5 yalign 0.5 ypos 0.3 zoom 0.05
        easeout 1.25 zoom 8.0
        time 70.25
        alpha 0.0 zoom 1.0
        #End Exception
        time 70.75
        Text(OPCredits08, style="credits")
        xanchor 0.5 yanchor 1.0 xpos 0.5 ypos 0.95 alpha 0.0
        linear 0.5 alpha 1.0
        time 74.75
        linear 0.5 alpha 0.0
        time 81
        Text(OPCredits09, style="credits")
        xanchor 0.5 yanchor 1.0 xpos 0.5 ypos 0.95 alpha 0.0
        linear 0.5 alpha 1.0
        time 85.5
        linear 0.5 alpha 0.0
        time 89.25
        Text(OPCredits10, style="credits")
        xanchor 0.5 yanchor 1.0 xpos 0.5 ypos 0.45 alpha 0.0
        linear 0.5 alpha 1.0
        #End Opening Credits



    #OP Sequence sub-animations go here...

    transform OP_lightshow:
        "video/OP_light1.png"
        alpha 1.00 rotate 0.0
        pause 0.033
        alpha 0.95 rotate 180.0
        pause 0.033
        alpha 1.00 rotate 45.0
        pause 0.033
        alpha 0.95 rotate 23.0
        pause 0.033
        alpha 1.00 rotate 360.0
        pause 0.033
        alpha 0.95 rotate 77.0
        pause 0.033
        alpha 1.00 rotate 224.0
        pause 0.033
        alpha 0.95 rotate 90.0
        pause 0.033
        repeat

    transform OP_teardropglow:
        "video/OP_teardropglow.png"
        linear 0.2 alpha 1.0
        linear 0.25 alpha 0.5
        linear 0.2 alpha 1.0
        linear 0.15 alpha 0.4
        linear 0.25 alpha 0.85
        linear 0.2 alpha 1.0
        linear 0.2 alpha 0.5
        repeat

    transform OP_teardropglow2:
        "video/OP_teardropglow.png"
        linear 0.02 alpha 1.0
        linear 0.05 alpha 0.8
        linear 0.02 alpha 1.0
        linear 0.03 alpha 0.7
        linear 0.05 alpha 0.95
        linear 0.02 alpha 1.0
        linear 0.03 alpha 0.8
        repeat

    transform OP_miharuwatersurface:
        "video/OP_miharuwatersurface.png" with Dissolve(0.2)
        linear 0.2 align (0.50, 0.50) zoom 1.0
        linear 0.2 align (0.49, 0.51) xzoom 1.05
        linear 0.2 align (0.48, 0.49) xzoom 1.03 yzoom 1.05
        linear 0.2 align (0.51, 0.51) yzoom 1.04 xzoom 1.0
        linear 0.2 align (0.50, 0.48) zoom 1.02
        linear 0.2 align (0.52, 0.49) yzoom 1.03 xzoom 1.0
        linear 0.2 align (0.49, 0.51) yzoom 1.02 xzoom 1.03
        repeat

    transform OP_foliagelight:
        OP_light
        alpha 1.0
        pause 0.04
        alpha 0.0
        pause 0.02
        alpha 1.0
        pause 0.06
        alpha 0.0
        pause 0.02
        alpha 1.0
        pause 0.02
        alpha 0.0
        pause 0.02
        alpha 1.0
        pause 0.1
        alpha 0.0
        pause 0.06
        alpha 1.0
        pause 0.02
        alpha 0.0
        pause 0.02
        alpha 1.0
        pause 0.02
        alpha 0.0
        repeat

    # end OP sequence

    image schoolchime:
        "images/bg_academy-close.jpg"
        alpha 0.0
        linear 1.5 alpha 1.0

    # I put the styles into this line, because it would be amazingly
    # tiring to get up and down, this document has at least over 1000 lines!
    $ style.create("act_popup", "default", u"(text) Act_popup")
    #$ style.act_popup.font = None #your favourite font
    $ style.act_popup.size = 28
    $ style.act_popup.color = "#FFFFFF"
    $ style.act_popup.outlines = [(2, "#000000", 0, 0)]

    image acttitle:
        Text(act_name, style="act_popup")
        xalign .25 yalign .05
        alpha .0
        time 2.5
        parallel:
            linear .5 alpha 1.0
        parallel:
            easein .5 xalign .15
        time 6
        linear 1 alpha 0.0

    image actgeez:
        "video/geez.png"
        alpha .0
        time 2
        easein 1 alpha 1.0
        time 6
        easeout 1 alpha 0.0

    # Define Arrow for 'click-to-continue', you can even chosse,
    # if it shall blink or not
    if persistent.arrow_anim == True:
        image ctc_arrow = anim.Filmstrip("gameui/arrow_stripe.png", (16, 16), (8, 8), .05, xalign=.97, yalign=.97)
    else:
        image ctc_arrow = im.Image("gameui/arrow.png", xalign=.97, yalign=.97)

    image konobangumiwa_1:
        "video/konobangumiwa_kana.jpg"

    image konobangumiwa_1b:
        "video/konobangumiwa_reina.jpg"

    image konobangumiwa_2:
        "video/konobangumiwa_sponsors1.png"
        time 5.0
        "video/konobangumiwa_sponsors2.png"
        time 9.0
        alpha 0.0

    image ED1_1:
        subpixel True
        "video/ED_room1.jpg"
        xpos 1.0 ypos 0.0 xanchor 1.0 yanchor 0.0 alpha 0.0
        parallel:
            linear 32.0 xpos 0.0 ypos 0.0 xanchor 0.0 yanchor 0.0
        parallel:
            linear 25.0 alpha 1.0
        time 31.75
        "video/ED_sketch2.png"
        xalign 0.0 yalign 0.0 alpha 1.0
        time 33.75
        "video/ED_room2.jpg"
        xpos 0.25 ypos 0.5 xanchor 0.25 yanchor 0.5 zoom 0.55 alpha 1.0
        parallel:
            linear 20.25 xpos 0.25 ypos 0.5 xanchor 0.2 yanchor 0.55
        parallel:
            linear 20.25 zoom 1.0

    image ED1_2:
        subpixel True
        "video/ED_sketch1.png"
        alpha 0.0
        time 31.25
        linear 0.15 alpha 1.0
        time 31.75
        linear 0.15 alpha 0.0
        time 32.50
        "video/ED_sketch3.png"
        alpha 0.0
        linear 0.25 alpha 1.0
        time 33.75
        alpha 0.0
        time 52.0
        "video/ED_room3.jpg"
        xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5 zoom 0.78
        parallel:
            linear 17.0 xpos 0.5 ypos 0.5 xanchor 0.35 yanchor 0.35 alpha 0.0
        parallel:
            linear 17.0 zoom 1.2
        parallel:
            linear 2.0 alpha 1.0

    image ED1_3:
        subpixel True
        "video/ED_room3.jpg"
        alpha 0.0
        time 67.0
        xpos 0.5 ypos 0.5 xanchor 0.35 yanchor 0.35 zoom 1.5 alpha 0.0
        parallel:
            linear 6.0 xpos 0.5 ypos 0.5 xanchor 0.35 yanchor 0.35
        parallel:
            linear 6.0 zoom 1.75
        parallel:
            linear 2.0 alpha 1.0

    image ED1_4:
        subpixel True
        Text(renpy.file("scripts/credits1.txt").read(), style="rollingcredits1")
        xpos 0.375 ypos 1.0 xanchor 0.0 yanchor 0.0
        linear 70 ypos 0.0 yanchor 1.0
        time 72.0
        "video/somerightsreserved.png"
        xpos 0.0 ypos 0.0 xanchor 0.0 yanchor 0.0 alpha 0.0
        linear 0.5 alpha 1.0

    image ED1_5:
        subpixel True
        Text(renpy.file("scripts/credits2.txt").read(), style="rollingcredits2")
        xpos 0.375 ypos 1.0 xanchor 0.0 yanchor 0.0
        linear 70.0 ypos 0.0 yanchor 1.0

    image creativecommons:
        "video/intro_creativecommons.png"

    image studiottpetok:
        "video/intro_studiottpetok.jpg"

    transform pigux_0:
        "video/intro_pigux-penguin.png"
        linear 0.05 xzoom 1.0
        linear 0.05 xzoom 0.0
        linear 0.05 xzoom -1.0
        linear 0.05 xzoom 0.0
        repeat

    image pigux_1:
        contains pigux_0
        xpos 0.5 ypos 0.45 xanchor 0.5 yanchor 0.5
        time 1.5
        alpha 0.0

    image pigux_2:
        "video/intro_pigux-penguin.png"
        alpha 0.0
        time 1.5
        xpos 0.5 ypos 0.45 xanchor 0.5 yanchor 0.5 alpha 1.0
        linear 0.25 xpos 0.9 ypos 0.45
        time 3.5
        linear 0.05 yanchor 0.40
        linear 0.05 yanchor 0.50
        linear 0.05 yanchor 0.40
        linear 0.05 yanchor 0.50
        time 5.0
        linear 0.5 xpos 0.57 ypos 0.45
        time 5.5
        linear 0.25 xpos 0.57 ypos 0.18

    image pigux_3:
        "video/intro_pigux-pig.png"
        alpha 0.0
        time 1.0
        xpos -0.2 ypos 0.52 xanchor 0.5 yanchor 0.5 alpha 1.0
        linear 0.5 xpos 0.45 ypos 0.52 rotate 1130.0
        rotate 0.0
        time 1.5
        xpos 0.45 ypos 0.52 xanchor 0.5 yanchor 0.5
        linear 1.0 xpos 0.1 ypos 0.52 rotate 365.0
        rotate 0.0
        time 4.0
        linear 0.05 yanchor 0.40
        linear 0.05 yanchor 0.50
        linear 0.05 yanchor 0.40
        linear 0.05 yanchor 0.50
        time 5.0
        linear 0.5 xpos 0.43 ypos 0.52
        time 5.5
        linear 0.25 xpos 0.43 ypos 0.25

    image pigux_4:
        "video/intro_piguxproductions.png"
        alpha 0.0
        time 6.0
        linear 0.5 alpha 1.0

    # All in-game ATL Animations here.

    transform PanAndZoom(STARTX, STARTY, STARTANCHORX, STARTANCHORY, ENDX, ENDY, ENDANCHORX, ENDANCHORY, TOTALTIME, STARTSIZE, ENDSIZE, ALPHATIME, STARTALPHA, ENDALPHA):
        xpos STARTX ypos STARTY xanchor STARTANCHORX yanchor STARTANCHORY zoom STARTSIZE alpha STARTALPHA
        parallel:
            linear TOTALTIME xpos ENDX ypos ENDY xanchor ENDANCHORX yanchor ENDANCHORY
        parallel:
            linear TOTALTIME zoom ENDSIZE
        parallel:
            linear ALPHATIME alpha ENDALPHA

    transform ZoomInOut(STARTX, STARTY, STARTANCHORX, STARTANCHORY, ENDX, ENDY, ENDANCHORX, ENDANCHORY, TOTALTIME, STARTSIZE, ENDSIZE):
        subpixel True
        xpos STARTX ypos STARTY xanchor STARTANCHORX yanchor STARTANCHORY zoom STARTSIZE
        parallel:
            linear TOTALTIME xpos ENDX ypos ENDY xanchor ENDANCHORX yanchor ENDANCHORY
        parallel:
            linear TOTALTIME zoom ENDSIZE

    transform Fling(STARTX, STARTY, ENDX, ENDY, TOTALTIME, REVOLUTIONS):
        xpos STARTX ypos STARTY xanchor 0.5 yanchor 0.5
        linear TOTALTIME xpos ENDX ypos ENDY rotate REVOLUTIONS
        rotate 0.0

    transform QuickFling(ENDX, ENDY, TOTALTIME, REVOLUTIONS):
        linear TOTALTIME xpos ENDX ypos ENDY rotate REVOLUTIONS
        rotate 0.0

    transform BackgroundFling(ENDX, ENDY, TOTALTIME, REVOLUTIONS, SIZE):
        linear TOTALTIME xpos ENDX ypos ENDY rotate REVOLUTIONS zoom SIZE

    transform Bobble(STARTX, STARTY, ENDX, ENDY, SPRING, TOTALTIME):
        parallel:
            xpos STARTX ypos STARTY xanchor 0.5
            linear TOTALTIME xpos ENDX ypos ENDY
        parallel:
            easein 0.25 yanchor SPRING
            easein 0.25 yanchor 0.5
            repeat

    transform EnterLeft(ENDX, TOTALTIME):
        xpos 0.0 xanchor 1.0 yalign 0.0
        easein TOTALTIME xalign ENDX

    transform EnterRight(ENDX, TOTALTIME):
        xpos 1.0 xanchor 0.0 yalign 0.0
        easein TOTALTIME xalign ENDX

    transform ExitLeft(TOTALTIME):
        easeout TOTALTIME xpos 0.0 xanchor 1.0

    transform ExitRight(TOTALTIME):
        easeout TOTALTIME xpos 1.0 xanchor 0.0

    transform MoveTo(ENDX, TOTALTIME):
        linear TOTALTIME xalign ENDX

    transform SendTo(ENDX, ENDY, TOTALTIME):
        linear TOTALTIME xpos ENDX ypos ENDY

    transform Appear(STARTX, STARTY, ANCHORX, ANCHORY):
        xpos STARTX xanchor ANCHORX ypos STARTY yanchor ANCHORY

    transform DissolveAppear(STARTX, STARTY, ANCHORX, ANCHORY, TOTALTIME):
        xpos STARTX xanchor ANCHORX ypos STARTY yanchor ANCHORY alpha 0.0
        linear TOTALTIME alpha 1.0

    transform SelfDissolve(STARTALPHA, ENDALPHA, TOTALTIME):
        alpha STARTALPHA
        linear TOTALTIME alpha ENDALPHA

    transform Rise(STARTX, TOTALTIME):
        xalign STARTX ypos 1.0 yanchor 0.0
        linear TOTALTIME ypos 0.0

    transform Sit(TOTALTIME):
        linear TOTALTIME ypos 1.0  yanchor 0.0

    transform RunInDistance(STARTX, ENDX, STARTY, TOTALTIME):
        zoom 0.25
        xpos STARTX ypos STARTY xanchor 0.0 yanchor 0.0
        linear TOTALTIME xpos ENDX
        zoom 1.0

    transform Bounce(ITERATIONS):
        linear 0.05 ypos -0.03
        linear 0.05 ypos 0.0
        repeat ITERATIONS

    transform SmartBounce(STARTANCHORY, ENDANCHORY, ITERATIONS):
        linear 0.05 yanchor ENDANCHORY
        linear 0.05 yanchor STARTANCHORY
        repeat ITERATIONS

    transform Laugh(ITERATIONS):
        easein 0.1 ypos 0.03
        easeout 0.1 ypos 0.0
        repeat ITERATIONS

    transform Bow(ITERATIONS):
        easein 0.4 ypos 0.10
        easeout 0.4 ypos 0.0
        repeat ITERATIONS

    transform VChatter:
        easein 0.50 ypos 0.03
        easeout 0.50 ypos 0.0
        repeat

    transform HChatter(STARTX, ENDX):
        choice:
            easein 0.50 xpos ENDX
            easeout 0.50 xpos STARTX
        choice:
            linear 0.25 xpos ENDX
            linear 0.25 xpos STARTX
            pause 0.25
        choice:
            linear 0.30 xpos ENDX
            linear 0.30 xpos STARTX
            linear 0.10 xpos ENDX
            linear 0.10 xpos STARTX
            linear 0.10 xpos ENDX
            linear 0.10 xpos STARTX
            pause 0.25
        choice:
            easein 0.40 xpos ENDX
            pause 0.25
            linear 0.10 xpos STARTX
            linear 0.10 xpos ENDX
            linear 0.10 xpos STARTX
            linear 0.10 xpos ENDX
            linear 0.10 xpos STARTX
            pause 0.25
        choice:
            linear 0.10 xpos ENDX
            linear 0.10 xpos STARTX
            pause 0.25
        repeat

    transform Shake(SPRING, ITERATIONS):
        easein 0.3 xanchor SPRING
        easeout 0.3 xanchor 0.5
        repeat ITERATIONS

    transform Heft(SPRING, ITERATIONS):
        easein 0.3 yanchor SPRING
        easeout 0.3 yanchor 0.5
        repeat ITERATIONS

    transform Rattle(ORIGIN, SPRING, ITERATIONS, TOTALTIME):
        easein TOTALTIME yanchor SPRING
        easeout TOTALTIME yanchor ORIGIN
        repeat ITERATIONS

    transform Dizzy(STARTX, STARTY, ANCHORX, ANCHORY, TOTALTIME):
        xpos STARTX ypos STARTY xanchor ANCHORX yanchor ANCHORY
        linear TOTALTIME xzoom 1.0
        linear TOTALTIME xzoom 0.0
        linear TOTALTIME xzoom -1.0
        linear TOTALTIME xzoom 0.0
        repeat

    transform SetPosition(SIZE, REVOLUTIONS):
        zoom SIZE rotate REVOLUTIONS

    transform CorrectionZooms(ZOOMX, ZOOMY):
        xzoom ZOOMX yzoom ZOOMY

    transform Panic(TOTALTIME, WAITTIME):
        linear TOTALTIME xpos -1.0
        pause WAITTIME
        linear TOTALTIME xpos 2.0
        pause WAITTIME
        repeat

    image lightning:
        "images/ambient_white.png"
        pause 0.03
        alpha 0.0
        pause 0.1
        alpha 0.8
        pause 0.02
        easeout 0.3 alpha 0.0

    image redsiren:
        "images/ambient_redsiren.png"
        alpha 0.0
        linear 1.5 alpha 1.0
        linear 1.5 alpha 0.0
        pause 0.5
        repeat

    image angrytwitch:
         "images/prop_twitch.png"
         zoom 0.5
         pause 0.2
         zoom 1.0
         pause 0.2
         repeat

    image hauntedtwirl:
        "images/prop_twirl.png"
        xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
        rotate 0.0
        linear 5.0 rotate 365.0
        repeat

    image creepyqueenhaku:
        subpixel True
        "images/prop_haku.png"
        xanchor 0.5 yanchor 0.5 xpos 0.5, ypos 0.5 zoom 1.0
        alpha 0.0
        linear 4.0 zoom 2.0 alpha 0.6
        linear 1.0 zoom 2.25 alpha 0.0
        im.Composite(None, (0,0), "character/queen_body.png", (0,0), "character/queen_mouth-frown.png", (0,0), "character/queen_eyes-normal.png", (0,0), "character/queen_eyebrows-angry.png")
        xanchor 0.55 yanchor 0.25 xpos 0.5, ypos 0.5
        alpha 0.0 zoom 2.0
        linear 4.0 zoom 4.0 alpha 0.4
        linear 1.0 zoom 4.5 alpha 0.0
        repeat

    ###### END DEFINITIONS ######


# Set splashscreen here
label splashscreen:
    $ mouse_visible = False
    $ _game_menu_screen = None
    scene black
    $ renpy.pause(1)
    show text "Studio TT Petok\n&\nPigux Productions\n\nProudly Present..."
    with dissolve
    with Pause(2.5)

    hide text
    with dissolve

    $ mouse_visible = True
    $ _game_menu_screen = "save"
    return

# The game starts here.
label start:
    $ mouse_visible = False
    $ _game_menu_screen = None
    stop music
    scene black
    with Pause(1.0)
    show creativecommons
    with dissolve
    with Pause(4.0)
    hide creativecommons
    with dissolve

    scene white
    show pigux_1
    show pigux_2
    show pigux_3
    show pigux_4 behind pigux_2
    $ renpy.pause(8.5)

    scene black
    with dissolve
    show studiottpetok
    with dissolve
    with Pause(3.5)
    hide studiottpetok
    with dissolve
    $ mouse_visible = True
    $ _game_menu_screen = "save"

    $ start_lang_script()

init -2 python:

    def start_lang_script():
        for i in languagechoice:
            if i[1] == persistent.lang:
                renpy.jump(i[2])

