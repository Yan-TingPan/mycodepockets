"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

"Player destroys all bricks in the window, level cleared!"
"When the ball exceeds the bottom boundary of the window three times, Game Over!"
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)
        graphics.bouncing()
        if lives > 0:
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            # update
            graphics.ball.move(dx, dy)
        # check
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                graphics.set_dx()
            if graphics.ball.y <= 0 or graphics.ball.y + graphics.ball.height >= graphics.window.height:
                graphics.dy = -dy
        #   When the ball exceeds the bottom boundary of the window, the ball will return to the initial coordinates.
        if graphics.ball.y > graphics.window.height:
            graphics.reset_ball()
            lives -= 1
        if lives == 0:
            break
        if graphics.eliminated == graphics.bricks:
            break


if __name__ == '__main__':
    main()
