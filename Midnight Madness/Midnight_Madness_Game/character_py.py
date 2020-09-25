import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#Set the max speed the player can move - changing this value can increase/decrease difficulty
PLAYER_SPEED = 5

#This function draws the smaller user-controllable stick figure on the screen
def draw_stick_figure(win, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
    print(x, y)
 
    # Legs
    #Right leg (colour, length of leg....)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    #Left Leg
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
 
    # Body
    pygame.draw.line(screen, Black, [5 + x, 17 + y], [5 + x, 7 + y], 2)
 
    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)

#This function ensures that the number entered is between the range of the min and max values (inclusive). 
#If the number is outside of this range, we return the closest allowed value. I.e. if the max was 10 and the number
#entered was 12, 10 would be returned as this is the maximum value allowed
def keep_in_range(number, min_no, max_no):
    if (number < min_no):
        return min_no
    elif (number > max_no):
        return max_no
    else:
        return number
# Setup
pygame.init()
 
# Set the width and height of the screen [width,height]

screen_size = [700, 500]
screen = pygame.display.set_mode(screen_size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(0)
 
# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 300
y_coord = 1
 
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key
 
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -PLAYER_SPEED
            elif event.key == pygame.K_RIGHT:
                x_speed = PLAYER_SPEED
            elif event.key == pygame.K_UP:
                y_speed = -PLAYER_SPEED
            elif event.key == pygame.K_DOWN:
                y_speed = PLAYER_SPEED
 
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
 
    # --- Game Logic
 
    # Move the object according to the speed vector.
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    if (x_coord < 0):
        x_coord = 0

    if (y_coord < 0):
        y_coord = 0

    #Adjust the x and y co-ordinates to ensure that the stick figure is kept on the screen and can't
    #travel off of it
    x_coord = keep_in_range(x_coord, 0, screen_size[0] - 10) #We adjust the upper limit of our allowed range to match the stick figures width
    y_coord = keep_in_range(y_coord, 0, screen_size[1] - 27) #We adjust the upper limit of our allowed range to match the stick figures height
    # --- Drawing Code
 
    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
 
    draw_stick_figure(screen, x_coord, y_coord) #draw the stick figure on the screen
 
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
