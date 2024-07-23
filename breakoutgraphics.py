"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=window_width/2 - paddle_width/2,
                            y=window_height-paddle_offset)
        self.paddle.filled = 'black'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=window_width / 2 - ball_radius, y=window_height / 2 - ball_radius)

        # for start_x and start_y
        self.start_x = window_width / 2 - ball_radius
        self.start_y = window_height / 2 - ball_radius

        # draw bricks [red 0 orange 1 yellow 2 green 3 blue 4]
        rows_y = brick_offset   # count the number of the rows y
        color = ['red', 'orange', 'yellow', 'green', 'blue']
        for i in range(brick_rows):  # y
            rows_y += brick_height + brick_spacing
            for j in range(brick_cols):  # x
                cols_x = j*(brick_width + brick_spacing)
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                brick.fill_color = color[i // 2]
                self.window.add(brick, cols_x, rows_y)
        # Initialize our mouse listeners
        onmousemoved(self.change_position)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.moving = False
        onmouseclicked(self.set_ball_velocity)
        self.eliminated = 0
        self. bricks = brick_cols*brick_rows

    # for mouse listeners
    def change_position(self, mouse):
        # 碰到左邊會停下來
        if mouse.x - self.paddle.width/2 < 0:
            self.paddle.x = 0
        # 碰到右邊會停下來
        elif mouse.x + self.paddle.width/2 >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        # 跟著mouse走
        else:
            self.paddle.x = mouse.x - self.paddle.width / 2

    def set_ball_velocity(self, _):
        if not self.moving:
            self.moving = True
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    #
    def get_dx(self):
        return self.__dx

    #
    def get_dy(self):
        return self.__dy

    def get_ball(self):
        return self.ball

    def set_dx(self):
        self.__dx = -self.__dx

    def set_dy(self):
        self.__dy = -self.__dy

    def bouncing(self):
        for i in range(2):
            for j in range(2):
                obj = self.window.get_object_at(self.ball.x+self.ball.width*i, self.ball.y+self.ball.height*i)
                if obj:
                    if obj is self.paddle:
                        if self.__dy > 0:
                            self.__dy = -self.__dy
                # check the brick
                    else:
                        if obj is not None and self.ball.y + BALL_RADIUS*2 > BRICK_HEIGHT*BRICK_COLS:
                            self.__dy = -self.__dy
                            self.window.remove(obj)
                            self.eliminated += 1

    def reset_ball(self):
        self.window.remove(self.ball)
        self.window.add(self.ball, x=self.start_x, y=self.start_y)
        self.__dx = 0
        self.__dy = 0
        self.moving = False

