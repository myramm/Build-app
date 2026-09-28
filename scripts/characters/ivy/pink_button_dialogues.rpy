label ivy_button_greet:
    show anon with dissolve
    ivy "Hi!"
    ivy "Can I help you with something?"
    anon f_worried a_behind_head "It's my first time here. I... Umm..."
    ivy @ f_laugh "It's okay! I understand! Everyone's a little shy when they first come here..."
    ivy "We have a large selection of {b}toys{/b} and {b}sexy apparel{/b} that you can view on our wall display."
    show anon f_surprised a_idle with dissolve
    ivy "We can also offer a... {b}full body massage session{/b} in one of our... Private rooms."
    ivy "Our masseuse uses a variety of natural body relaxation techniques... That will surely satisfy your needs..."
    anon f_normal @ f_confused "Oh... I didn't know you offered massages here."
    ivy @ f_laugh "It's one of our... Less advertised... Services."
    ivy "Would you like to see our massage selection {b}pamphlet{/b}?"
    return


label ivy_button_greet_repeat:
    show anon with dissolve
    ivy "Hi!"
    ivy "Can I help you with something?"
    return


label button_ivy_massage:
    anon f_shy "Could I see... Your massage pamphlet?"
    show ivy a_flyer with dissolve
    ivy "Sure! Suit yourself!"
    anon "Thanks..."
    return


label button_ivy_just_shopping:
    anon f_worried "I'm fine, thank you."
    anon "I'm just here to do some shopping..."
    show anon f_normal
    ivy @ f_laugh "Alright, then! Let me know if you need anything else."
    return


label button_ivy_massage_first:
    show ivy a_flyer
    anon f_normal @ f_shy "I guess I could have a look at it..."
    ivy "Sure! Suit yourself!"
    hide ivy
    hide anon
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
