import random
import os

from pico2d import *

import game_framework
import sys
sys.path.append('../LabsAll/Labs')

stage = None
coin1 = None
laborer1 = None

class Stage:
    def __init__(self):
        self.image = load_image('office.png')

    def draw(self):
        self.image.draw(400, 300)

class Coin1:
    # SHOW_coin, HIDE_coin = 0, 1

    def __init__(self):
        self.x, self.y = 70, 50
        #self.state = self.SHOW_coin
        self.image = load_image('coin.png')

    def draw(self):
        self.image.draw(70, 50)

class Laborer1:

    PIXEL_PER_METER = (10.0 /0.3) # 10 pixel 30cm
    RUN_SPEED_KMPH = 20.0 # 20km/h
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0) # m/m
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0) # m/s
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    image = None

    LEFT_RUN, RIGHT_RUN = 0, 1

    def __init__(self):
        self.x, self.y = 100, 90
        self.frame = random.randint(0, 7)
        self.life_time = 0.0
        self.total_frames = 0
        self.dir = 1
        self.state = self.RIGHT_RUN
        if Laborer1.image == None:
            Laborer1.image = load_image('Boy_animation2_sheet.png')

    def update(self, frame_time):
        self.life_time += frame_time
        distance = Laborer1.RUN_SPEED_PPS * frame_time
        self.total_frames += Laborer1.FRAMES_PER_ACTION * Laborer1.ACTION_PER_TIME * frame_time
        self.frame = (self.frame + 1) % 4
        self.x += (self.dir * distance)

        if self.x > 220:
            self.x = 220
            self.dir = 0
            self.state = self.LEFT_RUN
            #print("Change Time: %f, Total Frames: %d" % (self.life_time, self.total_frames))

        elif self.x < 100:
            self.x = 100
            self.dir = 1
            self.state = self.RIGHT_RUN
            #print("Change Time: %f, Total Frames: %d" % (self.life_time, self.total_frames))


    def draw(self):
        self.image.opacify(random.random())
        self.image.clip_draw(self.frame * 90, self.state * 150, 90, 140, self.x, self.y)
        #font.draw(self.x - 50, self.y + 40, 'Time: %3.2f' % self.life_time)
        #self.image.clip_draw(self.frame * 90 , self.state * 150, 90, 140, self.x, self.y)

def handle_events(frame_time):
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

def update(frame_time):
    global laborer1
    laborer1.update(frame_time)
    delay(0.05)

def draw(frame_time):
    global laborer1, coin1, stage

    clear_canvas()
    stage.draw()
    laborer1.draw()
    coin1.draw()
    update_canvas()

def enter():
    global laborer1, stage
    open_canvas()
    laborer1 = Laborer1()
    stage = Stage()
    game_framework.reset_time()

def exit():
    global laborer1, stage
    del (coin1)
    del (laborer1)
    del (stage)
    close_canvas()


