import simplegui
import random

comp_scr=0
human_scr=0;
comp_choice=""
human_choice=""

def choice_number(choice):
    if choice=='rock':
        return 0
    elif choice=='paper':
        return 1
    else:
        return 2
    
def number_choice(number):
    if number==1:
        return 'rock'
    elif number==2:
        return 'paper'
    else:
        return 'scissor'

def random_comp_choice():
    return random.choice(['rock','paper','scissor'])
    
def choice_result(human_choice,comp_choice):
    global human_scr
    global comp_scr
    
    a=choice_number(human_choice)
    b=choice_number(comp_choice)
    if(a-b)%3==1:
        comp_scr=comp_scr+1
    elif (a==b):
        print("Tie")
    else:
        human_scr=human_scr+1

def test_choice_number():
    assert choice_number('rock')==0
    assert choice_number('paper')==1
    assert choice_number('scissor')==2
def test_number_choice():
    assert number_choice(0)=='rock'
    assert number_choice(1)=='paper'
    assert number_choice(2)=='scissor'
def test_all():
    test_choice_number()
    test_number_choice()

def rock():
    global human_choice,comp_choice
    global human_scr,comp_scr
    human_choice='rock'
    comp_choice=random_comp_choice()
    choice_result(comp_choice,human_choice)
def paper():
    global human_choice,comp_choice
    global human_scr,comp_scr
    human_choice='paper'
    comp_choice=random_comp_choice()
    choice_result(comp_choice,human_choice)
def scissor():
    global human_choice,comp_choice
    global human_scr,comp_scr
    human_choice='scissor'
    comp_choice=random_comp_choice()
    choice_result(comp_choice,human_choice)

def draw(canvas):
    try:
        canvas.draw_text("You : "+ human_choice,[20,40],48,"Yellow")
        canvas.draw_text("COMPUTER : "+ comp_choice,[20,90],38,"Orange")
        canvas.draw_text("HUMAN SCORE: "+ str(human_scr),[10,150],30,"Green")
        canvas.draw_text("COMPUTER SCORE: "+ str(comp_scr),[10,190],30,"Red")
    except TypeError:
        pass

def frame_fun():
    # Create a frame and assign callbacks to event handlers
    frame = simplegui.create_frame("Backgrounds", 500,300)
    frame.set_canvas_background("Black")
   # frame = simplegui.create_frame("Home", 500, 300)
    frame.add_button("Rock",rock)
    frame.add_button("Paper", paper)
    frame.add_button("Scissors", scissor)
    frame.set_draw_handler(draw)
    


    frame.start()
    
frame_fun()
