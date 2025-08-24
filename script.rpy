label start:
    #SCENE 1: MC SELF INTRO
    scene bg room             #the bedroom bg

    $ name = renpy.input("To start, please enter a name.")
    $ name = name.strip()

     #in the case they dont write a name
    if not name:         
        $ name = "Ash"

    define mc = Character("[name]")
    define cl = Character ("Client 1")
    
    mc "Why does one write?"
    mc "I suppose everyone has a different answer."
    mc "But for me? Well..."
    mc "It’s because writing feels like reaching out your hand."
    mc "Both to ask for help and to offer help to others."
    mc "To make an impact, big or small, by doing what I love— That is my goal."
    mc "Which is why... I’m a freelance writer now!"

    #SCENE 2: CLIENT 1
    scene bg office        #purely for transition
    "The next day!"

    scene bg room
    mc "My first day! My first ever client!!"
    mc "Now, let's see..."

    #click logbook choice
    menu:
        "Open logbook":
            call logbook        #using call here para makabalik to this point once it reaches the return statement sa logbook 

    #SCENE 3: FLASHBACK
    scene bg office
    "Earlier that day!"
    
    mc "No one’s knocking yet… It’s been hours since I opened…"
    mc "Did I flop?..."
    mc "!!!"                     #audio here
    mc "Come in!"

    cl "Hello!!!! Are you [name]? Am I in the right place?"
    mc "Yes, yes— that’s me!" 
    mc "You're at the right tiny office with the right tiny desk." 
    mc "And you are?"
    cl "Nice! I’m Kadita!"
    mc "Nice to meet you, Kadita."
    mc "Please have a seat. How can I help you?"
    cl "Okay. Soooo, this is kind of last minute… but I really need help writing a cover letter."
    # ... continue dialogue here

    #SCENE 4: LETTER
    scene bg room
    "Back to present time..."

    default score = 0

    mc "Okay! Let's start!"

    #1
    menu:
        mc "Since this is a cover letter, what appropriate greeting should be used…"

        "Dear Mrs. XYZ,":
            $ score += 1
        "To whom it may concern":
            pass
    
   #2
    menu:
        mc "Hmm… In the intro, I should mention briefly why my client wants to apply for the job:"

        "This job looks super cool and I think I’d vibe well with the team":
            pass
        "This opportunity deeply aligns with my goals and values":
            $ score += 1

    #3
    mc "Wow… such a long list of experiences, Mx. C1 sure is passionate about this field. So:"
    menu:
        mc "My experiences (align/aligns) with your organization’s mission."

        "align":           
            $ score += 1
        "aligns":
            pass

    #4
    mc "Then how should I phrase their volunteer works…"
    menu:
        mc "I (lead/led) multiple campaigns promoting composting and sustainability in urban neighborhoods."
        
        "lead":
            pass
        "led":
            $ score += 1

    #5
    menu:
        mc "More about their skills and edge… Write: I am familiar with local environmental regulations and (had/have) hands-on experience collecting field samples and recording environmental data."

        "had":
            pass
        "have":
            $ score += 1

    #6
    mc "I want to mention how much the client is willing to grow too.."
    menu:
        mc "This role complements my commitment to (continuous/continuos) learning, professional growth, and taking part in impactful, on-the-ground environmental efforts."
    
        "continuous":
            $ score += 1
        "continuos":
            pass

    #7
    mc "…Almost done! Let’s wrap this up with intent and clarity."
    menu:
        mc "I hope to contribute meaningfully (to/with) your mission and values."

        "to":
            $ score += 1
        "with":
            pass

    mc "Wooh! I did it! My first ever commission! I hope it passes the standard of the client!"
    mc "total count: [score]"        #not final pero tama to

    #add feedback / scoring system
    
    return

#logbook
label logbook:
    #show client 1 profile
    mc "Hmm..."
    return


