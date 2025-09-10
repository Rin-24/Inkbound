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
            $ letter_2 = "I am writing to respectfully appeal your decision regarding my college application."
        "\"because I disagree with your decision to reject me. \"":
            $ letter_1 = "To the Admissions Committee,"
            $ letter_2 = "I am writing because I disagree with your decision to reject me. "
            pass
    
   #2
    mc "Hmm, she needs to talk about her academic standing."
    menu:
        mc "{cps=20}\"I ..... my current academic performance. \"{/cps}"
        "\"see no problem with\"":
            $ letter_3 = "see no problem with "
            pass
        "\"carefully evaluated\"":
            $ letter_3 = "carefully evaluated "
            $ total_score += 1
            $ score += 1

    #3
    mc "I should also mention what she has done to improve..."
    menu:
        mc "{cps=20}\"To strengthen my application for nursing school, I have...\"{/cps}"

        "\"studied the prerequisites\"":     
            $ letter_4 = "studied the prerequisites "
            $ total_score += 1
            $ score += 1
        "\"done enough already\"":
            $ letter_4 = "done enough already "       
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
            $ letter_6 = "Let me know if I got in or not "
            pass
        "\"Thank you for your time and consideration.\"":
            $ letter_6 = "Thank you for your time and consideration. "
            $ score += 1
            $ total_score += 1

    #6
    mc "The right sign-off goes a long way. "
    menu:
        mc "{cps=20}\"...\"{/cps}"
        "\"See you,\n Madison\"":
            $ letter_7 = "See you, \n Madison "
            pass
        "\"Respectfully,\n Madison \"":
            $ letter_7 = "Respectfully,\n Madison "
            $ score += 1
            $ total_score += 1
    return

