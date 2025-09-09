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

label
