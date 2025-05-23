image postgamegallery:
    im.Blur("gui/main_menu2_frame.png", 3.0)

style gallery_room_title_text:
    font gui.name_text_font
    size 125 color "#ffffff"

screen gallery_bg(): # a screen that display the numbers
    tag menu
    if persistent.act_2:
        add "postgamegallery"
    else:
        add "images/backgrounds/rural_road_twilight.jpg"
    text "Gallery" style "gallery_room_title_text" xalign 0.5 yoffset 60

############################# Position of the numbers #############################
    hbox:
        spacing -10
        yalign 0.98
        xalign 0.50

        imagebutton idle "gallery/numbers/idle/1.png" hover "gallery/numbers/hover/1.png" selected_idle "gallery/numbers/selected/1.png" selected_hover "gallery/numbers/selected/1.png" action ShowMenu("gallery")
        imagebutton idle "gallery/numbers/idle/2.png" hover "gallery/numbers/hover/2.png" selected_idle "gallery/numbers/selected/2.png" selected_hover "gallery/numbers/selected/2.png" action ShowMenu("gallery_002")
        imagebutton idle "gallery/numbers/idle/3.png" hover "gallery/numbers/hover/3.png" selected_idle "gallery/numbers/selected/3.png" selected_hover "gallery/numbers/selected/3.png" action ShowMenu("gallery_003")
        imagebutton idle "gallery/numbers/idle/4.png" hover "gallery/numbers/hover/4.png" selected_idle "gallery/numbers/selected/4.png" selected_hover "gallery/numbers/selected/4.png" action ShowMenu("gallery_004")
        imagebutton idle "gallery/numbers/idle/5.png" hover "gallery/numbers/hover/5.png" selected_idle "gallery/numbers/selected/5.png" selected_hover "gallery/numbers/selected/5.png" action ShowMenu("gallery_005")
        imagebutton idle "gallery/numbers/idle/6.png" hover "gallery/numbers/hover/6.png" selected_idle "gallery/numbers/selected/6.png" selected_hover "gallery/numbers/selected/6.png" action ShowMenu("gallery_006")
        imagebutton idle "gallery/numbers/idle/7.png" hover "gallery/numbers/hover/7.png" selected_idle "gallery/numbers/selected/7.png" selected_hover "gallery/numbers/selected/7.png" action ShowMenu("gallery_007")
        imagebutton idle "gallery/numbers/idle/8.png" hover "gallery/numbers/hover/8.png" selected_idle "gallery/numbers/selected/8.png" selected_hover "gallery/numbers/selected/8.png" action ShowMenu("gallery_008")

############################# Position of the numbers #############################

    # a return button
    textbutton _("Return") action Return() align (0.0, 1.0) text_size 50:
        left_margin 25 bottom_margin 25


############################# images for the gallery #############################
init python:
    g = Gallery()

###################################### page 1 ######################################
    g.transition = Dissolve(0.5)

    g.button("a1")
    g.unlock("no_help_1")
    g.image("images/illustrations/no_help_1.jpg")
    g.image("images/illustrations/no_help_2.jpg")

    g.button("a2")
    g.unlock("lake_emma_2")
    g.image("images/illustrations/lake_emma_1.jpg")
    g.image("images/illustrations/lake_emma_2.jpg")
    g.image("images/illustrations/lake_emma_3.jpg")

    g.button("a3")
    g.unlock("closet_1")
    g.image("images/illustrations/closet_1.jpg")
    g.image("images/illustrations/closet_2.jpg")
    g.image("images/illustrations/closet_3.jpg")

    g.button("a4")
    g.unlock("carcg")
    g.image("images/illustrations/car_1.jpg")
    g.image("images/illustrations/car_2.jpg")
    g.image("images/illustrations/car_3.jpg")
    g.image("images/illustrations/car_4.jpg")
    g.image("images/illustrations/car_5.jpg")

    g.button("a5")
    g.unlock("cam_lake_1")
    g.image("images/illustrations/cam_lake_1.jpg")

    g.button("a6")
    g.unlock("cam_lake_2")
    g.image("images/illustrations/cam_lake_2.jpg")
    g.image("images/illustrations/cam_lake_3.jpg")

###################################### page 2 ######################################

    g.button("b1")
    g.unlock("cam_lake_4")
    g.image("images/illustrations/cam_lake_4.jpg")

    g.button("b2")
    g.unlock("blazed")
    g.image("images/illustrations/blazed.jpg")

    g.button("b3")
    g.unlock("creepy")
    g.image("images/illustrations/creepy.jpg")

    g.button("b4")
    g.unlock("fight1")
    g.image("images/illustrations/fight1.jpg")

    g.button("b5")
    g.unlock("fight2")
    g.image("images/illustrations/fight2.jpg")

    g.button("b6")
    g.unlock("dev_window")
    g.image("images/illustrations/dev_window.jpg")

###################################### page 3 ######################################
    g.button("c1")
    g.unlock("panic")
    g.image("images/illustrations/panic.jpg")

    g.button("c2")
    g.unlock("bg trailerpark")
    g.image("images/backgrounds/trailerpark.jpg")

    g.button("c3")
    g.unlock("forestfull")
    g.image("images/illustrations/1.jpg")
    g.image("images/illustrations/2.jpg")

    g.button("c4")
    g.unlock("brian")
    g.image("images/illustrations/brian.jpg")

    g.button("c5")
    g.unlock("mirror2")
    g.image("images/illustrations/mirror2.jpg")
    g.image("images/illustrations/mirror3.jpg")
    g.image("images/illustrations/mirror4.jpg")

    g.button("c6")
    g.unlock("psilocybin")
    g.image("images/illustrations/psilocybin.jpg")

###################################### page 4 ######################################
    g.button("d1")
    g.unlock("trailer1")
    g.image("images/illustrations/trailer1.jpg")
    g.image("images/illustrations/trailer2.jpg")
    g.image("images/illustrations/trailer3.jpg")
    g.image("images/illustrations/trailer4.jpg")

    g.button("d2")
    g.unlock("victims_1")
    g.image("images/illustrations/victims_1.jpg")
    g.image("images/illustrations/victims_2.jpg")
    g.image("images/illustrations/victims_3.jpg")
    g.image("images/illustrations/victims_4.jpg")

    g.button("d3")
    g.unlock("struggle1")
    g.image("images/illustrations/struggle1.jpg")

    g.button("d4")
    g.unlock("struggle2")
    g.image("images/illustrations/struggle2.jpg")

    g.button("d5")
    g.unlock("2008")
    g.image("images/illustrations/2008.jpg")

    g.button("d6")
    g.unlock("choke1")
    g.image("images/illustrations/choke1.jpg")
    g.image("images/illustrations/choke2.jpg")

###################################### page 5 ######################################
    g.button("e1")
    g.unlock("camforest")
    g.image("images/illustrations/camforest.jpg")

    g.button("e2")
    g.unlock("headlights")
    g.image("images/illustrations/headlights.jpg")

    g.button("e3")
    g.unlock("duke_car")
    g.image("images/illustrations/duke_car.jpg")

    g.button("e4")
    g.unlock("catastrophic_failure1")
    g.image("images/illustrations/catastrophic_failure1.jpg")
    g.image("images/illustrations/catastrophic_failure2.jpg")

    g.button("e5")
    g.unlock("circles")
    g.image("images/illustrations/circles.jpg")

    g.button("e6")
    g.unlock("the_divide")
    g.image("images/illustrations/the_divide.jpg")
    g.image("images/illustrations/the_divide2.jpg")
    g.image("images/illustrations/the_divide3.jpg")

###################################### page 6 ######################################
    g.button("f1")
    g.unlock("the_arch3")
    g.image("images/illustrations/the_arch3.jpg")
    g.image("images/illustrations/the_arch2.jpg")

    g.button("f2")
    g.unlock("kitchen1")
    g.image("images/illustrations/kitchen.jpg")
    g.image("images/illustrations/kitchen2.jpg")
    g.image("images/illustrations/kitchen1.jpg")
    g.image("images/illustrations/kitchen4.jpg", "images/illustrations/kitchen/kitchen_camthinking.webp")
    g.image("images/illustrations/kitchen4.jpg", "images/illustrations/kitchen/kitchen_devconcern.webp", "images/illustrations/kitchen/kitchen_camthinking.webp")
    g.image("images/illustrations/kitchen3.jpg")
    g.image("images/illustrations/kitchen3.jpg", "images/illustrations/kitchen/kitchen_devfrown.webp")
    g.image("images/illustrations/kitchen6.jpg")
    g.image("images/illustrations/kitchen7.jpg")
    g.image("images/illustrations/kitchen8.jpg")
    g.image("images/illustrations/kitchen_morning.jpg")

    g.button("f3")
    g.unlock("altdev1")
    g.image("images/illustrations/altdev4.jpg")
    g.image("images/illustrations/altdev1.jpg")
    g.image("images/illustrations/altdev2.jpg")
    g.image("images/illustrations/altdev3.jpg")

    g.button("f4")
    g.unlock("artiescrib1")
    g.image("images/illustrations/artiescrib1.jpg")
    g.image("images/illustrations/artiescrib2.jpg")
    g.image("images/illustrations/artiescrib3.jpg")

    g.button("f5")
    g.unlock("maria")
    g.image("images/illustrations/maria.jpg")

    g.button("f6")
    g.unlock("realization")
    g.image("images/illustrations/realization.jpg")


###################################### page 7 ######################################
    g.button("g1")
    g.unlock("hope1")
    g.image("images/illustrations/hope.jpg")
    g.image("images/illustrations/hope1.jpg")

    g.button("g2")
    g.unlock("hope2")
    g.image("images/illustrations/hope9.jpg")
    g.image("images/illustrations/hope8.jpg")
    g.image("images/illustrations/hope2.jpg")
    g.image("images/illustrations/hope4.jpg")
    g.image("images/illustrations/hope5.jpg")
    g.image("images/illustrations/hope6.jpg")
    g.image("images/illustrations/hope7.jpg")
    g.image("images/illustrations/hope3.jpg")

    g.button("g3")
    g.unlock("something")
    g.image("images/illustrations/something.jpg")

    g.button("g4")
    g.unlock("shortstory01_01")
    g.image("images/illustrations/shortstory01_01.jpg")
    g.image("images/illustrations/shortstory01_02.jpg")

    g.button("g5")
    g.unlock("badend")
    g.image("images/illustrations/vessels/badend.jpg")

    g.button("g6")
    g.unlock("kitchen_dev1")
    g.image("images/illustrations/vessels/kitchen_dev1.jpg")
    g.image("images/illustrations/vessels/kitchen_dev2.jpg")
    g.image("images/illustrations/vessels/kitchen_dev3.jpg")
    g.image("images/illustrations/vessels/kitchen_dev4.jpg")
    g.image("images/illustrations/vessels/kitchen_dev5.jpg")

###################################### page 8 ######################################
    g.button("h1")
    g.unlock("music_room1")
    g.image("images/illustrations/vessels/music_room1.jpg")

    g.button("h2")
    g.unlock("music_room2")
    g.image("images/illustrations/vessels/music_room2.jpg")
    g.image("images/illustrations/vessels/music_room3.jpg")
    g.image("images/illustrations/vessels/music_room4.jpg")

    g.button("h3")
    g.unlock("camulation")
    g.image("images/illustrations/vessels/camulation.jpg")

############################# images for the gallery #############################


############################ gallery 1 ############################
screen gallery:
    tag menu
    use gallery_bg

    grid 3 2:
        spacing 25
        yalign 0.50
        xalign 0.50

        add g.make_button("a1","gallery/cg/cg_1.png", locked = "gallery/locked.png")
        add g.make_button("a2","gallery/cg/cg_2.png", locked = "gallery/locked.png")
        add g.make_button("a3","gallery/cg/cg_3.png", locked = "gallery/locked.png")
        add g.make_button("a4","gallery/cg/cg_4.png", locked = "gallery/locked.png")
        add g.make_button("a5","gallery/cg/cg_5.png", locked = "gallery/locked.png")
        add g.make_button("a6","gallery/cg/cg_6.png", locked = "gallery/locked.png")

    imagebutton xpos 420 yalign 0.98 idle "gallery/numbers/idle/previous.png" hover "gallery/numbers/hover/previous.png" action ShowMenu("gallery_008")
    imagebutton xpos 1225 yalign 0.98 idle "gallery/numbers/idle/next.png"  hover "gallery/numbers/hover/next.png" action ShowMenu("gallery_002")

############################ gallery 2 ############################
screen gallery_002:

    tag menu
    use gallery_bg

    grid 3 2:
        spacing 25
        yalign 0.50
        xalign 0.50

        add g.make_button("b1","gallery/cg/cg_7.png", locked = "gallery/locked.png")
        add g.make_button("b2","gallery/cg/cg_8.png", locked = "gallery/locked.png")
        add g.make_button("b3","gallery/cg/cg_9.png", locked = "gallery/locked.png")
        add g.make_button("b4","gallery/cg/cg_10.png", locked = "gallery/locked.png")
        add g.make_button("b5","gallery/cg/cg_11.png", locked = "gallery/locked.png")
        add g.make_button("b6","gallery/cg/cg_12.png", locked = "gallery/locked.png")

    imagebutton xpos 420 yalign 0.98 idle "gallery/numbers/idle/previous.png" hover "gallery/numbers/hover/previous.png" action ShowMenu("gallery")
    imagebutton xpos 1225 yalign 0.98 idle "gallery/numbers/idle/next.png"  hover "gallery/numbers/hover/next.png" action ShowMenu("gallery_003")


############################ gallery 3 ############################
screen gallery_003:

    tag menu
    use gallery_bg

    grid 3 2:
        spacing 25
        yalign 0.50
        xalign 0.50

        add g.make_button("c1","gallery/cg/cg_13.png", locked = "gallery/locked.png")
        add g.make_button("c2","gallery/cg/cg_14.png", locked = "gallery/locked.png")
        add g.make_button("c3","gallery/cg/cg_15.png", locked = "gallery/locked.png")
        add g.make_button("c4","gallery/cg/cg_16.png", locked = "gallery/locked.png")
        add g.make_button("c5","gallery/cg/cg_17.png", locked = "gallery/locked.png")
        add g.make_button("c6","gallery/cg/cg_18.png", locked = "gallery/locked.png")

    imagebutton xpos 420 yalign 0.98 idle "gallery/numbers/idle/previous.png" hover "gallery/numbers/hover/previous.png" action ShowMenu("gallery_002")
    imagebutton xpos 1225 yalign 0.98 idle "gallery/numbers/idle/next.png"  hover "gallery/numbers/hover/next.png" action ShowMenu("gallery_004")

############################ gallery 4 ############################
screen gallery_004:

    tag menu
    use gallery_bg

    grid 3 2:
        spacing 25
        yalign 0.50
        xalign 0.50

        add g.make_button("d1","gallery/cg/cg_19.png", locked = "gallery/locked.png")
        add g.make_button("d2","gallery/cg/cg_20.png", locked = "gallery/locked.png")
        add g.make_button("d3","gallery/cg/cg_21.png", locked = "gallery/locked.png")
        add g.make_button("d4","gallery/cg/cg_22.png", locked = "gallery/locked.png")
        add g.make_button("d5","gallery/cg/cg_23.png", locked = "gallery/locked.png")
        add g.make_button("d6","gallery/cg/cg_24.png", locked = "gallery/locked.png")

    imagebutton xpos 420 yalign 0.98 idle "gallery/numbers/idle/previous.png" hover "gallery/numbers/hover/previous.png" action ShowMenu("gallery_003")
    imagebutton xpos 1225 yalign 0.98 idle "gallery/numbers/idle/next.png"  hover "gallery/numbers/hover/next.png" action ShowMenu("gallery_005")


############################ gallery 5 ############################
screen gallery_005:

    tag menu
    use gallery_bg

    grid 3 2:
        spacing 25
        yalign 0.50
        xalign 0.50

        add g.make_button("e1","gallery/cg/cg_25.png", locked = "gallery/locked.png")
        add g.make_button("e2","gallery/cg/cg_26.png", locked = "gallery/locked.png")
        add g.make_button("e3","gallery/cg/cg_27.png", locked = "gallery/locked.png")
        add g.make_button("e4","gallery/cg/cg_28.png", locked = "gallery/locked.png")
        add g.make_button("e5","gallery/cg/cg_29.png", locked = "gallery/locked.png")
        add g.make_button("e6","gallery/cg/cg_30.png", locked = "gallery/locked.png")

    imagebutton xpos 420 yalign 0.98 idle "gallery/numbers/idle/previous.png" hover "gallery/numbers/hover/previous.png" action ShowMenu("gallery_004")
    imagebutton xpos 1225 yalign 0.98 idle "gallery/numbers/idle/next.png"  hover "gallery/numbers/hover/next.png" action ShowMenu("gallery_006")



############################ gallery 6 ############################
screen gallery_006:

    tag menu
    use gallery_bg

    grid 3 2:
        spacing 25
        yalign 0.50
        xalign 0.50

        add g.make_button("f1","gallery/cg/cg_31.png", locked = "gallery/locked.png")
        add g.make_button("f2","gallery/cg/cg_32.png", locked = "gallery/locked.png")
        add g.make_button("f3","gallery/cg/cg_33.png", locked = "gallery/locked.png")
        add g.make_button("f4","gallery/cg/cg_34.png", locked = "gallery/locked.png")
        add g.make_button("f5","gallery/cg/cg_35.png", locked = "gallery/locked.png")
        add g.make_button("f6","gallery/cg/cg_36.png", locked = "gallery/locked.png")

    imagebutton xpos 420 yalign 0.98 idle "gallery/numbers/idle/previous.png" hover "gallery/numbers/hover/previous.png" action ShowMenu("gallery_005")
    imagebutton xpos 1225 yalign 0.98 idle "gallery/numbers/idle/next.png"  hover "gallery/numbers/hover/next.png" action ShowMenu("gallery_007")


############################ gallery 7 ############################
screen gallery_007:

    tag menu
    use gallery_bg

    grid 3 2:
        spacing 25
        yalign 0.50
        xalign 0.50

        add g.make_button("g1","gallery/cg/cg_37.png", locked = "gallery/locked.png")
        add g.make_button("g2","gallery/cg/cg_38.png", locked = "gallery/locked.png")
        add g.make_button("g3","gallery/cg/cg_39.png", locked = "gallery/locked.png")
        add g.make_button("g4","gallery/cg/cg_40.png", locked = "gallery/locked.png")
        add g.make_button("g5","gallery/cg/cg_41.png", locked = "gallery/locked.png")
        add g.make_button("g6","gallery/cg/cg_42.png", locked = "gallery/locked.png")

    imagebutton xpos 420 yalign 0.98 idle "gallery/numbers/idle/previous.png" hover "gallery/numbers/hover/previous.png" action ShowMenu("gallery_006")
    imagebutton xpos 1225 yalign 0.98 idle "gallery/numbers/idle/next.png"  hover "gallery/numbers/hover/next.png" action ShowMenu("gallery_008")

############################ gallery 8 ############################
screen gallery_008:

    tag menu
    use gallery_bg

    grid 3 1:
        spacing 25
        yalign 0.50
        xalign 0.50

        add g.make_button("h1","gallery/cg/cg_43.png", locked = "gallery/locked.png")
        add g.make_button("h2","gallery/cg/cg_44.png", locked = "gallery/locked.png")
        add g.make_button("h3","gallery/cg/cg_45.png", locked = "gallery/locked.png")

    imagebutton xpos 420 yalign 0.98 idle "gallery/numbers/idle/previous.png" hover "gallery/numbers/hover/previous.png" action ShowMenu("gallery_007")
    imagebutton xpos 1225 yalign 0.98 idle "gallery/numbers/idle/next.png"  hover "gallery/numbers/hover/next.png" action ShowMenu("gallery")
