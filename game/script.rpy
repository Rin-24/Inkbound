#reminder (for later): make a label for each client for organization

label start:
    #SCENE 1: MC SELF INTRO
    scene bg room             #the bedroom bg

    $ name = renpy.input("To start, please enter a name.")
    $ name = name.strip()

     #in the case they dont write a name
    if not name:         
        $ name = "Ash"

    define mc = Character("[name]", color = "#627d8e")        #color based on mc's color palette
    define cl = Character ("Client 1", color = "#58b0a1")     #color based on cl's color palette
    
    mc "Why does one write?"
    mc "I suppose everyone has a different answer."
    mc "But for me? Well..."
    mc "It’s because writing feels like reaching out your hand."
    mc "Both to ask for help and to offer help to others."
    mc "To make an impact, big or small, by doing what I love— That is my goal."
    show mc base center
    mc "Which is why... I’m a freelance writer now!"
    hide mc base center

    #SCENE 2: CLIENT 1
    scene bg office        #purely for transition
    "The next day!"

    scene bg room
    show mc base center
    mc "My first day! My first ever client!!"
    mc "Now, let's see..."
    hide mc base center

    #click logbook choice
    menu:
        "Open logbook":
            call logbook        #using call here para makabalik to this point once it reaches the return statement sa logbook 

    #SCENE 3: FLASHBACK
    scene bg office
    "Earlier that day!"

    show mc base center
    mc "No one’s knocking yet… It’s been hours since I opened…"
    mc "Did I flop?..."
    mc "!!!"                     #audio here
    mc "Come in!"
    hide mc base center

    show cl base center
    cl "Hello!!!! Are you [name]? Am I in the right place?"
    hide cl base center

    show mc base center
    mc "Yes, yes— that’s me!" 
    mc "You're at the right tiny office with the right tiny desk." 
    mc "And you are?"
    hide mc base center

    show cl base center
    cl "Nice! I’m Kadita!"
    hide cl base center

    show mc base center
    mc "Nice to meet you, Kadita."
    hide mc base center

    show mc base left
    mc "Please have a seat. How can I help you?"
    hide mc base left

    show cl base right
    cl "Okay. Soooo, this is kind of last minute… but I really need help writing a cover letter."
    hide cl base right

    show mc base left
    mc "Sure! Are you applying for a job?"
    hide mc base left

    show cl base right
    cl "Yep. I want to apply as an Assistant to an Environmental Specialist in this Organization."
    hide cl base right

    show mc base left
    mc "Ooh, interesting!"
    mc "Alright, a few quick questions first so you get the kind of letter you need."
    mc "Who’s the letter addressed to?"
    hide mc base left

    show cl base right
    cl "It says Mrs. XYZ in the poster of the regional environmental office. I can send you the details later!"
    hide cl base right

    show mc base left
    mc "Noted. What kind of tone do you want to go for? Formal and strictly professional? Or something more warm and personal?"
    hide mc base left

    show cl base right
    cl "The latter please! Still professional, of course, but I want them to see I’m genuine and not robotic."
    hide cl base right

    show mc base left
    mc "Haha got it!"
    mc "And for the last one: What exactly do you want this letter to do? Get you in the door? Show off your passion? Highlight your background?"
    hide mc base left

    show cl base right
    cl "Well, all of that! If it’s not much trouble hehe"
    cl "But mostly— I want to secure the interview. I want them to read the letter and not hesitate to contact me. If they talk to me, I know I can convince them!"
    hide cl base right

    show mc base left
    mc "Woah, so confident. I like your energy!"
    hide mc base left

    show cl base right
    cl "Hehe, thank you! Here’s the rest of my details and background that I feel is necessary to add by the way."
    hide cl base right

    show mc base center
    mc "Don’t worry, I will get this letter back right away after I finish it. Hope you get the interview!"
    hide mc base center

    show cl base center
    cl "Ah you’re such a life saver. I’m kind of busy with my other papers so I need all the help that I can get right now. I’m counting on you!"
    hide cl base center

    #SCENE 4: LETTER
    scene bg room
    "Back to present time..."

    default score = 0

    mc "Okay! Let's start!"

    #1
    menu:
        mc "Since this is a cover letter, what appropriate greeting should be used…"

        "\"Dear Mrs. XYZ,\"":
            $ score += 1
        "\"To whom it may concern\"":
            pass
    
   #2
    menu:
        mc "Hmm… In the intro, I should mention briefly why my client wants to apply for the job:"

        "\"This job looks super cool and I think I’d vibe well with the team\"":
            pass
        "\"This opportunity deeply aligns with my goals and values\"":
            $ score += 1

    #3
    mc "Wow… such a long list of experiences, Mx. C1 sure is passionate about this field. So:"
    menu:
        mc "My experiences (align/aligns) with your organization’s mission."

        "\"align\"":           
            $ score += 1
        "\"aligns\"":
            pass

    #4
    mc "Then how should I phrase their volunteer works…"
    menu:
        mc "I (lead/led) multiple campaigns promoting composting and sustainability in urban neighborhoods."
        
        "\"lead\"":
            pass
        "\"led\"":
            $ score += 1

    #5
    menu:
        mc "More about their skills and edge… Write: I am familiar with local environmental regulations and (had/have) hands-on experience collecting field samples and recording environmental data."

        "\"had\"":
            pass
        "\"have\"":
            $ score += 1

    #6
    mc "I want to mention how much the client is willing to grow too.."
    menu:
        mc "This role complements my commitment to (continuous/continuos) learning, professional growth, and taking part in impactful, on-the-ground environmental efforts."
    
        "\"continuous\"":
            $ score += 1
        "\"continuos\"":
            pass

    #7
    mc "…Almost done! Let’s wrap this up with intent and clarity."
    menu:
        mc "I hope to contribute meaningfully (to/with) your mission and values."

        "\"to\"":
            $ score += 1
        "\"with\"":
            pass

    mc "Wooh! I did it! My first ever commission! I hope it passes the standard of the client!"
    mc "total count: [score]"        #not final pero tama to

    #feedback / scoring system
    menu:
        "Send the Letter to Client 1 ":
            call feedback        #using call here para makabalik to this point once it reaches the return statement sa logbook 

    return

label logbook:
    #show client 1 profile
    return

label feedback:
    if score == 7:
        cl "5 STARS! OMG! Thank you so much! Not only did I pass the interview but I also got the job!!"
    elif score >= 5:
        cl "4 STARS! It’s not perfect but I still got the interview and the job! ;)"
    elif score >= 3:
        cl "3 STARS! Hello! Someone else had their interview before mine and ended up getting the job :("
    elif score == 2:
        cl "2 STARS! Hello! They rejected my application. I didn’t get the interview…"
    else:
        cl "1 STAR! I applied but never heard back from them since :("

    menu:
        "Reveal Answers":            
            call screen answers
    return

screen answers:
    frame:
        xsize 1180
        ysize 680
        xalign 0.5
        yalign 0.5
        padding (40,40,25,50)
        has vbox

        text "{size=+12}Answers and Explanations{/size}{vspace=10}" xalign 0.5

        viewport id "ans":
            draggable True
            mousewheel True
            scrollbars "vertical"
            ysize 600
            
            has vbox
            text "1. Standard Cover Letter Greetings: \n{b}{color=#818063}Dear Mrs. XYZ{/color}{/b} / To whom it may concern{vspace=2}"
            text "“To whom it may concern” sounds generic and outdated, which isn’t what the client wants. Using “Dear Mrs. XYZ” sounds more personal and fits the disposition of the client better.{vspace=10}"
            
            text "2. Appropriate Tone: \n This job looks super cool and I think I’d vibe well with the team. / {b}{color=#818063}This opportunity deeply aligns with my goals and values.{/color}{/b}{vspace=2}"
            text "Even though the client wants the letter to show their upbeat character, a cover letter should still be professional and formal.{vspace=10}"

            text "3. Grammar: \nMy experiences ( {b}{color=#818063}align{/color}{/b} / aligns ) with your organization’s mission.{vspace=2}"
            text "“Experiences” is plural, so by subject-verb agreement, “align” should be used.{vspace=10}"

            text "4. Grammar: \nI ( lead / {b}{color=#818063}led{/color}{/b} ) multiple campaigns promoting composting and sustainability in urban neighborhoods.{vspace=2}"
            text "Since it happened in the past, “led” should be used, as the past tense of “lead”.{vspace=10}"

            text "5. Grammar: \nI am familiar with local environmental regulations and (had / {b}{color=#818063}have{/color}{/b} ) hands-on experience collecting field samples and recording environmental data.{vspace=2}"
            text "Based on tense consistency and context, “have” is more suitable to use than “had”. Inconsistent tenses causes confusion to the client’s ability. Using “have” implies they still remember how to do it.{vspace=10}"

            text "6. Spelling: \nThis role complements my commitment to ( {b}{color=#818063}continuous{/color}{/b} \ continuos ) learning, professional growth, and taking part in impactful, on-the-ground environmental efforts.{vspace=2}"
            text "Proper Spelling.{vspace=10}"

            text "7. Grammar: \nI hope to contribute meaningfully ( {b}{color=#818063}to{/color}{/b} \ with ) your mission and values.{vspace=2}"
            text "The right preposition here is “to”; “with” feels grammatically off and awkward.{vspace=10}"

            textbutton "Back" action Return()
        #position the vertical scrollbar
        vbar:
            value YScrollValue("ans")
    











