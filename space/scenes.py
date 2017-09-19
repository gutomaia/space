import wx
import pygame


class SceneBase(object):

    def __init__(self):
        self.next = self
        self.context = {}

    def process_input(self, events, keys):
        pass

    def update(self, deltaTime):
        pass

    def render(self, screen):
        pass

    def go_to_scene(self, next_scene):
        self.next = next_scene

    def terminate(self):
        self.go_to_scene(None)


class TitleScene(SceneBase):

    def process_input(self, events, keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.go_to_scene(GameScene())

    def render(self, screen):
        screen.fill((255, 0, 0))


from players import Missile
from consts import BLACK


class GameScene(SceneBase):

    def __init__(self):
        self.next = self
        from movement import Seek
        from consts import Vector
        self.missile = Missile(Vector(100,100))


        self.target = Missile(Vector(300, 300))
        self.missile.movement = Seek(self.missile, self.target)
        # self.missiles = pygame.sprite.Group()
        # self.missiles.add(self.missile)

    def process_input(self, events, keys):
        for e in events:
            if e.type == pygame.MOUSEMOTION:
                self.target.position.x += e.rel[0]
                self.target.position.y += e.rel[1]
                print e.pos, e.rel

    def update(self, dt):
        self.missile.update(dt)

    def render(self, screen):
        screen.fill(BLACK)
        self.missile.render(screen)
        self.target.render(screen)
        # self.missiles.update(1, 2)
        # self.missiles.draw(screen)



def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    active_scene = starting_scene

    deltaTime = 0
    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()

        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                active_scene.terminate()
            else:
                filtered_events.append(event)

        active_scene.process_input(filtered_events, pressed_keys)
        active_scene.update(deltaTime)
        active_scene.render(screen)

        active_scene = active_scene.next

        pygame.display.flip()
        deltaTime = 1 / float(clock.tick(fps))
