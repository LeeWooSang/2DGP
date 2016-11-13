import sys
import game_framework
sys.path.append('../LabsAll/Labs')

import random
from pico2d import *

running = None


class Stage:
    def __init__(self):
        self.image = load_image('office.png')

    def draw(self):
        self.image.draw(400, 300)

class Coin1:
    image = None
    SHOW_coin, HIDE_coin = 0, 1

    def __init__(self):
        self.x, self.y = 70, 50
        self.state = self.SHOW_coin
        self.image = load_image('coin.png')

    def draw(self):
        self.image.draw(self.x, self.y)

class Laborer1:

    PIXEL_PER_METER = (10.0 /0.3) # 10 pixel 30cm
    RUN_SPEED_KMPH = 20.0 # 20km/h
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0) # m/m
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0) # m/s
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None

    LEFT_RUN, RIGHT_RUN = 1, 0

    def handle_left_run(self):
        self.x -= 5
        self.run_frames += 1

        if self.x < 100:
            self.state = self.RIGHT_RUN
            self.x = 100

    def handle_right_run(self):
            self.x += 5
            self.run_frames += 1

            if self.x > 220:
                self.state = self.LEFT_RUN
                self.x = 220

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run
    }

    def update(self):
       #distance = Laborer1.RUN_SPEED_PPS * frame_time
       self.run_frames += 1.0
       self.frame = (self.frame + 1) % 4
       self.handle_state[self.state](self)


    def __init__(self):
        self.x, self.y = 100, 90
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.state = self.RIGHT_RUN
        if self.state == self.RIGHT_RUN:
            self.run_frames = 0
            self.state = self.LEFT_RUN

        if Laborer1.image == None:
            Laborer1.image = load_image('Boy_animation2_sheet.png')

    def draw(self):
        self.image.clip_draw(self.frame * 90 , self.state * 150, 90, 140, self.x, self.y)

class Laborer2:
    image = None

    LEFT_RUN, RIGHT_RUN = 1, 0

    def handle_left_run(self):
        self.x -= 5
        self.run_frames += 1

        if self.x < 400:
            self.state = self.RIGHT_RUN
            self.x = 400

    def handle_right_run(self):
            self.x += 5
            self.run_frames += 1

            if self.x > 550:
                self.state = self.LEFT_RUN
                self.x = 550

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run
    }

    def update(self):
       self.frame = (self.frame + 1) % 4
       self.handle_state[self.state](self)


    def __init__(self):
        self.x, self.y = 400, 250
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.state = self.RIGHT_RUN
        if self.state == self.RIGHT_RUN:
            self.run_frames = 0
            self.state = self.LEFT_RUN

        if Laborer2.image == None:
            Laborer2.image = load_image('Boy_animation2_sheet.png')

    def draw(self):
        self.image.clip_draw(self.frame * 90 , self.state * 150, 90, 140, self.x, self.y)

class Laborer3:
    image = None

    LEFT_RUN, RIGHT_RUN = 1, 0

    def handle_left_run(self):
        self.x -= 5
        self.run_frames += 1

        if self.x < 220:
            self.state = self.RIGHT_RUN
            self.x = 220

    def handle_right_run(self):
            self.x += 5
            self.run_frames += 1

            if self.x > 300:
                self.state = self.LEFT_RUN
                self.x = 300

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run
    }

    def update(self):
       self.frame = (self.frame + 1) % 4
       self.handle_state[self.state](self)


    def __init__(self):
        self.x, self.y = 300, 350
        self.frame = random.randint(0, 7)
        self.run_frames = 0
        self.state = self.RIGHT_RUN
        if self.state == self.RIGHT_RUN:
            self.run_frames = 0
            self.state = self.LEFT_RUN

        if Laborer3.image == None:
            Laborer3.image = load_image('Boy_animation2_sheet.png')

    def draw(self):
        self.image.clip_draw(self.frame * 90 , self.state * 150, 90, 140, self.x, self.y)

def handle_events():
    global running
    global coin1

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()
laborer1 = Laborer1()
laborer2 = Laborer2()
laborer3 = Laborer3()

def main():

    stage = Stage()

    global coin1
    coin1 = Coin1()

    global running
    running = True

    while running:
        handle_events()

        laborer1.update()
        laborer2.update()
        laborer3.update()

        clear_canvas()

        stage.draw()
        coin1.draw()

        laborer1.draw()
        laborer2.draw()
        laborer3.draw()

        update_canvas()

        delay(0.02)

    close_canvas()

if __name__ == '__main__':
    main()