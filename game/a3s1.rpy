label a3s1:
window hide
pause 1.0
play music neuronintro fadein 10.0 volume 0.3
queue music neuronloop volume 0.3
pause 1.0
play ambient heartbeat
show bg closed_eyes5 as original
show bg closed_eyes5 at zooming5 as extra
show bg forest_night_shadows_b at zooming5 as extra2 behind original
with medium_dissolve
pause 1.0
window show
"Pain pounds rhythmically in their head like a heavy drumbeat, making their ears pin back tightly before they begin to whine, then they croak as their sore throat protests against making the sound."
window hide
hide original
hide extra
show bg forest_night_shadows_b
with slow_dissolve
pause 1.0
window show
"They stare at the scene before them, then they blink."
window hide
show bg closed_eyes5 as extra4
with dis
pause 1.0
hide extra4
show bg forest_night_shadows_b
with dis
pause 1.0
window show
"But it doesn't help them make sense of what's in front of them."
"In fact, it seems to make it worse."
"{i}Who's making sense of what that's in front of who?{/i}"
"These intrusive thoughts about not existing."
"{i}Who's having these thoughts?{/i}"
window hide
stop ambient fadeout 6.0
hide bg forest_night_shadows_b
show bg forest_night_shadows_a
hide extra3
hide extra2
hide extra
with medium_dissolve
pause 0.5
show bri neutral red3 at left
show expression AlphaMask("foliage3", At("bri neutral red3", left)) as mask
with dissolve
window show
b "\"See? You're comin' 'round.\""
hide mask
hide bri
with dissolve
"Fear rises up into his throat, something deep in his brain telling him to flee that voice, to escape from it."
"But he's still too confused to figure out who or what he even is right now, because he still feels like nothing."
"But he's also still conscious enough to know that he is, in fact, something."
window hide
play ambient heartbeat
show camforest
show bg forest_night_shadows_b at zooming5 as extra2 behind camforest
show camforest at zooming5 as extra
with medium_dissolve
pause 1.0
window show
"He remembers that he's someone named Cameron."
"He remembers his situation, and he remembers that he's been drugged with shrooms and Xanax."
"His trip has reached its dizzying peak, his sense of self so utterly decimated that he isn't sure how he's ever going to feel the same again."
"The terror and torture of the past two days has culminated to this, the moment that his mind gives in and breaks, and Cameron can't tell what's real and what isn't anymore."
"... But there's something else, too."
"Despite the terrible loss of who he was, Cameron, this amalgamation he calls Cameron, is sensing things even more vividly than he had just a few minutes ago, when he'd contacted Dev."
"Cameron sees what's ahead of him, but he's seeing so much more."
hide camforest
hide extra
hide extra2
show bg hollow_visions
show bri evilgrin red at left:
    xoffset -150
show brianshadow2 at left:
    xoffset -150
show black as temp behind bri:
    alpha 0.6
show dev angry s red at center:
    flip
    xoffset 200
show devshadow at center:
    xoffset 200
show cam horror red at twelve
show camshadow at twelve
show blood08:
    alpha 0.5
with dis3
"In his mind's eye, he looks {i}forward{/i}, and he sees a myriad of people in front of him, though they're all the same people: Devon, Brian, and himself, locked in a vicious, spinning blur of claws and teeth, blood and horrific, unidentifiable viscera."
show black
with dis2
"It's confusing, seeing so many versions of himself and his boyfriend, and he turns his head to glance away, not wanting to see that violence."
hide bg hollow_visions
hide black
hide bri
hide dev
hide cam
hide camshadow
hide devshadow
hide brianshadow2
hide blood08
show bg forest_night_shadows_a behind extra2:
    zoom 1.02
    truecenter
show bri evilgrin red3 at left
show brianshadow2 at left
show expression AlphaMask("foliage3", At("bri evilgrin red3", left)) as mask
show cam horror red3 at center
show camshadow at center
show expression AlphaMask("foliage3", At("cam horror red3", center)) as mask2
show blood08:
    alpha 0.5
hide black
with dis2
"Then, noticing something over his shoulder, he looks {i}back{/i}, and this time he sees one version of himself, along with Brian."
"He sees his unconscious body being pinned against the tree for a while longer before he crumples to the ground."
window hide
pause 0.5
stop ambient fadeout 6.0
scene bg forest_night_shadows_a:
    zoom 1.02
    truecenter
with medium_dissolve
pause 0.5
window show
c "\"What the hell?\""
show cam sad_alt red3 at right
show expression AlphaMask("foliage3", At("cam sad_alt red3", right)) as mask2
with dissolve
"His voice is low, husky, and barely audible."
"Brian laughs, startling the coyote out of his visions of violence."
show bri evilgrin red3 at left,jumping
show expression AlphaMask("foliage3", At("bri evilgrin red3", left)) as mask at jumping
show cam shocked red3 at jumping
show expression AlphaMask("foliage3", At("cam shocked red3", right)) as mask2 at jumping
b "\"I choked you the fuck out, that's what!\""
show cam worried_alt red3
show expression AlphaMask("foliage3", At("cam worried_alt red3", right)) as mask2
with dis
"Cameron blinks at the bear, then back at the forest."
c "\"I thought I died.\""
show bri smirk2 red3
show expression AlphaMask("foliage3", At("bri smirk2 red3", left)) as mask
with dis
b "\"Heh, not yet, kid. We got a few things to do first, and you probably wanna see your boyfriend too, eh? Not sure you'll get to talk to him since he's knocked out.\""
show cam confused a red3
show expression AlphaMask("foliage3", At("cam confused a red3", right)) as mask2
with dis
c "\"Knocked out?\""
show bri smirk red3
show expression AlphaMask("foliage3", At("bri smirk red3", left)) as mask
with dis
b "\"Yep.\""
show cam scared red3
show expression AlphaMask("foliage3", At("cam scared red3", right)) as mask2
with dis
c "\"Wait, with what?\""
show bri smirk2 red3
show expression AlphaMask("foliage3", At("bri smirk2 red3", left)) as mask
with dis
b "\"Relax, It's just Rohypnol. Sure, I gave him a good amount, but they're a few decades old because they made 'em illegal in the States back in the 90s, and you know, when pills get old, they don't work so good anymore--\""
"Brian goes on and on about Rohypnol and how it used to be the premiere date rape drug in the country."
show cam serious a red3
show expression AlphaMask("foliage3", At("cam serious a red3", right)) as mask2
with dis
"Cameron watches the bear's mouth move in waves and ripples, yellow teeth poking out from behind his lips as saliva collects and becomes frothy at the corners."
"{i}Who's watching this?{/i}"
"Cameron reassures himself automatically."
"I'm {i}watching this, and{/i} I {i}need to save Devon.{/i}"
"He's not so convinced by the first part, though."
window hide
show forest_night_shadows_b as extrabg:
    zoom 1.02
    truecenter
show black:
    alpha 0.6
with fast_dissolve
pause 1.0
centertext "I."
centertext "Me."
centertext "Cameron."
centertext "Simple concepts that aren't so simple anymore."
centertext "Just like in high school, he's stopped existing."
centertext "It's different this time, though."
centertext "The Xanax is certainly quashing the panic he should be feeling right now, but this time, his perspective is from a completely different angle."
centertext "Cameron's amalgamation does still exist, but the borders have dissolved, and he seems to be seeping into everything."
centertext "Despite already knowing he's insignificant, he's still\n awestruck by how small 'Cameron' is compared to the world."
centertext "Even the bugs crawling beneath the leaves make Cameron\n feel small; an entire world he knows nothing about."
centertext "But entangling his identity with the universe\n means he's also entangled with Brian."
centertext "The bear is missing parts of himself, kind of like Artie, shattered\n pieces and jagged holes pockmarking the landscape of his life."
centertext "Cameron almost feels sorry for him, that maybe if things had\n been just a little different, the odds just a little more in Brian's favor,\n he could have been a very different person."
pause 1.0
hide black
hide extrabg
with fast_dissolve
window show
"What's really disturbing though, is the genuine affection he has for Cameron, his urge to caress and hold the coyote, but..."
"There's a hatred there too, a disgust for what Cameron is."
"Young, attractive, and a fag..."
"Not just {i}queer{/i} like Brian considers himself to be, but a faggot."
"The kind of queer that acts real cute before fucking over the real men who should be doing all the fucking."
"So it feels good to punish Cameron, but it's even better to watch him suffer, to watch the way his body writhes, his mouth open for air, his eyes wide and fearful."
"Cameron feels himself recoil from understanding Brian's thought process, a way of thinking he'd never consider himself."
"But that thought process isn't what makes Brian the terrible person that he is."
"Cameron knows that most don't have a say in how their sexual interests and fetishes develop, so the thoughts themselves aren't exactly evil, at least not to Cameron."
"Cameron knew a few guys from college who had interests similar to Brian."
"During his first year of dating Devon, the bear had timidly asked him if he could gently close his teeth over the coyote's neck and growl."
"It was thrilling and intense, and Cameron loved the rush."
"But then Devon had a nightmare about tearing out Cameron's throat, and that was the end of that."
"So, to Cameron, Brian isn't all that strange."
"What makes Brian different isn't that he has fetishes."
"He's not crazy."
"He's not a psychopath."
"No, the true root of Brian's evil is clear."
"He's selfish, and he's never satisfied with what he gets."
"Selfish enough to put dozens of young people through hellish torture until they finally died."
"All while having the capacity to fully control himself."
"All while having full access to alternatives like role-play."
"But it's not enough for Brian."
"He always needs more."
"All for his own fleeting, drug-fueled, sexual gratification because at one point, Brian decided that's what makes him feel good, so fuck this world that makes him feel bad."
"But he'd found some release in strangling Cameron, and now his focus is turning back to a vague idea on how to use Cameron's abilities."
"Something to stop him from spending the rest of eternity with his victims torturing him."
"Cameron could spoil the ending for Brian, let him know that when everyone dies, they just cease to be what they were."
"That's it."
"Ghosts, demons, poltergeists?"
"Creations of the living... and whatever it is that's in Echo."
show cam worried a l red3
show expression AlphaMask("foliage3", At("cam worried a l red3", right)) as mask2
with dis
"Cameron draws back at this point, getting overwhelmed by all the thoughts coming from the old bear, unable to understand them without more context."
show cam worried_alt red3
show expression AlphaMask("foliage3", At("cam worried_alt red3", right)) as mask2
with dis
"Looking {i}forward{/i}, he glimpses the various scenarios again, and the one constant is death."
"Most involve him dying, and a good amount involve Devon dying as well."
"Cameron imagines that this is indicative of what's most likely to happen."
"But a few, just two, in fact, show Cameron and Devon surviving, with Brian either living or dying."
"Cameron doesn't care much about the latter, just as long as he can get Devon and himself out of Echo alive."
"They can deal with Brian afterwards."
"Cameron doesn't even care much if he doesn't make it, especially in this state of mind, but he won't accept not being able to save Devon."
"Suddenly remembering what he had done earlier, Cameron tries to subtly brush his pocket, and is amazed that the key is still there."
show cam worried a red3
show expression AlphaMask("foliage3", At("cam worried a red3", right)) as mask2
with dis
"Does Brian know?"
"Well, he does know what Cameron had planned, but in his own excitement, and especially because he's tweaked out, he's hyper-focusing on other things."
"He'd also missed the key being taken out of his pocket."
"That, and Brian's memory is terrible."
"Decades of drugs at neurotoxic doses had dismantled who he used to be."
"He doesn't even seem to remember why he choked Cameron in the first place."
show bri smirk2 red3
show expression AlphaMask("foliage3", At("bri smirk red3", left)) as mask
with dis
b "\"...had to make connections down in Sonora. Stuff was over-the-fucking-counter there, so it was easy to get, but getting it over-the-fucking-border is a whole different issue--\""
show bri serious red3
show expression AlphaMask("foliage3", At("bri serious red3", left)) as mask
with dis
"Brian suddenly stops talking, eyes narrowing."
"Cameron's pulse quickens as he wonders if Brian had just remembered his plan."
stop music fadeout 10.0
play ambient crickets fadein 10.0
show cam surprised a red3
show expression AlphaMask("foliage3", At("cam surprised a red3", right)) as mask2
with dis
c "\"What's wrong?\""
"His voice is still rough from the strangling, a deep soreness starting to emanate from the core of his neck."
b "\"I dunno, I just like you better when you're smilin', but if I'm fuckin' borin' ya, just say so.\""
"It takes Cameron a few seconds to understand what Brian is even talking about, then a few more to scan the bear's thoughts."
"In Brian's mind, his smiling has a lot to do with how interesting the bear's over-explanation of Rohypnol is, so Cameron quickly puts one on his face."
show cam smile c red3
show expression AlphaMask("foliage3", At("cam smile c red3", right)) as mask2
with dis
play music zen fadein 5.0 volume 0.2
c "\"Oh, sorry, it is really interesting. I'm just so overwhelmed with the drugs and--\""
show bri angry red3
show expression AlphaMask("foliage3", At("bri angry red3", left)) as mask
with dis
b "\"Shut up.\""
show cam worried a red3
show expression AlphaMask("foliage3", At("cam worried a red3", right)) as mask2
with dis
"Cameron shuts up."
"Brian starts to work his jaw, like he's chewing something, before clenching his fists."
show bri angry fists red3
show expression AlphaMask("foliage3", At("bri angry fists red3", left)) as mask
show cam horrified red3
show expression AlphaMask("foliage3", At("cam horrified red3", right)) as mask2
with dis
"Cameron tenses up, preparing himself to be hit again."
b "\"You're cute, but not that cute, and I'm not that stupid. I hate fags like you, sucking up and sucking dick so you get what you really want.\""
"Brian's mind flicks through a few faces, but the only one defined enough for Cameron to comprehend is a fox in a red hat."
"Then Brian seems to relax, but the anger is still there, the bear having honed it to become more cool and collected, which only makes it all the more terrifying."
"Sure, stimulants increase empathy in a normal brain, but if Brian abused them to the point that amphetamines feel like caffeine, then it probably only increases his irritability and rage."
"That's what his mother was like at the end, and it always confused Cameron as to why someone would want to do a drug that makes them feel worse."
b "\"I got a better idea.\""
window hide
show cam scared red3
show expression AlphaMask("foliage3", At("cam scared red3", right)) as mask2
with dis
pause 0.5
hide bri
hide cam
hide mask
hide mask2
with vpunch
window show
"Cameron gasps as Brian grabs him by the ear."
c "\"No, no! Stop, I can walk with you.\""
c "\"I won't try to run--{w=0.4}{nw}"
extend" OW!\"" with vpunch
"Cameron senses the bear's amusement at his fear of being pulled up by his ear again, and the coyote quickly stifles his begging, realizing it might shift Brian's interests back to using Cameron for torture rather than his abilities."
"The pain had been blinding, but it's nothing, absolutely nothing compared to what this bear has done to others."
"Cameron manages to settle into a stumbling walk as Brian pulls him along, bent over and trying to see the ground in the darkness, all while he tries to carefully follow the bear's rough, unpredictable movements."
"Every minute or so, Cameron looks {i}forward{/i}, and sees the scenario he's aiming for, still within reach, so he keeps walking."
"Meanwhile, a van emerges from the trees, parked a ways off the side of the road."
show bri horror red3 at left
show expression AlphaMask("foliage3", At("bri horror red3", left)) as mask
with dissolve
"Brian freezes, staring."
"Then he lets out a surprised laugh."
stop music fadeout 10.0
show bri evilgrin red3
show expression AlphaMask("foliage3", At("bri evilgrin red3", left)) as mask
with dis
b "\"Well, I'll be damned. The fucker got away!\""
show cam confused c red3
show expression AlphaMask("foliage3", At("cam confused c red3", center)) as mask2
with dis
c "\"Who?\""
"The coyote winces as Brian continues to hold him by his ear."
"Cameron hopes that he's talking about Devon, even though he can sense the presence of the younger bear just ahead of them."
"The coyote would be glad to be proven wrong about his abilities, especially if it means Devon gets away."
"But Cameron knows."
show bri evilgrin3 red3
show expression AlphaMask("foliage3", At("bri evilgrin3 red3", left)) as mask
with dis
b "\"That cat! I swear I shot him twice, too. Then again, he didn't do that weird jerking thing people do when you give 'em the kill shot, so I must've missed the second time.\""
b "\"Thought maybe I'd just killed him with the first.\""
show cam worried_alt red3
show expression AlphaMask("foliage3", At("cam worried_alt red3", center)) as mask2
with dis
"Cameron looks where Brian is staring, and sees the spot where Arturo must have been."
show cam sad red3
show expression AlphaMask("foliage3", At("cam sad red3", center)) as mask2
with dis
"Dark stains cover the leaves, along with what looks like vomit, and Cameron feels his own stomach churn at the sight."
"It's difficult to connect his outgoing, oblivious friend to the mess, and Cameron feels guilt mingle with his misery as he realizes that what's happening to Artie is their fault."
"But he knows Artie is far away now, miles away, and Cameron silently encourages the cat to keep going, to do whatever he can to save them and himself, even though he's clearly in terrible shape."
"Cameron hopes Artie can hear him, even if he's awake right now."
show bri lookdown red3
show expression AlphaMask("foliage3", At("bri lookdown red3", left)) as mask
with dis
"Cameron senses another ominous shift in the bear's motivation."
"Brian doesn't think that Artie will make it to the interstate, and he knows he should go looking for the cat."
"But everything is so fucked from the start: three young men who likely have close family and friend groups, all three of them injured, and beaten, and all three knowing full well what Brian is capable of..."
"There's no point to it anymore."
"Brian had almost reverted to thinking he'd get away with all of this somehow, but no."
"This is the end."
show bri neutral red3
show expression AlphaMask("foliage3", At("bri neutral red3", left)) as mask
with dis
b "\"Well... Guess that's it, then. Figured it was gettin' close for a while now. Kinda knew that when I left the kid's phone ringin' in my trailer.\""
show cam worried a red3
show expression AlphaMask("foliage3", At("cam worried a red3", center)) as mask2
with dis
"The calm with which Brian accepts his nearing demise makes Cameron want to try to escape all over again."
"Why can't this bear just end it without taking them down with him?"
"It's the end for him, not them."
show cam smile a red3
show expression AlphaMask("foliage3", At("cam smile a red3", center)) as mask2
with dis
c "\"Can I see Devon?\""
"Cameron half-heartedly smiles, hoping it might sway the bear, but he's not paying attention to the coyote."
"Brian shakes his head at the sober version of himself, the version that actually did plan to let Cameron go, because why would he add to his problems by killing the yote if said yote could take them all away?"
"That's why he'd tried to be nice to him, and then of course things got out of hand."
"Cameron begins to shake as he senses Brian's arousal and excitement."
"He's thinking about Cameron, about his baggie full of bath salts, and about how long it might take to find them in--"
show cam scared red3
show expression AlphaMask("foliage3", At("cam scared red3", center)) as mask2
with dis
stop music fadeout 10.0
"Cameron blanches mentally, unsure of what that dark place full of death is, but he knows he does not want to go there."
c "\"Where are you taking me?\""
show bri angry red3
show expression AlphaMask("foliage3", At("bri angry red3", left)) as mask
with dis
b "\"You're the psychic. Figure it out.\""
hide bri
hide mask
hide mask2
hide cam
with dissolve
"Keeping his hold on the coyote, Brian pulls Cameron toward the van."
window hide
pause 0.5
scene black with medium_dissolve
pause 1.0
play music lingeringintro fadein 15.0 volume 0.3
queue music lingeringloop volume 0.3
scene bg outskirts_night with medium_dissolve
pause 0.5
window show
"It isn't long before Artie realizes that the lights along the interstate are actually a lot farther away than he had thought."
"He has no idea how long he's been walking, but it feels like at least an hour, and the road is maybe just a little closer."
"At this point, he's so weak, his movements so uncoordinated, that deep down, he knows his body is about to give up."
"Every dizzy spell, every wave of anxiety, it terrifies the cat that he might have another seizure, and if he does, he knows he won't be getting back up."
c "\"{i}Artie, please...{/i}\""
a "\"C-c-cam?\""
"Artie looks around hopefully."
"He'd probably start crying right now if Cameron just showed up, if only because he wouldn't be alone anymore."
"But then Artie sees a pair of headlights closer than the others."
"And it gets closer and closer."
"Artie notes that the lights are coming right toward him, and he doesn't bother getting off the road, feeling like this must be a light-at-the-end-of-the-tunnel situation."
window hide
pause 0.5
play background engine fadein 5.0
show headlights with medium_dissolve
pause 0.5
window show
"And then the lights slow and Artie hears the sound of an engine."
unk "\"What the FUCK are you doing standing there like a fucking IDIOT on the fucking ROAD!\""
"Artie's ears twitch, recognizing the voice from somewhere in his past, in what might as well be another life."
"It's hard to tell because they're screaming at him."
play sound cardoor3
"A car door opens and Artie just stands there, lost in the light."
unk "\"I told you guys to fuck off! First the fuckin' bar is closed because of some fuckin' cold, and now you're still here to fuck with me? I just wanna {i}cunting{/i} drink to {i}cunting{/i} relax!\""
"Arturo furrows his brows, never having heard that particular word used in such a way."
"A figure starts to materialize in front of Arturo, and finally, he recognizes him."
window hide
pause 0.5
scene duke_car
with medium_dissolve
pause 0.5
window show
Weasel "\"What happened to you?\""
"The weasel stares at him, then tilts his head to the side, squinting before reaching out and turning Arturo slightly by the shoulder."
#show duk angry dark with dis
Weasel "\"Shit, there's no way! He couldn't be that fucking...\""
"The weasel trails off, then looks at Artie's face."
Weasel "\"Who did this?\""
"Artie reluctantly opens his mouth, for some reason feeling almost embarrassed about his condition."
a "\"B-b-b-baaar...\""
"The weasel stares at him with an odd look."
#show duk neutral dark with dis
Weasel "\"Bar? Yeah, I was at the bar. It's closed.\""
a "\"B-b-bear.\""
#show duk angry dark with dis
Weasel "\"Bear? Brian?\""
"Arturo nods and regrets it immediately as he almost falls over."
#show duk neutral dark with dis
Weasel "\"Damn, you're real fucked up aren't ya?\""
"Arturo stares back at the weasel and notices his expression, like he's trying to decide something."
"It's not the right reaction to the situation, and Artie suddenly feels like he might be in danger, but he has no idea why."
"All he remembers is that this old man had floored Devon with two swings, so combined with his current state, he can't do a thing."
"Then, the weasel seems to come out of whatever it is he was thinking about."
#show duk smirk dark with dis
Weasel "\"Well, I'll be damned. This is it, then, isn't it? That stupid motherfucker. All right, get in. We're going to the hospital.\""
#hide duk with dissolve
show duke_car2 with dis2
"Arturo stumbles forward, and once the weasel realizes he's having trouble moving at all, he helps Arturo inside."
"As he does, the weasel sucks in a breath, grimacing."
Weasel "\"Jesus Christ, this is really makin' me not wanna do what I'm gonna have to do after this. But ya know, everything's gotta end eventually.\""
"Arturo isn't sure what the old weasel is talking about, but if he's taking him to the hospital, then he's at least on the right track."
a "\"F-f-f-free end...F-f-friends.\""
Weasel "\"Yeah, yeah, I'll call Payton PD... once I drop ya off. Gotta make sure I can beat 'em back, though.\""
"Arturo decides that it's the weasel who's acting strange."
"But, as the strange weasel starts to make a three-point turn to drive back toward the interstate, Arturo is only grateful."
stop background fadeout 7.0
stop music fadeout 10.0
"He's done what he can, and now the rest is up to God."
"He can only pray."
"So he prays for Devon, Cameron, Maria, and himself, because if he survives, he knows the road in front of him is long, fractured, and broken."
window hide
stop ambient fadeout 6.0
pause 0.5
scene black with medium_dissolve
pause 0.5
play background roughdrive fadein 10.0
pause 1.0
scene van_night at car with medium_dissolve:
    zoom 1.02
    truecenter
pause 1.0
window show
"Devon feels his body bouncing and shaking on a hard, metallic surface, occasionally leaning from side to side, feeling like he's lying down in a car taking sharp turns."
"The bear opens his eyes, groaning."
c "\"Dev?\""
d "\"Nnh, Cam?\""
"Is Cameron driving?"
"The coyote has his own sedan that he drives, but usually if they're out together, it's in Devon's jeep."
"At first, he thinks maybe he's given the wheel to the coyote so that he himself can get some rest, but they came in the Jeep, and Cameron can't drive standard, right?"
"{i}Come on, stop assuming things{/i}."
"Lately, Cameron seems to bristle whenever he does."
"Lately, as in ever since they got to Echo."
c "\"Devon? I'm here. How are you doing?\""
"Cameron's concerned, gentle voice is clearly masking something strained and desperate underneath."
d "\"Cameron? Whu-Wha's it? Wha's wrong?\""
b "\"I told you, he's all drugged up.\""
c "\"But he can barely talk.\""
d "\"Cam?\""
b "\"Exactly, I already told you I roofied him. It's like blacking out. Anyway, it's wearing off. He's just tired.\""
c "\"Is that blood?{w=0.3} Why is he bleeding!?\""
b "\"Did it to himself. Imagine what a mess we'd have if he wasn't drugged, right? Never trust a bear to stay put when you chain 'em up.\""
c "\"Devon, can you hear me? Are you okay?\""
d "\"Yeah, yes...\""
window hide
scene bg black with medium_dissolve
stop background fadeout 6.0
window show
"Then, he's drifting back to sleep again."
"More sounds of driving on a rough road, gravel grinding under wheels and hitting the undercarriage."
window hide
play ambient crickets fadein 5.0
scene van_night with medium_dissolve:
    zoom 1.02
    truecenter
pause 1.0
window show
"When he comes to again, it's stopped and Devon realizes the van doors are open."
b "\"Looks like it did wear off just in time.\""
c "\"Can I go to him... Please?\""
"Devon sees that one of Cameron's ears is twisted in the older bear's grasp, the coyote's head tilted to the side, wincing as he tries to get a better look at Devon."
"The younger bear becomes very still, seeing his best friend being held by the worst person he's ever met."
"One of his soft, sensitive ears that Devon had played with countless times in the past is now twisted tightly onto itself."
"In Brian's other paw, he holds a shotgun."
"On top of it all, Brian looks angrier than usual."
"In fact, he's looking at Cameron with an expression of utter contempt, all while Cameron isn't paying attention to him, looking intently at Devon instead."
b "\"Of course. Fuckin' typical. I'm glad I saved this.\""
"He suddenly grabs the coyote by the shoulders and turns Cameron around to face him, to face away from Devon."
"Even so, there's no confusion as to what happens to Cameron next."
"Brian turns slightly away from Cameron, then spins and sends the back of his fist across the coyote's muzzle."
window hide None
play sound "<from 0.11>sounds/punch.ogg"
with vpunch
stop ambient
play music solderingloop fadein 5.0 volume 0.3
pause 0.5
window show
"The sound is so loud Devon is shocked awake, adrenaline compensating for the sedative."
"At first, Devon refuses to believe what he just saw, that a sound like that could have been made with Cameron's muzzle."
"The coyote's head snaps to the right before he instantly starts to crumple, but Brian holds him up."
d "\"Hey!\""
"Devon yells automatically, shocked by what he just saw."
"He'd never seen someone hit that hard in his entire life."
"In the silence that follows, the distinct sound of something small clatters around the van, as if a plastic bead had been thrown against the metal walls."
"Devon hears it land next to him, and looking down, he sees something long spinning in place before finally coming to a stop."
"It's thin, white, and it starts wide, but tapers to a sharp point."
"Devon only has a moment to focus on it before he grunts as Cameron lands on top of him, Brian having pushed him over."
play sound thud
scene catastrophic_failure1:
    zoom 1.02
    truecenter
"As he's looking down at the coyote and sees the blood beginning to seep from his mouth, Devon realizes the white thing is one of Cameron's teeth, and shocked anger overcomes the fear." with vpunch
scene catastrophic_failure2 with dis:
    zoom 1.02
    truecenter
d "\"HEEEEEY!\""
"All sense has seemingly left Devon, everything he's feeling and thinking condensing down to that one word that he screams to express his rage."
scene catastrophic_failure1 with dis:
    zoom 1.02
    truecenter
d "\"Cam?{w=0.3} CAM!\""
"Panic is making him breathe fast, though he tries to keep his chest from heaving to avoid bouncing Cameron's head."
"Brian had hit him so hard that it definitely could have killed him."
"What makes it all the more terrifying is the way Cameron's body went limp."
"It had been so reminiscent of Artie's sudden collapse when he had suddenly lost his life."
"But Cameron is breathing, though it's in a terrible, snorting way."
d "\"Cammy, baby, can you hear me?\""
"The panic in his voice lowers to an almost pitiful whine as he stares at the coyote twitching, his eyes half open and his head turning back and forth slowly."
b "\"Whoops, took out a bit more on him than I meant to, heh. Fuck, that hurt!\""
"Brian shakes the paw he'd used to hit Cameron, as if bashing Cameron's muzzle made it sting."
"Devon's rage crescendos once more."
scene catastrophic_failure2 with dis:
    zoom 1.02
    truecenter
d "\"BRIAN!{w=0.3} I will fucking kill you!\""
"Brian looks surprised for just a second, then he goes on grinning, enjoying the reaction, as if he's watching a show."
"This only makes Devon angrier."
d "\"I'll knock every tooth out of your fucking head! I'll tear your throat out, I'll-- I'll...\""
"Devon's voice weakens, breaks, then trails off under Brian's apparent glee at the younger bear's fury."
stop music fadeout 10.0
play ambient crickets fadein 10.0
"Realizing that Cameron's ears are twitching at his shouting, Devon returns his attention to Cameron as the coyote lets out a low, rasping groan."
scene catastrophic_failure1 with dis:
    zoom 1.02
    truecenter
d "\"Cameron, honey, you can hear me, right? Cameron?\""
"Meanwhile, blood oozes out of the coyote's nose and mouth, seeping into the fur on Devon's stomach and side."
"Devon tries to keep his sobbing and gasping to a minimum as Cameron's head continues to rest over his diaphragm."
"Cameron's eyes flutter, then he blinks, and Devon sees the light of consciousness re-enter his eyes."
d "\"Cam!\""
c "\"... Devon?\""
#NOTE: SONG EDIT
play music sagebrushcut fadein 20.0 volume 0.3
"Cameron grunts under his breath, lifting his head slightly."
"Brian already looks bored at the catastrophe he just created, and now he keeps looking over his shoulder into the darkness that stretches behind him, shifting impatiently."
b "\"Alright, make it quick, yote. We need to get movin'.\""
scene catastrophic_failure2 with dis:
    zoom 1.02
    truecenter
d "\"Don't you touch him!{w=0.3} You could have broken his fucking neck!\""
"Devon's voice cracks and turns hoarse again."
scene catastrophic_failure1 with dis:
    zoom 1.02
    truecenter
"Brian bristles, finally reacting, but Devon turns his attention back to Cameron, continuing to try and gently coax him into a state of consciousness."
d "\"Come on, baby, can you hear me? Can you understand what I'm saying?\""
window hide
scene van_night with leftwipe
window show
"Slowly, Cameron lifts his head, a mixture of blood and saliva connecting his lip to Devon's fur in a long strand."
c "\"I'm okay. I'm fine.\""
"Cameron sounds confused as he mumbles, trying to get up unsteadily."
d "\"No! Stay still.\""
b "\"No, get up. Didn't I tell you what I'd do to your bear if you don't--\""
d "\"Then do it! Come over here and do it, you fucking coward! You fucking scum--\""
c "\"Devon.\""
"Cameron's voice is calm, albeit quiet, and weak, and the bear goes silent as he focuses back on the coyote."
"He has his head lifted, trying to focus on Devon's face."
c "\"Who's feeling this right now?\""
"The question catches the bear by surprise."
d "\"What?\""
c "\"The mines, that's right. I'm going to the mines, and I'm coming back for you.\""
"Cameron clasps a paw to his muzzle, wincing hard as he shuts his eyes tight."
d "\"What? What mines? Stay here.\""
"Devon's eyes well up with tears, seeing that the coyote is barely coherent, barely able to understand what's happening."
"Then Cameron leans in to kiss the bear, again taking Devon by surprise."
"He immediately smells and tastes Cameron's blood, making the gorge rise in his throat."
"It reminds him of his predation nightmares, but Cameron insists, so Devon just concentrates on not heaving."
"He doesn't want to feel the gap where Cameron's lower-left canine used to be, the unevenness of his already-swelling muzzle."
"As he forces himself to kiss back, he feels something else press against his lips."
"Something hard and oddly shaped, and Devon opens his muzzle, allowing the blood to flood into his mouth, but with it comes something else, and Devon realizes all at once that it's the key."
"Devon maneuvers the key into his muzzle as subtly as he can, hearing Brian sigh impatiently behind Cameron."
"It slides under his tongue easily, small in his comparatively large muzzle."
"Cameron whispers into Devon's ear."
c "\"We're gonna go back home together. I promise.\""
d "\"But where are you going? Why the mines? Honey, please?\""
stop music fadeout 15.0
play ambient crickets fadein 15.0
"Devon can't keep the whining panic out of his voice, sounding like a cub, but managing to keep the words clear with the tiny key under his tongue."
"Devon just stares at Cameron as he pulls back, tears rolling down his cheeks as his coyote crawls weakly to his feet and steadies himself against the wall of the van."
b "\"Eh, you're fine.\""
"He turns his gaze back to the furious, sobbing bear."
b "\"Sit tight, kid. We'll be back in a little while. I promise.\""
window hide
pause 0.5
scene black with medium_dissolve
pause 1.0
scene mines with medium_dissolve
pause 0.5
window show
"Being knocked out, regaining consciousness, stumbling his way through the dark, all while on an untold amount of shrooms is... harrowing."
"That's the only word Cameron feels is appropriate for this situation: harrowing."
"The world is more dreamlike than his dreams."
"This combination of disorientating factors leaves Cameron fumbling through a series of events immediately after he'd reached the old bear."
"Brian grabbed his paw, and suddenly they were moving swiftly through the desert before Cameron is pulled into a place that's cold and dark, lit up dimly by an old electric lantern, its handle hanging from the barrel of Brian's shotgun."
"If Cameron thought his perception of time was fucked on weed, now it's twisted over on itself."
"He's exhausted, having not eaten a proper meal in well over a day, and his throat is so dry, he thinks he might be willing to drink Brian's drugged water."
stop ambient fadeout 5.0
"Each time Brian goes around a bend first, or his bulk obscures it, the lantern's light disappears and leaves Cameron in darkness."
"Each time that happens, brilliant red arcs crowd his vision."
window hide
pause 0.5
play ambient mines02 fadein 3.0 volume 0.3
scene black with medium_dissolve
pause 1.0
#scene bg closed_eyes5 with slow_dissolve:
#    zoom 1.02
#    truecenter
scene mine_blur:
    alpha 0.5
    zoom 1.02
    truecenter
show black behind mine_blur
show lamp:
    zoom 1.02
    truecenter
with slow_dissolve
pause 1.0
window show
"{i}Who's in darkness?{/i}"
show cam confused b mine at right behind lamp with dissolve
c "\"I am. I'm in the darkness.\""
"{i}Everything is in darkness{/i}."
show cam worried b mine at right with dis
c "\"No, just me.\""
show bri vaguestare mine at left behind lamp with dissolve
show cam shocked b mine at jumping
b "\"Stop fighting it. It'll only make it worse.\""
"Cameron is surprised by the bear's sudden appearance."
c "\"Where am I?\""
show bri serious mine with dis
"Brian sighs heavily again."
b "\"Doesn't matter.\""
c "\"But--\""
hide cam
hide bri
scene black:
    zoom 1.02
    truecenter
play sound thud
"Cameron crumples up as something jabs him hard in the sternum, twisting in on himself, feeling a blackhole open in his chest." with vpunch
"It sucks the rest of his body and attention into it as the canine curls up on the hard dirt floor, whining and grunting."
"Finally, air returns to his lungs, and as it does, he hears a snorting sound again."
"After a while, Cameron looks up from his position on the ground to see Brian on his knees, appearing to smell the stock of his shotgun."
"Then Cameron notices the white powder, and he understands what's happening."
play background droneandvoice fadein 15.0
"Cameron hears a familiar voice, one that he's sure he's hearing, and not imagining."
window hide
scene mine_blur:
    zoom 1.02
    truecenter
show lamp:
    zoom 1.02
    truecenter
with slow_dissolve
pause 0.5
window show
dy "\"Don't snort it. You're trying to coat your nasal cavity, not your fucking lungs.\""
show cam sad b mine at right behind lamp with dissolve
c "\"That's how my friends did it.\""
dy "\"Then your friends are fucking idiots.\""
"Brian looks up from his disappearing line of bath salts."
show bri neutral mine at left behind lamp with dissolve
b "\"Who you talkin' to?\""
show cam horrified b mine with dis
"Cameron quietly tries to hush Dylan, but Brian already heard them."
"On top of that, Brian doesn't seem angry or upset, but his continued stare demands an answer."
show cam worried b mine with dis
c "\"Um, his name's Dylan. He's my ex. Sorry, we don't get along well.\""
show bri smirk mine with dis
b "\"You gettin' some third man syndrome? Whenever I get real fucked up on too many drugs for too long, a person always shows up. I end up having a conversation with 'em and everything.\""
"Brian readjusts the way he's holding his lantern and gun and grabs Cameron's arm with the other."
show bri confused mine with dis
b "\"I hear it happens to people in survival situations, too. Anyway, I'm always too delirious to remember who the third man is.\""
show cam worried b mine with dis
c "\"Yeah...\""
"Cameron can't understand how Dylan isn't real, but this nightmare bear apparently is."
"Is he being tricked?"
show bri angry mine with dis
b "\"Alright, here's the deal: I'll stop hitting you as long as you're smiling, got it?\""
show cam confused b mine with dis
c "\"Huh?\""
show bri angry fists mine with dis
"Brian clenches his fists meaningfully."
show cam scared b mine with dis
"Cameron winces, then quickly stretches his mouth into a large smile, even though it hurts to the point that tears well up in his eyes."
show cam happy b mine with dis
c "\"Oh! Sorry, I didn't realize what you were talking about for a second. I remember now!\""
show bri smirk2 mine with dis
b "\"Sure you do. Pathetic faggot.\""
show cam grinning b mine with dis
"Brian continues to inspect Cameron as the coyote remains quiet, keeping a smile plastered on his face."
"This experience is too much."
"All of this is too much."
"He just wants it to stop, and he'll do whatever this bear, this source of his torment, wants if it prevents him from being hurt again."
show bri surprised mine with dis
b "\"Guess I did bust your chops pretty good, huh? Hmm--\""
hide bri
show bri angry mine at center behind cam
with dissolve
show cam surprised mine at jumping
"Cameron flinches as the bear grabs his badly aching muzzle in one giant paw."
c "\"Wait, please don't--\""
show cam scared b mine at jumping
c "\"Agh!\""
"Cameron cringes hard, but tries his best to hold still."
show bri confused mine
with dis
b "\"Yep, broke your tooth, too. Swellin' up a bit, but you're cuter with your face all messed up like that. Too bad it's gonna look real ugly by tomorrow morning, not that it'll matter.\""
dy "\"It's just hard to look at you now, with that stupid scar.\""
show cam sad b mine with dis
"Brian lets go and grabs his shoulder instead, at the same time glancing at Cameron's shirt."
show bri smirk2 mine with dis
b "\"You from Bridgetown? Timber city? Or did you just pick that up at the Goodwill?\""
b "\"I always say, when you're shoppin' at the Goodwill, NEVER pick up clothes that have anything to do with a place. Fuck, just a few years back, I took a Weston sweatshirt from the Salvation Army and--\""
show cam worried b mine with dis
"Cameron follows along silently."
"Meanwhile, that third presence has shifted into something else, something a bit more familiar."
"Brian's getting chatty again from the second dose he took."
b "\"--Anyway, I hear that city's overrun with Antifa and all that. A true liberal hellscape if there ever was one.\""
"His mother, following behind them, is holding his paw."
"Looking back, he can't see her clearly, but he knows it's her."
show cam sad b mine with dis
c "\"It's... It's okay. A lot of the time it's outside groups coming into the city making trouble.\""
"He even sounds like her, defending the city they both grew up in despite its problems, despite its streets becoming a stage for the country's culture wars to physically play out."
"Even while they suffered on the outskirts of what was supposed to be a liberal bastion lit up by the lights of tolerance and welfare, but instead glowing orange from burning cars and flash-bangs."
"And yet, they defended it, because they both believed in its core principles."
"Now, though..."
hide bri with dissolve
show cam worried b mine with dis
"Cameron looks behind himself while also looking {i}back{/i}."
"He's taller than she is, and he's reminded of just how small she was, how small she'd seem to him now if she'd survived."
"He would have saved her too, if she could have held on just a little longer..."
"But how much longer?"
"Four, five years? Could she have held on that long?"
"No, not with her habit and the amount she was using."
"And though Cameron doesn't want to admit it, it was her death that spurred him to make the first serious change in his life."
"His mom wasn't a good mom."
"All things considered, she shouldn't have ever had children."
"But how can he judge?"
"She was still a teenager, excited, and in love, living out of a 70s Chevy van, but all of that came to an end when he was born in December, 1995."
"The next year, his abusive, probably-schizophrenic father left and committed suicide sometime in the mid-2000s."
"But, for a few months in 1995, his parents truly wanted to make a good life for him, and that feeling of love from that moment in time overwhelms Cameron."
show cam sad b mine with dis
"They wanted him to be happy, successful, and they truly thought he'd be the one to break the family cycle of dropping out and being broke."
"And even though they wanted that for him, they especially wanted him to be happy, to have a family life and a childhood that both his parents were only able to see other kids enjoy."
"They tried."
"But it's the most typical love story for people like them."
"Because eventually, like in all those other stories, things break, and then things settle."
"He'd done the exact same before Devon."
"She should have taken more precautions."
"She left him alone in the trailer often, her medications and recreational drugs freely available for him to experiment with while she was at work."
"He became an addict just like her, and he had come to understand the baggage that comes with that label, that it's not just about a craving, or a desire for something."
"Everyone has those feelings."
"No, it's about who you are as a person: a liar, a thief, a cheater."
"Someone willing to do anything to get whatever it is their addiction demands, anything to feel good."
"Whether it's pathetically checking all the coin dispensers in a casino once you've spent your life-savings, or pathetically combing through the carpet for whatever drug it is that you're starting to come down from."
"The only thing that had saved him from that life, and death, was his mother's insistence he keep his grades up."
"Of course, Devon saved him, too, but he would have never met the bear without good grades and a decent ACT score."
"And despite her losing touch with life in his senior year, that habit of academic discipline she'd drilled into him stuck."
"That's what got him a partial scholarship to the University of Pueblo."
"And that's what got him out of the trailer parks surrounding Bridgetown, and into this state's flagship university."
"A few schools in his own state had better offers, but Pueblo was the most prestigious of the schools he got accepted into."
"{i}A top 100 school with the best ranked nursing and engineering programs in the region!{/i}"
"That, and at the time, Cameron wanted to be far away from Bridgetown, even if that meant the desert."
"And then he met Devon."
show cam crying b mine with dis
"She wasn't a good mom..."
"... But she was a great person, a wonderful person, and she did the best she could with what she had at the time."
"She'd brought him into a chaotic, unstable life, a life that she saved multiple times, and while he occasionally wished his mother would have just let him die..."
"... Now, Cameron is only thankful."
"While most of his life was tough, the past five years have been better than he would have even dared to dream was possible."
"His life was perfect up until yesterday, when they got here."
"Tears run down his face, conflicted about how he should feel, but just knowing that he misses her, that he loves her, and that he hopes she's okay, wherever she is."
"This third person squeezes his paw reassuringly."
"Cameron squeezes back, and he's comforted by the feeling that for this moment, he's sealed off from Brian and the town, and it's just him and his mom walking through these mines."
"She tells him she's proud of him for graduating high school and college, and she's happy he found Devon."
show cam sad b mine with dis
"Would she really be proud of him if she knew what he studied?"
"If she was still around..."
c "\"--I would've majored in business administration, or something.\""
show bri angry mine at left behind lamp with dissolve
b "\"What did you major in?\""
show cam worried b mine with dis
"\"{i}Smile{/i}.\""
"A gentle voice from behind him, barely audible, and carried on the soft breeze that grows weaker the deeper they go into these tunnels."
show cam grinning b mine with dis
c "\"Uh, music theory.\""
show bri vaguestare mine with dis
b "\"And what the hell are you supposed to do with that?\""
show cam smile b mine with dis
c "\"Teach.\""
"The automatic answer, the one he had prepared for all of his skeptical friends who were going into STEM-related fields."
b "\"You a teacher?\""
show cam smile b mine with dis
c "\"No, but that was my plan.\""
show bri serious mine with dis
b "\"Some plan.\""
show cam grinning b mine with dis
c "\"I mean, I didn't go into any debt, so I had financial freedom after I graduated.\""
show bri smirk mine with dis
b "\"You know, you're pretty coherent for someone that's on that many shrooms. Most people would lose their minds.\""
show cam happy b mine with dis
c "\"Oh, I am, I definitely am, it's... I don't know. I have more control than I did the first time I tried it.\""
"In fact, Cameron feels like he's losing his mind right now, laughing even though it makes every part of his body ache."
show bri serious mine with dis
b "\"Xanax is like magic when you're panicking. Anyway, what is it that you do for a living, did it all pay off?\""
"Judging by the tone in Brian's voice, he already knows the answer to that."
show cam confused b mine with dis
c "\"Um... Customer support... For Hulian.\""
show bri angry mine with dis
b "\"Sad, workin' for a country that we nuked twice. Back in the 80s, we used to beat people up for working for companies like that.\""
show cam confused b mine with dis
"Cameron is at loss for words, but only for a moment."
show cam smile b mine with dis
c "\"Oh... Okay.\""
"Hulian, the current market leader in smartphone manufacturing, is Tayovanese, and the coyote assumes that the bear is thinking of a certain other country in the same region."
"Either way, it's a strange and disturbing aside."
"But that's just Brian, and sometimes with Brian, it's best for Cameron to just keep his mouth shut and to also keep on smiling."
show bri confused mine with dis
b "\"So why music? You sing?\""
"Cameron wishes the bear would stop asking him questions, making small talk like any of this is a routine part of their lives."
"But the coyote assumes bath salts will make anyone talkative."
c "\"Uh, kind of--\""
b "\"Whaddaya mean, kinda? Either you sing, or you don't.\""
show cam confused b mine with dis
c "\"Well, yeah, I mean, I sing, but I'm not very good--\""
show bri evilgrin3 mine with dis
b "\"I mean, you fucking better be if you spent four years learning. How about you sing, and I'll decide.\""
"It's getting harder to keep up the cheerful charade as Cameron senses the cruel, malicious arousal rising up inside of Brian again."
"The second dose is making him do more than just talk too much."
show cam grinning b mine with dis
c "\"Uh, sure, just gotta think of one to sing. Anything you want to hear? I know a lot of 90s grunge and alternative rock.\""
show bri smirk mine with dis
b "\"Heh, you're a walkin', talkin' stereotype, aren't ya? You write your own music?\""
show cam smile b mine with dis
c "\"I definitely tried.\""
"A subtle twitch of annoyance ripples through the air."
show bri vaguestare mine with dis
b "\"You know, one thing that really pisses me off is when someone's acting like an overly-humble little bitch. Either you do, or you don't. Either you're good at it, or you're not. Either you offer something different, or you fucking don't.\""
show bri evilgrin2 mine with dis
b "\"So which the fuck is it?\""
show cam happy b mine with dis
c "\"I do! I can! Uh, just give me a second.\""
"The corners of Cameron's muzzle turn down slightly, his composure almost crumbling."
"He's doing the best he can under the current circumstances, but he needs help."
"{i}Devon, where are you?{/i}"
show bri smirk mine with dis
"Brian's attitude shifts from one extreme to the next, making Cameron feel a sort of emotional whiplash, but as long as it keeps him from getting hit, or more importantly, killed, then he's fine with that."
hide bri
hide cam
with dissolve
"Tentatively, Cameron starts to sing, choosing the song that got him the most attention."
"The one that was played in moderate rotation at Mountain West colleges, along with a few in the Northwest."
"A song about his ex, Dylan, about their mutual love and hate for each other, about the abuse they used to hurl at each other, physical and mental, and finally, about their breakup."
"His voice is rough and cracked, and while some of it is because he isn't warmed up, it's mostly due to having his throat crushed."
"Dehydration, and screaming doesn't help either."
"But aside from jolting each time Brian pulls him in a different direction, Cameron finds the melody and rhythm."
"As he does, he becomes a bit more bold, singing louder until his voice carries through the tunnels."
"It feels very strange with his swelling muzzle and missing tooth."
"Brian still says nothing, and Cameron realizes he's listening intently."
"While this makes the coyote nervous, he knows it's better than the bear being angry, and mainly, he just needs to keep singing."
"Devon is in the mines with them, and he needs directions."
"Cameron just wishes it doesn't feel like he's leading Devon to his own demise."
stop ambient fadeout 6.0
stop background fadeout 6.0
window hide
pause 0.5
scene black with medium_dissolve
pause 1.0
play ambient2 crickets fadein 5.0
pause 1.0
scene mines with medium_dissolve
pause 0.5
window show
"Finding the entrance wasn't hard."
"While the main entrance had been blocked off with rebar before being filled and sealed with concrete, he'd known about the side entrance from the supernatural forums he researched before coming here."
"That, and Cameron's blood was sprinkled here and there, and the scent of it spurred Devon on."
"Of course, it lead right to that entrance."
"He had started unlocking his cuffs the second he thought Brian might be out of earshot."
"He had fumbled with the tiny, slippery key, before freeing his wrists, revealing blood-crusted fur matted down to the broken skin."
stop ambient2 fadeout 5.0
"Now, Devon moves through the mines in complete darkness."
window hide
pause 0.5
play ambient mines01 fadein 6.0 volume 0.5
scene bg black with medium_dissolve
pause 0.5
window show
"It's almost suffocating, almost panic-inducing, but the scent of Cameron mixing with the foul odor of Brian pushes the younger bear deeper into the tunnels."
show dev angry s dark5 with dissolve
"The air feels tense, as if the mine itself is intent on seeing what happens next."
"He's not going to fall into another abyss."
"When Lupita died, it had been an accident, one that happened after a tornado shredded their town, leveling the block across the street, but leaving their house mostly intact."
"As a 12-year-old, he just didn't think that it could happen."
"They had survived the actual disaster, but just as the relief started to set in, and his guard started to come down, it happened."
"He felt powerless in that situation, and he knew that her death had happened because of him."
"But this time is different."
"He couldn't fight what took Lupita, but he can fight what's taking Cameron."
show dev worried s dark5 with dis
d "\"Damn it...\""
"After about ten minutes though, Devon starts to become more agitated, unable to hear them any longer, and going by scent alone, Devon can tell that he's lost the trail."
show dev frustrated s dark5 with dis
d "\"Shit... Shit, shit, shit!\""
"He hisses through his teeth, trying to keep quiet in case Brian is somehow nearby, lying in wait."
"And then, somehow, he hears Cameron's singing voice."
show dev shocked dark5 with dis
"Devon goes completely still."
"He'd recognize his boyfriend's voice anywhere, of course, but Cameron's style is different, having the qualities of a singer from the 50s while retaining a grunge-like roughness."
"The coyote was heavily influenced by the black and white musicals his mother used to watch late at night."
"He was embarrassed about it after being critiqued in one of his vocal performance classes, and he had been trying to change his technique when Devon first met him."
"But Devon always liked Cameron's voice, and it was due to Devon's urging that Cameron leaned in to his style."
"He knows the song too, the one about Cameron's ex, the one that he doesn't like to hear because it's violent and vicious."
"He never asked Cameron about it because he assumed the coyote would bring it up in his own time."
"Now, he needs to make sure he even has that chance."
show dev angry s dark5 with dis
"Devon begins moving as fast as he can while staying quiet."
"He knocks his nose into a few walls, and scrapes up his elbows and shoulders, but he keeps moving, simply trying to force his way in the direction of the voice."
"Then, just as he thinks he's a few turns away, it stops."
"Then Cameron screams, and Devon drops all attempts at stealth."
show dev angry yelling s dark5 at jumping
d "\"Cam!{w=0.3} BRIAN!\""
"He calls out to let Brian know he's there, to at least distract him from the coyote."
"Then he barrels his way through the darkness, trying to find what he's sure is the last turn."
"Why Brian has brought Cameron here, he doesn't know."
"He doesn't even know what he's going to do when he meets them."
stop ambient fadeout 6.0
"Well, anything."
"He'll do anything."
window hide
pause 0.5
play background droneandvoice fadein 15.0
scene black with medium_dissolve
scene mine_blur:
    zoom 1.02
    truecenter
show lamp:
    zoom 1.02
    truecenter
show bri vaguestare mine behind lamp at left
show cam surprised b mine behind lamp at right
with medium_dissolve
window show
"Brian is looking a bit more distracted, starting to scan the tunnel wall before his eyes settle on what looks like a large crack from the ceiling to the ground."
show cam happy b mine with dis
"Cameron turns up his singing a notch, knowing that this is their destination, the end of the road."
show bri confused mine with dis
"The old bear glances at him, looking annoyed."
"This, for whatever reason, is what brings Brian out of his stimulant-induced hyper-focus."
show bri horror mine
show cam shocked b mine with dis
with dis
stop background fadeout 15.0
"Brian finally realizes what's happening."
"It's only now that the old bear remembers Cameron's plan to take the key."
"Even Cameron forgot."
"But now, a huge paw flies to his pocket, digging inside and realizing it's too late before he whirls on Cameron."
play music drowning fadein 3.0
show bri rage mine with dis
b "\"Oh, you little faggot!\""
show cam scared at jumping
hide bri
hide cam
with dissolve
"Cameron turns and runs, trying to take advantage of Brian letting him go for those couple of seconds."
hide lamp
play sound punch
scene mine_blur red:
    zoom 1.02
    truecenter
show lamp red:
    alpha 0.7
    zoom 1.02
    truecenter

show redarch_05 behind lamp:
    alpha 0.4
    yoffset 500
    zoom 1.05
show redarch_04 behind lamp:
    alpha 0.4
    yoffset 500
    zoom 0.85
show redarch_03 behind lamp:
    alpha 0.4
    yoffset 500
    zoom 0.62
show redarch_02 behind lamp:
    alpha 0.4
    yoffset 500
    zoom 0.4
show redarch_01 behind lamp:
    alpha 0.4
    yoffset 500
    zoom 0.2

show redarch_05 as extra1 behind lamp at drugtriparch01:
    yoffset 500
    zoom 1.05
show redarch_04 as extra2 behind lamp at drugtriparch02:
    yoffset 500
    zoom 0.85
show redarch_03 as extra3 behind lamp at drugtriparch03:
    yoffset 500
    zoom 0.62
show redarch_02 as extra4 behind lamp at drugtriparch04:
    yoffset 500
    zoom 0.4
show redarch_01 as extra5 behind lamp at drugtriparch05:
    yoffset 500
    zoom 0.2
show bg black:
    zoom 1.3
    truecenter
"Something pounds into Cameron's lower back, just to the right, and it feels like a cannonball being smashed through his body." with hpunch
"Cameron is launched forward against the tunnel wall directly in front of him, and he tries to hold on to it, sliding down slightly as he stares straight up into the darkness."
window hide
pause 0.5
hide bg black with medium_dissolve
pause 2.0
window show
"It's so dark that Cameron can't tell if the ceiling is a few feet above him, or if it's simply endless space full of glowing arches that stretch on forever."
"His eyes stay wide, his breath leaking out of his muzzle in a slow, high-pitched rasp, not wanting to believe the pain he feels spreading through his insides is real."
"Then, he's on the ground, writhing and groaning uncontrollably while electric pain spiderwebs through his body."
"The blows Brian had delivered before are nothing compared to this."
"Cameron thrashes around in the dirt, desperate to find a way out of the hell."
"He's in hell."
"{i}Who's in hell?{/i}"
"He has to be."
"What are these red arches, and why are flames spreading from his guts up into his lungs?"
show bri lookdown red at left behind lamp
with dissolve
window show
b "\"Damn. You'll probably only piss blood after that one.\""
"Brian's mock-concerned voice snaps Cameron back to the situation he's in, and in the very back of his head, he realizes his trip is beginning its descent."
"The pain is still present though, and it's not letting up."
"How can he feel pain if he's nothing?"
"He's finally breathing again, but each exhale is accompanied by a whining wheeze, involuntary tears rolling down his face."
"Brian leans over him and the coyote cringes."
c "\"No,{w=0.3} stop!{w=0.3} Please!\""
show bri neutral red with dis
"Brian pauses, then just grabs Cameron by the arm and yanks him up."
hide bri with dissolve
"Cameron lets out a hoarse, breathless scream as his aching body is forced to move again."
"It echoes around them before cutting off as a huge arm tightens around Cameron's throat."
d "\"Cam!{w=0.3} BRIAN!\"" with vpunch
"Devon's voice is very close, maybe only a tunnel or two away."
"Brian mumbles quietly next to Cameron's ear."
b "\"Shut the fuck up right now, or I obliterate your other kidney, got it?\""
"Cameron feels the threat hovering over the left side of his back this time, and he quickly shuts his muzzle, even though groans still force their way up, muffled behind his lips."
"This seems to at least satisfy Brian, and he drops the chokehold before shoving Cameron forward."
"At first, Cameron is surprised that the bear didn't just hit him again anyway, but Brian's distracted again."
"Devon's too close, and a few terrible plans go through the older bear's head that causes Cameron's already aching abdomen to lurch with nausea and fear."
"Brian considers waiting and ambushing Dev, but he quickly discards the idea as he realizes Cameron might try to warn Devon by making noise right as he reaches them."
"That's exactly what Cameron would do, even if it means being beaten to death by Brian."
"Deciding again that nothing matters anymore, he pushes Cameron forward through the narrow opening, the passage becoming more tight until Brian has to turn sideways and struggle through, and then it opens up."
window hide
pause 0.5
scene black with leftwipe
pause 0.5
scene bg hollow_visions with leftwipe:
    zoom 1.02
    truecenter
pause 0.5
window show
"Cameron smells death."
"He instinctively backs up, right into Brian."
show cam terror b red with dissolve
c "\"No.{cps=3}..{/cps}{w=0.4} No...{w=0.3} No,{w=0.2} no,{w=0.2} no,{w=0.2} please don't do this!\""
c "\"I can't...{w=0.3} I can't--\""
"He can't finish his sentence."
"Brian's victims felt pain that still seems unimaginable to the coyote."
hide cam with dissolve
"Knowing Devon is close behind them, Cameron makes one last effort to turn and dodge around Brian, but the bear is far too large, and he easily grabs up the coyote and throws him further into the hollow."
play sound thud
"Cameron comes up immediately, trying to suppress his whines and whimpers." with hpunch
show cam shocked b red at twelve,jumping
c "\"Brian, just wait a second. Think about it. I can {i}help{/i} you. Why did you bring me here in the first place?\""
show bri neutral red at left with dissolve
"Brian gives Cameron a dispassionate look, but he does pause, and that gives Cameron some hope."
"And some time."
show cam scared b red with dis
c "\"Let me talk to them. Let me see if I can reason with them. We both know that this, all of this, is over.\""
show bri vaguestare red with dis
"Cameron senses a slight shift in Brian's intentions as the bear begins to seriously consider Cameron's reasoning."
show cam horror b red with dis
c "\"I know you need my help. I can feel them. They want you, Brian, and they're waiting for you!\""
show cam worried b red with dis
show bri confused red with dis
c "\"I know what it can be like, walking in circles for most of your life, making the same stupid mistakes and knowing what you need to do to get better, and just never doing it.\""
show bri smirk red with dis
b "\"Oh yeah?\""
c "\"But I finally did, and my life was almost perfect.\""
"{i}Until I met you{/i}."
show cam surprised b red with dis
c "\"So let's do it. Let's end this nightmare right now.\""
show bri closedeyes red with dis
"Brian takes a deep breath, and holds it."
"The entire mine, the entire town, seems to hold its breath with him, and Cameron starts to understand how deeply entwined this bear is with this place, this entity that seems to be pulling all the strings."
"Cameron can feel the monolithic entity shift and turn, as if it too senses an inevitable end."
"Brian is close to taking the coyote's offer."
"But it isn't meant to be, and Cameron, of course, knows that."
"A scuffling from the entrance announces Devon's arrival."
show bri angry fists red with dis
b "\"Guess he's finally here, huh? Glad I brought my 10-gauge. Always wanna make sure you got good firepower when bears are involved, eh?\""
hide bri with dis
play sound pumpback
show cam scared b red with dis
"Cameron watches in horror as the old bear opens up the shotgun before inserting a shell."
play sound pumpforward
hide cam
hide bri
with dis
"Cameron's mind is blank as he automatically lunges at the huge bear, grabbing at the shotgun barrel as Brian snarls in rage."
"\"{i}Everything's falling apart. You're spiraling.\""
window hide
pause 0.5
scene bg black with leftwipe
window show
"Devon shoves his bulk through the narrow passage, squeezing through to the hollow on the other side."
window hide
scene bg hollow:
    zoom 1.02
    truecenter
show dev angry s mines at left
with leftwipe
pause 0.5
window show
"When he stumbles into the open space, Devon spots Cameron immediately, the coyote being swung left and right as he fights with Brian over the shotgun."
stop music fadeout music fadeout 10.0
"Cameron is covered in blood, tears matting the fur on his cheeks."
"The situation is already a terrible one, but again, his fear for Cameron turns to anger at Brian as he sees the bear throwing vicious, crushing kicks at Cameron's lower-body."
"Devon realizes this is it, and he has no time to think."
play music terrorbelowthesurface
hide dev with dis
show bg hollow at zooming6 as extra
"Devon charges up behind the older bear, and bites deeply into the side of Brian's neck."
"Apparently, biting someone other than himself is a lot more effective, and he feels his canines sink deep into the flesh beneath the thick fur."
"The old man is covered in a layer of protective padding, just like himself, but the older bear clearly has a lot more of it."
"Still, Brian screams, high-pitched and full of fury."
"Then, Cameron is finally shaken loose from the shotgun, and Brian grabs the barrel with both paws before ramming the butt of the shotgun back into Devon's stomach."
play sound thud2
"The younger bear retches and crumples over, but he manages to grab the shotgun, holding onto the stock tightly." with vpunch
"Brian, clearly aware of how bad the situation could become for him, lets go of the shotgun so he can throw an elbow into Devon's face, bashing the left side of his muzzle and face."
"This stuns him and gives the bigger bear time to turn around and throw a knee up into Devon's hunched form, an inch above the navel, almost the exact spot he'd hit earlier."
play sound punch
"Devon feels as if his guts are flattened to his spine before liquifying, the force actually lifting him off the ground for a half-second." with hpunch
"Even though he lands on his feet, he immediately sinks to his knees, his muzzle wide open as he continues a battle with his own lungs, all while still trying to hold on to the shotgun."
show bri rage mines with dissolve
b "\"You're a dead man walkin', boy! Well, on your knees, anyway. What a surprise!\""
"Brian fumbles shakily to find the stock of the shotgun, hidden somewhere under Devon's bulk while simultaneously trying to avoid the end of the barrel, in case Devon is able to find the trigger."
"The attack had been enough to rattle Brian, even if it was short-lived."
"Devon curses himself, trying to move, knowing he probably can't win, but he needs to do something, maybe hurt Brian so bad that Cameron can at least get away."
"{i}Get up!{/i}"
"But he can't breathe, so there's not much he can do to defend himself, let alone stand up."
"So, Devon keeps his hold on the shotgun even as Brian starts trying to yank it from his weakened grasp, and he's starting to succeed."
d "\"Cam... run...\""
"Devon rasps, not even sure where Cameron is right now, assuming he still might be on the ground after being kicked so many times."
play sound thud
show bri horror mines at jumping
"Brian squeals."
"Looking up from his doubled-up position, Devon sees Brian in front of him, bent over as well, the grizzled bear grabbing between his legs."
hide bri
with dissolve
show cam shocked b mines with dis
"As Brian sinks lower, Cameron appears, lowering a foot."
show cam happy b mines with dis
"The coyote smiles with relief and joy at seeing Devon, and seeing that he's got the shotgun."
"Cameron seems so sure that they've won that he doesn't see Brian's quick recovery, the old bear forcing himself up, murderous vengeance in his eyes as he runs at Cameron with another animalistic scream."
show bri rage mines at left,jumping
show cam scared b mines at jumping
"Devon can only watch as the huge bear charges at Cameron."
c "\"No!\""
"The much smaller coyote can only yelp in panic before Brian smashes into him and crushes him against the wall."
hide cam
hide bri
play sound punch2
show blood06:
    zoom 1.02
    truecenter
"Devon hears a crunching sound just as he gets his first tiny sip of air, just as he hears Cameron's own air wheeze out in a yowl-like moan." with hpunch
"And then, even more viciously than Devon had attacked Brian, the old bear begins to maul Cameron."
window hide
play sound punch
show blood07 with vpunch:
    zoom 1.02
    truecenter
pause 0.5
play sound punch3
show blood08 with vpunch:
    zoom 1.02
    truecenter
window show
"Brian bashes him left and right with blows aimed at the coyote's face before Cameron collapses."
"There, Brian begins to rip and tear into the coyote with his claws."
"Devon begins to move, but it's slow, and he just wishes his lungs would start working."
"Cameron tries to crawl away from Brian, and Devon sees the horror mirrored in his boyfriend's eyes."
play sound bite
show blood03:
    zoom 1.02
    truecenter
"Then Brian comes down on him again, and Cameron throws his left elbow back at the bear's face, only for Brian to sink his teeth into Cameron's forearm and elbow." with hpunch
"Cameron lets out a yelp and curls around Brian's muzzle, scratching and biting at it with his claws and teeth."
"But then, Brian twists and tears, and Cameron lets out a howling sound, his body twisting violently."
show blood03_2 with dis2:
    zoom 1.02
    truecenter
"He's on his back now, and he goes quiet, staring in shock at the wall he's lying perpendicular to, his eyes beginning to roll up as Brian thrashes his head and a crunch comes from Cameron's arm."
"The coyote can't make any sounds now, the breath seemingly knocked out of him by the pain."
"Devon has never heard Cameron make those feral pain sounds, not like this."
"The shotgun had opened up at some point during the struggle, and Devon drops the awkward weapon, too intent on saving Cameron to figure it out right now."
"And to see him in so much agony that he can't breathe, can't even vocalize it anymore, it gives Devon the final push he needs."
play sound punch
hide blood06
hide blood07
hide blood08
hide blood03
hide blood03_2
hide black
"He charges into Brian and the force knocks the old bear off the coyote." with hpunch
"Devon has never seriously mauled someone in his entire life."
"But it's something that comes naturally to him and Brian, and while he had play-mauled people in the past, including Cameron, this is the first time he brings his claws, teeth, and muscles to full use."
"Straddling the older bear, Devon roars at Brian before lunging down."
"First, he bites Brian's neck again, but from the front this time while his paws rip and tear into the bigger bear's hide."
"Brian seems to concentrate for a second before burying his fist up into Devon's stomach with a deep, muffled thud."
"But the younger bear is tensed up this time, and the fist gets no further than his stomach muscles."
"Still, Brian's power is almost supernatural, and Devon lurches forward and grunts, folding over, an ache forming deep in the pit of his belly, but this only makes him bite harder."
"Devon can feel that he's truly stunned the old bear, at least for now, and as Brian takes his fist back, he resorts to panicked shoves instead of actually trying to fight."
"When Brian finally does try to claw at Devon's face and eyes, the younger bear leans back and smashes his head into Brian's muzzle."
play sound thud8
show blood06:
    zoom 1.02
    truecenter
"The sound it makes indicates a broken snout, and Brian lets out another high pitched whine before screaming and trying to lunge up to bite Devon's neck." with vpunch
"Devon leans back, just avoiding the teeth before smashing his head a second time into Brian's face."
play sound punch2
show blood02:
    zoom 1.02
    truecenter
"Then, as Brian lays dazed, Devon lays into his snout three times, full force, trying to pound every bit of agony into Brian that the old bear had given all of them." with hpunch
"That would be impossible, though."
"Still, Devon feels a savage satisfaction as he sees at least two of the old bear's yellow teeth roll out of his muzzle."
"Brian howls and rolls violently, finally dislodging the slightly smaller bear."
stop music fadeout 15.0
"Devon heaves for breath, watching as Brian comes up several feet away, crouching and also heaving for breath."
b "\"You fuckin'... You!\""
"Brian can barely form words, but not just because he's out of breath."
window hide
play ambient mines03 fadein 6.0
play ambient2 wind2
scene black with fast_dissolve
window show
"His bitter hatred is evident, so mad that only frothy spit flies from his lips as he sputters."
"But then Brian's eyes flick to the right, and Devon remembers all at once that he'd left the gun there, having been focused on helping Cameron."
"The old bear moves lighting fast once again, and he shoots off to the right, and Devon realizes Cameron is there too."
d "\"Cameron, look out!\""
scene bg hollow_visions with dis2
play music solderingloop fadein 15.0 volume 0.3
"Cameron, lying in agony after Brian's vicious attack, knows something is deeply wrong with his body."
"The crushing against the wall of the chamber had done it."
"The true pain though, emanates from his left arm, and Cameron knows that it's mangled, broken, and useless."
"But he can still use his legs, and Cameron forces himself to get up and start moving for the shotgun, hearing the snarls and growls of the bears behind him."
"He does his best to stay quiet, but stifled grunts and small squeaks force their way out of his throat."
"As soon as he touches the shotgun though, he hears Devon shout."
d "\"Cameron, loo--\""
scene blood04 with dis2
"And again, the nightmare that is Brian is tearing at his body, pinning him to the wall, and Cameron screams in terror as the huge bear starts trying to bite his neck."
"The panicked coyote is only just able to get his unbroken arm up."
"It's maybe only three seconds before Devon is there, but it feels like an eternity, Cameron considering how badly it might feel to die from having his throat ripped out."
"Cameron's right arm is torn up as well, but since Brian isn't shaking his head this time, his bones at least remain intact."
play sound thud
scene bg hollow_visions:
    zoom 1.02
    truecenter
"Then, Devon wrenches the bigger bear off of him." with vpunch
"Cameron tries to get up, to crawl, but it's useless, his body too beaten and broken to do anything other than dragging himself away."
"Then he hears Brian's high-pitched squealing again, and this time, it's genuinely terrified."
"Cameron looks over, and sees the old bear is now on his back with his arm in a sort of hold by Devon."
"Devon is lying on his back, Brian's arm pulled towards his chest, Devon's hips close to the older bear's shoulder as his legs lock together at the ankles."
"Devon grunts and heaves with all his might, his huge, powerful body arching toward the ceiling."
scene bg hollow with dis2:
    zoom 1.02
    truecenter
"Devon is intent on really hurting Brian this time, wanting to make sure he pays the old man back for Cameron's tooth and arm."
"So, with the tooth part avenged, Devon focuses on destroying the other bear's arm."
window hide
scene black with fast_dissolve
window show
"Bear bones are especially hard to break."
"Devon has never had a broken bone in his life."
"But the younger bear knows a thing or two about applying force."
"His dad watched MMA all the time, and while he knows little about fighting, he knows why armbars can be so devastating."
"But even as he leans back, bending the big bear's arm over his inner-thigh, only a few cracks are heard, but it's nothing serious."
"Devon needs the arm to have less resistance, and more distance from the fulcrum."
"Unlocking his legs, he takes just a second to slam his foot right into the old bear's jaw."
play sound thud8
"For just a second, Brian goes limp, and Devon re-locks his ankles before lifting the limp arm away from his chest, and curling up."
"Then, he heaves back on the arm again, arching hard while he twists his body."
d "\"Torque!\""
"\"{i}Now you're thinking like an engineer!{/i}\""
window hide
play sound crack
play sound2 punch2 volume 0.6
scene bg hollow:
    zoom 1.02
    truecenter
show blood05:
    zoom 1.02
    truecenter
with vpunch
pause 0.3
hide blood05 with dis2
pause 0.5
window show
"As the catchphrase of one of Devon's old professors comes to his mind, a crack splits the air, and Brian's screams somehow reach a new, panicked pitch."
"Devon looks over to see Cameron has dragged himself a few feet away, leaving a dark, horrible, blood trail smeared behind him."
"There's a lot of blood, and Devon panics, thinking the coyote is bleeding out from his neck."
"Devon stumbles over to him, hovering his paws over the coyote's head."
d "\"Baby, your neck! Let me see it!\""
c "\"He-- He didn't get me. Let's go!\""
"Cameron is in no shape to run, so he groans as Devon lifts him into his arms, the bear starting to stumble toward the exit."
"Devon looks down at the coyote in his arms, just now seeing how truly terrible Cameron's injuries are."
"And then he glances back, shocked to see Brian standing."
"How the old bear was able to get up without making noise is beyond Devon."
play sound thud
d "\"UNGH!\"" with hpunch
"The butt of the shotgun, powered by the old bear's huge body, slams into his side, spreading a sickening ache in a wave through his body."
scene bg hollow_visions with dis2:
    zoom 1.02
    truecenter
stop music fadeout 6.0
"Cameron hears the dull thud followed by the vibration through Devon's thick body."
"He feels the bear cringe as he sinks to his knees, huddled over Cameron."
window hide
pause 0.5
scene black with medium_dissolve
scene circles with medium_dissolve
pause 0.5
window show
"The huge bear lifts up the shotgun he'd managed to keep a hold of."
"He struggles to hold it up with only his left paw, and his injured right arm dangles before he practically swings it up to prop his right elbow against the wall, a few pops coming from his shoulder as he does."
"He screams again when that happens, but with his fully functional wrist, he can now take steady aim, and with how narrow the hollow is, there's nowhere to go."
play sound pumpback
b "\"Don't.{cps=3}..{/cps}{w=0.4} Don't you fucking move.{w=0.3} You got that?\""
b "\"This is over. I'm killing that yote in front of you, and then I'm ripping your fucking arm off, boy!\""
"Brian's expression is an odd mixture of excitement and disgust."
b "\"Pity you ain't half as cute as the pup.\""
window hide
pause 0.5
scene the_divide with medium_dissolve
pause 0.5
window show
"Devon can only wheeze in response, and Cameron holds onto him tightly as he's cradled in his arms."
b "\"God, you fucking ruined it! He was perfectly fine 'till you showed up. Now he's fuckin' fucked up to the point he's not even fuckable!\""
"Cameron's ability to see and feel things is fading, just as the effects of the shrooms are fading."
"Still, there's just a bit left, and Cameron tries his best to use it."
"Devon's body begins trembling, and Cameron holds on to him more tightly."
"Devon's voice, still breathless, whispers into Cameron's ear."
d "\"Honey, whatever happens, just play dead, okay? No matter what.\""
scene the_divide2 with dis2
"But Cameron suddenly turns--"
window hide None
stop ambient
stop ambient2
play sound shotgun
scene white
pause 0.5
scene bg black with dissolve
pause 2.0
window show
"Devon watches as Cameron's face becomes a bouquet of red ribbons, and the bear stumbles as the shot hits his arm as well."
"Cameron's body jerks violently in his arms before going incredibly still."
"Devon quickly looks down to see Cameron no longer with a face."
window hide
play ambient2 wind2
show blood01 with medium_dissolve
window show
"Everything that used to make up his face is splattered against the walls, and it still pours from..."
"Cameron is gone."
"In shock, Devon looks at his arm and sees the white of bone shards, at first thinking it's his own, but then he sees a few of Cameron's sharp teeth also embedded into his arm."
"Devon leans over Cameron's body, an expression of untold anguish on his face as he starts to let out a low, terrible groan that rises in pitch to a bearish howl--"
window hide
stop ambient2 fadeout 2.0
pause 2.0
play sound reverse fadein 2.0
pause 1.6
scene the_divide2 with dis
play ambient mines03 fadein 2.0
play ambient2 wind2
"After looking {i}forward{/i}, Cameron does the only thing he can think of."
scene the_divide3 with dis
d "\"No!\""
"Cameron grabs the barrel and shoves up."
window hide None
stop ambient
stop ambient2
play sound shotandring
scene white
pause 0.5
scene bg black with dissolve
window show
"The sound is so loud it instantly deafens Cameron, and though the ringing starts to subside, the hearing in his right ear doesn't come back."
d "\"Cameron!{w=0.3} Cameron?\""
c "\"I'm fine! I'm fine.\""
"Cameron looks to where Brian is, the kickback from the 10-gauge had hit him hard, squarely in the chest."
"Cameron can almost visualize the shock sent through that old, worn-out heart, already exhausted from the stimulant and the fight."
play ambient2 wind2
"The old bear, still on unsteady feet, stumbles back a bit more before hitting the wall and sliding down it to sit."
window hide
scene mines_alt with medium_dissolve:
    zoom 1.02
    truecenter
pause 0.5
window show
play music submergedintro fadein 10.0 volume 0.3
queue music submergedloop volume 0.3
play sound heartattack01 fadein 3.0
queue sound heartattack02 loop
"Brian sits propped up against it, looking confused."
"He clutches his chest, rubbing it and grimacing."
"The shotgun is on the ground, out of Brian's reach, and the old bear makes no move to get it."
b "\"Fuck...\""
"He starts to try and get back up, but falls back down."
b "\"Oh fuck.{cps=3}..{/cps}{w=0.4} Oh fuck...\""
"Brian clutches at his chest and stomach and groans."
b "\"Oh no, that was it?{w=0.3} Is this it?{w=0.3} What the fuck?\""
b "\"What the fuck...\""
b "\"What the...\""
play sound2 thud
"Brian slumps back, his body convulsing, then he thrashes about, as if trying to escape something." with vpunch
scene bg black:
    zoom 1.02
    truecenter
play sound lantern
play sound2 shatter01
"He knocks over and smashes the electric lantern, crushing it under his weight." with vpunch
stop music fadeout 10.0
play ambient mines03 fadein 10.0 volume 0.4
"For several more seconds, they both listen to Brian's groaning, rasping, and snorting before it's silent."
"It's quiet for a little while longer, Cameron and Devon not daring to move."
"Brian had seemed invincible for so long, Cameron can't get himself to believe that it might be over."
"Devon whispers into Cameron's ear."
d "\"Cameron? How do you feel?\""
"Cameron gives Devon a look that's a mix of love and exasperation, even if Devon can't see it right now."
"They both know he's badly fucked up."
c "\"I think something ruptured. It feels all wrong.\""
"Cameron places his right paw on his own torso, wincing."
d "\"Don't move, okay? I'll get us out. I'll get us out in no time.\""
play sound2 gravel_echo volume 0.5
stop ambient2 fadeout 7.0
stop ambient fadeout 7.0
"Devon starts to tentatively make his way forward, and just as Cameron is realizing how long this might actually take, possibly too long if there is internal bleeding, his vision flickers."
window hide
pause 0.5
scene hollow_arch_0 with slow_dissolve2
pause 1.0
play music2 neuroprotection volume 0
play music neuroprotectionintro volume 0.3
queue music neuroprotectionloop volume 0.3
scene bg hollow_arch with slow_dissolve2
show bg hollow_arch_anim
pause 1.0
window show
"Cameron stares at it, then looks at Devon, wincing at the bear's bloodied and bruised face."
"But Devon doesn't react to the light, like Cameron is the only one seeing it."
"But a shroom trip can't emit light no matter how hard you're tripping."
c "\"I think I can see where to go. Just walk straight.\""
d "\"How--\""
"Cameron starts to shake his head, then stops as his neck sends a pang of fiery pain down his back."
c "\"I don't know, but I can see. Let's just get out of here... please.\""
"Cameron tries hard not to look at Brian's crumpled form against the side wall of the hollow, his wide-open eyes glinting from the gentle glow."
d "\"Okay. Just tell me where, okay?\""
"And sure enough, as they leave, arch after arch appears, and Cameron is confident they'll lead to the exit."
"These arches had tortured his mother, but this {i}feels{/i} like his mother, somehow."
window hide
pause 0.5
scene bg black with medium_dissolve
window show
"As they move, they both hear rustling sounds far behind them in the mines, but Brian is definitely dead, or at least had been when they left."
"So they keep moving, trying to keep quiet."
"Then, within an hour, real light."
window hide
scene the_arch3 with slow_dissolve
window show
d "\"Daylight.\""
"Devon looks down at Cameron and winces just like Cameron did when he saw Devon's face."
d "\"God, honey, we're gonna get you help, and you're gonna get better, okay?\""
c "\"But what about you? Do you feel okay?\""
"Cameron's voice is weaker than it was earlier, and Cameron feels Devon quicken his pace."
d "\"I'm fine.\""
"Devon says it sternly, setting his jaw, and Cameron stays quiet."
d "\"Cameron, I'm sorry.\""
c "\"And that's the... the last time you're saying that to me, okay? I don't blame you for anything. I'm just so glad I met you.\""
"He listens to the bear's heartbeat, steady for most of the journey, but getting faster as they get closer to the exit."
d "\"I think I hear a helicopter? And maybe a megaphone? Shit, did people come for us?\""
c "\"The shotgun blew out my hearing, so I'm not... I'm not really sure.\""
window hide
scene the_arch2 with slow_dissolve
show the_arch2_anim
pause 0.5
window show
"His trip is mostly over, yet these visions are so vivid."
"Cameron stares at this new arch, and something about it feels different."
c "\"Oh.{cps=3}..{/cps}{w=0.4} Mom,{w=0.3} I found it.\""
d "\"Huh?\""
c "\"Her arch.\""
d "\"You're seeing arches?\""
c "\"You know how something can happen that's so impactful, it splits your life in two? Like, you see life as before, and after that moment. It can be good or bad.\""
"Devon hesitates, like he wants an answer to the question he just asked, but he lets it go, for now."
d "\"Of course.\""
c "\"I think meeting you is the good divide in my life. I think what happened here, and what's going to happen after, I think it's the bad divide.\""
"It had always been his mother's death, and it still is."
"A divide."
"But this time, Cameron realizes he's been deeply affected mentally, and it's not something that he can just recover from."
"Something's truly wrong with him."
"That's been the case for a long time, but now, after this, something's been pushed over the edge."
"So, another divide."
d "\"I think we're gonna be okay, Cameron.\""
c "\"Devon, whatever happens after this, I love you, and I'm so happy I met you.\""
d "\"Come on, you didn't have to say that first part. We made it. Okay? It's just... It's just a fork in the road.\""
"Cameron gasps."
c "\"Oh, Devon, Artie is alive! He went to get us help, I think... I hope.\""
d "\"What? How?\""
c "\"I don't know. He got shot, but he got away. Brian was pissed. He's hurt, but I think he made it.\""
d "\"Oh.{cps=3}..{/cps}{w=0.4} Oh,{w=0.3} that's...\""
"Devon' lips tremble and his face twists up slightly as he tries not to cry, but it's out of incredible relief and happiness."
"Cameron doesn't tell him how bits of Artie are missing, or that he can't sense him anymore, both because of his waning powers and because Artie is too far away, at least that's what he hopes."
"Cameron stares up at the arch, looking both beautiful and terrible at the same time."
"Raincoat Monster stands to the side as they pass, and this time, Cameron does think it's his old hallucination."
"Cardboard, and unmoving, just like he's always been."
"But... something about all of this, the way he's seeing things, something has changed."
"It's not his psychic abilities, because now it's subtle and hardly noticeable again."
"No, something else happened, and his mind feels wrong."
"Looking {i}forward{/i} is no longer clear, but as Cameron uses the last of the psilocybin in his system to peer into their future, he becomes afraid by what he sees."
"So he just turns his muzzle slightly to Devon."
d "\"Cameron, we are going to make it.\""
"Based on what he saw, Cameron isn't sure."
"Devon will stay, he was able to see that much, but should he?"
"More than anything, they both want to stay together, but if Cameron becomes a burden to Devon, he doesn't know how he can stay."
"He just hopes that Devon can still love him after this terrible change, and he hopes he can fight it, whatever it is."
"So, Cameron leans his head against Devon's shoulder, smiling in a mostly happy, but in a bittersweet way."
c "\"Alright.\""
d "\"Alright,{w=0.3} now let's get the hell out of here.\""
window hide
pause 0.5
play sound2 gravel_echo volume 0.5
scene the_arch with slow_dissolve
show the_arch_anim
stop ambient fadeout 10.0
stop music2
stop music fadeout 10.0
pause 1.0
scene white with archtrans
pause 0.5
scene black with slow_dissolve
pause 2.0
jump a3s2
