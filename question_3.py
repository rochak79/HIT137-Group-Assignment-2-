import turtle

# Recursive function to draw a tree pattern
def draw_tree_pattern(branch_length, left_angle, right_angle, depth, reduction_factor):
    if depth == 0:  # Base case: stop when depth reaches 0
        return

    # Set the color based on the depth
    if depth :
        turtle.color("green")
    else:
        turtle.color("brown")

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