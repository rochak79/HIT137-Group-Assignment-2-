import turtle

# Recursive function to draw a tree pattern
def draw_tree_pattern(branch_length, left_angle, right_angle, depth, reduction_factor):
    if depth == 0:  # Base case: stop when depth reaches 0
        return

    # Set the color for branches
    turtle.color("green")

    # Draw the current branch
    turtle.pensize(depth)  # Adjust branch thickness based on depth
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
    turtle.backward(branch_length)

# Main function to set up the turtle and take user input
def main():
    # Taking inputs from the user
    left_angle = int(input("Enter the left branch angle (e.g., 20): "))
    right_angle = int(input("Enter the right branch angle (e.g., 25): "))
    branch_length = int(input("Enter the starting branch length (e.g., 100): "))
    depth = int(input("Enter the recursion depth (e.g., 5): "))
    reduction_factor = float(input("Enter the branch length reduction factor (e.g., 0.7): "))

    # Setting up the turtle
    turtle.speed("fastest")  # Set speed to fastest
    turtle.left(90)  # Point the turtle upwards
    turtle.penup()
    turtle.goto(0, -200)  # Move to the bottom center of the screen
    turtle.pendown()

    # Draw the trunk (bottom part)
    turtle.color("red")
    turtle.pensize(depth)  # Make the trunk thick
    turtle.forward(branch_length)

    # Draw the tree branches
    draw_tree_pattern(branch_length, left_angle, right_angle, depth - 1, reduction_factor)
    
    # Keep the window open until the user closes it
    turtle.done()

# Run the program
main()
