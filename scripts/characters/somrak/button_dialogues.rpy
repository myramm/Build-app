label button_somrak_afternoon_dialogue:
    scene expression player.location.background_closeup with None
    show anon
    show somrak
    with dissolve
    somrak "Ah, good afternoon, young monkey."

    show anon b_dressed_bow with dissolve
    anon "Hello, {b}Master Somrak{/b}."

    show anon b_dressed with dissolve
    somrak "Have you mastered those techniques I taught you?"

    anon "Saya kira demikian."

    return

label button_somrak_morning_dialogue:
    scene expression player.location.background_closeup with None
    show anon f_worried with dissolve
    anon @ -m_talk "( Best I not bother him while he's meditating. )"

    anon @ -m_talk "( I should seek him out in the {b}Afternoon{/b} if I want training. )"

    hide anon with dissolve
    return

label button_somrak_panties_repeatable_continue:
    show somrak f_normal
    show anon f_grin
    anon "Hehe, terima kasih!"

    show anon f_normal
    somrak "That's enough for today, I think."

    somrak "I want you to meditate tonight over the techniques I taught you."

    somrak "Burn them into your mind until understanding dawns upon you."

    show anon b_dressed_bow with dissolve
    anon "Yes, {b}Master Somrak{/b}!"

    hide anon with dissolve
    somrak "Until next time, young monkey!"

    hide somrak with dissolve
    return

label button_somrak_panties_next_times:
    show anon f_normal
    show somrak f_normal
    with dissolve
    anon "Phew, how was that?"

    somrak "Well, done, young monkey!"

    somrak "We'll make a tiger of you yet."

    return

label button_somrak_panties_first_time:
    show anon f_normal
    show somrak f_normal
    with dissolve
    somrak "Very good, young monkey!"

    somrak "I see a lot of potential in you."

    return

label button_somrak_panties_repeatable:
    show anon f_worried
    anon "Hmm, oke."

    anon "So, can we continue my training now?"

    show somrak f_normal
    somrak @ -m_talk "Hmmmm..."

    pause
    somrak "Baiklah."

    show anon f_normal
    show somrak a_back with dissolve
    somrak "Follow me to the heavy bag, and we'll begin the next phase of your training."

    hide anon
    hide somrak
    with dissolve
    return

label button_somrak_nevermind:
    show anon f_normal
    anon "Anyways, I'm just passing through."

    show anon b_dressed_bow with dissolve
    anon "I'll see you later, {b}Master Somrak{/b}."

    show anon b_dressed with dissolve
    show somrak f_normal
    somrak "Remember to keep your guard up, young monkey!"

    show somrak a_cane_up with dissolve
    show anon b_dressed_blocking with dissolve
    pause
    show somrak f_perv a_idle with dissolve
    somrak "Bagus..."

    hide anon
    hide somrak
    with dissolve
    return

label button_somrak_panties_obsession:
    show anon f_worried
    anon "{b}Master{/b}, what's with the whole panties thing?"

    show somrak f_normal
    somrak "Hmm?"

    anon "Why do you require your students to make offerings in used panties?"

    somrak "Because the shot of {b}chi energy{/b} makes me feel invigorated!"

    anon "Hah?"

    somrak "You are aware that women store a tremendous amount of {b}chi energy{/b} inside them, yes?"

    anon "{b}Chi{/b}?"

    somrak "{b}Life force{/b}, young monkey."

    somrak "Women store it in their bodies on a scale many thousand times greater than you or I."

    anon "Benar-benar?!"

    show somrak f_closed a_point with dissolve
    somrak "Oh ya."

    show somrak f_normal a_idle with dissolve
    somrak "They are absolutely infused with it!"

    show somrak f_perv
    somrak "So much so that it tends to leak out through their sex."

    anon @ f_skeptical "... And into their panties?"

    somrak "Just so!"

    somrak "I'm getting up in age, young monkey and my {b}chi{/b} is getting weaker and weaker."

    show somrak a_lick with dissolve
    somrak "One pair of these panties though is enough to make me feel almost young again!"

    show somrak f_closed a_eat with dissolve
    pause
    show somrak f_eat a_back with dissolve
    somrak "Aahhhh!"

    anon @ f_laugh "And here I thought you were just a creepy old pervert..."

    somrak "Oh, I'm absolutely a creepy old pervert!"

    show anon f_surprised
    somrak "... But the {b}chi{/b} thing is true too."

    show somrak f_closed
    somrak "Delicious."

    show somrak f_perv
    return

label button_somrak_monkey_thing:
    show anon f_worried
    anon "Do you have to keep calling me 'Monkey'?"

    show somrak f_normal
    somrak "Are you ashamed of what you are?"

    anon "Uhh {b}Master{/b}, I'm not a monkey..."

    somrak "{i}*Gasp*{/i} What do you think you are?"

    anon a_point_self f_unimpressed "... Human?"

    show somrak f_surprised
    pause
    show somrak f_laugh
    somrak "Hahahahaha!"

    anon f_worried a_idle "..."
    somrak "{i}*Snort*{/i} I'm sorry, I've just never met a monkey who thought he was human before..."

    show somrak f_normal
    anon f_unimpressed @ -m_talk "..."
    pause
    show somrak f_laugh
    somrak "Hahaha, I haven't laughed like this in ages!"

    show somrak f_normal
    somrak "Thank you, young monkey."

    anon @ -m_talk "..."
    somrak "If you learn nothing else from my teachings, learn this:"

    somrak "You can gather every little scrap of knowledge this world has to offer..."

    somrak "... But it's all worthless if you don't know yourself."

    anon f_worried "Apa maksudmu?"

    somrak "Learn your strengths, my student."

    somrak "Learn your weaknesses!"

    somrak "Understand your limitations."

    pause
    show somrak f_laugh
    somrak "And for god's sake, understand that you are a monkey of the lowest order."

    show somrak f_normal
    anon f_unimpressed @ -m_talk "..."
    anon "Jika Anda berkata demikian."

    somrak "Don't look so glum, young monkey."

    somrak "Take my lessons to heart and one day, I promise, you'll become the tiger you seek to be."

    show anon f_worried
    return

label button_somrak_more_training_not_trained_3:
    show somrak f_normal
    somrak "I'm afraid I cannot train you further without another offering."

    show anon f_tired a_facepalm with dissolve
    pause
    anon a_idle f_worried @ a_rub "You want another pair of {b}used panties{/b}?"

    show somrak f_perv
    somrak "Memang."

    anon f_sad_down "{i}*Sigh*{/i} I'll see what I can do..."

    show anon f_worried
    return

label button_somrak_more_training_not_trained_1:
    show anon f_normal
    anon "I'm ready to learn more, {b}Master Somrak{/b}."

    return

label button_somrak_more_training_not_trained_2:
    show somrak f_normal
    somrak "Very good, follow me to the heavy bag, and we'll begin the next phase of your training."

    hide somrak
    hide anon
    with dissolve
    return

label button_somrak_more_training_trained:
    show anon f_normal
    anon "I'm ready to learn more, {b}Master Somrak{/b}."

    show somrak f_normal
    somrak "Tsk, no, no, no!"

    somrak "You must meditate over the previous lesson first, silly monkey."

    somrak "Return to me tomorrow."

    anon f_worried "Ah, kawan..."

    hide anon
    hide somrak
    with dissolve
    return

label button_somrak_panties_story:
    show somrak a_meditation f_closed zorder 1
    with dissolve
    somrak "..."
    somrak "{i}*Mengendus*{/i}"

    show somrak f_perv
    somrak "Is that..."

    somrak "{i}*Sniff* *Sniff*{/i}"

    show anon f_worried zorder 0 with dissolve
    somrak "It is!!!"

    somrak "You've brought me panties, haven't you?!"

    show anon f_surprised
    pause
    anon f_worried @ f_skeptical "How can you tell?"

    show somrak a_hand with dissolve
    somrak "Give them here!"

    show anon f_shy_down a_backpack with dissolve
    pause
    show anon f_normal a_give_panties with dissolve
    anon "Here-"

    show anon f_surprised a_idle
    show somrak a_hand_panties
    with fastdissolve
    pause
    show somrak f_closed a_smell with dissolve
    somrak "{i}*Sniiiiiiiiiiiiiiff*{/i}"

    show somrak f_perv
    call expression game.dialog_select("somrak_panty_sniffin_dialogue_01_{}".format(M_somrak.get('delivered_panties')))
    show somrak f_closed
    somrak "{i}*Sniiiiiiiiiiiiiiff*{/i}"

    show somrak f_perv
    call expression game.dialog_select("somrak_panty_sniffin_dialogue_02_{}".format(M_somrak.get('delivered_panties')))
    show somrak f_closed
    somrak "{i}*Sniff* *Sniff*{/i}"

    show somrak f_perv
    call expression game.dialog_select("somrak_panty_sniffin_dialogue_03_{}".format(M_somrak.get('delivered_panties')))
    show somrak f_closed
    somrak "{i}*Sniiiiiiiiiiiiiiff*{/i}"

    show somrak f_perv
    call expression game.dialog_select("somrak_panty_sniffin_dialogue_04_{}".format(M_somrak.get('delivered_panties')))
    anon f_worried "K-kamu yakin?"

    show somrak f_closed
    somrak "{i}*Mengendus*{/i}"

    show somrak f_perv
    call expression game.dialog_select("somrak_panty_sniffin_dialogue_05_{}".format(M_somrak.get('delivered_panties')))
    show somrak f_perv a_idle with dissolve
    call expression game.dialog_select("somrak_panty_sniffin_dialogue_06_{}".format(M_somrak.get('delivered_panties')))
    return


label somrak_panty_sniffin_dialogue_01_Debbie:
    somrak "Oh, this is a high quality offering, young monkey!"

    return
label somrak_panty_sniffin_dialogue_02_Debbie:
    somrak "I sense, a mature woman..."

    return
label somrak_panty_sniffin_dialogue_03_Debbie:
    somrak "... Full of love and compassion."

    return
label somrak_panty_sniffin_dialogue_04_Debbie:
    somrak "I also sense strong feelings of loss and consternation."

    return
label somrak_panty_sniffin_dialogue_05_Debbie:
    somrak "... And just a hint of lilac."

    return
label somrak_panty_sniffin_dialogue_06_Debbie:
    somrak "I hope you're taking good care of the woman to whom these panties belong..."

    somrak "I sense that she would do anything for you."

    return

label somrak_panty_sniffin_dialogue_01_Jenny:
    somrak "Oh, this is an extremely high quality offering, young monkey!"

    return
label somrak_panty_sniffin_dialogue_02_Jenny:
    somrak "I sense, a young woman..."

    return
label somrak_panty_sniffin_dialogue_03_Jenny:
    somrak "... Full of greed and lust."

    return
label somrak_panty_sniffin_dialogue_04_Jenny:
    somrak "I also sense strong feelings of aimlessness and frustration."

    return
label somrak_panty_sniffin_dialogue_05_Jenny:
    somrak "... Mmm, she's a wild one and you'll find she won't be easily broken."

    return
label somrak_panty_sniffin_dialogue_06_Jenny:
    somrak "Be careful around this woman, young monkey."

    somrak "I sense that she will never be satisfied, no matter how much you sacrifice for her."

    return

label somrak_panty_sniffin_dialogue_01_Roxxy:
    somrak "Oh, this is an offer of the HIGHEST quality, young monkey!"

    return
label somrak_panty_sniffin_dialogue_02_Roxxy:
    somrak "I sense, a young woman..."

    return
label somrak_panty_sniffin_dialogue_03_Roxxy:
    somrak "... Full of anger and resentment."

    return
label somrak_panty_sniffin_dialogue_04_Roxxy:
    somrak "I also sense strong feelings of abandonment and insecurity..."

    return
label somrak_panty_sniffin_dialogue_05_Roxxy:
    somrak "... Mmm, she's waiting for the right man to save her."

    return
label somrak_panty_sniffin_dialogue_06_Roxxy:
    somrak "You should pursue the woman to whom these panties belong, young monkey."

    somrak "I sense that she will prove loving and loyal to the right man."

    return

label somrak_panty_sniffin_dialogue_01_Mia:
    somrak "Oh, this is an offer of the HIGHEST quality, young monkey!"

    return
label somrak_panty_sniffin_dialogue_02_Mia:
    somrak "I sense, a young woman..."

    return
label somrak_panty_sniffin_dialogue_03_Mia:
    somrak "... Full of hope and curiosity."

    return
label somrak_panty_sniffin_dialogue_04_Mia:
    somrak "I also sense strong feelings of confinement and boredom..."

    return
label somrak_panty_sniffin_dialogue_05_Mia:
    somrak "... Mmm, she's yearning to escape her prison and experience new things."

    return
label somrak_panty_sniffin_dialogue_06_Mia:
    somrak "You should help her to break her shackles, young monkey."

    somrak "I sense that her joyous demeanor will bring you nothing but happiness."

    return

label somrak_panty_sniffin_dialogue_01_Eve:
    somrak "Well now, this is interesting..."

    anon "Hmm?"

    return
label somrak_panty_sniffin_dialogue_02_Eve:
    somrak "Oh, this musk... It's truly intoxicating!"

    somrak "The owner of these panties must be very special, indeed!"

    return
label somrak_panty_sniffin_dialogue_03_Eve:
    somrak "I sense a vast amount of creativity and passion..."

    return
label somrak_panty_sniffin_dialogue_04_Eve:
    somrak "... But also loneliness and overwhelming feelings of self-doubt."

    return
label somrak_panty_sniffin_dialogue_05_Eve:
    somrak "... Mmm, this girl is hiding something, young monkey..."

    somrak "Something in her past that has scarred her deeply."

    return
label somrak_panty_sniffin_dialogue_06_Eve:
    somrak "If you intend to pursue her, I'd advise great caution..."

    somrak "I sense that if you break her heart, it might shatter completely."

    return

label somrak_panty_sniffin_dialogue_01_Grace:
    somrak "Oh, this is an extremely high quality offering, young monkey!"

    return
label somrak_panty_sniffin_dialogue_02_Grace:
    somrak "I sense, a young woman..."

    return
label somrak_panty_sniffin_dialogue_03_Grace:
    somrak "... Who hides behind a mask of selflessness and optimism."

    return
label somrak_panty_sniffin_dialogue_04_Grace:
    somrak "I sense that underneath the facade, she's tormented by anxiety and guilt."

    return
label somrak_panty_sniffin_dialogue_05_Grace:
    somrak "... Mmm, she's struggling to find balance in her life."

    return
label somrak_panty_sniffin_dialogue_06_Grace:
    somrak "You should try and help her, young monkey."

    somrak "I sense that she will repay your kindness tenfold."

    return

label somrak_panty_sniffin_dialogue_01_Odette:
    somrak "Oh, this is a unique offering, young monkey!"

    return
label somrak_panty_sniffin_dialogue_02_Odette:
    somrak "Hmm, there's a dark aura to these panties..."

    return
label somrak_panty_sniffin_dialogue_03_Odette:
    somrak "I sense a cunning mind and a penchant for mischief."

    return
label somrak_panty_sniffin_dialogue_04_Odette:
    somrak "I also sense that she's madly in love with someone close to her..."

    return
label somrak_panty_sniffin_dialogue_05_Odette:
    somrak "... Mmm, she's consumed by a desire to see those feelings returned."

    return
label somrak_panty_sniffin_dialogue_06_Odette:
    somrak "Be wary of this woman, young monkey."

    somrak "She'll sink her fangs into anyone to fill that void."

    return

label somrak_panty_sniffin_dialogue_01_Bridget:
    somrak "Wow, now that is one STRONG offering, young monkey!"

    return
label somrak_panty_sniffin_dialogue_02_Bridget:
    somrak "I sense, a mature woman..."

    return
label somrak_panty_sniffin_dialogue_03_Bridget:
    somrak "... Full of frustration and regret."

    return
label somrak_panty_sniffin_dialogue_04_Bridget:
    somrak "I sense that she's struggling to regain her identity..."

    return
label somrak_panty_sniffin_dialogue_05_Bridget:
    somrak "... Mmm, she's yearning to return to the life she left behind."

    return
label somrak_panty_sniffin_dialogue_06_Bridget:
    somrak "You'll need to be sound in body before attempting to aid her, young monkey..."

    somrak "I'd suggest you hit the weight bench."

    return

label button_somrak_has_panties:
    show anon f_worried
    anon "Hmm, oke."

    anon "So, you'll teach me now?"

    show somrak f_normal
    somrak @ -m_talk "Hmmmm..."

    pause
    show somrak f_closed
    somrak "Baiklah."

    show somrak f_normal
    anon f_normal "Akhirnya!"

    somrak "However, you must promise that you'll only use my teachings for good."

    somrak "The crane will not abide his techniques being used for evil."

    anon "Ehh, okay-"

    show somrak f_closed a_point with dissolve
    somrak "Unless said evil sees you into the bed of a stunningly beautiful woman!"

    show somrak f_normal a_idle with dissolve
    anon f_surprised "..."
    somrak "Is that understood?"

    show anon b_dressed_bow with dissolve
    anon "Yes, {b}Master Somrak{/b}."

    show anon b_dressed f_normal with dissolve
    somrak "Very good, young monkey."

    somrak "Your first lesson is this..."

    show somrak a_poke
    show anon b_dressed_blocking
    "{i}*Thunk*{/i}" with hpunch
    show somrak a_idle with fastdissolve
    hide anon
    show player 88 at left
    with dissolve
    anon "{i}*Huurk*{/i}"

    show somrak f_perv
    somrak "Always keep your guard up."

    show player 89b
    anon "{i}*Cough*{/i} Uggh..."

    show player 89
    show somrak f_normal
    somrak "Assume everyone wants to hit you..."

    somrak "... Because they do, young monkey!"

    pause
    somrak "Everyone wants to hit a person with a haircut as bad as yours..."

    show player 89b
    anon "Y-yes, {b}Master Somrak{/b}."

    show player 89
    show somrak a_back with dissolve
    somrak "Now, follow me to the heavy bag, and we'll see what we're working with."

    hide player
    hide somrak
    with dissolve
    return

label button_somrak_waiting_for_panties:
    show somrak a_meditation f_closed
    show anon f_worried
    with dissolve
    anon "{b}Master Somrak{/b}?"

    pause
    anon @ f_skeptical "Permisi?!"

    pause
    somrak "..."
    anon f_depressed "{i}*Huh*{/i}"

    hide somrak
    with dissolve
    anon "( It's no use. )"

    anon "( He's not gonna talk to me unless I bring him a pair of {b}used panties{/b}. )"

    pause
    anon f_worried @ -m_talk "( I should {b}speak with Kevin{/b} about this. )"

    hide anon with dissolve
    return

label button_somrak_start:
    show somrak a_meditation f_closed
    show anon f_worried
    with dissolve
    anon @ -m_talk "..."
    pause
    anon "Permisi, Pak?"

    pause
    pause
    anon "S-sir?"

    pause
    pause
    anon f_surprised @ f_skeptical "Umm, hello?"

    somrak "The crane does not suffer the monkey during meditation..."

    anon f_worried "A-apa?"

    anon "I don't understand..."

    somrak "{i}*Sigh*{/i} What do you want?"

    anon "Oh, um..."

    anon "I'm looking for {b}Master Somrak{/b}?"

    anon "He's supposed to be a {b}Muay Thai{/b} trainer here."

    anon "I-is that you?"

    somrak "Oooh, so the monkey wishes to become a tiger?"

    anon "... Hah?"

    somrak "Did you bring me an offering?"

    anon @ f_confused "O-offering?"

    show somrak f_perv a_idle with dissolve
    somrak "{i}*Sniff* *Sniff*{/i}"

    anon "Eh?"

    show somrak f_angry
    somrak "Eugh, I cannot teach you!"

    show somrak f_normal
    anon "What, how come?!"

    somrak "You reek of inexperience!"

    anon @ f_confused "Inexperience?!"

    anon "B-but I..."

    somrak "Listen closely, young monkey..."

    somrak "My teachings are ancient and VERY powerful!"

    somrak "But they come at a great cost and you are not prepared to pay it!"

    anon "What kind of cost?"

    show somrak f_perv
    pause
    somrak "{b}USED PANTIES{/b}!!!"

    anon f_skeptical "Hah?"

    somrak "You heard me, young monkey..."

    anon "Why in the heck would you need {b}used panties{/b}?!"

    show somrak f_normal
    somrak "One cannot fully unlock the tiger before taking down a gazelle..."

    anon @ -m_talk "..."
    anon "That doesn't make any-"

    show anon f_surprised
    show somrak f_angry a_point with dissolve
    somrak "Tsk, the monkey does not argue with the crane!"

    show somrak f_normal a_idle with dissolve
    anon f_worried @ -m_talk "..."
    anon "{i}*Sigh*{/i} So you won't teach me unless I bring you a pair of {b}used panties{/b}?"

    somrak "Ahh, finally understanding dawns upon the monkey..."

    show somrak f_closed a_meditation with dissolve
    anon "... Bagus."

    anon "I guess I'll be on my way then..."

    somrak @ -m_talk "..."
    show anon f_skeptical
    hide somrak
    with dissolve
    anon @ -m_talk "( What a weirdo! )"

    anon @ -m_talk "( Where am I going to get a pair of {b}used panties{/b}?! )"

    anon @ -m_talk "( I should {b}speak with Kevin{/b} about this. )"

    hide anon with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
