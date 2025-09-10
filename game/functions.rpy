init python:
    tutorial_pages = [
        "Welcome, [name].\nYou don’t remember much, but your hands still know how to write.\n\nHere’s how this works:\n\n{b}Meet Your Client{/b}\n\nSomeone will come to you with a request.\nThey’ll ask for a letter. A message. A speech.\nYou are their ghostwriter. Their pen. Their voice.",
        
        "{b}Choose How To Write{/b}\n\nYou’ll shape the message by making choices, but each choice will be evaluated on three elements:\n\n{b}Tone{/b} - Does the letter sound warm, professional, cold, or emotional?\nThe tone sets the emotional mood of the message. It’s how your client will be heard.\n\n{b}Grammar{/b} - How the message is written.\nPerfect grammar may sound smart and polished.\nCasual or messy writing might feel more honest or personal.\n\n{b}Appropriateness{/b} - This is about how well the message fits the context.\nIs it too formal for a personal moment? Too blunt for a delicate situation?\nA message might be well-written but still completely wrong for the audience.\n\n",
        
        "{b}Receive Ratings{/b}\n\nWhen the letter is done, the client will give you a star rating (1–5):\n- Was the tone right?\n- Was the grammar appropriate?\n- Did you write what they really needed?\n\nEvery client gives you stars.",

        "{b}Unlock New Chapters{/b}\n\nAs you collect stars, you’ll unlock new chapters in the main storyline.\nEach new chapter reveals:\n• More about your lost memories\n• New types of clients\n• Harder choices with higher stakes\n\nEarn enough stars to move forward.\nChoose wisely to uncover the truth.",

        "Ready to begin?\nYour first client is waiting."
    ]

screen tutorial_screen(current_page=0):
    tag tutorial

    default page = current_page

    frame:
        style "menu_frame"
        xalign 0.5
        yalign 0.5
        padding (40, 30)
        xmaximum 1000

        vbox:
            spacing 20

            # show tutorial text
            text tutorial_pages[page] size 35

            hbox:
                spacing 20
                xalign 1.0

                if page > 0:
                    textbutton "Back" action [SetScreenVariable("page", page - 1)]

                if page < len(tutorial_pages) - 1:
                    textbutton "Next" action [SetScreenVariable("page", page + 1)]
                else:
                    textbutton "Continue" action Return()

label client_1:
    cl1 "Hi, I'm Madison! I need your help."
    $cl1 ="Madison"
    mc "Hi, Madison! What can I do for you?"
    cl1 "Can you help me write an appeal letter for college?"
    mc "Wait, let me guess your program..."
    menu:
        "Fashion Design":
            mc "Fashion design? Your outfit looks so nice!"
        "Theatre":
            mc "Theatre? You look like someone who performs!"

    cl1 "Haha, thank you! I wish, but no, I'm taking up nursing."
    cl1 "Well..I should be. They turned me down."
    cl1 "They told me I can write a formal appeal to the admissions committee for reconsideration."
    mc "You must really like nursing to write an appeal, huh?"
    cl1 "Um..not really. But we are a family of medical professionals."
    cl1 "I wouldn't want to disappoint them. You understand, right?"
    mc "I get you... If you really want that spot, I'll help you!"
    mc "So, a college appeal letter to the admissions committee for reconsideration, right?"
    cl1 "Yes, thank you! Can I come back for it later?"
    mc "Sure! But Madison...why don't you think about this first?"
    mc "It's your life and time, won't you rather spend it on something you enjoy doing?"
    cl1 "I know...I'll think about it. See you later!"
    #letter proper

    mc "Let's start! It should be addressed to the admissions committee."
    mc "Hmmm, it should be formal. No one wants to read a complaint disguised as an appeal."   
    #1
    menu:
        mc "{cps=20}\"I am writing...\"{/cps}"
        "\"to respectfully appeal your decision regarding my college application.\"":
            $ letter_1 = "To the Admissions Committee,"
            $ total_score += 1
            $ score += 1
            $ letter_2 = "  I am writing to respectfully appeal your decision regarding my college application."
        "\"because I disagree with your decision to reject me. \"":
            $ letter_1 = "To the Admissions Committee,"
            $ letter_2 = "  I am writing because I disagree with your decision to reject me. "
            pass
    
   #2
    mc "Hmm, she needs to talk about her academic standing."
    menu:
        mc "{cps=20}\"I ..... my current academic performance. \"{/cps}"
        "\"see no problem with\"":
            $ letter_3 = "I see no problem with my current academic performance.  "
            pass
        "\"carefully evaluated\"":
            $ letter_3 = "I carefully evaluated my current academic performance. "
            $ total_score += 1
            $ score += 1

    #3
    mc "I should also mention what she has done to improve..."
    menu:
        mc "{cps=20}\"To strengthen my application for nursing school, I have...\"{/cps}"

        "\"studied the prerequisites\"":     
            $ letter_4 = "To strengthen my application for nursing school, I have studied the prerequisites. "
            $ total_score += 1
            $ score += 1
        "\"done enough already\"":
            $ letter_4 = "To strengthen my application for nursing school, I have done enough already. "       
            pass

    #4
    mc "Hmmm, let's make sure they see she's serious about this."
    menu:
        mc "{cps=20}\"...\"{/cps}"
        
        "\"I am the best candidate you have and deserve to be reconsidered.\"":
            $letter_5 = "I am the best candidate you have and deserve to be reconsidered. "
            pass
        "\"I am dedicated to putting in the effort in this program.\"":
            $letter_5 = "I am dedicated to putting in the effort in this program. "
            $ score += 1
            $ total_score += 1

    #5
    mc "Nice, time to wrap it up...something that leaves a lasting impression"
    menu:
        mc "{cps=20}\"...\"{/cps}"
        "\"Let me know if I got in or not\"":
            $ letter_6 = "\nLet me know if I got in or not. "
            pass
        "\"Thank you for your time and consideration.\"":
            $ letter_6 = "\nThank you for your time and consideration. "
            $ score += 1
            $ total_score += 1

    #6
    mc "The right sign-off goes a long way. "
    menu:
        mc "{cps=20}\"...\"{/cps}"
        "\"See you,\n   Madison\"":
            $ letter_7 = "\nSee you, \n Madison "
            pass
        "\"Respectfully,\n Madison \"":
            $ letter_7 = "\nRespectfully,\n   Madison "
            $ score += 1
            $ total_score += 1

    menu:
        "Show letter":
            call write_letter # shows the full letter

    menu:
        "Send the Letter to Client 1 ":
            show screen feedback_cl1(score)        #using call here para makabalik to this point once it reaches the return statement sa logbook 
            pause
            hide screen feedback_cl1

    return

screen feedback_cl1(score):
    if score == 7:
        add "five stars.png" at truecenter
    elif score >= 5:
        add "four stars.png" at truecenter
    elif score >= 3:
        add "three stars.png" at truecenter
    elif score == 2:
        add "two stars.png" at truecenter
    else:
        add "one star.png" at truecenter

label write_letter:
    show screen letter_display
    pause
    hide screen letter_display

    return

label client_2:
    #audio
    $ score = 0
    # "score = [score]" to check score

    show cl2 base center with fade
    cl2 "Good day! Are you [name]? Am I in the right place?"
    hide cl2 base center
    
    show mc base center
    mc "That’s me! And you are?" 
    hide mc base center

    show cl2 base center
    cl2 "I’m Luke! I saw your flyer."
    $ cl2 = "Luke" 
    hide cl2 base center

    show mc base left
    mc "Nice to meet you, Luke. What can I help you with?"
    hide mc base center

    show cl2 base right
    cl2 "Uhm.. You see… I’m in my mid-30s.\nI don’t come from money, and my current job barely pays enough to support my family…"
    hide cl2 base right

    show mc base left
    mc "That sounds really tough…"
    hide mc base center

    show cl2 base right
    cl2 "Yeah… I need to start applying for something that pays better, but I’m plenty busy with life as is."
    cl2 "I thought, since you’re a writer, maybe... you could help me write a solid cover letter?"
    hide cl2 base right

    show mc base left
    mc "Is there a specific job you have in mind?"
    hide mc base left

    show cl2 base right
    cl2 "Yep. I’m eyeing this Assistant position to an Environmental Specialist. It’s with the Regional Environmental Office. Seems stable, and it pays way better than my current gig."
    hide cl2 base right

    show mc base left
    mc "(Oh, environmental specialist?)"
    mc "Alright, I'll need you to answer a few questions first.\nWho’s the letter addressed to?"
    hide mc base left

    show cl2 base right
    cl2 "It says Mrs. Gonzales in the poster."
    hide cl2 base right

    show mc base left
    mc "(...)\n(The name... sounds oddly familiar? Wait—)"
    mc "(FOCUS!)"
    mc "Uh That's noted. What kind of tone do you want to go for? Formal and strictly professional? Or something warmer and personal?"
    hide mc base left

    show cl2 base right
    cl2 "Definitely the latter. Still professional, of course, but I want them to feel I’m genuine and not robotic."
    hide cl2 base right

    show mc base left
    mc "Got it."
    mc "And for the last one: What exactly do you want this letter to do?\nGet you in the door? Show off your passion? Highlight your background?"
    hide mc base left

    show cl2 base right
    cl2 "All of it, honestly."
    cl2 "But mostly— I want to secure the interview. I want them to read the letter and not hesitate to contact me. If they talk to me, I know I can convince them!"
    hide cl2 base right

    show mc base left
    mc "Woah, that’s the spirit!"
    hide mc base left

    show cl2 base right
    cl2 "Thank you. Here’s my background and strengths. Use whatever you need."
    hide cl2 base right

    show mc base center
    mc "Perfect."
    #audio here
    hide mc base center

    "Continue or end the conversation?"
    menu:
        "Converse some more":
            show mc base center
            mc "Hmm, environmental specialist huh…"
            mc "For a role like this, they’ll probably want someone who can handle environmental review cycles. Mention your ability with compliance reports too."
            mc "Oh— and familiarity with GIS or real-time data logging tools could give you an edge so—"
            hide mc base center

            show cl2 base right
            cl2 "Woah you seem to know a lot about this position. It’s not even on the job poster..."
            cl2 "Have you ever worked in this field?"
            hide cl2 base right

            show mc base center
            mc "(Oh. Now that you’ve mentioned it… How…)"
            mc "I… I don’t know. It just kind of… came to me?"
            mc "(I don’t know how to describe this weird familiarity.\nI don’t even know why I got here)"

            mc "Nevermind. I will get this letter back right away after I finish it."
            hide mc base center
        "End it here":
            mc "This is enough. I will get this letter back right away after I finish it."

    show cl2 base center
    cl2 "You’re a lifesaver, seriously. I’m already stretched thin just trying to survive. This takes a huge load off my shoulders.\nThank you, [name]"
    hide cl2 base center

    mc "Another client who needs help. Let's get right into this."

    #1
    menu:
        mc "Since this is a cover letter, what appropriate greeting should be used…"

        "\"Dear Mrs. XYZ,\"":
            $ total_score += 1
            $ score += 1
            $ letter_1 = "Dear Mrs. XYZ,"
        "\"To whom it may concern\"":
            $ letter_1 = "To whom it may concern: "
            pass
    
   #2
    menu:
        mc "Hmm… In the intro, I should mention briefly why my client wants to apply for the job:"

        "\"This job looks super cool and I think I’d vibe well with the team\"":
            $ letter_2 = "This job looks super cool and I think I’d vibe well with the team. "
            pass
        "\"This opportunity deeply aligns with my goals and values\"":
            $ letter_2 = "This opportunity deeply aligns with my goals and values. "
            $ total_score += 1
            $ score += 1

    #3
    mc "Wow… such a long list of experiences, Mx. C1 sure is passionate about this field. So:"
    menu:
        mc "My experiences (align/aligns) with your organization’s mission."

        "\"align\"":     
            $ letter_3 = "My experiences align with your organization’s mission. "
            $ total_score += 1
            $ score += 1
        "\"aligns\"":
            $ letter_3 = "My experiences aligns with your organization’s mission. "       
            pass

    #4
    mc "Then how should I phrase their volunteer works…"
    menu:
        mc "I (lead/led) multiple campaigns promoting composting and sustainability in urban neighborhoods."
        
        "\"lead\"":
            $letter_4 = "I lead multiple campaigns promoting composting and sustainability in urban neighborhoods. "
            pass
        "\"led\"":
            $letter_4 = "I led multiple campaigns promoting composting and sustainability in urban neighborhoods. "
            $ score += 1
            $ total_score += 1

    #5
    mc "More about their skills and edge… "
    menu:
        mc "Write: I am familiar with local environmental regulations and (had/have) hands-on experience collecting field samples and recording environmental data."

        "\"had\"":
            $ letter_5 = "I am familiar with local environmental regulations and had hands-on experience collecting field samples and recording environmental data. "
            pass
        "\"have\"":
            $ letter_5 = "I am familiar with local environmental regulations and have hands-on experience collecting field samples and recording environmental data. "
            $ score += 1
            $ total_score += 1

    #6
    mc "I want to mention how much the client is willing to grow too.."
    menu:
        mc "This role complements my commitment to (continuous/continuos) learning, professional growth, and taking part in impactful, on-the-ground environmental efforts."
    
        "\"continuous\"":
            $ letter_6 = "This role complements my commitment to continuous learning, professional growth, and taking part in impactful, on-the-ground environmental efforts. "
            $ score += 1
            $ total_score += 1
        "\"continuos\"":
            $ letter_6 = "This role complements my commitment to continuos learning, professional growth, and taking part in impactful, on-the-ground environmental efforts. "
            pass

    #7
    mc "…Almost done! Let’s wrap this up with intent and clarity."
    menu:
        mc "I hope to contribute meaningfully (to/with) your mission and values."

        "\"to\"":
            $ letter_7 = "I hope to contribute meaningfully to your mission and values. "
            $ score += 1
            $ total_score += 1
        "\"with\"":
            $ letter_7 = "I hope to contribute meaningfully with your mission and values. "
            pass
    mc "Done! I hope it gets what Luke wants."
    
    # mc "total count: [score]"  
    #feedback / scoring system
    menu:
        "Show letter":
            call write_letter # shows the full letter

    menu:
        "Send the Letter to Client 1 ":
            show screen feedback(score)        #using call here para makabalik to this point once it reaches the return statement sa logbook 
            pause
            hide screen feedback

    menu:
        "Reveal Answers":            
            call screen cl2_answers
    "DONE"

    return

