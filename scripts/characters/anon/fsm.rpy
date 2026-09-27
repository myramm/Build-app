init -1 python:
    M_anon = Machine('anon')


init -3 python:
    T_ano01_cops = Trigger()

    T_ano02_food = Trigger()
    T_ano02_thug = Trigger()
    T_ano02_warn = Trigger()

    T_ano03_init = Trigger()

    T_ano04_init = Trigger()
    T_ano04_tony = Trigger()
    T_ano04_test = Trigger()
    T_ano04_work = Trigger()

    T_ano05_init = Trigger()
    T_ano05_prat = Trigger()
    T_ano05_deal = Trigger()
    T_ano05_cell = Trigger()
    T_ano05_bait = Trigger()
    T_ano05_sale = Trigger()
    T_ano05_wage = Trigger()
    T_ano05_work = Trigger()

    T_ano06_init = Trigger()
    T_ano06_cook = Trigger()
    T_ano06_coax = Trigger()
    T_ano06_work = Trigger()

    T_ano07_init = Trigger()
    T_ano07_deal = Trigger()
    T_ano07_mech = Trigger()
    T_ano07_find = Trigger()
    T_ano07_give = Trigger()
    T_ano07_perk = Trigger()
    T_ano07_sale = Trigger()
    T_ano07_wage = Trigger()
    T_ano07_work = Trigger()

    T_ano08_init = Trigger()
    T_ano08_sack = Trigger()
    T_ano08_work = Trigger()

    T_ano09_init = Trigger()
    T_ano09_brat = Trigger()
    T_ano09_deal = Trigger()
    T_ano09_vest = Trigger()
    T_ano09_blow = Trigger()
    T_ano09_sale = Trigger()
    T_ano09_wage = Trigger()
    T_ano09_work = Trigger()

    T_ano10_init = Trigger()
    T_ano10_tina = Trigger()
    T_ano10_tony = Trigger()

    T_ano11_init = Trigger()
    T_ano11_prep = Trigger()
    T_ano11_bone = Trigger()
    T_ano11_done = Trigger()

    T_ano12_init = Trigger()
    T_ano12_zoom = Trigger()
    T_ano12_dark = Trigger()
    T_ano12_oops = Trigger()

    T_ano13_init = Trigger()
    T_ano13_tony = Trigger()
    T_ano13_hint = Trigger()
    T_ano13_clue = Trigger()
    T_ano13_tina = Trigger()

    T_ano14_init = Trigger()
    T_ano14_sobs = Trigger()
    T_ano14_meet = Trigger()
    T_ano14_find = Trigger()
    T_ano14_tony = Trigger()
    T_ano14_done = Trigger()

    T_ano15_fail = Trigger()
    T_ano15_pass = Trigger()

    T_ano16_init = Trigger()
    T_ano16_tree = Trigger()

    T_ano17_init = Trigger()
    T_ano17_erik = Trigger()
    T_ano17_talk = Trigger()
    T_ano17_porn = Trigger()

    T_ano18_init = Trigger()
    T_ano18_yell = Trigger()
    T_ano18_yard = Trigger()
    T_ano18_rage = Trigger()
    T_ano18_trap = Trigger()
    T_ano18_hide = Trigger()
    T_ano18_flee = Trigger()

    T_ano20_init = Trigger()
    T_ano20_oval = Trigger()
    T_ano20_find = Trigger()
    T_ano20_open = Trigger()
    T_ano20_cops = Trigger()

    T_ano21_init = Trigger()
    T_ano21_cops = Trigger()
    T_ano21_home = Trigger()
    T_ano21_news = Trigger()

    T_ano22_init = Trigger()
    T_ano22_sign = Trigger()
    T_ano22_ally = Trigger()

    T_ano23_init = Trigger()
    T_ano23_seek = Trigger()
    T_ano23_help = Trigger()

    T_ano24_init = Trigger()
    T_ano24_seek = Trigger()
    T_ano24_find = Trigger()

    T_ano25_init = Trigger()
    T_ano25_plan = Trigger()
    T_ano25_sick = Trigger()
    T_ano25_find = Trigger()
    T_ano25_done = Trigger()

    T_ano26_init = Trigger()
    T_ano26_talk = Trigger()
    T_ano26_move = Trigger()
    T_ano26_take = Trigger()

    T_ano27_init = Trigger()
    T_ano27_home = Trigger()
    T_ano27_yumi = Trigger()
    T_ano27_tony = Trigger()
    T_ano27_plan = Trigger()
    T_ano27_jabb = Trigger()
    T_ano27_peek = Trigger()
    T_ano27_yolo = Trigger()
    T_ano27_free = Trigger()
    T_ano27_help = Trigger()
    T_ano27_boss = Trigger()

    T_ano28_init = Trigger()
    T_ano28_food = Trigger()
    T_ano28_clue = Trigger()
    T_ano28_dink = Trigger()
    T_ano28_cash = Trigger()
    T_ano28_debt = Trigger()


init python:
    S_ano00_init = State()
    S_ano00_done = State()


    S_ano01_init = State(_("I'm worried about [deb_name], but what can I do?"))
    S_ano01_cops = State(_("Someone's at the door downstairs. I wonder who?"))
    S_ano01_done = State(_("The cops are still investigating. I guess we just wait."))


    S_ano02_init = State(_("The cops are still investigating. I guess we just wait."))
    S_ano02_food = State(_("Something smells good! I should get to the kitchen; don't want to miss out!"))
    S_ano02_thug = State(_("Someone's at the door again. I wonder who?"))
    S_ano02_next = State(_("Woah. I just need to do something else for a while, and process."))
    S_ano02_warn = State(_("I can't let them get to me. I've just got to live my life."), delay=5)
    S_ano02_done = State(_("It's been a while since those guys showed up. Maybe they've decided to leave us alone."), delay=10)


    S_ano03_init = State(_("The streets feel safe again, I guess the cop patrols paid off."))
    S_ano03_done = State(_("This just got a whole lot more complicated. I need to sleep on it."))


    S_ano04_init = State()
    S_ano04_tony = State(_("I should go see Tony at the Pizzeria, maybe he can help. At least with a job."))
    S_ano04_test = State(_("Woah! $200! I need to return to Tony with a bike and prove I can do this job!"))
    S_ano04_work = State(_("Time to show Tony what a hard worker I am. Pizzas won't deliver themselves!"))
    S_ano04_done = State(_("So many pizzas, I'll never get sick of this smell! <3"))


    S_ano05_init = State(_("This bicycle is a real drag, didn't Tony mention something better?"))
    S_ano05_prat = State(_("Fingers crossed the car dealership has something in my price bracket!"))
    S_ano05_deal = State(_("What a fantastical douche! I hope the intern can be more help!"))
    S_ano05_cell = State(_("How do I get into these situations? I need to get her cellphone from the Manager's office."))
    S_ano05_bait = State(_("Mission accomplished! I should return Josie's phone to her right away."))
    S_ano05_sale = State(_("That was great! Hope I still get a discount though. I should talk to Josie."))
    S_ano05_wage = State(_("This scooter glides along so well! I can't wait to tell Tony!"))
    S_ano05_work = State(_("Delivering pizzas is so much easier now. I bet Tony has more deliveries for me."))
    S_ano05_done = State(_("I'm really getting the hang of this pizza thing now! \o/"))


    S_ano06_init = State(_("Food delivery is an essential service! I better get out there!"))
    S_ano06_cook = State(_("To the kitchen I go, let's hope Maria's a good teacher... Ready? Steady? Cook!"))
    S_ano06_wait = State(_("That was awkward, I got the day off though. Can see how things are tomorrow."))
    S_ano06_coax = State(_("I wonder how Tony and Maria are doing today."))
    S_ano06_work = State(_("This is no time to ease up, I'm doubling down on pizza deliveries!"))
    S_ano06_done = State(_("Pizza transportation is a precise business."))


    S_ano07_init = State(_("Not really sure what you're expecting anymore... It's obviously pizza delivery time!"))
    S_ano07_deal = State(_("Huh. Upgrades. Time to see what Josie might have for me at the dealership!"))
    S_ano07_mech = State(_("Kim: Wrong 'un. No question. I really hope Jiang can help, he'll be in the garage."))
    S_ano07_find = State(_("Jiang thinks he left his tools either at the apartment complex, the pool or in a toilet stall at mall."))
    S_ano07_give = State(_("Got 'em! Time to see if Jiang had any luck getting Kim to part with his phone."))
    S_ano07_perk = State(_("I should tell Josie the good news, maybe I'll even get a discount now!"))
    S_ano07_sale = State(_("Josie's dad is weeeird. Still I guess now I can see about that upgrade..."))
    S_ano07_wage = State(_("Not sure what Tony's going to make of this. Hopefully he'll be proud?"))
    S_ano07_work = State(_("Thankfully pizza won't deliver itself... I'd be out of a job!"))
    S_ano07_done = State(_("I didn't even know there were that many people in Summerville. They sure love pizza though."))


    S_ano08_init = State(_("Pizzaaaaa. Must deliver pizzaaaaa."))
    S_ano08_sack = State(_("Flour for a pretty lady? It's in the store room, and Maria's waiting."))
    S_ano08_work = State(_("Who knew NPCs had such a hankering for pizza? Better get to it."))
    S_ano08_done = State(_("I've delivered so much pizza, and not {i}one{/i} order for extra sausage? Come on already!"))


    S_ano09_init = State(_("There's nothing clever left to say. Pizza. Go. Deliver."))
    S_ano09_brat = State(_("Tony's right, as much as I love this nippy pink little number, it's time to move on."))
    S_ano09_deal = State(_("Seems the Russians were in the dealership. I wonder if Josie knows anything..."))
    S_ano09_vest = State(_("Seeee myyy vest! See my vest! Fetch it from the office, for this quest!"))
    S_ano09_blow = State(_("The things I'll do for a good deal... I wonder what kind of memes Josie has to show me..."))
    S_ano09_wait = State(_("That was nerve-racking... Josie is fearless! So exciting though, I need to calm down."))
    S_ano09_sale = State(_("I wonder if Josie's in the mood to make a sale now... Or will we get distracted again!"))
    S_ano09_wage = State(_("Aww yis! Tony's going to be so impressed, this'll be great for deliveries too!"))
    S_ano09_work = State(_("Just brought a new car. So there's only one possible thing to do now... Pizza delivery time!"))
    S_ano09_done = State(_("After all this delivering, I could really trade these margheritas for margaritas. >_>"))


    S_ano10_init = State(_("I never expected delivering pizza could pay so well!"))
    S_ano10_tina = State(_("The quicker I reach room 301 the better, this monstrosity of a pizza is almost starting to smell good!"))
    S_ano10_wait = State(_("Woah! I can't believe I finally got an \"extra sausage\" order... And it was from Becca's mom!"))
    S_ano10_tony = State(_("I wonder how Tony and Maria got on at the adoption agency. I should check in with them."))
    S_ano10_done = State(_("Well that blows! Tony and Maria would be great parents, and I hope Eddie can give us a lead."))


    S_ano11_init = State(_("Tony should have met with Eddie by now. I should head to the pizzeria and see what info we got."))
    S_ano11_prep = State(_("I can't decide if I'm more nervous or excited. Tony and Maria are expecting me this evening."))
    S_ano11_bone = State(_("No sense hanging around, just gotta push past the weirdness."))
    S_ano11_done = State(_("That was... Well anyway, I can't let Tony and Maria down, we'll just keep trying until she's pregnant."))


    S_ano12_init = State(_("Tony needs to see me urgently at the pizzeria. I wonder what's the matter!"))
    S_ano12_zoom = State(_("The binoculars will make scoping out the warehouse a cinch. I think they're in the treehouse."))
    S_ano12_dark = State(_("I have everything I need, all set to stake out the warehouse after dark."))
    S_ano12_oops = State(_("It's too open here, I need to find a good vantage point."))
    S_ano12_done = State(_("My head is killing me... I just need to lie down in my own bed."))


    S_ano13_init = State()
    S_ano13_tony = State(_("Oh man... I should go see Tony. He needs to know about what happened."))
    S_ano13_hint = State(_("I should talk to [deb_name] about this box of evidence."))
    S_ano13_clue = State(_("[deb_name] said she put the evidence in the attic, I wonder what's inside."))
    S_ano13_tina = State(_("Tony will want to see this! Maybe he can help identify that shady-looking guy too."))
    S_ano13_done = State(_("Wow... I can't believe Dad was really involved with the Russians... I need to sleep on this."))


    S_ano14_init = State(_("Tina said she could help with the lockbox. She works at the bank on weekdays."))
    S_ano14_sobs = State(_("Jeez, Kim is such an asshole, I should see if Liu is OK."))
    S_ano14_meet = State(_("Liu said I should meet her downstairs, I wonder what Dad could have been keeping here..."))
    S_ano14_find = State(_("Just need to find box number... Hmm, I should check the photo again."))
    S_ano14_tony = State(_("Empty! I just... Dang it! I wonder what Tony will make of this."))
    S_ano14_done = State()


    S_ano15_init = State(_("Security will be tight, but perhaps I can talk my way on to the Rump estate."))
    S_ano15_hint = State(_("The mayor's security seem pretty competent, but maybe if I keep trying I can catch them distracted."))
    S_ano15_done = State(_("I can't believe Erik just pulled off mysterious. I guess I'll meet him at the treehouse tomorrow."))


    S_ano16_init = State(_("I guess Erik has a plan... He said he'll be waiting at the treehouse in the afternoon."))
    S_ano16_tree = State(_("I can't say I'm not intrigued! I should get up there!"))
    S_ano16_done = State(_("Soooo, party at Erik's a little later then. What could I possibly do to pass the time..."))


    S_ano17_init = State(_("Party time! I should make sure to arrive at Erik's early this evening, before Iwanka."))
    S_ano17_erik = State(_("Hopefully Erik's got everything ready; if not, perhaps I can help."))
    S_ano17_talk = State(_("If Erik keeps this up, Iwanka will pass out before I can find out anything. I should speak with him."))
    S_ano17_porn = State(_("Iwanka needs me for something. With how much she's had to drink, I shouldn't keep her waiting."))
    S_ano17_done = State(_("I've peaked. Orgy anecdotes! Japanese tentacle porn! A blowjob! And a way into the Rump estate!?"))


    S_ano18_init = State(_("Time to head over to the Rump estate. I look like I could be an assistant... Right?"))
    S_ano18_yell = State(_("I wonder what all the shouting is about, a little peek couldn't hurt."))
    S_ano18_yard = State(_("Sounds like there's more happening outside. I should check out the backyard."))
    S_ano18_rage = State(_("Time to head back the way I came like they suggested."))
    S_ano18_trap = State(_("I wonder what the rest of this place looks like, it's so fancy."))
    S_ano18_hide = State(_("I can't get caught in here! I need to hide!"))
    S_ano18_flee = State(_("Now's my chance! Time to blow this popsicle stand!"))
    S_ano18_done = State(_("What are the odds? Real staff credentials! Now I can return to the Rump estate any time."))


    S_ano19_init = State(_("The mayor really didn't like anyone being in his office. Maybe Iwanka can help me get inside?"))
    S_ano19_code = State(_("Great! Melonia's on board, now I just need to get the code from Iwanka."))
    S_ano19_help = State(_("Great! Iwanka's on board, now I just need to convince Melonia to help with the guards."))
    S_ano19_done = State(_("Office code? Check! Guard patrols? Check! It's almost time!"))


    S_ano20_init = State(_("It's finally time. I should speak to Melonia in the evening about the guards."))
    S_ano20_oval = State(_("All clear! Time to find out what kind of secrets the mayor has been hiding in his office!"))
    S_ano20_find = State(_("There has to be something incriminating somewhere in here, better keep looking."))
    S_ano20_open = State(_("That safe definitely seems promising, if only I could figure out the combination..."))
    S_ano20_cops = State(_("Woah! I think this is what's known in the biz as a slam-dunk! I should get this to Harold. Now!"))
    S_ano20_done = State(_("I'll let Harold do his thing and go see him in the morning."))


    S_ano21_init = State()
    S_ano21_cops = State(_("Time to go see how Harold got on with the mayor, and how he's going to deal with the Russians."))
    S_ano21_home = State(_("I should have listened to Tony; if you want something done right, do it yourself."))
    S_ano21_news = State(_("Something's going on in the living room. Sounds like the TV is on. I wonder what's up?"))
    S_ano21_done = State(_("I can't watch any more. I'm done. I just want to have a nice long nap."))


    S_ano22_init = State(_("I wonder how Tony's feeling about Rump going down. Maybe I could swing by the pizzeria."))
    S_ano22_sign = State(_("Dad's grave... I've kinda been avoiding it... That stops now, in the clear light of day."))
    S_ano22_ally = State(_("Father Keeves, man. I'm speechless. It's almost like he took my breath away."))
    S_ano22_done = State(_("That was different. I should talk to Tony about this as soon as possible."))


    S_ano23_init = State(_("Time to fill Tony in about Nadya, no need to worry Maria though. I'll catch him at the pizzeria."))
    S_ano23_seek = State(_("Liu might be willing to help, I'll speak to her at the bank."))
    S_ano23_help = State(_("Wow, that guy is such a prick! I can't just leave Liu to his mercy!"))
    S_ano23_done = State(_("I really hope we can find something to nail Kim to the wall later!"))


    S_ano24_init = State(_("Liu said to visit her this evening. Apartment 204, Beachside."))
    S_ano24_seek = State(_("Something around here must hold a clue to Kim's criminality..."))
    S_ano24_find = State(_("Well that was a bust, hopefully the bedroom will yield a better result."))
    S_ano24_done = State(_("Huge success! Now Liu should be safe, and she'll help get the case! Bonus!"))


    S_ano25_init = State(_("The pizzeria is shut today, I'll meet Liu there tomorrow."))
    S_ano25_plan = State(_("Liu said she'd meet me at the pizzeria, I should head over there."))
    S_ano25_sick = State(_("The heist gear is at Tony's, I should head over there ASAP. Apartment 302, Beachside."))
    S_ano25_find = State(_("Tony's heist gear should be in his bedroom closet. Thankfully Maria's sleeping!"))
    S_ano25_done = State(_("Got it! Time to get out of here all sneaky-beaky like!"))


    S_ano26_init = State(_("Tony's said he'll meet me outside the bank on Tuesday morning."))
    S_ano26_talk = State(_("The guard is handled, I should deal with Liu, and make it convincing!"))
    S_ano26_move = State(_("I need to take Liu down to the vault and \"force\" her to open it."))
    S_ano26_take = State(_("Time's a-wastin'! I need to grab that case and skedaddle!"))
    S_ano26_done = State(_("Phew! We actually pulled it off! I should lay low and stay away from the bank."))


    S_ano27_init = State(_("Nadya said she'll be at Raven Hill in the evening. Am I ready for this?"))
    S_ano27_home = State(_("I think that went well. Time to grab some shut eye, need to make sure I'm well rested."))
    S_ano27_yumi = State(_("Oh shit! What the hell happened here!? I need to make sure everyone is OK!"))
    S_ano27_tony = State(_("I can't believe this is happening. I need to get over to the pizzeria right now!"))
    S_ano27_plan = State(_("Nadya's waiting at the warehouse, I hope Tony and Harold can keep from fighting each other..."))
    S_ano27_jabb = State(_("Never. Again. Now, Jab should be around here somewhere."))
    S_ano27_peek = State(_("Need to find a way to let Tony and Harold in, I should snoop around a bit."))
    S_ano27_yolo = State(_("Jab's no help, but something around here must be able to give me an advantage..."))
    S_ano27_free = State(_("Jenny and Debbie are probably on the ground floor, we should keep searching!"))
    S_ano27_help = State(_("Dimitri and fun sounds like a terrifying combination! I need to get in there now!"))
    S_ano27_boss = State(_("It's finally time. Time to get justice for my Dad. Raz will be in the office upstairs."))
    S_ano27_done = State()


    S_ano28_init = State()
    S_ano28_food = State(_("It does smell really good. I should get to the kitchen ASAP!"))
    S_ano28_clue = State(_("Liu invited me to her place for some fun. I should head over when she's not at work."))
    S_ano28_dink = State(_("What is it with Dad and hiding stuff in frames? It's old, but the Dink will be at the treehouse."))
    S_ano28_cash = State(_("Woah! This is a small fortune! Maybe Liu can help me deal with all this cash."))
    S_ano28_debt = State(_("Debbie is going to be so surprised when I tell her the house is safe! I can't wait!"))
    S_ano28_done = State()


init python:
    S_ano00_init.add(T_debbie_debt_help, S_ano00_done)
    S_ano00_done.add(T_all_sleep, S_ano01_init,
                     actions=('priority', 2))

    S_ano01_init.add(T_all_sleep, S_ano01_cops,
                     actions=('exec', 'game.lock_sleep()'))
    S_ano01_cops.add(T_ano01_cops, S_ano01_done,
                     actions=('exec', 'game.unlock_sleep()',
                              'set', (M_debbie, 'dad question')))
    S_ano01_done.add(T_all_sleep, S_ano02_init)

    S_ano02_init.add(T_all_sleep, S_ano02_food,
                     actions=('exec', 'game.lock_sleep()'))
    S_ano02_food.add(T_ano02_food, S_ano02_thug)
    S_ano02_thug.add(T_ano02_thug, S_ano02_next,
                     actions=('exec', 'game.unlock_sleep()'))
    S_ano02_next.add(T_all_tick, S_ano02_warn,
                     actions=('set', (M_debbie, 'bad guys question')))
    S_ano02_warn.add(T_ano02_warn, S_ano02_done)
    S_ano02_done.add(T_all_sleep, S_ano03_init)

    S_ano03_init.add(T_ano03_init, S_ano03_done)
    S_ano03_done.add(T_all_sleep, S_ano04_init)

    S_ano04_init.add(T_ano04_init, S_ano04_tony)
    S_ano04_tony.add(T_ano04_tony, S_ano04_test)
    S_ano04_test.add(T_ano04_test, S_ano04_work,
                     actions=('assign', ('player', 'deliveries', 3),
                              'assign', ('tony', 'cooldown',
                                         'game.timer._game_day + 3')))
    S_ano04_work.add(T_ano04_work, S_ano04_done)
    S_ano04_done.add(T_all_sleep, S_ano05_init)

    S_ano05_init.add(T_ano05_init, S_ano05_prat,
                     actions=('location', ('josie', {'place': L_dealership_showroom}),
                              'location', ('kim', {'place': L_dealership_showroom}),
                              'location', ('sato', {'place': L_dealership_office}),
                              'force', ('josie', {'flag': True}),
                              'force', ('kim', {'flag': True}),
                              'force', ('sato', {'flag': True})))
    S_ano05_prat.add(T_ano05_prat, S_ano05_deal,
                     actions=('location', ('kim', {'place': L_NULL})))
    S_ano05_deal.add(T_ano05_deal, S_ano05_cell,
                     actions=('unforce', 'kim'))
    S_ano05_cell.add(T_ano05_cell, S_ano05_bait)
    S_ano05_bait.add(T_ano05_bait, S_ano05_sale,
                     actions=('unforce', 'josie',
                              'unforce', 'sato'))
    S_ano05_sale.add(T_ano05_sale, S_ano05_wage)
    S_ano05_wage.add(T_ano05_wage, S_ano05_work,
                     actions=('assign', ('player', 'deliveries', 5),
                              'assign', ('tony', 'cooldown',
                                         'game.timer._game_day + 4')))
    S_ano05_work.add(T_ano05_work, S_ano05_done)
    S_ano05_done.add(T_all_sleep, S_ano06_init)

    S_ano06_init.add(T_ano06_init, S_ano06_cook)
    S_ano06_cook.add(T_ano06_cook, S_ano06_wait)
    S_ano06_wait.add(T_all_sleep, S_ano06_coax)
    S_ano06_coax.add(T_ano06_coax, S_ano06_work,
                     actions=('assign', ('player', 'deliveries', 4)))
    S_ano06_work.add(T_ano06_work, S_ano06_done)
    S_ano06_done.add(T_all_sleep, S_ano07_init)

    S_ano07_init.add(T_ano07_init, S_ano07_deal,
                     actions=('location', ('josie', {'place': L_dealership_showroom}),
                              'location', ('jiang', {'place': L_dealership_garage}),
                              'force', ('josie', {'flag': True}),
                              'force', ('jiang', {'flag': True})))
    S_ano07_deal.add(T_ano07_deal, S_ano07_mech)
    S_ano07_mech.add(T_ano07_mech, S_ano07_find)
    S_ano07_find.add(T_ano07_find, S_ano07_give,
                     actions=('unforce', 'josie'))
    S_ano07_give.add(T_ano07_give, S_ano07_perk)
    S_ano07_perk.add(T_ano07_perk, S_ano07_sale,
                     actions=('unforce', 'jiang'))
    S_ano07_sale.add(T_ano07_sale, S_ano07_wage)
    S_ano07_wage.add(T_ano07_wage, S_ano07_work,
                     actions=('assign', ('player', 'deliveries', 8),
                              'assign', ('tony', 'cooldown',
                                         'game.timer._game_day + 5')))
    S_ano07_work.add(T_ano07_work, S_ano07_done)
    S_ano07_done.add(T_all_sleep, S_ano08_init)

    S_ano08_init.add(T_ano08_init, S_ano08_sack)
    S_ano08_sack.add(T_ano08_sack, S_ano08_work,
                     actions=('assign', ('player', 'deliveries', 7)))
    S_ano08_work.add(T_ano08_work, S_ano08_done)
    S_ano08_done.add(T_all_sleep, S_ano09_init)

    S_ano09_init.add(T_ano09_init, S_ano09_brat)
    S_ano09_brat.add(T_ano09_brat, S_ano09_deal,
                     actions=('location', ('josie', {'place': L_dealership_showroom}),
                              'force', ('josie', {'flag': True})))
    S_ano09_deal.add(T_ano09_deal, S_ano09_vest)
    S_ano09_vest.add(T_ano09_vest, S_ano09_blow)
    S_ano09_blow.add(T_ano09_blow, S_ano09_wait,
                     actions=('unforce', 'josie'))
    S_ano09_wait.add(T_all_sleep, S_ano09_sale)
    S_ano09_sale.add(T_ano09_sale, S_ano09_wage)
    S_ano09_wage.add(T_ano09_wage, S_ano09_work,
                     actions=('assign', ('player', 'deliveries', 10),
                              'assign', ('tony', 'cooldown',
                                         'game.timer._game_day + 4')))
    S_ano09_work.add(T_ano09_work, S_ano09_done)
    S_ano09_done.add(T_all_sleep, S_ano10_init)

    S_ano10_init.add(T_ano10_init, S_ano10_tina,
                     actions=('location', ('tina', {'place': L_tina_lounge}),
                              'force', ('tina', {'flag': True}),
                              'unlocklocation', L_tina_lounge))
    S_ano10_tina.add(T_ano10_tina, S_ano10_wait,
                     actions=('location', ('becca', {'place': L_tina_lounge}),
                              'force', ('becca', {'flag': True}),
                              'clear', ('player', 'is_virgin')))
    S_ano10_wait.add(T_all_sleep, S_ano10_tony,
                     actions=('unforce', 'becca',
                              'unforce', 'tina',
                              'location', ('tony', {'place': L_pizzeria_interior}),
                              'force', ('tony', {'flag': True})))
    S_ano10_tony.add(T_ano10_tony, S_ano10_done,
                     actions=('unforce', 'tony'))
    S_ano10_done.add(T_all_sleep, S_ano11_init)

    S_ano11_init.add(T_ano11_init, S_ano11_prep,
                     actions=('location', ('maria', {'place': L_pizzeria_kitchen}),
                              'location', ('tony', {'place': [[L_pizzeria_storage] * 2 + [L_pizzeria_interior] * 2]}),
                              'force', ('maria', {'flag': True}),
                              'force', ('tony', {'flag': True})))
    S_ano11_prep.add(T_ano11_prep, S_ano11_bone,
                     actions=('location', ('maria', {'place': L_pizzeria_storage}),
                              'location', ('tony', {'place': L_NULL})))
    S_ano11_bone.add(T_ano11_bone, S_ano11_done,
                     actions=('unforce', 'maria',
                              'unforce', 'tony'))
    S_ano11_done.add(T_ano11_done, S_ano12_init,
                     actions=('location', ('tony', {'place': L_pizzeria_interior}),
                              'force', ('tony', {'flag': True})))

    S_ano12_init.add(T_ano12_init, S_ano12_zoom,
                     actions=('unforce', 'tony',
                              'condition', ('player.has_item("binoculars")',
                                            ('trigger', T_ano12_zoom))))
    S_ano12_zoom.add(T_ano12_zoom, S_ano12_dark)
    S_ano12_dark.add(T_ano12_dark, S_ano12_oops)
    S_ano12_oops.add(T_ano12_oops, S_ano12_done)
    S_ano12_done.add(T_all_sleep, S_ano13_init)

    S_ano13_init.add(T_ano13_init, S_ano13_tony)
    S_ano13_tony.add(T_ano13_tony, S_ano13_hint)
    S_ano13_hint.add(T_ano13_hint, S_ano13_clue)
    S_ano13_hint.add(T_ano13_clue, S_ano13_tina,
                     actions=('location', ('tina', {'place': L_pizzeria_interior}),
                              'force', ('tina', {'flag': True}),
                              'location', ('maria', {'place': L_pizzeria_interior}),
                              'force', ('maria', {'flag': True})))
    S_ano13_clue.add(T_ano13_clue, S_ano13_tina,
                     actions=('location', ('tina', {'place': L_pizzeria_interior}),
                              'force', ('tina', {'flag': True}),
                              'location', ('maria', {'place': L_pizzeria_interior}),
                              'force', ('maria', {'flag': True})))
    S_ano13_tina.add(T_ano13_tina, S_ano13_done,
                     actions=('location', ('tina', {'place': L_NULL,
                                                    'dow': [0, 1, 2, 3, 4],
                                                    'tod': [0, 1]}),
                              'force', ('tina', {'flag': True}),
                              'unforce', 'maria'))
    S_ano13_done.add(T_all_sleep, S_ano14_init,
                     actions=('set', ('tina', 'fertile')))

    S_ano14_init.add(T_ano14_init, S_ano14_sobs)
    S_ano14_sobs.add(T_ano14_sobs, S_ano14_meet,
                     actions=('location', ('liu', {'place': L_bank_office}),
                              'force', ('liu', {'flag': True})))
    S_ano14_meet.add(T_ano14_meet, S_ano14_find,
                     actions=('location', ('liu', {'place': L_bank_vault})))
    S_ano14_find.add(T_ano14_find, S_ano14_tony,
                     actions=('unforce', 'liu',
                              'unforce', 'tina'))
    S_ano14_tony.add(T_ano14_tony, S_ano14_done)
    S_ano14_done.add(T_ano14_done, S_ano15_init)

    S_ano15_init.add(T_ano15_pass, S_ano15_done)
    S_ano15_init.add(T_ano15_fail, S_ano15_hint)
    S_ano15_hint.add(T_ano15_pass, S_ano15_done)
    S_ano15_done.add(T_all_sleep, S_ano16_init,
                     actions=('location', ('erik', {'place': L_treehouse}),
                              'force', ('erik', {'tod': [1]})))

    S_ano16_init.add(T_ano16_init, S_ano16_tree,
                     actions=('location', ('erik', {'place': L_treehouse_interior}),
                              'force', ('erik', {'flag': True})))
    S_ano16_tree.add(T_ano16_tree, S_ano16_done,
                     actions=('location', ('erik', {'place': L_erikhouse_backroom}),
                              'force', ('erik', {'tod': [2]}),
                              'location', ('mrsj', {'place': L_erikhouse_entrance}),
                              'force', ('mrsj', {'tod': [2]})))
    S_ano16_done.add(T_all_tick, S_ano17_init)

    S_ano17_init.add(T_ano17_init, S_ano17_erik)
    S_ano17_erik.add(T_ano17_erik, S_ano17_talk,
                     actions=('location', ('erik', {'place': L_erikhouse_basement}),
                              'location', ('iwanka', {'place': L_erikhouse_backroom}),
                              'force', ('iwanka', {'flag': True})))
    S_ano17_talk.add(T_ano17_talk, S_ano17_porn)
    S_ano17_porn.add(T_ano17_porn, S_ano17_done,
                     actions=('unforce', 'erik',
                              'unforce', 'iwanka',
                              'unforce', 'mrsj'))
    S_ano17_done.add(T_all_sleep, S_ano18_init)

    S_ano18_init.add(T_ano18_init, S_ano18_yell,
                     actions=('location', ('consuela', {'place': L_rump_back}),
                             'force', ('consuela', {'tod': 1})))
    S_ano18_yell.add(T_ano18_yell, S_ano18_yard)
    S_ano18_yard.add(T_ano18_yard, S_ano18_rage,
                     actions=('location', ('iwanka', {'place': L_NULL}),
                              'force', ('iwanka', {'flag': True}),
                              'location', ('melonia', {'place': L_NULL}),
                              'force', ('melonia', {'flag': True})))
    S_ano18_rage.add(T_ano18_rage, S_ano18_trap)
    S_ano18_trap.add(T_ano18_trap, S_ano18_hide)
    S_ano18_hide.add(T_ano18_hide, S_ano18_flee)
    S_ano18_flee.add(T_ano18_flee, S_ano18_done,
                     actions=('unforce', 'consuela',
                              'trigger', T_iwa00_init,
                              'trigger', T_mel00_init))
    S_ano18_done.add(T_all_sleep, S_ano19_init,
                     actions=('unforce', 'iwanka',
                              'unforce', 'melonia'))

    S_ano19_init.add(T_mel05_init, S_ano19_code)
    S_ano19_init.add(T_iwa01_pier, S_ano19_help)
    S_ano19_code.add(T_iwa01_pier, S_ano19_done)
    S_ano19_help.add(T_mel05_init, S_ano19_done)
    S_ano19_done.add(T_all_tick, S_ano20_init)

    S_ano20_init.add(T_ano20_init, S_ano20_oval)
    S_ano20_oval.add(T_ano20_oval, S_ano20_find)
    S_ano20_find.add(T_ano20_find, S_ano20_open)
    S_ano20_open.add(T_ano20_open, S_ano20_cops,
                     actions=('location', ('harold', {'place': L_police_office}),
                              'force', ('harold', {'flag': True})))
    S_ano20_cops.add(T_ano20_cops, S_ano20_done,
                     actions=('unforce', 'harold'))
    S_ano20_done.add(T_all_sleep, S_ano21_init,
                     actions=('setdefaultloc', (
                                'iwanka', [[L_rump_second, L_boat_bridge, L_boat_bridge, L_NULL]]),
                              'setdefaultoutfit', (
                                'iwanka', [['naked', 'naked', 'swimsuit', 'naked']]),
                              'setdefaultloc', (
                                'melonia', [[L_rump_master, L_rump_back, L_rump_master, L_NULL]]),
                              'setdefaultoutfit', ('melonia', 'naked'),
                              'exec', rump_cleanup))

    S_ano21_init.add(T_ano21_init, S_ano21_cops,
                     actions=('location', ('harold', {'place': L_police_office}),
                              'force', ('harold', {'flag': True})))
    S_ano21_cops.add(T_ano21_cops, S_ano21_home,
                     actions=('unforce', 'harold',
                              'location', ('yumi', {'place': L_home}),
                              'force', ('yumi', {'flag': True}),
                              'location', ('debbie', {'place': L_home_livingroom}),
                              'force', ('debbie', {'tod': [1, 2]}),
                              'location', ('jenny', {'place': L_home_livingroom}),
                              'force', ('jenny', {'tod': [1, 2]})))
    S_ano21_home.add(T_ano21_home, S_ano21_news,
                     actions=('exec', 'game.lock_sleep()'))
    S_ano21_news.add(T_ano21_news, S_ano21_done,
                     actions=('exec', 'game.unlock_sleep()'))
    S_ano21_done.add(T_all_sleep, S_ano22_init,
                     actions=('unforce', 'debbie',
                              'unforce', 'jenny',
                              'location', ('tony', {'place': L_pizzeria_interior, 'dow': [0, 1, 2, 3, 4, 5]}),
                              'force', ('tony', {'tod': [2]})))

    S_ano22_init.add(T_ano22_init, S_ano22_sign,
                     actions=('unforce', 'tony'))
    S_ano22_sign.add(T_ano22_sign, S_ano22_ally)
    S_ano22_ally.add(T_ano22_ally, S_ano22_done)
    S_ano22_done.add(T_all_sleep, S_ano23_init,
                     actions=('location', ('tony', {'place': L_pizzeria_interior, 'dow': [0, 1, 2, 3, 4, 5]}),
                              'force', ('tony', {'tod': [2]})))

    S_ano23_init.add(T_ano23_init, S_ano23_seek,
                     actions=('unforce', 'tony'))
    S_ano23_seek.add(T_ano23_seek, S_ano23_help,
                     actions=('location', ('liu', {'place': L_bank_hallway}),
                              'force', ('liu', {'flag': True})))
    S_ano23_help.add(T_ano23_help, S_ano23_done,
                     actions=('unforce', 'liu',
                              'unlocklocation', L_liu_lounge))
    S_ano23_done.add(T_all_tick, S_ano24_init,
                     actions=('location', ('liu', {'dow': [6], 'place': L_NULL}),
                              'force', ('liu', {'flag': True})))

    S_ano24_init.add(T_ano24_init, S_ano24_seek,
                     actions=('location', ('liu', {'place': L_NULL})))
    S_ano24_seek.add(T_ano24_seek, S_ano24_find)
    S_ano24_find.add(T_ano24_find, S_ano24_done,
                     actions=('unforce', 'liu',
                              'locklocation', L_liu_lounge,
                              'exec', kim_cleanup))
    S_ano24_done.add(T_all_sleep, S_ano25_init,
                     actions=('setdefaultloc', ('yoyo', [[L_dealership_showroom,
                                                          L_dealership_showroom,
                                                          L_dealership_lounge,
                                                          L_NULL]])))

    S_ano25_init.add(T_ano25_init, S_ano25_plan,
                     actions=('location', ('liu', {'place': L_pizzeria_interior}),
                              'force', ('liu', {'flag': True}),
                              'location', ('maria', {'place': L_NULL}),
                              'force', ('maria', {'flag': True}),
                              'location', ('tony', {'tod': [2], 'place': L_pizzeria_interior}),
                              'location', ('tony', {'tod': [2], 'place': L_NULL, 'dow': [6], 'stack' : True}),
                              'force', ('tony', {'flag': True})))
    S_ano25_plan.add(T_ano25_plan, S_ano25_sick,
                     actions=('unforce', 'liu',
                              'location', ('maria', {'place': L_maria_lounge}),
                              'location', ('tony', {'dow': [1], 'tod': [0], 'place': L_bank, 'stack' : True})))
    S_ano25_sick.add(T_ano25_sick, S_ano25_find)
    S_ano25_find.add(T_ano25_find, S_ano25_done)
    S_ano25_done.add(T_ano25_done, S_ano26_init)

    S_ano26_init.add(T_ano26_init, S_ano26_talk,
                     actions=('location', ('tony', {'place': L_bank_lobby}),
                              'force', ('tony', {'flag': True})))
    S_ano26_talk.add(T_ano26_talk, S_ano26_move,
                     actions=('location', ('liu', {'place': L_bank_basement}),
                              'force', ('liu', {'flag': True})))
    S_ano26_move.add(T_ano26_move, S_ano26_take,
                     actions=('location', ('liu', {'place': L_bank_vault}),
                              'location', ('tony', {'place': L_bank_vault}),
                              'unlocklocation', L_liu_lounge))
    S_ano26_take.add(T_ano26_take, S_ano26_done)
    S_ano26_done.add(T_all_sleep, S_ano27_init,
                     actions=('unforce', 'liu',
                              'unforce', 'maria',
                              'unforce', 'tony'))

    S_ano27_init.add(T_ano27_init, S_ano27_home,
                     actions=('location', ('yumi', {'place': L_home_entrance})))
    S_ano27_home.add(T_ano27_home, S_ano27_yumi)
    S_ano27_yumi.add(T_ano27_yumi, S_ano27_tony)
    S_ano27_tony.add(T_ano27_tony, S_ano27_plan,
                     actions=('unforce', 'yumi',
                              'location', ('jab', {'place': L_warehouse_cargo}),
                              'force', ('jab', {'flag': True})))
    S_ano27_plan.add(T_ano27_plan, S_ano27_jabb)
    S_ano27_jabb.add(T_ano27_jabb, S_ano27_peek)
    S_ano27_peek.add(T_ano27_peek, S_ano27_yolo)
    S_ano27_yolo.add(T_ano27_yolo, S_ano27_free,
                     actions=('unforce', 'jab'))
    S_ano27_free.add(T_ano27_free, S_ano27_help)
    S_ano27_help.add(T_ano27_help, S_ano27_boss)
    S_ano27_boss.add(T_ano27_boss, S_ano27_done)
    S_ano27_done.add(T_all_sleep, S_ano28_init)

    S_ano28_init.add(T_ano28_init, S_ano28_food,
                     actions=('exec', 'game.lock_sleep()'))
    S_ano28_food.add(T_ano28_food, S_ano28_clue,
                     actions=('exec', 'game.unlock_sleep()',
                              'location', ('liu', {'place': L_liu_lounge}),
                              'force', ('liu', {'flag': True})))
    S_ano28_clue.add(T_ano28_clue, S_ano28_dink,
                     actions=('unforce', 'liu'))
    S_ano28_dink.add(T_ano28_dink, S_ano28_cash)
    S_ano28_cash.add(T_ano28_cash, S_ano28_debt)
    S_ano28_debt.add(T_ano28_debt, S_ano28_done)


init python:
    M_anon.add(
        S_ano00_init, S_ano00_done,
        S_ano01_init, S_ano01_cops, S_ano01_done,
        S_ano02_init, S_ano02_food, S_ano02_thug, S_ano02_next,
            S_ano02_warn, S_ano02_done,
        S_ano03_init, S_ano03_done,
        S_ano04_init, S_ano04_tony, S_ano04_test, S_ano04_work, S_ano04_done,
        S_ano05_init, S_ano05_prat, S_ano05_deal, S_ano05_cell, S_ano05_bait,
            S_ano05_sale, S_ano05_wage, S_ano05_work, S_ano05_done,
        S_ano06_init, S_ano06_cook, S_ano06_wait, S_ano06_coax,
            S_ano06_work, S_ano06_done,
        S_ano07_init, S_ano07_deal, S_ano07_mech, S_ano07_find,
            S_ano07_give, S_ano07_perk, S_ano07_sale, S_ano07_wage,
            S_ano07_work, S_ano07_done,
        S_ano08_init, S_ano08_sack, S_ano08_work, S_ano08_done,
        S_ano09_init, S_ano09_brat, S_ano09_deal, S_ano09_vest,
            S_ano09_blow, S_ano09_wait, S_ano09_sale, S_ano09_wage,
            S_ano09_work, S_ano09_done,
        S_ano10_init, S_ano10_tina, S_ano10_wait, S_ano10_tony, S_ano10_done,
        S_ano11_init, S_ano11_prep, S_ano11_bone, S_ano11_done,
        S_ano12_init, S_ano12_zoom, S_ano12_dark, S_ano12_oops, S_ano12_done,
        S_ano13_init, S_ano13_tony, S_ano13_hint, S_ano13_clue,
            S_ano13_tina, S_ano13_done,
        S_ano14_init, S_ano14_sobs, S_ano14_meet, S_ano14_find,
            S_ano14_tony, S_ano14_done,
        S_ano15_init, S_ano15_hint, S_ano15_done,
        S_ano16_init, S_ano16_tree, S_ano16_done,
        S_ano17_init, S_ano17_erik, S_ano17_talk, S_ano17_porn, S_ano17_done,
        S_ano18_init, S_ano18_yell, S_ano18_yard, S_ano18_rage, S_ano18_trap,
            S_ano18_hide, S_ano18_flee, S_ano18_done,
        S_ano19_init, S_ano19_code, S_ano19_help, S_ano19_done,
        S_ano20_init, S_ano20_oval, S_ano20_find, S_ano20_open,
            S_ano20_cops, S_ano20_done,
        S_ano21_init, S_ano21_cops, S_ano21_home, S_ano21_news, S_ano21_done,
        S_ano22_init, S_ano22_sign, S_ano22_ally, S_ano22_done,
        S_ano23_init, S_ano23_seek, S_ano23_help, S_ano23_done,
        S_ano24_init, S_ano24_seek, S_ano24_find, S_ano24_done,
        S_ano25_init, S_ano25_plan, S_ano25_sick, S_ano25_find, S_ano25_done,
        S_ano26_init, S_ano26_talk, S_ano26_move, S_ano26_take, S_ano26_done,
        S_ano27_init, S_ano27_home, S_ano27_yumi, S_ano27_tony, S_ano27_plan,
            S_ano27_jabb, S_ano27_peek, S_ano27_yolo, S_ano27_free,
            S_ano27_help, S_ano27_boss, S_ano27_done,
        S_ano28_init, S_ano28_food, S_ano28_clue, S_ano28_dink, S_ano28_cash,
            S_ano28_debt, S_ano28_done)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
