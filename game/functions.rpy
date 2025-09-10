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
            $letter_1 = "To the Admissions Committee,"
            $ total_score += 1
            $ score += 1
            $ letter_2 = "to respectfully appeal your decision regarding my college application."
        "\"because I disagree with your decision to reject me. \"":
            $ letter_1 = "because I disagree with your decision to reject me. "
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
    return

