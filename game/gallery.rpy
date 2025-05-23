#CG Gallery
# Codebase https://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=48056
init-1:
    #Build 1
    image no_help_1 = "images/illustrations/no_help_1.jpg"
    image no_help_2 = "images/illustrations/no_help_2.jpg"
    image lake_emma_1 = "images/illustrations/lake_emma_1.jpg"
    image lake_emma_2 = "images/illustrations/lake_emma_2.jpg"
    image lake_emma_3 = "images/illustrations/lake_emma_3.jpg"
    image closet_1 = "images/illustrations/closet_1.jpg"
    image closet_2 = "images/illustrations/closet_2.jpg"
    image closet_3 = "images/illustrations/closet_3.jpg"
    #Build 2
    image car_1 = "images/illustrations/car_1.jpg"
    image car_2 = "images/illustrations/car_2.jpg"
    image car_3 = "images/illustrations/car_3.jpg"
    image car_4 = "images/illustrations/car_4.jpg"
    image car_5 = "images/illustrations/car_5.jpg"
    image cam_lake_1 = "images/illustrations/cam_lake_1.jpg"
    image cam_lake_2 = "images/illustrations/cam_lake_2.jpg"
    image cam_lake_3 = "images/illustrations/cam_lake_3.jpg"
    image cam_lake_4 = "images/illustrations/cam_lake_4.jpg"
    #Build 3
    image blazed = "images/illustrations/blazed.jpg"
    image creepy = "images/illustrations/creepy.jpg"
    image fight1 = "images/illustrations/fight1.jpg"
    image fight2 = "images/illustrations/fight2.jpg"
    #Build 4
    image dev_window = "images/illustrations/dev_window.jpg"
    image panic = "images/illustrations/panic.jpg"
    image forest = "images/illustrations/1.jpg"
    image forest_shadow = "images/illustrations/2.jpg"
    #Build 5
    image brian = "images/illustrations/brian.jpg"
    image mirror2 = "images/illustrations/mirror2.jpg"
    image mirror3 = "images/illustrations/mirror3.jpg"
    image mirror4 = "images/illustrations/mirror4.jpg"
    image psilocybin = "images/illustrations/psilocybin.jpg"
    #Build 6
    image trailer2 = "images/illustrations/trailer2.jpg"
    image trailer3 = "images/illustrations/trailer3.jpg"
    image trailer4 = "images/illustrations/trailer4.jpg"
    image victims_4 = "images/illustrations/victims_4.jpg"
    image struggle1 = "images/illustrations/struggle1.jpg"
    image struggle2 = "images/illustrations/struggle2.jpg"
    image choke1 = "images/illustrations/choke1.jpg"
    image choke2 = "images/illustrations/choke2.jpg"
    #Build 7
    image camforest = "images/illustrations/camforest.jpg"
    image headlights = "images/illustrations/headlights.jpg"
    image duke_car = "images/illustrations/duke_car.jpg"
    image catastrophic_failure1 = "images/illustrations/catastrophic_failure1.jpg"
    image catastrophic_failure2 = "images/illustrations/catastrophic_failure2.jpg"
    image circles = "images/illustrations/circles.jpg"
    image the_divide = "images/illustrations/the_divide.jpg"
    image the_divide2 = "images/illustrations/the_divide2.jpg"
    image the_divide3 = "images/illustrations/the_divide3.jpg"
    image the_arch2 = "images/illustrations/the_arch2.jpg"
    image the_arch3 = "images/illustrations/the_arch3.jpg"
    #Build 8
    image kitchen1 = "images/illustrations/kitchen1.jpg"
    image kitchen2 = "images/illustrations/kitchen2.jpg"
    image kitchen3 = "images/illustrations/kitchen3.jpg"
    image kitchen4 = "images/illustrations/kitchen4.jpg"
    image kitchen5 = "images/illustrations/kitchen5.jpg"
    image kitchen6 = "images/illustrations/kitchen6.jpg"
    image kitchen7 = "images/illustrations/kitchen7.jpg"
    image kitchen8 = "images/illustrations/kitchen8.jpg"
    image altdev1 = "images/illustrations/altdev1.jpg"
    image altdev2 = "images/illustrations/altdev2.jpg"
    image altdev3 = "images/illustrations/altdev3.jpg"
    image altdev4 = "images/illustrations/altdev4.jpg"
    image artiescrib1 = "images/illustrations/artiescrib1.jpg"
    image artiescrib2 = "images/illustrations/artiescrib2.jpg"
    image artiescrib3 = "images/illustrations/artiescrib3.jpg"
    image maria = "images/illustrations/maria.jpg"
    image realization = "images/illustrations/realization.jpg"
    image hope1 = "images/illustrations/hope1.jpg"
    image hope2 = "images/illustrations/hope2.jpg"
    image hope3 = "images/illustrations/hope3.jpg"
    image hope4 = "images/illustrations/hope4.jpg"
    image hope5 = "images/illustrations/hope5.jpg"
    image hope6 = "images/illustrations/hope6.jpg"
    image hope7 = "images/illustrations/hope7.jpg"
    image hope8 = "images/illustrations/hope8.jpg"
    image hope9 = "images/illustrations/hope9.jpg"
    image something = "images/illustrations/something.jpg"
    #Short Stories
    image shortstory01_01 = "images/illustrations/shortstory01_01.jpg"
    image shortstory01_02 = "images/illustrations/shortstory01_02.jpg"


init python:
    #Galleries settings - start
    #list the CG gallery images here:
    gallery_cg_items = ["no_help_1","no_help_2","lake_emma_1","lake_emma_2","lake_emma_3","closet_1","closet_2","closet_3","car_1","car_2","car_3","car_4","car_5","cam_lake_1","cam_lake_2","cam_lake_3","cam_lake_4","creepy","blazed","fight1","fight2","dev_window","panic","forest","forest_shadow","brian","mirror2","mirror3","mirror4","psilocybin","trailer2","trailer3","trailer4","victims_4","struggle1","struggle2","choke1","choke2","camforest","headlights","duke_car","catastrophic_failure1","catastrophic_failure2","circles","the_divide","the_divide3","the_divide2","the_arch3","the_arch2","kitchen1","kitchen2","kitchen3","kitchen4","kitchen5","kitchen6","kitchen7","kitchen8","altdev1","altdev2","altdev4","altdev3","artiescrib1","artiescrib2","artiescrib3","maria","realization","hope1","hope2","hope9","hope4","hope5","hope6","hope7","hope8","hope3","something","shortstory01_01", "shortstory01_02"]
    #how many rows and columns in the gallery screens?
    gal_rows = 2
    gal_cols = 4
    #thumbnail size in pixels:
    thumbnail_x = 307
    thumbnail_y = 190
    #the setting above will work well with 4:3 screen ratio. Make sure to adjust it, if your are using 16:9 (such as 267x150) or something else.
    #Galleries settings - end

    gal_cells = gal_rows * gal_cols
    g_cg = Gallery()
    for gal_item in gallery_cg_items:
        g_cg.button(gal_item + " butt")
        g_cg.image(gal_item)
        g_cg.unlock(gal_item)
    g_cg.transition = fade
    cg_page=0

init +1 python:
    #Here we create the thumbnails. We use a special "locked" image for CGs to prevent spoilers.
    for gal_item in gallery_cg_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))

screen gallery():
    tag menu
    use game_menu(_("Gallery"), scroll="viewport"):
        hbox:
            style_prefix "galleryhbox"
            grid gal_cols gal_rows:
                style_prefix "galleryhbox"
                spacing 30
                xoffset 0
                yoffset 0
                $ i = 0
                $ next_cg_page = cg_page + 1
                if next_cg_page > int(len(gallery_cg_items)/gal_cells):
                    $ next_cg_page = 0
                for gal_item in gallery_cg_items:
                    $ i += 1
                    if i <= (cg_page+1)*gal_cells and i>cg_page*gal_cells:
                        add g_cg.make_button(gal_item + " butt", gal_item + " butt", im.Scale("gui/lockedCG.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=0)
                for j in range(i, (cg_page+1)*gal_cells): #we need this to fully fill the grid
                    null

            frame:
                xpos -710
                ypos 420
                background None
                if len(gallery_cg_items)>gal_cells:
                    textbutton _("Next") action [SetVariable('cg_page', next_cg_page), ShowMenu("gallery")]

style galleryhbox_button_text:
    idle_color "ffffff50"
    hover_color "c9af8f"
    selected_hover_color "c9af8f"
    selected_color "ffffff50"
