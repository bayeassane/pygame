from app import *


class Demo(App):

    def __init__(self):
        super().__init__()
       
        Scene(caption='Intro')
        Text('Default text', pos=(20, 20))
        Text('fontsize = 24', font_size=24)
        Text('fontcolor = RED', font_color=Color('red'))
        Text('48 pts, blue', font_size=48, font_color=Color('blue'))
        Text('fontbg = yellow', background=Color('yellow'))

        Text('italic', pos=(400, 20), italic=True)
        Text('bold', bold=True)
        Text('underline', underline=True, background=None)
      
       

        App.scene = App.scenes[0]



if __name__ == '__main__':
    Demo().run()