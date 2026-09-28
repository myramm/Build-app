label okita_button_dress_code:
    scene expression player.location.background_closeup
    show okita 1 at right
    show anon f_worried
    with dissolve
    anon "Hi {b}Miss Okita{/b}, I was hoping you could talk to {b}Mrs. Smith{/b} about the new dress code policy..."
    show okita 1
    okita "Hmmph!"
    show okita 2
    okita "I'm not going to subject myself to that foul woman just so you kids can wear baggy pants and short skirts!"
    anon "No, that's not it... I'm concerned about the part restricting hair dye and I'd really like to-"
    show okita 10c with dissolve
    okita "Hair dye?"
    show okita 11 with dissolve
    okita "That's what you're worried about?"
    show okita 4
    anon "Y-yes, ma'am."
    anon "My friend {b}Eve{/b} likes to dye her hair blue, and I was hoping you could convince {b}Mrs. Smith{/b} into changing the policy?"
    show okita 2
    okita "Well, that's just silly!"
    okita "I've got a device upstairs that alters the pigmentation in hair follicles."
    show okita 1
    anon f_worried @ f_surprised "You do?"
    show okita 2
    okita "Sure."
    okita "I mean, it's still got a few kinks I need to work out..."
    okita "... But if your friend is willing to be my lab rat for a few tests, I'm sure I can get it working in no time!"
    show okita 1
    anon f_surprised "T-tests?"
    pause
    anon f_worried "I don't think that's a good idea, {b}Miss Okita{/b}..."
    show okita 2
    okita "Oh, come now!"
    okita "It's all noninvasive stuff... Well, mostly..."
    okita "There's a small chance she'll lose her hair completely but that's the absolute worst case scenario!"
    show okita 1
    anon a_facepalm @ -m_talk "..."
    show okita 2
    okita "We're talking less than a one percent chance!"
    show okita 1
    anon a_idle f_worried @ f_unimpressed_bored "Ehh, I think I'll just check with the other teachers and see if one of them can help me..."
    show okita 2
    okita "Alright, suit yourself."
    show okita 1
    anon "Thanks anyways, {b}Miss Okita{/b}."
    hide anon with dissolve
    return

label button_okita_intro:
    scene location_school_science_closeup
    show anon
    show okita 4 at right
    with dissolve
    anon "Alright, {b}Miss Okita{/b}. What do I have to do to get my grades up?"
    show okita 5
    okita "You're going to help me break free of my imposed banishment to the land of deficients."
    show okita 4
    anon f_worried "Huh? Banishment? What in the world are you on about?"
    show okita 3
    okita "Do you actually believe somebody of my intelligence belongs here, teaching basic science to a bunch of neanderthals?"
    show okita 4
    anon "Uhh..."
    show okita 3
    okita "You think this is what I aspire to do with my life?!"
    show okita 4
    anon @ f_skeptical "... No?"
    show okita 11
    okita "I used to be the bleeding edge, {b}[firstname]{/b}!"
    okita "I worked alongside some of the brightest minds on the planet, striving to forward humanity into the future!"
    show okita 11b
    anon f_normal "That sounds... Intense! How did you end up here?"
    show okita 11
    okita "One day my colleagues forced me out!"
    show okita 11b
    anon f_surprised "What?! Why did they do that?"
    show okita 5
    okita "Well, they claimed I was losing sight of the bigger picture."
    okita "That I'd become so concerned with advancing the science that I'd lost sight of the ethics I'd sworn to uphold."
    show okita 4
    anon f_worried @ -m_talk "..."
    show okita 11
    okita "The truth of the matter, is that they were just intimidated by my intelligence."
    okita "They couldn't keep up, so they banded together and got me blacklisted!"
    show okita 11b
    anon @ f_confused "Blacklisted? What does that mean?"
    show okita 3
    okita "It means no worthwhile scientific institution will have me!"
    show okita 11
    okita "I've been ostracized to live out a dull existence in a monotonous place like this..."
    okita "... Surrounded by children and half-wits!"
    show okita 11b
    anon "Well, that's a sad story and all but how am I supposed to help you?"
    show okita 3
    okita "Yes, well, it's simple really."
    show okita 5
    okita "I just need to finish what I started."
    show okita 4
    anon "Huh?"
    show okita 2
    okita "My inventions! The ones I was working on at Cuntech before those morons blacklisted me."
    okita "If I could just prove they work and get one of them published."
    show okita 1
    anon "You think that would get you your job back?"
    show okita 11
    okita "... I don't care about the job!"
    okita "I want to show those backstabbers just how foolish they were, dismissing {b}Tori Okita{/b}!"
    show okita 5
    okita "Besides, if even one of my inventions works, it'll be worth a fortune!"
    show okita 2
    okita "I'll buy my own lab!"
    show okita 1
    anon @ f_skeptical "... Still not seeing how I fit into all of this."
    show okita 5
    okita "Well, first off, I need you to {b}help me get into my office{/b}."
    show okita 4
    anon f_normal @ f_laugh "You're locked out of your own office?"
    show okita 5
    okita "Yeah, that tyrant {b}Mrs. Smith{/b} locked me out!"
    show okita 4
    anon "The principal?!"
    anon "Why would she do that?"
    show okita 5
    okita "She doesn't want me pursuing my pet projects during the school term."
    show okita 9
    okita "... Says I should remain one hundred percent focused on the curriculum."
    show okita 11
    okita "It's utter nonsense!"
    show okita 4
    anon f_worried @ f_confused "... How am I supposed to get you in?"
    show okita 5
    okita "With the {b}key code{/b} of course. {b}Mrs. Smith{/b} will have it {b}stashed away somewhere in her office{/b}, I'm sure."
    show okita 4
    anon "You want me to {b}break into the principal's office and steal from her{/b}?!"
    show okita 5
    okita "It's not really stealing... I just need you to figure out the code."
    show okita 3
    okita "Besides, you have nothing to lose... Remember?"
    show okita 4
    anon @ a_point f_skeptical "She could expel me!"
    show okita 5
    okita "Would it really matter? You'll be stuck here for another year regardless if you flunk my class..."
    show okita 4
    anon "Yeah, but..."
    show okita 3
    okita "Don't be foolish. This is a good deal! If you get the blueprints out of my office, help me build what's on them, and run a few tests to prove they work..."
    show okita 5
    okita "... I'll give you an A+ in my class."
    show okita 4
    anon f_normal "An A+?!"
    anon a_thinking f_thinking "Hmm..."
    anon "So, basically, either I help you do this or I'm stuck with a failing grade?"
    show okita 3
    okita "Yeah. Without my help, I calculate your odds of passing my class to be about 3,720 to 1."
    show okita 4
    anon a_idle f_worried @ f_skeptical "Sheesh, well, it's not like I have much choice then."
    show okita 7
    okita "You're finally starting to get a grasp on the situation!"
    show okita 6
    anon "So, how do I {b}get the key code from Mrs. Smith's office{/b}?"
    show okita 5
    okita "That's your problem."
    show okita 4
    anon f_sad_down "..."
    anon "Wonderful."
    show anon f_tired
    show okita 7
    okita "Best of luck, {b}[firstname]{/b}!"
    show okita 5
    okita "... Oh and while you're in my office, why don't you {b}grab a lab coat and a pair of safety glasses{/b}."
    okita "You're gonna need them."
    hide okita with dissolve
    anon f_sad_down "Ugh..."
    anon @ -m_talk "( I'll have to wait for {b}Mrs. Smith to leave her office if I want to search it properly{/b}. )"
    hide anon with dissolve
    return

label button_okita_get_keycode:
    scene location_school_science_closeup
    show anon
    show okita 3 at right
    with dissolve
    okita "Any luck getting that {b}key code{/b}?"
    show okita 4
    anon "I'm still working on it."
    show okita 3
    okita "Well, time is ticking."
    show okita 4
    anon f_worried "I know..."
    show okita 9
    okita "Tch..."
    hide okita with dissolve
    show anon f_sad_down
    anon "Ugh..."
    anon @ -m_talk "( I'll have to wait for {b}Mrs. Smith to leave her office if I want to search it properly{/b}. )"
    hide anon with dissolve
    return

label button_okita_foam_misshap:
    scene location_school_science_closeup
    show anon
    show okita 5 at right
    with dissolve
    okita "Good, you're here. We can get started."
    show okita 4
    anon "Yeah, alright."
    anon "So what are we building first?"
    show okita 5
    okita "I'll show you."
    hide anon
    show player 109f zorder 0 at Position(xpos=0.25, ypos=1.0)
    show okita 12 zorder 1 at Position(xpos=0.85, ypos=1.0)
    with dissolve
    okita "I call these beauties, the Okitatron Oculars."
    show bp 1 zorder 2 at Position(xpos=0.5, ypos=0.95) with dissolve
    pause
    anon "Glasses?"
    okita "Hah, not glasses..."
    hide bp with dissolve
    show player 109f
    show okita 12
    okita "These are an optical head-mounted display, a true ubiquitous computer."
    show anon f_worried
    hide player
    with dissolve
    show okita 13
    anon "I don't understand."
    show okita 9 at right
    with dissolve
    okita "Of course you don't. You're an imbecile."
    show okita 5
    okita "Let me just put it this way, the Okitatron Oculars will soon replace every smartphone on the planet."
    show okita 4
    anon "So it's a phone?"
    show okita 3
    okita "{i}*Sigh*{/i}"
    show okita 5
    okita "Let's just focus on building it, and once it's complete, I'll show you what it does..."
    show okita 4
    anon f_normal @ f_laugh "Works for me."
    anon "How do we start?"
    show okita 10b with dissolve
    okita "Hmm."
    show okita 10c
    okita "Well, I'm missing a few components..."
    show okita 10b
    okita "..."
    show okita 5 with dissolve
    okita "I can gather most of what we need on my own."
    show okita 3
    okita "Could you {b}find me a pair of lenses{/b}?"
    show okita 4
    anon @ f_thinking "{b}Lenses{/b}? Like in a telescope?"
    show okita 5
    okita "Not from a telescope. I need {b}lenses from a pair of spectacles. Specifically, varifocal lenses{/b}."
    show okita 4
    anon @ f_confused "{b}Varifocal{/b}?"
    show okita 3
    okita "Yes, that means it's a {b}lens{/b} with two different prescriptions; a top and a bottom."
    show okita 4
    anon f_surprised "Like for someone who is both nearsighted and farsighted?"
    show okita 2
    okita "Precisely!"
    show okita 1
    anon f_normal "Hmm, I might be able to track something like that down."
    show okita 3
    okita "Might?"
    show okita 1
    anon "I mean, I know a few people who wear glasses. Maybe one of them have a spare set."
    show okita 2
    okita "Very good. {b}Report back to me here, in the science lab, once you have them{/b}."
    show okita 1
    anon "Alright."
    hide anon with dissolve
    return

label button_okita_get_bifocal_lenses:
    scene location_school_science_closeup
    show anon
    show okita 3 at right
    with dissolve
    okita "Did you find what we need?"
    show okita 4
    anon "What did you want me to find again?"
    show okita 3
    okita "Pfft, you have one task to do and you've forgotten it?"
    show okita 4
    anon f_sad_down "I-I guess so..."
    show okita 9
    okita "Typical."
    show okita 5
    okita "I need you to {b}find a pair of varifocal lenses{/b}."
    show okita 4
    anon f_normal @ f_laugh a_point "Oh, right! Both farsighted and nearsighted."
    show okita 5
    okita "Correct."
    show okita 3
    okita "Perhaps I should write it backwards on your forehead, so you won't forget?"
    show okita 4
    anon f_worried "... No, that's alright. I've got it now."
    okita "Mmmhmm."
    hide okita with dissolve
    anon f_thinking a_thinking @ -m_talk "( Hmm, I should {b}check around school and see if someone has a spare set of varifocal lenses{/b}. )"
    hide anon with dissolve
    return

label button_okita_get_faptic_engine:
    scene location_school_science_closeup
    show anon
    show okita 4 at right
    with dissolve
    anon "Hey, {b}Miss Okita{/b}. Have you solved the problem with the glasses?"
    show okita 3
    okita "You mean the Okitatron Oculars?"
    show okita 4
    anon "Yeah, sorry. T-that's what I meant."
    show okita 5
    okita "Yes, I sorted it out. I'm in the process of patenting them now."
    show okita 4
    anon "That's good news, right?"
    show okita 5
    okita "It's good for a start."
    show okita 3
    okita "... But never mind the Oculars, {b}[firstname]{/b}!"
    okita "Yesterday's news!"
    show okita 1
    anon @ f_laugh "... O-okay."
    show okita 2
    okita "Today I've got something truly innovative!"
    show okita 1
    anon f_flirt "More innovative than X-ray glasses?"
    show okita 3
    okita "Oh, please. X-ray technology hasn't been innovative since the 1980s."
    show okita 1
    anon f_flirt_grin @ -m_talk "..."
    hide anon
    show player 109f zorder 0 at Position(xpos=0.25, ypos=1.0)
    show okita 12 zorder 1 at Position(xpos=0.85, ypos=1.0)
    with dissolve
    okita "I call this, the Okitatron Belt."
    show bp 2 zorder 2 at Position(xpos=0.5, ypos=0.95) with dissolve
    pause
    anon "... Belt?"
    okita "Yeah, the name could use some work..."
    hide bp with dissolve
    show player 109f
    show okita 12
    okita "But I'll worry about that later!"
    okita "For now, let's focus on what the device does."
    hide player
    show anon f_worried
    show okita 2 at right
    with dissolve
    okita "The Okitatron Belt is gonna revolutionize the way people keep in shape!"
    show okita 1
    anon @ -m_talk "..."
    anon "You mean it's a workout device?"
    show okita 2
    okita "No. This is going to make exercise a thing of the past!"
    okita "It targets all of the major muscle groups with undetectable micro-vibrations!"
    okita "It stimulates muscle growth so you'll never have to workout again!"
    show okita 1
    anon f_normal "That sounds incredible!"
    show okita 9
    okita "Well, of course it's incredible! Who do you think you're talking to?"
    show okita 1
    anon @ -m_talk "..."
    show okita 2
    okita "However, I'm missing a key component."
    show okita 1
    anon @ f_laugh "... Which is where I come in?"
    show okita 2
    okita "Precisely!"
    show okita 3
    okita "These micro-vibrations have to be fine-tuned to a very specific frequency otherwise, it won't work."
    show okita 1
    anon "Okay, so how do we do that."
    show okita 2
    okita "We'll need a {b}faptic engine{/b}."
    show okita 1
    anon f_worried @ f_skeptical "... Huh?"
    show okita 3
    okita "A {b}faptic engine{/b}."
    show okita 1
    anon f_hurt a_thinking @ -m_talk "..."
    show okita 9
    okita "{i}*Sigh*{/i}"
    show okita 5
    show anon f_worried a_idle with dissolve
    okita "{b}Go find June{/b}. She's helped me out with tough projects in the past."
    okita "{b}Tell her I sent you for a faptic engine{/b}."
    okita "She'll know what to do."
    show okita 4
    anon f_normal @ a_point "{b}Faptic engine{/b}. Alright, I'll be back."
    hide anon with dissolve
    show okita 9
    okita "Poor kid is dumber than a box of rocks..."
    return

label button_okita_get_faptic_engine_repeat:
    scene location_school_science_closeup
    show anon
    show okita 5 at right
    with dissolve
    okita "Back already? Do you have it?"
    show okita 4
    anon f_worried "Where am I supposed to get this {b}faptic engine{/b} thingy again?"
    show okita 9
    okita "{i}*Sigh*{/i}"
    show okita 5
    okita "Just {b}go talk to June{/b}, she will explain."
    show okita 4
    anon f_normal @ f_laugh "Oh, right! I'll be right back."
    hide anon with dissolve
    return

label button_okita_tired_from_belt:
    scene location_school_science_closeup
    show anon
    show okita 1 at right
    with dissolve
    anon @ a_wave "Hey, {b}Miss Okita{/b}! Are you feeling any better?"
    show okita 2
    okita "Never mind that, {b}[firstname]{/b}."
    okita "I'm glad you're here, there's work to be done!"
    show okita 1
    anon f_worried @ f_sad_down "{i}*Sigh*{/i} You never let up, do you?"
    show okita 5
    okita "I'll let up when my inventions are published and those Cuntech creeps are eating a big bowl of crow!"
    show okita 4
    anon "... Fine."
    anon "What crazy invention are we working on this time?"
    show okita 10c at Position(xpos=0.98, ypos=1.0) with dissolve
    okita "Hmm, we'll have to take a detour from the inventions for the time being."
    okita "At least until we get {b}Mrs. Smith{/b} off of my case!"
    show okita 10b
    anon "How are we supposed to accomplish that?"
    show okita 10c
    okita "I've been pondering that myself..."
    show okita 2 at right with dissolve
    okita "I think a simple mind wipe serum is our best course."
    show okita 1
    anon f_surprised "{i}Mind wipe{/i}? That doesn't sound good..."
    show okita 2
    okita "Bah, it's perfectly safe! So long as you follow my directions to the letter!"
    okita "The only thing she'll forget is her aversion to my experiments."
    show okita 1
    anon f_worried @ f_skeptical "You're sure?"
    show okita 3
    okita "Well, there's no way to be entirely sure without proper testing..."
    show okita 4
    anon @ -m_talk "..."
    show okita 9
    okita "She'll be fine!"
    show okita 4
    anon "... What do you need me to do?"
    show okita 5
    okita "You'll start by {b}gathering the ingredients{/b} we need."
    show okita 4
    anon "Ugh, alright. How many?"
    show okita 5
    okita "We'll need {b}five{/b} in total."
    show okita 101 at Position(xpos=1.01, ypos=1.0) with dissolve
    okita "Here's a list."
    hide anon
    show player 556 at left
    show okita 4 at right
    with dissolve
    anon "{b}Falicum mushroom{/b}, {b}Horny Toad extract{/b}, {b}Psychotropic Euphorbia{/b}, {b}base liquid{/b}..."
    show player 557
    anon "I've never even heard of these things before!"
    hide player
    show anon f_worried
    with dissolve
    show okita 2
    okita "Well, {b}falicum mushrooms grow in the forest{/b} here in Summerville."
    show okita 3
    okita "They are easy to spot because of their phallic shape."
    show okita 1
    anon "... Gross."
    show okita 2
    okita "The {b}Horny Toad and Psychotropic Euphorbia can also be found in the forest{/b}."
    show okita 1
    anon "Psychotropic what?"
    show okita 2
    okita "It's a luminescent flower... You might know it as the \"forget-me-not\" blossom."
    show okita 1
    anon "Nope, never heard of it."
    show okita 3
    okita "Really?"
    show okita 2
    okita "You'll only find it in dark places. Your {b}best bet would be a cave{/b}."
    show okita 1
    anon @ f_surprised "There are caves in Summerville?"
    show okita 3
    okita "Of course."
    show okita 2
    okita "As for the {b}Horny Toad{/b}, it's their breeding season. So {b}look for a pond or stream{/b}."
    okita "They should be easily identifiable by their lumpy purple backsides."
    show okita 1
    anon "Okay, that's not too bad, but {b}what about this base liquid{/b}? What is that?"
    show okita 2
    okita "We just need something mild to act as a base for the serum. {b}Vegetable stock would work best{/b}."
    okita "You should be able to {b}pick some up at Consum-R{/b}."
    show okita 1
    anon f_surprised "What about this last ingredient?"
    anon "{b}Mrs. Smith's DNA{/b}?!"
    anon f_confused "How the heck am I supposed to get that?!"
    show okita 3
    okita "... Yeah, that's gonna be the difficult one."
    show okita 2
    okita "A hair or saliva sample would work best."
    okita "I'm sure you'll figure something out..."
    show okita 1
    anon f_worried "Great..."
    anon "Well, I guess I had better get started."
    show okita 2
    okita "Come talk to me if you need help finding any of the ingredients."
    show okita 5
    okita "... And hurry up! We gotta get this done before {b}Mrs. Smith{/b} changes the code to my office again!"
    hide anon with dissolve


    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
