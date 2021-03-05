from graphics import *
from random import randrange

##
## Problem 15
##

def p15():
    """This function displays the student grade data in a horizontal bar chart"""
    infile = open("exam-scores.dat")
    num_scores = int(infile.readline())
    print("There are", num_scores, " scores")
    
    #
    # Define some variables used in sizing and placement
    #
    student_data_height = 40
    inter_data_spacing = 10
    left_spacing = 10
    top_spacing = 25
    name_width = 50
    bar_width = 200
    bar_height = 10
    
    #
    # Dynamically sized window
    #
    win = GraphWin("Student Scores", left_spacing + name_width + inter_data_spacing + bar_width + left_spacing, 
                   (student_data_height + inter_data_spacing) * (num_scores -1))
    
    # 
    # Starting y position for placing the score information
    #
    data_y_position = top_spacing
    
    #
    # Counter used to draw the score info
    #
    index = 0
    
    #
    # Process each line in the file
    #
    for line in infile:
        # Extract the name and score
        name, score_str = line.split()
        score = float(score_str)

        # Set the y position for this score data by using the
        y_pos = top_spacing + index * student_data_height
        
        name_text = Text(Point(name_width / 2 + left_spacing, y_pos + 5), name)
        name_text.setSize(10)
        name_text.draw(win)
        index = index + 1
        
        bar_x_pos = left_spacing + name_width + inter_data_spacing
        Rectangle(Point(bar_x_pos, y_pos), 
                  Point(bar_x_pos + (score / 100) * 200, y_pos + bar_height)).draw(win)
        
    pt = win.getMouse()
    win.close()
    infile.close()

##
## Problem 16
##

def generate_data(num_points):
    outfile = open("quiz-scores.dat", "w")
    for i in range(0, num_points):
        value = randrange(0, 11)
        print(value, file=outfile)
    outfile.close()

def p16():
    """This function displays the student quiz grade data in a histogram"""
    infile = open("quiz-scores.dat", "r")

    #
    # Create the initial count list
    #
    score_list = []
    for i in range(0, 11):
        score_list.append(0)

    #
    # Update the counts
    #
    total_possible_count = 0
    for line in infile:
        score = int(line)
        score_list[score] = score_list[score] + 1
        total_possible_count = total_possible_count + 1
        
    print("Counted score list", score_list)

    #
    # Define some variables used in sizing and placement
    #
    bar_width = 20
    left_spacing = 10
    right_spacing = 10
    bottom_spacing = 10
    top_spacing = 10
    inter_bar_spacing = 10
    bar_height = 100
    label_height = 10
    
    #
    # Dynamically sized window
    #
    window_height = bottom_spacing + bar_height + top_spacing + label_height
    win = GraphWin("Student Scores", left_spacing + (bar_width + inter_bar_spacing) * 10 + right_spacing, 
                   window_height)
    
    #
    # Display the labels and bars
    #
    for i in range(0, 11):
        x_pos = left_spacing + (bar_width + inter_bar_spacing) * i
        y_pos = window_height - 10 - (label_height / 2)
        label = Text(Point(x_pos, y_pos), str(i))
        label.setSize(10)
        label.draw(win)
        
        x_pos = left_spacing + (bar_width + inter_bar_spacing) * i
        y_pos = y_pos - label_height / 2 - inter_bar_spacing
        Rectangle(Point(x_pos, y_pos), 
                  Point(x_pos + bar_width, y_pos - (100 * score_list[i] / total_possible_count))).draw(win)

    # Mouse click to close
    pt = win.getMouse()
    win.close()
    infile.close()
    