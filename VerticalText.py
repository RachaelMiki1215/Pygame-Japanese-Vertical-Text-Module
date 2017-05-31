import pygame, pygame.freetype
from pygame.locals import *

class VerticalText(object):
    '''This is a class used to blit text vertically and/or get the rectangle (4-element tuple) of the 
    vertical text. It is intended for use with the Pygame and pygame.freetype module to display Japanese 
    text vertically.
    text_list is a list of n strings intended to be rendered as multi-line text.
    font_obj must be in the form pygame.freetype.Font(font_type, font_size).
    font_color is the intended color of the rendered font.
    x_right_pos is the rightmost x-coordinate which the rendering of the text would begin.
    y_init_pos is the y-coordinate which the rendering would begin.
    line_spacing is the spacing between lines in multi-line text.
    vert-spacing is the spacing between characters in the same line.'''
    def __init__(self, text_list, font_obj, font_color, x_right_pos, y_init_pos, line_spacing, vert_spacing):
        self.text_list = text_list
        self.font_obj = font_obj
        self.font_color = font_color
        self.x_right_pos = x_right_pos
        self.y_init_pos = y_init_pos
        self.line_spacing = line_spacing
        self.vert_spacing = vert_spacing
        self.font_width = self.font_obj.get_rect('あ')[2]

    def draw_vert_text(self, surface):      # vertical text draw method
        '''This method allows for blitting text vetically onto a surface.'''
        for i in range(len(self.text_list)):
            for j in range(len(self.text_list[i])):
                if self.text_list[i][j] == '「' or self.text_list[i][j] == '」' or self.text_list[i][j] == '『' or self.text_list[i][j] == '』':
                    rendered = self.font_obj.render(self.text_list[i][j], self.font_color, rotation = -90)
                else:
                    rendered = self.font_obj.render(self.text_list[i][j], self.font_color)
                if j == 0:
                    y_pos = self.y_init_pos
                    surface.blit(rendered[0], (self.x_right_pos - (i + 1)*self.font_width - self.line_spacing*i, y_pos))
                    if self.text_list[i][j] == '『':
                        y_pos += (self.font_obj.get_rect(self.text_list[i][j])[3] + self.vert_spacing)*0.7
                    else:
                        y_pos += self.font_obj.get_rect(self.text_list[i][j])[3] + self.vert_spacing
                else:
                    if self.text_list[i][j] == '。':
                        surface.blit(rendered[0], (self.x_right_pos - (i + 0.5) * self.font_width - self.line_spacing * i, y_pos))
                    else:
                        surface.blit(rendered[0], (self.x_right_pos - (i + 1) * self.font_width - self.line_spacing * i, y_pos))
                    if self.text_list[i][j] == '『' or self.text_list[i][j] == '』':
                        y_pos += (self.font_obj.get_rect(self.text_list[i][j])[3] + self.vert_spacing)*0.8
                    else:
                        y_pos += self.font_obj.get_rect(self.text_list[i][j])[3] + self.vert_spacing

    def get_text_rect(self):        # get rectangle tuple from vertical text
        '''The method obtains rectangle of vertical text.'''
        text_box_width = (self.font_width + self.line_spacing) * len(self.text_list)
        y_max = []
        for i, text in enumerate(self.text_list):
            for j, letter in enumerate(text):
                if j == 0:
                    y_pos = self.y_init_pos
                    if self.text_list[i][j] == '『':
                        y_pos += (self.font_obj.get_rect(self.text_list[i][j])[3] + self.vert_spacing) * 0.7
                    else:
                        y_pos += self.font_obj.get_rect(self.text_list[i][j])[3] + self.vert_spacing
                else:
                    if self.text_list[i][j] == '『' or self.text_list[i][j] == '』':
                        y_pos += (self.font_obj.get_rect(self.text_list[i][j])[3] + self.vert_spacing)*0.8
                    else:
                        y_pos += self.font_obj.get_rect(self.text_list[i][j])[3] + self.vert_spacing
            y_max.append(y_pos)
        text_box_height = max(y_max) - self.y_init_pos
        return (self.x_right_pos - text_box_width, self.y_init_pos, text_box_width, text_box_height)
