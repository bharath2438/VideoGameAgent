import pygame as pg
from math import cos, sin, degrees, radians
from pygame.math import Vector2

pg.init()
screen = pg.display.set_mode((800, 600))

class Car:
    def __init__(self, x, y, angle=0.0, length=4):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.acceleration = 0.0001
        self.steering = 0.0
        self.movingForward = False
        self.movingBackward = False
        self.isSteering = False

    def update(self):
        if self.movingForward:
            self.velocity += (self.acceleration, 0)
        if self.movingBackward:
            self.velocity += (-self.acceleration, 0)
        if self.isSteering and not self.steering == 0:
            turning_radius = self.length / sin(radians(self.steering))
            angular_velocity = self.velocity.x / turning_radius
        else:
            angular_velocity = 0

        self.position += self.velocity.rotate(-self.angle)
        self.angle += degrees(angular_velocity)
       
def main():
    carImage = pg.image.load("sprites/car.png")
    carImage = pg.transform.scale(carImage, (64, 32))
    bgImage = pg.image.load("sprites/bg.jpeg")
    bgImage = pg.transform.scale(bgImage, (800, 600))
    car = Car(10, 10)
    clock = pg.time.Clock()
    ppu = 32
    while True:
        
        dt = clock.get_time() / 1000

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                break
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    car.movingForward = True
                if event.key == pg.K_s:
                    car.movingBackward = True
                if event.key == pg.K_a:
                    car.steering += 60
                    if car.steering == 0:
                        car.steering += 60
                    car.isSteering = True
                if event.key == pg.K_d:
                    car.steering -= 60
                    if car.steering == 0:
                        car.steering -= 60
                    car.isSteering = True                
            if event.type == pg.KEYUP:
                if event.key == pg.K_w:
                    car.movingForward = False
                    car.velocity = Vector2(0.0, 0.0)
                if event.key == pg.K_s:
                    car.movingBackward = False
                    car.velocity = Vector2(0.0, 0.0)
                if event.key == pg.K_a:
                    car.steering -= 60
                    if car.steering == 0:
                        car.steering -= 60                    
                    car.isSteering = False
                if event.key == pg.K_d:
                    car.steering += 60
                    if car.steering == 0:
                        car.steering += 60                    
                    car.isSteering = False 

        car.update()
        
        screen.fill((255, 255, 255))
        rotated = pg.transform.rotate(carImage, car.angle)
        rect = rotated.get_rect()
        screen.blit(bgImage, (0, 0))
        screen.blit(rotated, car.position * ppu - (rect.width / 2, rect.height / 2))
                   
        pg.display.update()        
        clock.tick(120)


if __name__ == "__main__":
    main()
