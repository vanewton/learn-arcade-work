""" Sprite Sample Program """
import math
import random
import arcade



# --- Constants ---
SPRITE_SCALING_PLAYER = 0.07
SPRITE_SCALING_ASTEROID = 0.1
ASTEROID_COUNT = 10
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
asteroid_sound = arcade.load_sound("bomb_sound.wav")




class Asteroid(arcade.Sprite):

    def update(self):
        self.center_x -= 1
        if self.center_x < 0:
            self.center_x = SCREEN_WIDTH

class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")


        # Variables that will hold sprite lists
        self.player_list = None
        self.asteroid_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)





    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()

        # Score
        self.score = 0
        # Tails sprite
        self.player_sprite = arcade.Sprite("tails_sprite.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)


        # Placing the asteroids
        for i in range(ASTEROID_COUNT_COUNT):

            asteroid = Asteroid("bomb_sprite.png", SPRITE_SCALING_ASTEROID)
            asteroid.center_x = random.randrange(SCREEN_WIDTH)
            asteroid.center_y = random.randrange(SCREEN_HEIGHT)
            self.asteroid_list.append(asteroid)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.player_list.draw()
        self.asteroid_list.draw()


        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.asteroid_list.update()

        # Generate a list of all sprites that collided with the player.

        # Loop through each colliding sprite, remove it, and add to the score.

        asteroid_hit_list = arcade.check_for_collision_with_list(self.player_sprite,self.asteroid_list)

        for asteroid in asteroid_hit_list:
            asteroid.remove_from_sprite_lists()
            self.score -= 1
            arcade.play_sound(asteroid_sound)

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()