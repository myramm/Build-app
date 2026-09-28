label pa_announcement:
    if random.randint(1,100) < 5 and not game.timer.is_dark() and not game.timer.is_weekend() and M_smith.get("school intro done"):
        scene expression player.location.background_blur
        show anon f_normal_high with dissolve
        call expression "pa_announcement_{}".format(random.randint(1,23))
        anon @ -m_talk "..."
    return

label pa_announcement_1:
    PA "Attention seniors:"
    PA "The end of the term is quickly approaching and you know what that means..."
    PA "It's time to find yourself a date and hit the dance floor at our Annual Sorority Ball!"
    PA "We hope to see you all there!"
    return

label pa_announcement_2:
    PA "Attention students:"
    PA "This is a reminder that PDA is strictly forbidden within the halls of Summerville College..."
    PA "So keep your hands and more importantly your genitals to yourselves!"
    PA "Thank you and have a great day!"
    return

label pa_announcement_3:
    PA "Attention:"
    PA "{b}Mrs. Smith{/b}, you have a large package waiting for you in your office."
    show anon f_thinking
    PA "I repeat."
    PA "{b}Mrs. Smith{/b}, you have a large package waiting for you in your office."
    return

label pa_announcement_4:
    PA "Attention students:"
    PA "Taco Day in the cafeteria has been canceled, due to a malfunctioning refrigeration unit."
    PA "Chili will be served as a substitute."
    show anon f_thinking
    PA "... On an unrelated note. Anyone showing signs of food poisoning should be brought to the main office immediately."
    PA "Thank you and have a pleasant day!"
    return

label pa_announcement_5:
    PA "Attention faculty:"
    PA "Whoever left the brownies in the teachers' lounge is asked to report to {b}Mrs. Smith{/b}'s office ASAP."
    show anon f_thinking
    PA "I repeat."
    PA "Whoever left the brownies in the teachers' lounge is asked to report to {b}Mrs. Smith{/b}'s office ASAP."
    PA "Thank you!"
    return

label pa_announcement_6:
    PA "Attention students:"
    PA "This is a reminder that bullying is strongly frowned upon here at Summerville College."
    PA "Anyone who feels they are being bullied is encouraged to report the situation to our student well-being representative, {b}Dexter{/b}."
    PA "Thank you and have a pleasant day!"
    return

label pa_announcement_7:
    PA "Attention faculty:"
    PA "This is a reminder that alcoholic beverages are strictly prohibited within Summerville College."
    PA "This includes personal offices."
    show anon f_thinking
    PA "Thank you and have a pleasant day!"
    return

label pa_announcement_8:
    PA "Attention students:"
    PA "We would like to invite you all to come out and support our school Basketball Team."
    PA "I mean, sure. They're 0-12 this season but that doesn't mean we can't show our school pride by attending!"
    show anon f_laugh
    PA "Come and cheer them on as they look to acquire their first win of the season!"
    return

label pa_announcement_9:
    PA "Attention students:"
    PA "We are still looking to fill a few spots on the Summerville Athletics Team."
    PA "Speak with {b}Coach Bridget{/b} if you are interested in representing your school out on the track!"
    PA "... No wussies allowed."
    show anon f_laugh
    return

label pa_announcement_10:
    PA "Attention students:"
    PA "This is a reminder that defacing school property is a crime!"
    PA "... And any student caught doing this will be handed over to the proper authorities."
    PA "Thank you and have a pleasant day!"
    return

label pa_announcement_11:
    PA "Attention students:"
    PA "The Sexual Education DVDs stolen from {b}Coach Bridget{/b}'s office are still unaccounted for."
    show anon f_grin
    PA "If anyone has any information regarding the DVDs whereabouts or the person who stole them."
    PA "Please report to {b}Coach Bridget{/b} immediately!"
    show anon f_normal_high
    PA "Thank you and have a pleasant day!"
    return

label pa_announcement_12:
    PA "Attention music lovers:"
    PA "{b}Miss Dewitt{/b} is still looking for talented individuals to aid her in forming a school band."
    PA "If you have any interest, please report to her after class."
    PA "Thank you and have a pleasant day!"
    return

label pa_announcement_13:
    PA "Attention students:"
    PA "{b}Miss Okita{/b} would like to remind students that a lab coat and safety glasses must be worn inside the school lab at all times."
    PA "Anyone failing to abide this rule will be subject to strict disciplinary action."
    PA "Thank you and have a pleasant day!"
    return

label pa_announcement_14:
    PA "Attention:"
    PA "To the owner of the red Conda Hivic, license number - 637 5chw1f7y."
    PA "Your car is illegally parked and will be towed if you don't move it immediately."
    show anon f_thinking
    PA "... Again."
    PA "To the owner of the red Conda Hivic, license number - 637 5chw1f7y."
    PA "Your car is illegally parked and will be towed if you don't move it immediately."
    PA "Thank you!"
    return

label pa_announcement_15:
    PA "Attention art lovers:"
    PA "{b}Miss Ross{/b} will be offering a special, one time lecture, to students this Saturday."
    PA "... Entitled, 'Finding the Happiness in Everything!'"
    PA "Anyone attending is encouraged to bring snacks."
    PA "Thank you and have a pleasant day!"
    return

label pa_announcement_16:
    PA "Attention:"
    PA "{b}Miss Bissette{/b}, your presence is requested on the third floor immediately."
    PA "We have reports of a foul odor emanating from your office."
    show anon f_thinking
    PA "I repeat."
    PA "{b}Miss Bissette{/b} to the third floor, immediately."
    PA "Thank you!"
    return

label pa_announcement_17:
    PA "Attention students:"
    PA "This is a reminder that pornographic material is not allowed on school property."
    PA "... And yes, that does include nude drawings of green skinned fantasy characters."
    show anon f_surprised
    PA "Thank you and have a pleasant day!"
    return

label pa_announcement_18:
    PA "Attention students:"
    PA "This is a reminder that striking school property is expressly forbidden."
    PA "... Unless it's that piece of shit printer in the computer lab."
    PA "In which case it's expressly encouraged!"
    show anon f_laugh
    PA "Thank you and have a pleasant day!"
    return

label pa_announcement_19:
    PA "Attention students:"
    PA "We've received several complaints involving the theft of used panties from the locker room."
    PA "We encourage anyone with information regarding these incidents to come forward immediately."
    PA "Thank you and have a pleasant day!"
    return

label pa_announcement_20:
    PA "Attention cheerleaders:"
    PA "Tonight's practice has been suspended in favor of what {b}Coach Bridget{/b} referred to as, 'Real Sports.'"
    PA "Thank you and have a pleasant day!"
    return

label pa_announcement_21:
    PA "Attention basketball players:"
    PA "An extra extra small jockstrap was found abandoned after practice last night."
    PA "If the owner of said jockstrap would like to reclaim it, please come to the main office at your earliest convenience."
    PA "Thank you and have a pleasant day!"
    return

label pa_announcement_22:
    PA "Attention students:"
    PA "This is a reminder that your personal lockers are not meant for food storage."
    PA "Please be considerate of others and clean those disgusting things out once in a while..."
    PA "Thank you and have a pleasant day!"
    return

label pa_announcement_23:
    PA "Attention students:"
    PA "This is a reminder that roof access is strictly forbidden."
    PA "When asked about the subject, {b}Mrs. Smith{/b} commented, 'This isn't Japan, you fucking weebs...'"
    PA "Thank you and have a pleasant day!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
