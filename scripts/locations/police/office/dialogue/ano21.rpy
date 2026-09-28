label ano21_cops_police_office:
    scene expression background() as stage
    show earl a_hips:
        xoffset -300
    show harold:
        flip
        xoffset -150
    show anon behind earl with dissolve:
        flip
        xoffset 100
    earl "This is quite the collar {b}Harold{/b}."
    earl "I don't know how your contact got his hands on that evidence but it's the proverbial smoking gun."
    harold "Yes, sir."
    harold f_smirk @ a_hands_up "Oh, actually..."
    show earl with {'master': dissolve}:
        flip
        xoffset 110
    harold "... Here's the guy who brought it in now."
    earl f_confused "This kid?"
    show anon f_sad_down
    harold "That's right, sir."
    anon f_unimpressed @ a_frustrated "I'm not a kid."
    earl f_normal @ f_laugh "Whoa, heh... Take it easy, slick."
    earl "I didn't mean to offend."
    pause
    earl f_happy "What's your name, son?"
    anon f_normal "{b}[firstname]{/b}."
    earl "Well, {b}[firstname]{/b}..."
    show earl a_handshake
    show anon a_empty
    with dissolve
    earl "... You did good work bringing that stuff in!"
    earl "That scumbag {b}Rump is downstairs in our lockup{/b} because of you."
    earl "He's gonna be going away for a long time."
    anon "Good."
    earl "Tell me, son."
    earl "Have you ever considered joining the force one day?"
    anon f_surprised "Me?"
    anon "A police officer?"
    show earl a_hips
    show anon a_idle
    with dissolve
    earl "{b}Harold{/b} here tells me you're quite the little detective."
    pause
    anon f_shy "Ehh, no... Not really, sir."
    earl "Well, I think you should give it some thought."
    earl "I could use a man with your gumption."
    anon "Umm, yeah... Okay?"
    anon "Maybe."
    pause
    show earl with dissolve:
        unflip
        xoffset -300
    earl f_normal "Don't forget you've got roll call in an hour."
    harold "Of course, sir."
    earl @ a_point_back "I'll be on the horn with Chief Lassard if you need me."
    harold "Good luck!"
    earl f_happy "Heh, I don't need luck {b}Harold{/b}."
    hide earl
    show harold:
        unflip
        xoffset -600
    with dissolve
    earl "I just need a hot cup of joe and a couple of those jelly donuts from the break room!"
    show harold with dissolve:
        flip
        xoffset 0
    anon f_skeptical "Chief Lassard?"
    harold "He's trying to requisition some officers from up north to help us with our mafia problem."
    anon f_normal "Does that mean you guys are going to move on them soon?"
    harold f_suspicious "\"Move on them?\""
    harold f_smirk "Where'd you learn to talk like that, kid?"
    anon f_unimpressed "Don't call me kid!"
    anon f_shy @ a_behind_head "And I dunno... Cop shows on TV, I guess."
    harold "Well, {b}[firstname]{/b}, I'm afraid I can't really give you a timeline yet."
    harold "We can't really proceed with anything until the Captain gets us some support."
    anon "Yeah, but that shouldn't take too long, right?"
    harold @ f_suspicious "I have no idea."
    harold "They could have guys down here in a few days or it could take months."
    anon f_shock "Months?!"
    anon f_angry a_sides @ a_frustrated "My friends and I can't wait months for you guys to resolve this!"
    harold f_concerned @ a_hands_up "I'm sure it won't take months."
    harold "But you gotta understand that as of this moment, we are not staffed to take on an organization this large."
    anon "So what am I supposed to do, {b}Harold{/b}?!"
    anon "They're threatening to kill us."
    harold "That's not going to happen."
    harold "You have my word."
    harold "In fact, I'm assigning {b}Officer Yumi{/b} to look after you guys until this matter is resolved."
    harold "She's going to be outside your home twenty-four seven."
    anon @ -m_talk "..."
    harold "If we're lucky, this \"{b}Raz Putin{/b}\" character will realize he's vulnerable now with {b}Rump{/b} behind bars."
    harold "He might even pack up his goons and flee the country."
    anon "How would that be lucky?!"
    anon "They killed my dad and you want to let them get away with it?!"
    harold "Of course not, {b}[firstname]{/b}..."
    harold "I wanna see these animals pay for their crimes just as much as you."
    anon "Do you?"
    anon "Because you sure as hell haven't done much to prove it!"
    harold f_angry a_hips "C'mon, that's not fair."
    harold "We're doing everything we can to-"
    anon "You wouldn't have even gotten {b}Rump{/b} if I hadn't handed him to you on a silver platter!"
    show harold f_concerned
    anon "{b}Tony{/b} was right about you guys being worthless..."
    hide anon with dissolve
    harold f_surprised a_hands_up "Hey, where are you going?"
    harold f_concerned "{b}[firstname]{/b}?!"
    show harold a_hips
    pause
    harold "Grr!"
    harold f_angry "{b}Yumi{/b}!"
    harold "I need you over here now!"
    show yumi with dissolve
    yumi "Sir?"
    harold "I want you to get over to the Cummings residence ASAP and check on the family."
    yumi "Right away, sir!"
    harold f_suspicious "And pack a bag."
    harold "You're gonna be there a while."

    scene expression background(l=L_police_front)
    show anon f_angry a_sides
    with fade
    anon @ -m_talk "( {i}*Sigh*{/i} I can't believe, after all this... The Russians might just get away with it. )"
    anon @ -m_talk "( I can't let that happen. )"
    anon @ -m_talk "( There has to be something I can do! )"
    anon @ -m_talk "( Maybe {b}Tony{/b} will have an idea? )"
    anon @ -m_talk "( {b}I should speak with him.{/b}} )"
    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
