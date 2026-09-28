label crystal_police_cell_dialogue_roxxy_talk_to_crystal:
    scene police_cell
    show old_crystal jail 2
    show cell_bars at left
    show old_crystal_jail hands
    pause .5
    show player 5f at right
    show old_roxxy 3d at Position (xpos=700)
    with dissolve
    crystal "Is that mah daughter?"
    crystal "What are ya'll doing here?"
    show old_crystal jail 1
    show player 11f
    show old_roxxy 3
    roxxy "You really screwed up this time, {b}Mom{/b}!"
    roxxy "They foreclosed the trailer, and they're talking about sending you to prison!"
    show old_roxxy 3d
    show old_crystal jail 2
    crystal "Pfft, these pigs ain't gonna do nuthin'."
    crystal "They're all talk!"
    show old_crystal jail 1
    show player 5f
    show old_roxxy 3c
    roxxy "{b}Mom{/b}, this isn't a joke!"
    roxxy "They found a pound of meth!"
    roxxy "You're going to get sent away for a long time!"
    show old_roxxy 3d
    show old_crystal jail 2
    crystal "Phew, at least they didn't find the big stash!"
    show old_crystal jail 1
    show player 11f
    player_name "!!!" with hpunch
    show player 10f
    player_name "You mean there's more?!"
    show player 5f
    show old_crystal jail 2
    crystal "Huh?"
    crystal "I dunno what yer talkin' about..."
    crystal "Why'd you bring your boyfriend down here anyways?!"
    crystal "This is family business and it's personal!"
    crystal "Didn't I teach you that?"
    show old_crystal jail 3
    show old_roxxy 30
    roxxy "He's not my boyfrien-"
    show old_roxxy 3d
    roxxy "..."
    show old_roxxy 3c
    roxxy "Would you focus please!"
    roxxy "I know damn well that stuff all belongs to that idiot {b}Clyde{/b}!"
    show old_roxxy 3b
    show old_crystal jail 2
    crystal "What are you doin'?!"
    crystal "Shut yer mouth!"
    show old_crystal jail 3
    show old_roxxy 3c
    roxxy "Why are you taking the fall for him?"
    roxxy "This is his mess, not ours..."
    show old_roxxy 3d
    show old_crystal jail 2
    crystal "He's family, {b}Roxanne{/b}!"
    crystal "... And we take care of family!"
    crystal "Now, I know I taught you that!"
    show old_crystal jail 1
    show old_roxxy 30
    roxxy "This is stupid..."
    show old_roxxy 29
    show old_crystal jail 2
    crystal "I told your auntie I'd look after him while he was up here."
    crystal "I ain't about to watch him get hauled off to prison."
    show old_crystal jail 1
    show old_roxxy 3c
    roxxy "... And what am I supposed to do?!"
    roxxy "If you get convicted they're gonna repossess the trailer!"
    roxxy "Am I supposed to just sleep outside in the woods?"
    show old_roxxy 3b
    show old_crystal jail 2
    crystal "Don't be stupid."
    crystal "You can just go on down to live with your auntie and cousins."
    show old_crystal jail 1
    show old_roxxy 3
    roxxy "They live in an old run down cabin, in the middle of nowhere!"
    show old_roxxy 3d
    show old_crystal jail 2
    crystal "... So?"
    show old_crystal jail 1
    show old_roxxy 3
    roxxy "So, no fucking way!"
    roxxy "I'm gonna turn that jackass in myself and get the trailer back."
    show old_roxxy 3d
    show old_crystal jail 4
    crystal "{i}*Gasp*{/i}!"
    show old_crystal jail 2
    crystal "You'll do no such thing!"
    crystal "I didn't raise me no damned rat!"
    crystal "Now I dun told you, {b}Clyde{/b} is family and you don't snitch on family!"
    show old_crystal jail 3
    show old_roxxy 3b
    roxxy "..."
    show old_crystal jail 2
    crystal "You hear me girl?!"
    show old_crystal jail 3
    roxxy "..."
    show old_roxxy 3c
    roxxy "Yeah, we'll see..."
    roxxy "C'mon, {b}[firstname]{/b}. Let's get outta here."
    roxxy "I can't stand to look at her right now."
    hide old_roxxy with dissolve
    show player 5 with dissolve
    player_name "..."
    show old_crystal jail 2
    crystal "I'm not joking, {b}Roxanne{/b}!"
    crystal "If you snitch you can forget about livin' with me!"
    show old_crystal jail 3
    scene black with fade
    pause

    scene expression player.location.background_blur
    show player 5 at left
    show old_roxxy 3df at Position (xpos=400)
    show earl
    with dissolve
    earl "Well, did you have any luck convincing her to tell the truth about this mess?"
    show old_roxxy 29f
    roxxy "..."
    show player 10
    player_name "No, sir."
    show player 5
    earl "That's a damn shame..."
    player_name "..."
    show old_roxxy 3cf
    roxxy "What if I turned in the one responsible for all this?"
    show old_roxxy 3df
    earl "You got information for me?"
    show player 11
    show old_roxxy 3cf
    roxxy "I didn't say that!"
    roxxy "I'm just asking... \"What if.\""
    show old_roxxy 3bf
    show player 5
    earl f_tired @ -m_talk "Hmm..."
    earl "Well, if you did have information about the real culprit."
    earl "... And proof that your mother wasn't involved in the creation or distribution of the drugs."
    earl "I could get the charges dropped down to simple possession."
    show old_roxxy 3df
    earl "That's still a year in prison and a hefty fine."
    show old_roxxy 3bf
    roxxy "..."
    show old_roxxy 3cf
    roxxy "What if someone else hid the drugs in our trailer, and she didn't know about it?"
    show old_roxxy 3df
    earl f_normal "Oh, now that's interesting..."
    earl "If you could prove that she was unaware that someone else had hidden drugs in her home or had forced her to hide them against her will..."
    earl "... It's possible she won't see prison at all."
    show old_roxxy 3cf
    roxxy "... And the trailer?"
    show old_roxxy 3df
    earl @ f_tired -m_talk "Hmm..."
    earl "Well, she'd have to stay in jail until her trial."
    earl "In that case the trailer would need to remain foreclosed."
    earl "Unless you could post her bail money?"
    show player 12
    player_name "How much would that be?"
    show player 5
    earl "For this amount of narcotics?"
    earl "I'd expect nothing less than fifty thousand dollars..."
    show old_roxxy 2bf
    show player 23
    player_name "Holy crap!"
    show player 12
    player_name "That much?"
    show player 10
    player_name "Where would we get that kind of money?"
    show player 5
    show old_roxxy 14f
    roxxy "..."
    earl "Well, I'd best get back to work."
    earl "I'm sorry I can't do more to help you kids out..."
    show player 10
    player_name "Thanks again, Officer."
    show player 5
    hide earl with dissolve
    show player 10
    player_name "What are you gonna do?"
    show player 5
    show old_roxxy 33 at center with dissolve
    roxxy "... I dunno."
    roxxy "I could turn {b}Clyde{/b} in but that wouldn't really do me much good."
    roxxy "We'll still lose the trailer and {b}Mom{/b} will probably disown me."
    show old_roxxy 32
    player_name "..."
    show old_roxxy 33
    roxxy "I just need to think things over for a while."
    show old_roxxy 32
    show player 10
    player_name "... Do you need a place to stay? I'm sure my landlady wouldn't mind letting you crash on the couch for as long as you need."
    show player 5
    show old_roxxy 33
    roxxy "... No, thanks."
    roxxy "I can stay at {b}Becca{/b}'s place for a few days."
    show old_roxxy 32
    show player 10
    player_name "... Alright."
    player_name "I guess I'll see you at school then?"
    show player 5
    show old_roxxy 33
    roxxy "... Yeah."
    hide old_roxxy with dissolve
    player_name "( ... )"
    show player 24
    player_name "( Poor, {b}Roxxy{/b}. )"
    player_name "( I wish there was something I could do to help her. )"
    show player 90
    player_name "( ... Maybe I should {b}speak with Clyde{/b} tomorrow. )"
    player_name "( This whole mess is his fault after all... )"
    hide player with dissolve
    return

label crystal_police_cell_dialogue_default:
    scene police_cell
    show old_crystal jail 2
    show cell_bars at left
    show old_crystal_jail hands
    pause .5
    show player 5f at right
    with dissolve
    crystal "You best be keepin' your mouth shut about all this!"
    crystal "Ya hear me?!"
    show old_crystal jail 3
    show player 10f
    player_name "Y-yes, ma'am."
    show old_crystal jail 2
    show player 5f
    crystal "Good."
    crystal "Keep an eye on my daughter too, while yer at it..."
    crystal "I didn't raise her to be no snitch!"
    show old_crystal jail 3
    player_name "..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
