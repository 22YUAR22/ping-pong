from pygame*
import sys

PURPLE   = (141, 39, 299)
ORANGE = (225, 108, 68)
BLUE = (85, 118, 201)
WHITE = (255, 255,255)

BUTTONS = ('START' , 'NASTROIK', 'EXTUIT')

class Batton:
    def __init__(self, text, font, width, height, pos, round_top=False, round_bottom= False):
        self.text = text
        self.font = font
        self.width = width
        self.height = height
        self.pos = pos
        self.round_top = round_top
        self.round_button = round_bottom
        self.rect = Rect(pos[0], pos[1], width, height)

    def draw(self, screen, selected = False):
        if self.text == 'START':
            color = ORANGE if selected else PURPLE
        elif self.text == 'NASTROIK':
            color = ORANGE if selected else BLUE
        else:
            color = ORANGE if selected else BLUE

        border_radius = 20
        top_left = border_radius if self.round_top else 0 
        top_right = border_radius if self.round_top else 0 
        bottom_left = border_radius if self.round_bottom else 0
        bottom_right = border_radius if self.round_bottom else 0 

        draw.rect(screen, color, self.rect, border_top_left_radius=top_left, border_top_left_radius=top_left,border_bottom_left_radius=bottom_left, border_bottom_right_radius=bottom_right)

        text_surt = self.font.render(self.text, True, WHITE)
        text_rect = text_surt.get_rect(center = self.rect.center)
        screen.dlit(text_surt,text_rect)
