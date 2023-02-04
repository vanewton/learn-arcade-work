import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
arcade.set_background_color(arcade.color.DARK_BLUE)
arcade.start_render()

#draw the crust
arcade.draw_rectangle_filled(300,500,500,50, (115,58,58))

#draw the base with cheese
arcade.draw_triangle_filled(50,475,550,475,300,25, (247,208,52))

#draw the pepperoni
arcade.draw_circle_filled(200,400,50, (178,13,46))
arcade.draw_circle_filled(400,400,50, (178,13,46))
arcade.draw_circle_filled(300,300,50, (178,13,46))
arcade.draw_circle_filled(300,170,50, (178,13,46))

#  Finish and run
arcade.finish_render()
arcade.run()