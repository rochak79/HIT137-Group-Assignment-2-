import turtle

"""
Recursive function to draw a tree like pattern
Basically recursive function is a method used to solve certain problems by creating a function 
that calls itself until the program achieve the desired result.

What we are doing right here is we have defined a function and few parameters has been defined to let user 
type it according to how they would like to call it.
"""
def draw_tree_pattern(left_angle, right_angle, branch_length, depth, reduction_factor):
    if depth == 0:  # Base case: stop when depth reaches 0
        return

    # Set the color based on the depth
    if depth == 5:
        turtle.color("brown")
    else:
        turtle.color("green")

    # Draw the current branch
    turtle.pensize(depth)  # set the width of the pen for drawing
    turtle.forward(branch_length)
    
    # Draw the left branch
    turtle.left(left_angle)
    draw_tree_pattern(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    turtle.right(left_angle)  # Return to original position

    # Draw the right branch
    turtle.right(right_angle)
    draw_tree_pattern(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    turtle.left(right_angle)  # Return to original position

    # Return to the starting point of the current branch
    if branch_length==100:
        turtle.penup()
        turtle.hideturtle()
    turtle.backward(branch_length)

# Main function to set up the turtle and take user input
def main():
    # Taking all the inputs from user as defined in the question itself
    # As you anybody can see it is self explanatory and only asking whawt is needed.
    print("Before starting to draw a tree, let's input a few parameters to customize it.")
    left_angle = int(input("Please enter the left branch angle (e.g., 20): "))
    right_angle = int(input("Please enter the right branch angle (e.g., 25): "))
    branch_length = int(input("Please enter the starting branch length (e.g., 100): "))
    depth = int(input("Please enter the recursion depth (e.g., 5): "))
    reduction_factor = float(input("Please enter the branch length reduction factor (e.g., 0.7): "))


    """
    Set speed to fastest or it can be fast, normal, slow and slowest as per your need

    At first turtle pointer is always facing "right or east" 
    So, turning it left by 90 degree makes it point upwards

    next we only want to move to the bottm centre so we call pen up which picks up the 
    turtles tail so that it doesn't draw when it moves
    
    at the begning the turtle pointer is always at home position means at the center (0, 0)
    so, we are mobing it to the bottom center of the screen with (0, 200)

    Now we actually want to draw the tree so calling pendown will puts down the turtles tail 
    so that it draws when it moves and we choose the color to be 'brow'
    """
    # Setting up all the turtle attributes at first
    turtle.speed("fastest")
    turtle.left(90)  
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.color("brown")

    # Calling the recursive function to draw the tree
    draw_tree_pattern(branch_length, left_angle, right_angle, depth, reduction_factor)
    
    # this function help to keep the window open until the user closes it manually.
    turtle.done()

# Run the program
main()