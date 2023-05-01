""" Sprite Sample Program """
import math
import random
import arcade



# --- Constants ---
SPRITE_SCALING_PLAYER = 1
SPRITE_SCALING_ASTEROID = 0.3
SPRITE_SCALING_BULLET = 0.02
ASTEROID_COUNT = 10
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BULLET_SPEED = 5

class Asteroid(arcade.Sprite):

    def update(self):
        self.center_x -= 1
        if self.center_x < 0:
            self.center_x = SCREEN_WIDTH

class Bullet(arcade.Sprite):
    # Call update on all sprites
    def on_mouse_press(self):
        bullet = arcade.Sprite("bullet_sprite.png", SPRITE_SCALING_BULLET)
        # location of the bullets where the player is
        self.player_sprite = arcade.Sprite("chao_sprite.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)






class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")


        # Variables that will hold sprite lists
        self.player_list = None
        self.asteroid_list = None
        self.bullet_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

    def on_update(self, delta_time):
        self.bullet_list.update()

        # Loop through each bullet


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Score
        self.score = 0
        # Chao sprite
        self.player_sprite = arcade.Sprite("chao_sprite.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)


        # Placing the asteroids
        for i in range(ASTEROID_COUNT):

            asteroid = Asteroid("asteroid_sprite.png", SPRITE_SCALING_ASTEROID)
            asteroid.center_x = random.randrange(SCREEN_WIDTH)
            asteroid.center_y = random.randrange(SCREEN_HEIGHT)
            self.asteroid_list.append(asteroid)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.player_list.draw()
        self.asteroid_list.draw()
        self.bullet_list.draw()


        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """
        # Gunshot sound

        # Create a bullet
        bullet = arcade.Sprite("laser_sprite.png", SPRITE_SCALING_BULLET)

        # The image points to the right, and we want it to point up. So
        # rotate it.
        bullet.angle = 0

        # Give the bullet a speed
        bullet.change_x = BULLET_SPEED

        # Position the bullet
        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top
        bullet.center_y = self.player_sprite.center_y

        # Add the bullet to the appropriate lists
        self.bullet_list.append(bullet)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on bullet sprites
        self.bullet_list.update()

        # Loop through each bullet
        for bullet in self.bullet_list:

            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(bullet, self.asteroid_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists(),

            # For every coin we hit, add to the score and remove the coin
            for coin in hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1

                # Hit Sound


            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
# bullet motions


    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.asteroid_list.update()

        # Generate a list of all sprites that collided with the player.

        # Loop through each colliding sprite, remove it, and add to the score.

        asteroid_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.asteroid_list)

        for asteroid in asteroid_hit_list:
            asteroid.remove_from_sprite_lists()
            self.score -= 1



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()