label shortstory1:
$ quick_menu = False
stop music
stop background
pause 2.0
nvl clear
window hide
pause 1.0
$ renpy.music.set_volume(0.3, delay=3, channel=u'ambient')
play ambient wind4 fadein 6.0
pause 2.0
play ambient2 ticktock fadein 6.0
scene black with medium_dissolve
pause 2.0
scene bg forest_stormy with medium_dissolve:
    xzoom -1.0
pause 1.0
$ quick_menu = True
window show
"The first time I saw something “serious” was on the day I turned eight."
"My mom had bought me this old handheld and a few games to go with it."
"Even though it was a generation out-of-date, and all my friends had the newer version, I was still happy to have it. It was cool to just {i}own{/i} something."
"I was alone; Mom let me stay home from school that day as part of my birthday present."
"I was on this little sofa, sort of slouched down as far as I could go, practically laying my back on the seat cushion with my head propped up against it."
"I was playing this game that I can't even remember, just staring at the display."
"Then I saw this weird reflection on the plastic screen; easy to see because it didn't actually light up like the new model did."
"Anyway, there's this reflection of something really tall and dark in the corner next to me."
"All I can think is that Mom somehow hung up one of her long jackets or dresses on the floor lamp we have there."
stop ambient2 fadeout 3.0
$ renpy.music.set_volume(0.0, delay=3, channel=u'ambient')
"But that doesn't make sense, so I look up and to the right."
show black with dis3
"And then,{w=0.5} I saw it.{cps=3}..{/cps}{w=0.4} a face staring down at me."
play ambient2 darkambient01 volume 0.3
"Two yellow eyes with slit pupils,{w=0.5} no muzzle,{w=0.5} face flat,{w=0.5} and the edges of its mouth curled up in a grin.{w=0.5} Its teeth were long and sharp, all of them."
"I don't remember seeing ears,{w=0.5} I don't think it had any."
"I just know that it wasn't a person,{w=0.5} it was a thing.{cps=3}..{/cps}{w=0.4} a creature."
"The yellow eyes were standing out from the black matted fur that covered its face."
"I could only see the edges of its mouth because it had on it what I think was a raincoat, or something. There was this big collar that was turned up and covered the lower half of its face."
"And it was tall.{w=0.5} Its shoulders and the back of its head and neck were up against the ceiling, so it was looking straight down at me."
"The rest of its body was pushed back into that corner next to the sofa,{w=0.5} its arms out to the side and pressed to the walls,{w=0.5} like he's bracing himself."
"What I think were long, black claws stuck out from the openings at the ends of the sleeves, dug into the walls."
"And for the few seconds I stared up at it, it didn't move at all, not even a little bit - kind of like it was stuck in a still frame."
"It's weird to see something that you know shouldn't exist. Like, there's this extra moment where your brain absorbs what it’s seeing."
"Then instead of making you react right away,{w=0.5} like maybe seeing a spider would,{w=0.5} there's this extra beat where the brain is really analyzing it."
stop ambient2 fadeout 3.0
"Like “yep, this is really happening, and it really shouldn't be, but here it is.”"
window hide
pause 2.0
$ renpy.music.set_volume(0.5, delay=6, channel=u'ambient')
pause 2.0
hide black with leftwipefast
play ambient2 distantthunder
pause 0.5
window show
"It's hard to remember what exactly happened next. I just sort of ran, or at least scrambled on all fours trying to get the hell out of there."
"I didn't hear anything, didn't feel him move, and I was too scared to look back."
"I was tumbling out onto the wet grass, because it was cloudy and drizzling like always, and then onto the little paved walkway that wound its way through the trailer park."
"I was just running up that walkway, getting as far away from the thing I didn't understand as I could."
"What kind of fucks me up to this day, even worse than when I first saw it, is that when I was a good three trailers away, I looked back - not really expecting to see anything, but I did."
play music mines02 fadein 3.0
play sound horrorsting01
play sound2 horrorsting01
"There, framed in the little window of our trailer, was the flat-faced creature, still with the same expression, the collar still up, looking frozen in time."
"The blinds, which had always been bent and askew, were moving though - gently swaying behind its head as it grinned right at me with those yellow eyes."
"I just sat at the entrance of the park, shivering in the rain."
"After a moment, one of my neighbors rushed out of her trailer to check up on me."
"I told her that I was fine, but wasn't able to tell her why she saw me running out from my trailer, or why I couldn't go back to my trailer."
"So, she brought me into hers instead."
"I guess she thought that maybe someone broke in and scared me, because then the cops were there, then my mom was there, and I think she got into some trouble for leaving me alone."
stop music fadeout 6.0
$ renpy.music.set_volume(1.0, delay=6, channel=u'ambient')
"When the cops left, I got in BIG trouble, but I was just happy to have people around."
"Of course, I couldn't tell them what happened, because it couldn't have happened."
"But it did. And then it happened again, and again, and again..."
play sound2 windchimes fadein 7 volume 0.5
window hide
pause 7.0
stop sound2
stop ambient2
stop ambient
scene black
pause 4.0

play music sil_pre fadein 10.0
scene shortstory1nvl with medium_dissolve
pause 2.0
nvl show fast_dissolve
story "{w=1.0}They can't touch you, {w=0.7}they can't hurt you.{cps=2}..{/cps}{w=0.5} at least not in the physical way."
story "Mentally it's a different story, which makes sense because all of this is mental."
story "I was messed up waaaay before the thing that I saw in my trailer, which might explain why I saw it."
story "But it was me continuing to see it that traumatized me;{p}I never knew when I was going home to an empty trailer, or a trailer with a raincoat monster inside."
nvl clear
story "Eventually, I was able to realize that it didn't really notice me, I guess.{w} The first time it definitely wanted to make its presence known to me."
story "These days, it just kind of pops up every now and then, and it's really just a cardboard cutout of a spooky character from a horror movie."
story "Yeah, it's still startling when it's at the foot of your bed at 2 AM, but you learn to live with it."
nvl clear
play music2 silog fadein 10.0
story "Soon, the cardboard raincoat monster with claws became a man who would walk around our kitchen."
story "He was angry, {w=0.5}cursing, {w=0.5}throwing stuff around, {w=0.5}but I was okay with all of it, because he NEVER noticed me."
story "I couldn't say the same about the next thing though, and that was another flat-faced creature, but this one moved around on all fours with its elbows and legs at an angle like a spider."
story "He would crawl onto my bed, {w=0.5}over my face, {w=0.5}and whisper things at me."
nvl clear
story "That's when it really became hard, and things finally broke down after the first time I tried ketamine."
story "For most of my teenage years, I was a weed and opioid kind of guy.{w} Not like heroin, or anything, but a pill every now and then to go with the weed so I could really chill."
story "My friend, well, he loved stuff that was a bit more intense, stuff that REALLY made you feel something, or nothing at all, which is what he promised me before I took it."
story "You'll feel nothing but calm."
nvl clear
story "And then.{cps=3}.. {/cps}{w=0.4}while I was sitting in my friend's living room, {p=0.7}a bear broke through the window."
play sound sil_trans
story "He had on a ski mask{w=0.5} and he had a gun, {w=0.7}and I screamed, {w=0.5}and I ran, {w=0.7}and.{cps=2}.. {/cps}{w=0.3}I called 911."
story "And of course it wasn't real.{w} I was so out of it, actually, that I thought I was watching someone else do all of that."
nvl clear
story "I'm not friends with that guy anymore, but it was a turning point for me."
story "I knew drugs made these hallucinations worse."
story "I knew that the longer I stayed in one place, the more they appeared."
nvl clear
story "And I knew they weren't real."
story "I knew because.{cps=3}.. {/cps}{w=0.3}why was there a creature with foot-long claws in a raincoat that stood 10 feet tall?"
story "Well, {w=0.6}I'm going to bet such a thing never existed in that trailer."
story "I'm going to bet nothing like it ever existed at all."

nvl hide dissolve
scene black
with fast_dissolve
pause 2.0
stop music fadeout 8.0
stop music2 fadeout 8.0
centertext "{cps=40}I created it, {w=0.5}and it follows me,{w=0.5} and I ignore it, {p=0.7}even though it's starting to get weirdly insistent.{cps=2}.."
pause 3.0
window hide
$ fade_inout_chapter("October 2019", color="#FFFFFF", size=50)
play background roofrain fadein 6.0
pause 12
scene shortstory1front
show shortstory01_01 behind shortstory1front
show shortstory01_02 behind shortstory1front
show shortstory1back behind shortstory1front
show rain behind shortstory1front
with slow_dissolve
pause 1.0
window show
$ quick_menu = True
dev "You alright, babe?"
"Dev, somehow, already has his shirt off."
dev "Little eager, huh?"
"I don't answer the question as I slide my shirt over my head and immediately Dev's paws go to feeling out my sides."
"He's a little buzzed, so I don't think this is really going anywhere."
"We just wanted to get away from the party. We wandered around the little forest next to the house, Dev was looking for orbs or something."
"It started raining, so we ran to the car and decided to wait for Jason to come out so we could leave."
"Hopefully soon because this thing.{cps=2}..{/cps}{w=0.3} it stands outside the window."
"It's aware of us.{w=0.3} I don't like that,{w=0.3} even to this day."
dev "Is there someone out there, or something?"
window hide
scene black with fast_dissolve
pause 0.5
window show
"Dev looks behind us, right at the creature, and a chill runs down my back as he stares face-to-face with it."
"It's grinning at him with its sharp teeth, and stooped over deeply because it's too tall."
"But, as usual, Dev doesn't react. That's because he's normal."
dev "Are you seeing things again, Cam? Just because you told me it stopped doesn't mean it might not come back."
"{i}You'd really like that, wouldn't you?{/i}"
cam "Nope! {w=0.3}Things are ghost-free."
dev "Well, whatever YOU think they are. Are you seeing things again?"
"I sigh deeply."
cam "I mean,{w=0.3} it never goes away.{w=0.3} It's just better sometimes compared to other times."
"Dev rubs his bare arm, his big chest heaving, then shuddering as I run my paws up his pecs, squeezing them."
window hide
pause 0.5
play ambient2 timedthunder
scene shortstory3front
show shortstoryflash
show shortstory1back behind shortstory3front,shortstoryflash
show rain behind shortstory3front,shortstoryflash
with medium_dissolve
pause 0.5
window show
dev "I don't want to get you upset, {w=0.4}but..."
"I close my eyes, waiting to be upset. He already knows I don't like him treating me like I'm some psychic."
"I'm just a stupid kid that sees horrible, useless, things."
dev ".{cps=2}..{/cps}{w=0.5}But would you at least tell me if you see something that might... be important to me."
"I blink, thinking, then realize what, or rather who, he's talking about."
cam "Oh! {w=0.5}Well, {w=0.3}yeah, {w=0.3}of course I would.{w=0.3} It's just that I don't really see people."
cam "Just things.{w=0.3} And not good things."
"Dev has gone a bit quiet as I rub down his stomach, playing with the fur and the thick layers that come naturally to bears, something that I like."
"I feel weird doing this while waiting for our friend."
"I mean, it's our car, but we're both 25 and acting like it just can't wait, we gotta do this before we go home."
"Usually Dev just liked to be intimate like this, where he can just feel me, but he only grunts as I tentatively open his fly."
"He doesn't stop me, so I keep going."
dev "Well, you know I was supposed to visit Echo today, but Larry had some problems, or whatever, so now we're at this shitty party, and it's gonna be months before I have a chance again."
"I shrug, wanting to keep the conversation light."
cam "I've seen worse.{cps=2}..{/cps}{w=0.3} Parties, {w=0.3}I mean."
dev "Next time, I'm not bringing Larry. It's just gonna be me and whoever else wants to go."
"I nod for him to go on. Dev sighs in a frustrated way that has his chest expanding against me again."
"He pulls my paws from his crotch and he holds me, just pressing our bodies together."
dev "Obviously, I want you to go, but I don't want you to feel like some kind of tool, or something I'm just using. I think it could be a good experience for all of us."
"I stare back at him."
cam "Didn't like, ten people die, or something?"
dev "Well not that, but how things will change if we see something."
cam "And what does that mean?"
dev "That.{cps=3}..{/cps}{w=0.3} there's something more, {w=0.3}there's somewhere to go after we die."
"I think hard, trying to choose my words carefully."
cam "But how do we know that? Seeing something doesn't really mean anything. I've learned that over time."
dev "Just--"
"Dev sighs, not really annoyed, just tired, probably having a hard time thinking straight on the alcohol."
dev "I just need your help for a few days."
dev "I wanna know, {w=0.4}I need to know where she is."
"{i}{cps=30}Nowhere.{w=0.3} She's dead, {w=0.4}so she's nowhere.{w=0.3} I'm sorry.{i}"
"I don’t want to do this. It’s such a bad idea, but this is important for Dev, it always has been."
"So, now that he's finally asking me to go, I can only say:"
window hide
pause 0.5
scene black with fast_dissolve
pause 2.0
window show
cam "{cps=40}Of course."
"He grins and lets out a breath, like he's relieved."
"I had no idea he was this tense about it, though I guess my reactions to previous comments about the town told him I wasn't exactly a fan of going."
"But, {w=0.3}I can stand a few days of discomfort if Dev finds his answer, which I really, really hope he does."
dev "Thank you."
cam "No problem, man."
window hide
$ quick_menu = False
with Dissolve(0.5)
pause 2.0
centertext "{cps=30}I try not to jump, {w=0.5}because just as I said that, {p=0.5}for the first time in my life, {w=0.5}I see cardboard creature move."
stop background fadeout 3.0
stop ambient2 fadeout 3.0
play sound thunder
pause 1.0
scene white
pause 2.0
scene black with fast_dissolve
pause 7.0
return MainMenu
