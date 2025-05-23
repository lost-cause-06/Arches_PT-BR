define config.developer = "true"

define vpunch0 = Move((0, 6), (0, -6), .10, bounce=True, repeat=True, delay=0.275)

define updisslow = ImageDissolve("images/effects/upwardwipe.png", 3.0, ramplen=256)
define updismedium = ImageDissolve("images/effects/upwardwipe.png", 2.0, ramplen=256)
define updisfast = ImageDissolve("images/effects/upwardwipe.png", 1.0, ramplen=256)
define downdisslow = ImageDissolve("images/effects/downwardwipe.png", 3.0, ramplen=256)
define downdismedium = ImageDissolve("images/effects/downwardwipe.png", 2.0, ramplen=256)
define downdisfast = ImageDissolve("images/effects/downwardwipe.png", 1.0, ramplen=256)
define dooropenslow = ImageDissolve("images/effects/openwipe.png", 3.0, ramplen=256)
define dooropenmedium= ImageDissolve("images/effects/openwipe.png", 2.0, ramplen=256)
define dooropenfast= ImageDissolve("images/effects/openwipe.png", 1.0, ramplen=256)
define leftwipe = ImageDissolve("images/effects/leftwipe.png", 1.0, ramplen=256)
define leftwipemedium = ImageDissolve("images/effects/leftwipe.png", 1.5, ramplen=256)
define leftwipeslow = ImageDissolve("images/effects/leftwipe.png", 4.0, ramplen=256)
define leftwipefast = ImageDissolve("images/effects/leftwipe.png", 0.5, ramplen=256)
define rightwipe = ImageDissolve("images/effects/rightwipe.png", 1.0, ramplen=256)
define rightwipeslow = ImageDissolve("images/effects/rightwipe.png", 4.0, ramplen=556)
define rightwipefast = ImageDissolve("images/effects/rightwipe.png", 0.5, ramplen=256)
define sunlightright= ImageDissolve("images/effects/rightcornerwipe.png", 2.0, ramplen=256)
define archtrans = ImageDissolve("images/effects/archtrans.png", 4.0, ramplen=256)

init:

    $ medium_dissolve = Dissolve(0.25)
    $ fast_dissolve = Dissolve(1.0)
    $ superfast_dissolve = Dissolve(0.25)
    $ slow_dissolve = Dissolve(3.0)
    $ slower_dissolve = Dissolve(5.0)
    $ instantdis = Dissolve (0.00)

image bs:
    "images/effects/bs.jpg"
    yalign 0.5

image glitch1 = Movie(play="images/effects/glitch1.webm", loops=0)
image glitch2 = Movie(play="images/effects/glitch2.webm", loops=0)

image brianshadow = "images/effects/brianshadow1.png"


################ Drug Trip BG #################
transform drugtriparch01:
    subpixel True
    alpha 0.2
    parallel:
        pause 0.2
        ease 7 zoom 1.05
        pause 0.2
        ease 7 zoom 0.95
        repeat
transform drugtriparch02:
    subpixel True
    alpha 0.2
    parallel:
        pause 0.6
        ease 7 zoom 1.13
        pause 0.6
        ease 7 zoom 0.87
        repeat
transform drugtriparch03:
    subpixel True
    alpha 0.2
    parallel:
        pause 1.0
        ease 7 zoom 1.20
        pause 1.0
        ease 7 zoom 0.8
        repeat
transform drugtriparch04:
    subpixel True
    alpha 0.2
    parallel:
        pause 1.4
        ease 7 zoom 1.25
        pause 1.4
        ease 7 zoom 0.75
        repeat
transform drugtriparch05:
    subpixel True
    alpha 0.2
    parallel:
        pause 1.8
        ease 7 zoom 1.5
        pause 1.8
        ease 7 zoom 0.5
        repeat

transform drugtripbg:
    subpixel True
    zoom 1.1
    xalign 0.5
    yalign 0.5
    rotate 0
    alpha 0.3
    parallel:
        ease 3 xalign 0.50
        ease 3 xalign 0.50
        repeat
    parallel:
        ease 5 rotate renpy.random.randint(1, 3)
        ease 5 rotate renpy.random.randint(-3, -1)
        repeat
    parallel:
        ease renpy.random.randint(3, 10) alpha 0.2
        ease renpy.random.randint(3, 10) alpha 0.4
        repeat
    parallel:
        ease 3 zoom 1.05
        ease 3 zoom 1.15
        repeat

transform drugtripbg2:
    subpixel True
    zoom 1.1
    xalign 0.5
    yalign 0.5
    rotate 0
    alpha 0.3
    parallel:
        ease 3 xalign 0.50
        ease 3 xalign 0.50
        repeat
    parallel:
        ease 5 rotate renpy.random.randint(1, 10)
        ease 5 rotate renpy.random.randint(-10, -1)
        repeat
    parallel:
        ease renpy.random.randint(3, 10) alpha 0.2
        ease renpy.random.randint(3, 10) alpha 0.4
        repeat
    parallel:
        ease 6 zoom 1.45
        ease 6 zoom 1.55
        repeat

transform drugtripbg3:
    subpixel True
    zoom 1.1
    xalign 0.5
    yalign 0.5
    rotate 0
    alpha 0.3
    parallel:
        ease 3 xalign 0.50
        ease 3 xalign 0.50
        repeat
    parallel:
        ease 5 rotate renpy.random.randint(3, 4)
        ease 5 rotate renpy.random.randint(-4, -3)
        repeat
    parallel:
        ease renpy.random.randint(3, 6) alpha 0.4
        ease renpy.random.randint(3, 6) alpha 0.6
        repeat
    parallel:
        ease 5 zoom 1.45
        ease 5 zoom 1.55
        repeat

################ Drug Trip 2 #################
transform drugtrip2:
    subpixel True
    zoom 1.03
    xalign 0.5
    yalign 0.5
    rotate 0
    alpha 0.3
    parallel:
        ease 3 xalign 0.51
        ease 3 xalign 0.49
        repeat
    parallel:
        ease 5 rotate renpy.random.randint(1, 3)
        ease 5 rotate renpy.random.randint(-3, -1)
        repeat
    parallel:
        ease renpy.random.randint(3, 10) alpha 0.2
        ease renpy.random.randint(3, 10) alpha 0.2
        repeat

################ Drug Trip 3 #################
transform drugtrip3:
    subpixel True
    zoom 1.03
    xalign 0.5
    yalign 0.5
    rotate 0
    alpha 0.1
    parallel:
        ease 3 xalign 0.51
        ease 3 xalign 0.49
        repeat
    parallel:
        ease 5 rotate renpy.random.randint(1, 3)
        ease 5 rotate renpy.random.randint(-3, -1)
        repeat
    parallel:
        ease renpy.random.randint(3, 10) alpha 0.2
        ease renpy.random.randint(3, 10) alpha 0.2
        repeat

################ Drug Trip 4 #################
transform drugtrip4:
    subpixel True
    zoom 1.03
    xalign 0.5
    yalign 0.5
    rotate 0
    alpha 0.4
    parallel:
        ease 3 xalign 0.51
        ease 3 xalign 0.49
        repeat
    parallel:
        ease 5 rotate renpy.random.randint(1, 3)
        ease 5 rotate renpy.random.randint(-3, -1)
        repeat
    parallel:
        ease renpy.random.randint(3, 10) alpha 0.3
        ease renpy.random.randint(3, 10) alpha 0.3
        repeat

################ Zooming #################
transform zooming:
    subpixel True
    xalign 0.5
    yalign 0.5
    alpha 0.2
    parallel:
        ease 2 zoom 1.15
        ease 1 alpha 0
        zoom 1.0
    repeat
transform zooming2:
    subpixel True
    xalign 0.5
    yalign 0.5
    alpha 0.2
    parallel:
        ease 3 zoom 1.4
        ease 1 alpha 0
        zoom 1.0
    repeat
transform zooming3:
    subpixel True
    xalign 0.5
    yalign 0.5
    alpha 0.2
    parallel:
        ease 4 zoom 1.3
        ease 1 alpha 0
        zoom 1.0
    repeat
transform zooming4:
    subpixel True
    xalign 0.5
    yalign 0.5
    alpha 0.2
    parallel:
        ease 1.8 zoom 1.2
        ease 0.5 alpha 0
        zoom 1.0
    repeat
transform zooming5:
    subpixel True
    xalign 0.5
    yalign 0.5
    alpha 0.2
    parallel:
        ease 1.7 zoom 1.2
        ease 0.5 alpha 0
        zoom 1.0
    repeat

transform zooming6:
    subpixel True
    zoom 1.02
    truecenter
    alpha 0.2
    parallel:
        ease 1.8 zoom 1.2
        ease 0.5 alpha 0
        zoom 1.0
    repeat

transform car:
    pause 0.5
    choice:
        pause 1.0
    choice:
        easeout_back 0.5 yoffset -10
        easein_bounce 0.5 yoffset 0
    choice:
        pass
    pause 0.5
    repeat

init:
    transform flip:
        xzoom -1.0
################### Chapter ###################
init python:
    def fade_inout_chapter(text, *args, **kwargs):
        ui.add(At(Text(text, *args, **kwargs), fade_chapter_2s))


transform fade_chapter_2s:
        xalign 0.5
        yalign 0.5
        alpha 0.00
        easeout_back 4 alpha 0.9
        pause 3
        ease 3 alpha 0.0

################### Chapter Title ###################
init python:
    def fade_inout_title(text, *args, **kwargs):
        ui.add(At(Text(text, *args, **kwargs), fade_title_2s))

transform fade_title_2s:
        xalign 0.5
        yalign 0.55
        alpha 0.00
        easeout_back 4 alpha 0.9
        pause 3
        ease 1 alpha 0.0
