import turtle

"""
Recursive function to draw a tree like pattern
Basically recursive function is a method used to solve certain problems by creating a function 
that calls itself until the program achieve the desired result.

What we are doing right here is we have defined a function and few parameters has been defined to let user 
type it according to how they would like to call it.

After setting everything up we are calling the draw_tree_pattern() function inside itself
reducing depth by 1 and branch_lenth by 70% each time.

left_angle = this rotate to the left by the angle user has input.
right_angle = this rotate to the right by the angle user has input.
Depth = This tells how many “layers” of branches the tree should have. The deeper the tree, the more branches it will have.
reduction_factor = This will reduce the new branch by 70% compared to previous branch.
branch_length = This will be the length of the current branch input by user and it will be less each time calling it recursively.

Each time darwing left and right we return to the orginal postion  to draw the other side of the branches.

when reaching the condition depth = 0 then it will stop drawing becuase we have reached the smallest barnch.
and it stop calling itself and then the drawing ends.

"""

initial_depth = 0
initial_branch_length = 0
def draw_tree_pattern(branch_length, left_angle, right_angle, depth, reduction_factor):

    if depth == 0:  # Base case: stop when depth reaches 0 
        return

    # set the color based on the depth
    if depth == initial_depth:
        turtle.color("brown")
    else:
        turtle.color("green")

    # draw the current branch
    turtle.pensize(depth)  # adjust branch thickness based on depth
    turtle.forward(branch_length)
    
    # draw the left branch
    turtle.left(left_angle)
    draw_tree_pattern(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    turtle.right(left_angle)  # Return to original position

    # draw the right branch
    turtle.right(right_angle)
    draw_tree_pattern(branch_length * reduction_factor, left_angle, right_angle, depth - 1, reduction_factor)
    turtle.left(right_angle)  # Return to original position

    # return to the starting point of the current branch
    if branch_length == initial_branch_length:
        turtle.penup()
        turtle.hideturtle()
    turtle.backward(branch_length)

# Main function to set up the turtle and take user input
def main():
    # declare global variables
    global initial_depth, initial_branch_length
    # Taking all the inputs from user as defined in the question itself
    # As you anybody can see it is self explanatory and only asking whawt is needed.
    while True: 
        print("Before starting to draw a tree, let's input a few parameters to customize it.")
        try:
            left_angle = int(input("Please enter the left branch angle (e.g., 20): "))
            right_angle = int(input("Please enter the right branch angle (e.g., 25): "))
            branch_length = int(input("Please enter the starting branch length (e.g., 100): "))
            depth = int(input("Please enter the recursion depth (e.g., 5): "))
            reduction_factor = float(input("Please enter the branch length reduction factor (e.g., 0.7): "))
            
            # assigning the global variables
            initial_depth = depth
            initial_branch_length = branch_length


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
            # When the current turtle window is closed, the program will prompts the user if they want to run the program again 
            turtle.exitonclick()
            
            #Asks if the user wants to run the prgram again with different parameters
            program = input("Would you like to draw another tree? (yes/no): ").lower()
            if program != "yes" and program  != "y":
                print("Thank you for running the program")
                break
            
            
        except ValueError as ve:
            print(f"Invalid input: {ve}")
            print("Please try again and provide valid numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")

# Run the program
if __name__ == "__main__":
    main()