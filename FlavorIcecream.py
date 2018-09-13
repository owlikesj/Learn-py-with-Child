import easygui
flavor = easygui.choicebox("What is your favorite icecream flavor?", "Ice Cream Survey", choices = ["Vanilla", "Chocolate",
"Strawberry"])
easygui.msgbox("You picked " + flavor)
