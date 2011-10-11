#
## These settings let you customize the window containing the
## dialogue and narration, by replacing it with an image.
#

init python:
    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.

    # style.window.background = Frame("frame.png", 12, 12)

    ## Margin is space surrounding the window, where the background
    ## is not drawn.

    # style.window.left_margin = 6
    # style.window.right_margin = 6
    # style.window.top_margin = 6
    # style.window.bottom_margin = 6

    ## Padding is space inside the window, where the background is
    ## drawn.

    # style.window.left_padding = 6
    # style.window.right_padding = 6
    # style.window.top_padding = 6
    # style.window.bottom_padding = 6

    ## Some one-time settings

    ## The background of the main menu.
    animspindle = At("video/mainmenu-spindle.png", RotoZoom(0, 5, 1.0, 1, 1, 1, rot_repeat=True, opaque=False, xanchor=0.5, yanchor=0.5))
    animspindle2 = At(im.Alpha("video/mainmenu-spindle.png", 0.6), RotoZoom(5, 0, 1.0, 0.6, 0.6, 1, rot_repeat=True, opaque=False, xanchor=0.5, yanchor=0.5))
    animmenu = LiveComposite((800, 600), (0, 0), "video/mainmenu-bg.jpg", (-25, -225), animspindle, (300, 100), animspindle2)
    style.mm_root.background = animmenu

    ## The background of the game menu. Colour or image are allowed.
    style.gm_root.background = "video/menu-bg.jpg"

    ## dialog design, wohoo~
    style.window.background = Frame(im.Image("gameui/bg_speak_v2.png"),0,0)
    # these parameters places the Kana-avatar in the dialog text
    style.window.left_padding = 160 # the same as 'window_left_padding=160'
    style.window.right_padding = 15
    style.window.top_padding = 10

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)


    #########################################
    ## This lets you change the placement of the main menu.

    ## The way placement works is that we find an anchor point
    ## inside a displayable, and a position (pos) point on the
    ## screen. We then place the displayable so the two points are
    ## at the same place.

    ## An anchor/pos can be given as an integer or a floating point
    ## number. If an integer, the number is interpreted as a number
    ## of pixels from the upper-left corner. If a floating point,
    ## the number is interpreted as a fraction of the size of the
    ## displayable or screen.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5

    themechoice = [
        ("Kana",        "kana"),
        ("Miharu",      "miharu"),
        ("Q.U.E.E.N.",  "queen"),
        ]

    def set_theme():

        ## soft violett and pink... unlike her character
        ## that's the colour of Kana
        descript_col = "#F3E7EB"
        inselect_col = "#756067"
        control1_col = "#6D3855"
        control2_col = "#664B77"
        control3_col = (109,56,85,64) # the same as #664B77, but with 25% alpha
        txt_butt_col = "#FFD0DA"
        hove_but_col = "#E3D2CE"
        hove_txt_col = "#FCFCFC"
        sele_but_col = "#A40C2F"
        frame_color  = "#C7779F" #(199,119,159,225)

    ## Okay folks, this IS... no done yet ^^
    ## As you can see, you're able to change the colour only.
    ## but some of you clever people will see, you CAN change styles
    ## and images too, but for now, I've made the colours changeable.
    ## Now, again, it's up to YOU, if you want your theme in here
    #
    ## images normally are saved in '/gameui' and '/video',
    ## you can add your own things you like
    #
    ## to change the theme, you've unfortunately got to restart the game

        if persistent.theme is None:
            persistent.theme = "kana"


        elif persistent.theme == "miharu":
            ## strong orange and yellow
            ## that's Miharu ^^
            descript_col = "#F3F0E7"
            inselect_col = "#756B60"
            control1_col = "#6D5138"
            control2_col = "#936134"
            control3_col = (28,56,85,64) # the same as #936134, but with 25% alpha
            txt_butt_col = "#FFE8D0"
            hove_but_col = "#E3DDCE"
            hove_txt_col = "#FCFCFC"
            sele_but_col = "#D54200"
            frame_color  = "#CC8947"


        elif persistent.theme == "queen":
            ## elegant orange with direction to gold
            ## weak yellow, that's Q.U.E.E.N. ^^
            descript_col = "#F3F0E7"
            inselect_col = "#756B60"
            control1_col = "#6D5138"
            control2_col = "#936134"
            control3_col = (28,56,85,64) # the same as #936134, but with 25% alpha
            txt_butt_col = "#FFE8D0"
            hove_but_col = "#E3DDCE"
            hove_txt_col = "#FCFCFC"
            sele_but_col = "#D54200"
            frame_color  = "#D69948"

        ## I think the real theming will happen, if we have new images
        ## for slider and buttons and backgrounds.
        ## We could even change the size and fonts of text all sorts
        #
        ## Mina-san, kore wa hajimeru desu ^^v
        #

        style.text.size = 20
        style.text.color = descript_col

        style.label_text.size = 20
        style.label_text.color = descript_col

    ## The settings of the text in a widget
        style.button_text.size = 20
        style.button_text.color = txt_butt_col
        style.button_text.hover_color = hove_txt_col
        style.button_text.selected_color = sele_but_col
        style.button_text.insensitive_color = inselect_col

    ## The color of a frame containing widgets.
        round_corn = theme.OneOrTwoColor("gameui/rr6.png", frame_color)
        style.frame.background = Frame(round_corn, 6,6)
        style.menu_choice_button.background = Frame(round_corn, 6,6)

    ## large button background
        file_pbutt1 = theme.OneOrTwoColor("gameui/slot_button.png", descript_col)
        file_pbutt2 = theme.OneOrTwoColor("gameui/slot_button.png", hove_but_col)
        style.large_button.background = Frame(file_pbutt1,100,0)
        style.large_button.hover_background = Frame(file_pbutt2,100,0)
        style.large_button.insensitive_background = None

    ## large button text colour etc.
        style.large_button_text.color = descript_col
        style.large_button_text.hover_color = hove_but_col
        style.large_button_text.insensitive_color = inselect_col

        style.text['menu_butt'].color = descript_col
        style.text['menu_butt'].hover_color = hove_but_col
        style.text['menu_butt'].selected_color = sele_but_col

    ## bar, the normal horizontal, yes, that one, boring but important ^^
        bar_left = theme.OneOrTwoColor("gameui/bar.png", control1_col)
        bar_right = theme.OneOrTwoColor("gameui/bar.png", control3_col)
        bar_thumb = theme.OneOrTwoColor("gameui/bar_thumb.png", control2_col)

        style.bar.ymaximum = 30
        style.bar.left_bar = Frame(bar_left,10,0)
        style.bar.right_bar = Frame(bar_right,10,0)
        style.bar.thumb = bar_thumb

        vsbar_top = theme.OneOrTwoColor("gameui/vscollbar.png", control1_col)
        vsbar_bottom = theme.OneOrTwoColor("gameui/vscollbar.png", control3_col)
        vsbar_thumb = theme.OneOrTwoColor("gameui/vscrollbar_tumb.png", control2_col)

    ## vertical scrollbar, cool, ain't it?
        style.vscrollbar.unscrollable = "insensitive"
        style.vscrollbar.xmaximum = 25
        style.vscrollbar.top_bar = Frame(vsbar_top,10,0)
        style.vscrollbar.bottom_bar = Frame(vsbar_bottom,10,0)
        style.vscrollbar.thumb = vsbar_thumb

    ## button and co.
        ## The settings of an idle widget face. If None, no button frame.
        style.button.background = None
        style.button.ypadding = 5

        hov_butt = theme.OneOrTwoColor("gameui/hover_button.png", hove_but_col)
        style.button.hover_background = Frame(hov_butt,15,0)
        style.button.selected_background = None
        style.button.selected_hover_background = None
        style.button.insensitive_background = None

    ## button for preference
        check_idle = theme.OneOrTwoColor("gameui/checkbox_on.png", control1_col)
        uncheck_idle = theme.OneOrTwoColor("gameui/checkbox_off.png", control1_col)
        check_acti = theme.OneOrTwoColor("gameui/checkbox_on.png", control2_col)
        uncheck_acti = theme.OneOrTwoColor("gameui/checkbox_off.png", control2_col)

        style.button['cbx'].background = Frame(uncheck_idle,35,0)
        style.button['cbx'].hover_background = Frame(uncheck_acti,35,0)
        style.button['cbx'].selected_background = Frame(check_idle,35,0)
        style.button['cbx'].selected_hover_background  = Frame(check_acti,35,0)

        style.text['cbx'].color = descript_col
        style.text['cbx'].hover_color = control2_col

        style.text['info'].color = inselect_col
        style.text['info'].size = 15

    ## trash icon
        trash_idle = theme.OneOrTwoColor("gameui/trash.png", control1_col)
        trash_acti = theme.OneOrTwoColor("gameui/trash.png", control2_col)

        style.button['trash'].background = Frame(trash_idle,0,0)
        style.button['trash'].hover_background = Frame(trash_acti,0,0)

    ## sound test button
        sound_test_mute = theme.OneOrTwoColor("gameui/sound_test_mute.png", control1_col)
        sound_test_acti = theme.OneOrTwoColor("gameui/sound_test_acti.png", control2_col)

        style.button['sound_test'].background = Frame(sound_test_mute,30,0)
        style.button['sound_test'].hover_background = Frame(sound_test_acti,30,0)


        #########################################
        ## These let you customize the default font used for text in Ren'Py.

        ## The file containing the default font.

        # style.default.font = "DejaVuSans.ttf"

        ## The default size of text.

        style.default.size = 18

        ## Note that these only change the size of some of the text. Other
        ## buttons have their own styles.

    set_theme()
