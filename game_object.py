
class Game_object:
    def __init__(self, screen, pos, height, width, image=None):
        self.pos = pos
        self.screen = screen
        self.height = height
        self.width = width
        self.image = image

    def render(self):
        if self.image is not None:
            x = int(self.pos[0])
            y = int(self.pos[1])
            self.screen.blit(self.image, (x,y))
        else:
            print('cant display the object, no image provided please overwrite method render')

    def get_limits(self):
        x_min = self.pos[0]
        y_min = self.pos[1]
        x_max = self.pos[0] + self.width
        y_max = self.pos[1] + self.height
        return x_min, x_max, y_min, y_max
