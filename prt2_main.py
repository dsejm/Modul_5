from prt2_base import Model

state = Model()
state.title = "Hello, Mam!"
state.text = "I love you!"
state.author = "Jeremy!"

new_state = Model()
new_state.save()
state.save()