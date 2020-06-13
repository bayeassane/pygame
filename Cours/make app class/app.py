import pygame 
from pygame.locals import *



class Node:
    pos = [0, 0]
    gap = (0, 0)
    direction = (0, 1)
    size = (100, 50)

    def __init__(self, pos=(0, 0), size=(100, 50), gap=(10, 10), direction=(0, 1)):
        App.scene.nodes.append(self)

        if [0, 0] != list(pos):
            print('ok')
            Node.pos = pos

        if direction != (0, 1): # la position par défaut vertical
            Node.direction = direction
        
        if (10, 10) != gap: # l'espacement
            Node.gap = gap
        
        if (100, 50) != size: # la taille du noeud
            Node.size = size


        self.pos = Node.pos
        self.size = Node.size
        print(Node.direction)

       
        self.rect = pygame.Rect(self.pos, self.size)

        if (1, 0) == Node.direction: # horizontale
            Node.pos = [Node.pos[0] + self.size[0] + Node.gap[0], Node.pos[1]]
        elif (0, 1) == Node.direction: # verticale
            Node.pos = [Node.pos[0], Node.pos[1] + self.size[1] + Node.gap[1]]
        elif (1, 1) == Node.direction:
            Node.pos = [Node.pos[0] + self.size[0] + Node.gap[0], Node.pos[1] + self.size[1] + Node.gap[1]]           
    

        print(self.__dict__)
    
    def draw(self):
        pygame.draw.rect(App.screen, Color('blue'), self.rect, 1)


class Text(Node):
    fontname = None
    fontsize = 36
    fontcolor = Color('black')
    background = None
    italic = False
    bold = False
    underline = False
    
    def __init__(self, text, pos=(0, 0), font_name=None, background=None, font_size=48, font_color=Color('black'), italic=False, bold=False, underline=False):
        super().__init__(pos)
        App.scene.nodes.append(self)
        self.text = text
        self.font_name = font_name
        self.font_size = font_size
        self.font_color = font_color
        self.bold = bold
        self.underline = underline
        self.italic = italic
        self.background = background

        self.set_font()
        self.render()


    def set_font(self):
        self.font = pygame.font.Font(self.font_name, self.font_size)
        self.font.set_bold(self.bold)
        self.font.set_italic(self.italic)
        self.font.set_underline(self.underline)

    
    def render(self):
        self.img = self.font.render(self.text, True, self.font_color, self.background)
        self.rect = self.img.get_rect()
    
    def draw(self):
        App.screen.blit(self.img, self.rect)
        self.rect.topleft = self.pos
    

class Textdit(Text):
    
    def __init__(self):
        pass




class Scene:
    """Create new scene"""
    id = 0

    def __init__(self, bg=Color('gray'), *args, **kwargs):
        App.scenes.append(self)
        App.scene = self

        self.id = Scene.id
    
        self.bg = bg

        # liste des noeuds 
        self.nodes = []

        Scene.id += 1
    
    def __str__(self):
        return f'Scene {self.id}'

    def draw(self):
        if isinstance(self.bg, str):
            self.img = pygame.image.load(self.bg)
            self.rect = self.img.get_rect()
            App.screen.blit(self.img, self.rect)
        else:
            App.screen.fill(self.bg)
        for node in self.nodes:
            node.draw()
        pygame.display.flip()




class App:
    # liste des scenes 
    scenes = []
    # scène active
    scene = None

    def __init__(self):
        pygame.init()
        flags = RESIZABLE
        App.screen = pygame.display.set_mode((640, 300), flags)

        # App.t = Text('Pygame App', (20, 20))


        App.running = True

    
    def run(self):
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False
            
            App.screen.fill(Color('gray'))
            App.scene.draw()
            pygame.display.update()
