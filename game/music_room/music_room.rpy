################################################################################
## MUSIC ROOM DECLARATION
################################################################################
init python:
    #################### STEP 1: Set up the music room.
    ## You can make multiple music rooms consisting of different sets of tracks,
    ## if you so desire, or use one music room for all your music. You only need
    ## to pass in the name of the ExtendedMusicRoom object you set up here to
    ## the music room screens below.

    ## You can pass any of the following arguments to ExtendedMusicRoom:
    ## channel: The channel to play the music on. Defaults to 'music'.
    ## fadeout: The time in seconds to fade out the old song when changing
    ##          tracks. Defaults to 0.0 (no fade).
    ## fadein: The time in seconds to fade in the new song when changing tracks.
    ##         Defaults to 0.0 (no fade).
    ## loop: Whether to loop the music when reaching the end of the track list.
    ##       Defaults to True and can be toggled in the music room with a
    ##       button.
    ## single_track: If True, only a single track will loop. Defaults to False
    ##               and can be toggled in the music room with a button.
    ## shuffle: Whether to shuffle the tracks or play them in default order.
    ##          Defaults to False and can be toggled in the music room with a
    ##          button.
    ## stop_action: A screen action to run when the music stops. Defaults to
    ##              None, so no action is run.
    ## alphabetical : If True, the tracks will be sorted alphabetically.
    ##                If False, the default, they will be arranged in the order
    ##                they are added to the music room in.
    music_room = ExtendedMusicRoom(channel='music', fadeout=0.0, fadein=0.0,
        loop=True, single_track=False, shuffle=False, stop_action=None,
        alphabetical=False)

    ## This sets up a default art image for all tracks in this room which aren't
    ## given a more specific one. This default art is 600x600, but several
    ## layouts resize it. It should typically be square.
    music_room.default_art = "gui/music_room/cover_art.jpg"

    ## Now you can declare the music files. These will appear in the music room
    ## in the order you declare them in, unless you set alphabetical=True above.
    music_room.add(
        ## The title of the song. Used for alphabetization. Should probably
        ## be translatable.
        name=_("arches"),
        ## This should be the path to the song i.e. "audio/music/sugar_plum.ogg"
        path="audio/music/arches.ogg",
        ## The song artist. Optional; depends on how you want to set up
        ## your screens. The default layouts use the artist field.
        artist="Anthemics",
        ############ The following are more optional fields ####################
        ## This can be the path to album art specific for this song. If not
        ## provided/it is None (the default), it'll use the default_art,
        ## provided above. You can provide Null() if you'd like no image at all,
        ## not even the default.
        art="gui/music_room/cover_art.jpg",
        ## An optional extra field. You can put whatever information you like
        ## in here and display it however you want in the music room screen.
        ## By default, the screens do not display this information.
        description=_("Main menu theme"),
        ## You may optionally provide an unlock condition as a string, which
        ## will be evaluated to determine if the song is unlocked or not.
        ## In this case, the song is unlocked when the persistent variable
        ## persistent.watched_intro is True.
        ## By default, songs are unlocked when the player has listened to them
        ## in-game. You can also set this to "True" to have a song be always
        ## unlocked.
        unlock_condition="True",
    )

    music_room.add(
        name=_("soldering"),
        artist="Anthemics",
        path="audio/music/soldering.ogg",
    )

    music_room.add(
        name=_("roadside"),
        artist="Anthemics",
        path="audio/music/roadside.ogg",
    )

    music_room.add(
        name=_("unfold"),
        artist="Anthemics",
        path="audio/music/unfold.ogg",
    )

    music_room.add(
        name=_("monochrome"),
        artist="Anthemics",
        path="audio/music/monochrome.ogg",
    )

    music_room.add(
        name=_("looming"),
        artist="Anthemics",
        path="audio/music/looming.ogg",
    )

    music_room.add(
        name=_("closet"),
        artist="Anthemics",
        path="audio/music/closet.ogg",
    )

    music_room.add(
        name=_("solace"),
        artist="Anthemics",
        path="audio/music/solace.ogg",
    )

    music_room.add(
        name=_("it breathes {size=22}(from {i}Khemia{/i})"),
        artist="Anthemics",
        art="music_room/cover_art_khemia.jpg",
        path="audio/music/horror.ogg",
    )

    music_room.add(
        name=_("roots resting in the deep"),
        artist="Anthemics",
        path="audio/music/rootsrestinginthedeep.ogg",
    )

    music_room.add(
        name=_("pines"),
        artist="Anthemics",
        path="audio/music/pines.ogg",
    )

    music_room.add(
        name=_("silhouette"),
        artist="Anthemics",
        path="audio/music/sil.ogg",
    )

    music_room.add(
        name=_("still yearning"),
        artist="Anthemics",
        path="audio/music/stillyearning.ogg",
    )

    music_room.add(
        name=_("clockwork"),
        artist="Anthemics",
        path="audio/music/clockwork.ogg",
    )

    music_room.add(
        name=_("terror below the surface {size=22}(from {i}Echo{/i})"),
        artist="Anthemics",
        art="music_room/cover_art_echo.jpg",
        path="audio/music/terrorbelowthesurface.ogg",
    )

    music_room.add(
        name=_("höhlen"),
        artist="Anthemics",
        path="audio/music/hohlen.ogg",
    )

    music_room.add(
        name=_("sagebrush"),
        artist="Anthemics",
        path="audio/music/sagebrush.ogg",
    )

    music_room.add(
        name=_("zen"),
        artist="Anthemics",
        path="audio/music/zen.ogg",
    )

    music_room.add(
        name=_("amygdala"),
        artist="Anthemics",
        path="audio/music/amygdala.ogg",
    )

    music_room.add(
        name=_("lingering"),
        artist="Anthemics",
        path="audio/music/lingering.ogg",
    )

    music_room.add(
        name=_("neuron"),
        artist="Anthemics",
        path="audio/music/neuron.ogg",
    )

    music_room.add(
        name=_("submerged"),
        artist="Anthemics",
        path="audio/music/submerged.ogg",
    )

    music_room.add(
        name=_("neuroprotection"),
        artist="Anthemics",
        path="audio/music/neuroprotection.ogg",
    )

    music_room.add(
        name=_("bridges"),
        artist="Anthemics",
        path="audio/music/bridges.ogg",
    )

    music_room.add(
        name=_("when we had everything"),
        artist="Anthemics",
        path="audio/music/whenwehadeverything.ogg",
    )

    music_room.add(
        name=_("in years {size=22}(Bonus Track)"),
        artist="Anthemics",
        path="audio/music/inyears.ogg",
    )



################################################################################
## CONFIGURATION VALUES
################################################################################
## Set this to True if you want to unlock all tracks in the music room during
## development. Set it to False to test the unlock conditions. Tracks will
## automatically obey unlock rules in a distribution regardless of the value
## of this configuration variable.
define myconfig.UNLOCK_TRACKS_FOR_DEVELOPMENT = False

################################################################################
## IMAGES & DEFINITIONS
################################################################################
## These colours are used by the colorize_button transform in the screens below
## to colorize the default music controls. You can change these if you want to
## use the provided images, or simply supply your own and remove the lines
## `at colorize_button` from the screen below.
define MUSIC_ROOM_IDLE_COLOR = "#607c90"
define MUSIC_ROOM_HOVER_COLOR = "#6c90ab"
define MUSIC_ROOM_SELECTED_IDLE_COLOR = "#607c90"
define MUSIC_ROOM_SELECTED_HOVER_COLOR = "#6c90ab"
define MUSIC_ROOM_INSENSITIVE_COLOR = "#888"

## Here are the default buttons used for the music controls below. You can
## update these or replace them.
image play_button = "gui/music_room/play.webp"
image pause_button = "gui/music_room/pause.webp"
image next_button = "gui/music_room/next.webp"
image prev_button = Transform("gui/music_room/next.webp", xzoom=-1.0)
image repeat_all_button = "gui/music_room/repeat all.webp"
## Note that this image is just a foreground on top of the repeat_all button!
image repeat_one_button = "gui/music_room/repeat 1.webp"
image shuffle_button = "gui/music_room/shuffle.webp"
image back_10_button = "gui/music_room/back_10.webp"
image forward_10_button = "gui/music_room/forward_10.webp"

## The "audio level" bars. These are optional to show next to the currently
## playing song. There are four bars that randomly change height.
define AUDIO_BAR_HEIGHT = 30
define AUDIO_BAR_WIDTH = 8
image audio_bar = Transform(MUSIC_ROOM_HOVER_COLOR,
    xysize=(AUDIO_BAR_WIDTH, AUDIO_BAR_HEIGHT))
transform audio_bar_move():
    yzoom renpy.random.random() ## Start at a random height
    block:
        ## Choose a random height to be
        choice:
            ease 0.2 yzoom 1.0
        choice:
            ease 0.2 yzoom 0.2
        choice:
            ease 0.2 yzoom 0.8
        choice:
            ease 0.2 yzoom 0.0
        choice:
            ease 0.2 yzoom 0.5
        repeat
## The final audio bars image, with four bars that randomly change height.
image audio_bars = HBox(
    At('audio_bar', audio_bar_move),
    At('audio_bar', audio_bar_move),
    At('audio_bar', audio_bar_move),
    At('audio_bar', audio_bar_move),
    yalign=1.0, ysize=AUDIO_BAR_HEIGHT,
)

################################################################################
## TRANSFORMS
################################################################################
## A transform that makes it easier to apply colours to the various buttons.
## The default images are black, so it uses ColorizeMatrix to colorize them.
## The colours are defined at the top of the file.
transform colorize_button(idle=MUSIC_ROOM_IDLE_COLOR,
        hover=MUSIC_ROOM_HOVER_COLOR,
        selected_idle=MUSIC_ROOM_SELECTED_IDLE_COLOR,
        selected_hover=MUSIC_ROOM_SELECTED_HOVER_COLOR,
        insensitive=MUSIC_ROOM_INSENSITIVE_COLOR):
    matrixcolor ColorizeMatrix(insensitive, "#fff")
    on idle:
        matrixcolor ColorizeMatrix(idle, "#fff")
    on hover:
        matrixcolor ColorizeMatrix(hover, "#fff")
    on insensitive:
        matrixcolor ColorizeMatrix(insensitive, "#fff")
    on selected_idle:
        matrixcolor ColorizeMatrix(selected_idle, "#fff")
    on selected_hover:
        matrixcolor ColorizeMatrix(selected_hover, "#fff")

## A simple transform to easily resize buttons. Used by some layouts.
transform zoom_button(z):
    zoom z

## A screen that's only for development; allows you to try out the different
## layouts on each music room template. You can remove it and references to it
## once you've picked a layout.
#screen select_music_room_layout(mr, **properties):
#    frame:
#        style_prefix 'mr_layout'
#        properties properties
#        has hbox
#        xalign 0.5 spacing 20
#        textbutton "Layout 1" action ShowMenu("music_room", mr=mr)
#        textbutton "Layout 2" action ShowMenu("music_room2", mr=mr)
#        textbutton "Layout 3" action ShowMenu("music_room3", mr=mr)
style mr_layout_frame:
    background "#000000" xpadding 15 ypadding 10
style mr_layout_button:
    background None
style mr_layout_button_text:
    hover_color "#6c90ab" selected_color "#607c90"
    idle_color "#f7f7ed" insensitive_color "#666"

################################################################################
## SCREENS - VERSION 1
################################################################################
## Note! This music room gets passed in an ExtendedMusicRoom object as declared
## earlier. If you wanted to have multiple music rooms, you would need to
## declare multiple ExtendedMusicRoom objects, and you would pass those into
## the music_room screen to use.
screen music_room(mr):

    tag menu

    ## Needed to have easy access to information on the currently playing song.
    ## Required for ALL music rooms!
    ## If you'd like to begin the music room without any songs playing, remove
    ## this line and include the following three lines:
    # on 'show' action Stop(mr.channel)
    # on 'replace' action Stop(mr.channel)
    # default current_track = None
    ## Setting current_track to mr.get_current_song() as seen here will make it
    ## pick out whichever song is currently playing (e.g. the main menu track).
    default current_track = mr.get_current_song()

    style_prefix "music_room"

    add "images/backgrounds/rural_road_night_menu.jpg" ## The background image

    ## To return to the main menu
    textbutton _("Return") action Return() align (0.0, 1.0) text_size 40:
        left_margin 25 bottom_margin 25

    ## Buttons to go to the different layouts. Remove once you've decided
    ## on which layout to use.
    #use select_music_room_layout(mr, left_margin=200, align=(0.0, 1.0))

    ## The track list. These are displayed either in the order they were added
    ## to the music room in or in alphabetical order, depending on whether
    ## alphabetical sorting was turned on or not. You can arrange this however
    ## you like, with whichever information you like!
    frame:
        style_prefix 'track_list'
        xsize 850 left_margin 25 top_margin 50
        viewport:
            mousewheel True scrollbars "vertical" draggable True
            has vbox
            text "{size=50}{color=#607c90}Track List" style "music_room_title" yoffset 0
            #label _("Track List") style "music_room_title"
            ## get_tracklist takes one argument, all_tracks. If all_tracks is
            ## True, it shows all tracks, including locked ones (which will be
            ## shown grayed out). If all_tracks is False, it only shows unlocked
            ## tracks.
            for num, song in enumerate(mr.get_tracklist(all_tracks=True)):
                button:
                    action mr.Play(song.path)
                    has hbox
                    fixed:
                        if song is current_track:
                            ## If the song is currently playing, add a bit of
                            ## flair with some audio bars.
                            add Transform('audio_bars', ysize=30, xalign=0.5,
                                yzoom=-1.0, yalign=0.55)
                        else:
                            ## The track number. +1 is because enumerate starts
                            ## at 0 instead of 1.
                            text str(num+1) align (0.5, 0.55)
                    vbox:
                        spacing 4
                        ## Track info
                        label song.name
                        #text song.artist

    ## This holds the album art, song title, artist, music bar, and music
    ## controls. You may adjust this however you wish! The important part
    ## is generally the actions on the buttons, and the music bar is special
    ## so you can click it to seek in the song.
    frame:
        right_margin 45 background None
        xalign 1.0 yalign 0.2
        has vbox
        if current_track:
            add current_track.art xalign 0.5 ysize 440 fit "contain"
            text current_track.name
            #text current_track.artist
            ## Include more fields if you like e.g.
            # text current_track.description
        else:
            ## To maintain sizing, the default art is shown at alpha 0.0.
            ## You can also just include it without the alpha 0.0 to display
            ## it regardless of whether a track is playing or not.
            add mr.default_art xalign 0.5 alpha 0.0 ysize 440 fit "contain"
            text "" # This represents the space taken up by the song title
            text _("No song playing")

        hbox:
            spacing 8
            ## This fixed (and the duration one below it) ensure that the
            ## pos and duration text don't change size as the text updates
            ## (which could move the hbox around since it's center-aligned).
            fixed:
                yfit True xsize 100
                add mr.get_pos(style="music_room_pos")
            ## This makes a special music bar which shows the current position
            ## of the song, and also allows you to click the bar to skip around.
            ## It takes the same style properties as a regular bar, and in this
            ## case even gets the style "music_room_bar" because of the style
            ## prefix.
            ## It needs to be passed the music room - in our case, that's
            ## `room mr` because the music room is passed in as "mr".
            music_bar room mr
            ## Again, this fixed helps keep the hbox from changing size.
            fixed:
                yfit True xsize 100
                add mr.get_duration(style="music_room_duration")

        ## This contains the music controls. You can remove whichever ones
        ## you don't need.
        hbox:
            ################## Back 10 seconds button ##################
            imagebutton:
                idle "back_10_button"
                ## This automatically colorizes the button. If you are supplying
                ## your own images, you can remove any `at` ATL transforms to
                ## these buttons.
                at colorize_button()
                action mr.AdjustTrackPos(-10)
            ################## Shuffle button ##################
            imagebutton:
                idle "shuffle_button"
                at colorize_button(MUSIC_ROOM_INSENSITIVE_COLOR, MUSIC_ROOM_IDLE_COLOR)
                action mr.ToggleShuffle()
            ################## Previous, play/pause, next buttons ##################
            imagebutton:
                idle "prev_button"
                at colorize_button()
                action mr.Previous()
            imagebutton:
                at colorize_button()
                idle "pause_button" hover "pause_button"
                selected_idle "play_button" selected_hover "play_button"
                action mr.PlayAction()
            imagebutton:
                idle "next_button"
                at colorize_button()
                action mr.Next()
            ################## Repeat all, repeat one buttons ##################
            imagebutton:
                at colorize_button(idle=MUSIC_ROOM_INSENSITIVE_COLOR,
                    hover=MUSIC_ROOM_IDLE_COLOR)
                idle "repeat_all_button"
                if mr.single_track:
                    foreground "repeat_one_button"
                action mr.CycleLoop()
            ################## Forward 10 seconds button ##################
            imagebutton:
                idle "forward_10_button"
                at colorize_button()
                action mr.AdjustTrackPos(10)


        hbox:
            add "gui/music_room/volume.webp" zoom 0.5 yalign 0.5 xoffset -45:
                matrixcolor ColorizeMatrix(MUSIC_ROOM_HOVER_COLOR, "#fff")

            bar value MixerValue(mr.channel) xysize (400, 30):
                xalign 0.0 right_bar "#000000" thumb None yalign 0.5 xoffset -45
                left_bar "#6789a2"


################################################################################
## Styles for Music Room 1
################################################################################
image musicroombox:
    alpha 0.5
    "#000000"
style music_room_vbox:
    ycenter 0.5 spacing 25
style music_room_frame:
    background "musicroombox"
    yalign 0.5 xalign 0.0
    left_margin 25 padding (25, 25)
style music_room_text:
    color "#fff"
    xalign 0.5
style music_room_title:
    background None xalign 0.5 bottom_padding 15 top_padding 15
style music_room_title_text:
    font gui.name_text_font
    size 50 color "#607c90" xalign 0.5
style music_room_hbox:
    spacing 50 xalign 0.5 yalign 1.0
style music_room_image_button:
    align (0.5, 0.5)
style music_room_bar:
    xsize 700 xalign 0.5 ysize 38
    right_bar "#000000"
    left_bar "#6789a2"
style music_room_pos:
    color "#fff" xalign 0.5 adjust_spacing False
style music_room_duration:
    color "#fff" xalign 0.5 adjust_spacing False

################################################################################
## Styles for the track list, shared generally by the other rooms.
################################################################################
style track_list_frame:
    background "musicroombox"
    yalign 0.0 xalign 0.0
    padding (25, 25)
style track_list_viewport:
    xfill False yfill False ymaximum config.screen_height-200
style track_list_side:
    spacing 20
style track_list_vbox:
    spacing 0
style track_list_button:
    right_padding 45
    background Transform("#607c90", ysize=2, yalign=1.0)
    hover_foreground "#fff1"
    ypadding 15 xfill True
style track_list_hbox:
    xalign 0.0 spacing 18
style track_list_fixed:
    xsize 45 ysize 45 yalign 0.5
style track_list_text:
    color "#bfbfb9"
    insensitive_color "#666"
style track_list_label:
    background None padding (2, 0)
style track_list_label_text:
    color "#f7f7ed" hover_color "#6c90ab" selected_color "#607c90"
    insensitive_color "#666"
style track_list_vscrollbar:
    thumb "#6789a2" base_bar "#292835"

################################################################################
## SCREENS - VERSION 2
################################################################################
screen music_room2(mr):
    tag menu

    default current_track = mr.get_current_song()

    add "#292835" ## The background image

    ## Buttons to go to the different layouts. Remove once you've decided
    ## on which layout to use.
    #use select_music_room_layout(mr, yalign=1.0, bottom_margin=100)

    ## To return to the main menu
    textbutton _("Return") action Return() align (0.0, 1.0) text_size 40:
        left_margin 25 bottom_margin 25

    ## If you'd like to use a sidebar with this layout, you will need to indent
    ## everything in this vbox one level right and include:
    ##
    # use game_menu(_("Music Room")):
    ##
    ## See music_room3 for code you can use if you have Easy Ren'Py GUI with
    ## a sidebar.
    vbox:
        style_prefix 'music_room2' first_spacing 52
        hbox:
            ## The track list. These are displayed either in the order they
            ## were added to the music room in or in alphabetical order,
            ## depending on whether alphabetical sorting was turned on or not.
            ## You can arrange this however you like, with whichever information
            ## you like!
            frame:
                style_prefix 'track_list'
                ## If you want this to accommodate a sidebar, set the xsize
                ## smaller e.g. xsize config.screen_width-1050
                xsize config.screen_width-700
                ysize config.screen_height-250
                viewport:
                    mousewheel True scrollbars "vertical" draggable True
                    has vbox
                    label _("Track List") style "music_room_title" xalign 0.5
                    for num, song in enumerate(mr.get_tracklist()):
                        button:
                            action mr.Play(song.path)
                            has hbox
                            fixed:
                                if song is current_track:
                                    ## If the song is currently playing, add a
                                    ## bit of flair with some audio bars.
                                    add Transform('audio_bars', ysize=30,
                                        xalign=0.5, yzoom=-1.0, yalign=0.55)
                                else:
                                    ## The track number
                                    text str(num+1) align (0.5, 0.55)
                            vbox:
                                spacing 4
                                ## Track info
                                label song.name
                                text song.artist
            vbox:
                yalign 0.0
                if current_track:
                    add current_track.art xalign 0.5 xsize 550 fit "contain"
                    label current_track.name
                    text current_track.artist
                else:
                    add mr.default_art xalign 0.5 xsize 550 fit "contain"
                    label _("No song playing")

        ## The music controls
        ## This contains the music controls. You can remove whichever ones
        ## you don't need.
        hbox:
            spacing 45
            ################## Back 10 seconds button ##################
            imagebutton:
                idle "back_10_button"
                at colorize_button()
                action mr.AdjustTrackPos(-10)
            ################## Shuffle button ##################
            imagebutton:
                idle "shuffle_button"
                at colorize_button(MUSIC_ROOM_INSENSITIVE_COLOR, MUSIC_ROOM_IDLE_COLOR)
                action mr.ToggleShuffle()
            ################## Previous, play/pause, next buttons ##################
            imagebutton:
                idle "prev_button"
                at colorize_button(), zoom_button(0.65)
                action mr.Previous()
            imagebutton:
                at colorize_button(), zoom_button(0.35)
                idle "pause_button" hover "pause_button"
                selected_idle "play_button" selected_hover "play_button"
                action mr.PlayAction()
            imagebutton:
                idle "next_button"
                at colorize_button(), zoom_button(0.65)
                action mr.Next()
            ################## Repeat all, repeat one buttons ##################
            imagebutton:
                at colorize_button(idle=MUSIC_ROOM_INSENSITIVE_COLOR,
                    hover=MUSIC_ROOM_IDLE_COLOR)
                idle "repeat_all_button"
                if mr.single_track:
                    foreground "repeat_one_button"
                action mr.CycleLoop()
            ################## Forward 10 seconds button ##################
            imagebutton:
                idle "forward_10_button"
                at colorize_button()
                action mr.AdjustTrackPos(10)

        hbox:
            spacing 8
            ## This fixed (and the duration one below it) ensure that the
            ## pos and duration text don't change as the text updates (which
            ## could move the hbox around since it's changing size).
            fixed:
                yfit True xsize 100
                add mr.get_pos(style="music_room_pos")
            ## This makes a special music bar which shows the current position
            ## of the song, and also allows you to click the bar to skip around.
            ## It takes the same style properties as a regular bar, and in this
            ## case even gets the style "music_room_bar" because of the style
            ## prefix.
            music_bar room mr
            fixed:
                yfit True xsize 100
                add mr.get_duration(style="music_room_duration")
            ################## Music volume bar ##################
            null width 40
            imagebutton:
                idle "gui/music_room/volume.webp"
                at colorize_button(), zoom_button(0.45)
                hovered CaptureFocus("volume_slider_drop")
                action CaptureFocus("volume_slider_drop")

    ## This shows a volume bar popup when the volume control button is hovered
    ## or pressed.
    if GetFocusRect("volume_slider_drop"):
        default hide_volume = False
        nearrect:
            focus "volume_slider_drop" prefer_top True
            button:
                modal True
                action NullAction()
                hovered SetScreenVariable('hide_volume', False)
                unhovered SetScreenVariable('hide_volume', True)
                background None xpadding 65 top_padding 40
                bottom_padding 90 yoffset 75
                xalign 0.5 yalign 1.0
                vbar value MixerValue(mr.channel) xysize (25, 200):
                    xalign 0.5 top_bar "#000000" thumb None
                    hovered SetScreenVariable('hide_volume', False)
                    bottom_bar "#6789a2"
        if hide_volume:
            timer 1.0 action [ClearFocus("volume_slider_drop"),
                SetScreenVariable('hide_volume', False)]

################################################################################
## Styles for Music Room 2
################################################################################
style music_room2_vbox:
    xalign 0.5 spacing 20 yalign 0.5
style music_room2_hbox:
    spacing 15 xalign 0.5
style music_room2_image_button:
    align (0.5, 0.5)
style music_room2_bar:
    xsize 1050 xalign 0.5 ysize 38
    right_bar "#000000"
    left_bar "#6789a2"
style music_room2_slider:
    xsize 200 xalign 0.5 ysize 25 yalign 0.5
    right_bar "#000000"
    left_bar "#6789a2"
    thumb None
style music_room2_label:
    background None xalign 0.0
style music_room2_label_text:
    color "#f7f7ed"
style music_room2_text:
    color "#bfbfb9"

################################################################################
## SCREENS - VERSION 3
################################################################################
screen music_room3(mr):

    tag menu

    ## Needed to have easy access to information on the currently playing song.
    ## Required for ALL music rooms!
    default current_track = mr.get_current_song()

    style_prefix "music_room3"

    add HBox(Transform("#292835", xsize=350), "#000000b2") # Background

    ############################################################################
    ## If you have a standard Ren'Py UI sidebar, you can use this:
    ##
    # use game_menu(_("Music Room")):
    ##
    ## Otherwise, if you're using my Easy Ren'Py GUI (https://feniksdev.itch.io/easy-renpy-gui)
    ## you can use this:
    ##
    use game_menu(_("Music Room"))
    fixed:
        yfill True
        xsize config.screen_width-420
        align (1.0, 0.5)
    ##
    ############################################################################

        frame:
            style_prefix 'track_list'
            xfill True top_margin 25 yfill True bottom_margin 220
            viewport:
                mousewheel True scrollbars "vertical" draggable True
                has vbox
                label _("Track List") style "music_room_title"
                ## get_tracklist takes one argument, all_tracks. If all_tracks is
                ## True, it shows all tracks, including locked ones (which will be
                ## shown grayed out). If all_tracks is False, it only shows unlocked
                ## tracks.
                for num, song in enumerate(mr.get_tracklist(all_tracks=True)):
                    button:
                        action mr.Play(song.path)
                        has hbox
                        fixed:
                            if song is current_track:
                                ## If the song is currently playing, add a bit of
                                ## flair with some audio bars.
                                add Transform('audio_bars', ysize=30, xalign=0.5,
                                    yzoom=-1.0, yalign=0.55)
                            else:
                                ## The track number. +1 is because enumerate starts
                                ## at 0 instead of 1.
                                text str(num+1) align (0.5, 0.55)
                        add song.art ysize 100 fit "contain"
                        vbox:
                            spacing 4
                            ## Track info
                            label song.name
                            text song.artist

        ## This holds the album art, song title, artist, music bar, and music
        ## controls. You may adjust this however you wish! The important part
        ## is generally the actions on the buttons, and the music bar is special
        ## so you can click it to seek in the song.
        frame:
            style_prefix 'musicroom3'
            has hbox
            xalign 0.5 yalign 0.5
            if current_track:
                add current_track.art ysize 150 fit "contain"
            else:
                add mr.default_art ysize 150 fit "contain"
            vbox:
                xsize 250
                if current_track:
                    text current_track.name
                    text current_track.artist color "#bfbfb9"
                else:
                    text _("No song playing")

            null width 10

            vbox:
                yalign 0.5 spacing 15
                hbox:
                    xalign 0.5 spacing 30
                    ################## Shuffle button ##################
                    imagebutton:
                        idle "shuffle_button"
                        at colorize_button(MUSIC_ROOM_INSENSITIVE_COLOR,
                            MUSIC_ROOM_IDLE_COLOR), zoom_button(0.6)
                        action mr.ToggleShuffle()
                    ############ Previous, play/pause, next buttons ############
                    imagebutton:
                        idle "prev_button"
                        at colorize_button(), zoom_button(0.4)
                        action mr.Previous()
                    imagebutton:
                        at colorize_button(), zoom_button(0.25)
                        idle "pause_button" hover "pause_button"
                        selected_idle "play_button" selected_hover "play_button"
                        action mr.PlayAction()
                    imagebutton:
                        idle "next_button"
                        at colorize_button(), zoom_button(0.4)
                        action mr.Next()
                    ################## Repeat all, repeat one buttons ##################
                    imagebutton:
                        at colorize_button(idle=MUSIC_ROOM_INSENSITIVE_COLOR,
                            hover=MUSIC_ROOM_IDLE_COLOR), zoom_button(0.6)
                        idle "repeat_all_button"
                        if mr.single_track:
                            foreground "repeat_one_button"
                        action mr.CycleLoop()

                ################## Music Bar ##################
                hbox:
                    spacing 8
                    fixed:
                        yfit True xsize 100
                        add mr.get_pos(style="music_room_pos")
                    music_bar room mr
                    fixed:
                        yfit True xsize 100
                        add mr.get_duration(style="music_room_duration")

            add "gui/music_room/volume.webp" zoom 0.45 yalign 0.5:
                matrixcolor ColorizeMatrix(MUSIC_ROOM_HOVER_COLOR, "#fff")

            bar value MixerValue(mr.channel) xysize (150, 25):
                xalign 0.5 right_bar "#000000" thumb None yalign 0.5
                left_bar "#6789a2"


    ## Buttons to go to the different layouts. Remove once you've decided
    ## on which layout to use.
    #use select_music_room_layout(mr, align=(1.0, 0.0))

style musicroom3_hbox:
    spacing 20
style musicroom3_image_button:
    yalign 0.5
style musicroom3_bar:
    ysize 25 xsize 480
    yalign 0.5
    right_bar "#000000" thumb None
    left_bar "#6789a2"
style musicroom3_text:
    yalign 0.5 size 25 color "#f7f7ed"
style musicroom3_vbox:
    yalign 0.5
