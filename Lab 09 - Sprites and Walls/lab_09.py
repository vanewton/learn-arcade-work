import arcade


SPRITE_SCALING_BOX = 64


# Place boxes inside a loop
for x in range(173, 650, 64):
    wall = arcade.Sprite("grass_sprite.png", SPRITE_SCALING_BOX)
    wall.center_x = x
    wall.center_y = 350
    self.wall_list.append(wall)