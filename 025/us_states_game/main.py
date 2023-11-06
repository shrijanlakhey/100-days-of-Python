import turtle
import pandas
from state import State

screen = turtle.Screen()
screen.title("U.S. States Game")

data = pandas.read_csv("025/us_states_game/50_states.csv")
all_states = data.state.to_list()

# adding an image as a shape
image = "025/us_states_game/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
screen.tracer(0) # turns animations off

# getting coordinates on mouse click in turtle
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# # alternative way of keeping the screen openn even though the code has finished running (alternative to 'screen.exitonclick()')
# turtle.mainloop()


guessed_states = []
while len(guessed_states) < 50:
    answer =  screen.textinput(title=f"{len(guessed_states)}/50 Guess the state", prompt="What's another state's name?").title()
    answer_state = data[data.state == answer]

    if answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('025/us_states_game/states_to_learn.csv')
        
        break

    if answer in all_states:
        state_index = answer_state.index
        # getting x and y coordinates of the answer if it exists
        x_cor = int(answer_state.x[state_index])
        y_cor = int(answer_state.y[state_index])
        state = State(answer, x_cor=x_cor,y_cor=y_cor)
        screen.update()
        if answer not in guessed_states:
            guessed_states.append(answer)



# screen.exitonclick()