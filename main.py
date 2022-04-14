import pygame as pg

class Car:
    def __init__(self, sprite, w, h, x, y, angle):
        self.sprite = sprite
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.angle = angle

    def move(self, direction):
        if direction == 0:
            self.y -= 5   ##up
        elif direction == 1:
            self.x += 5   ##right
        elif direction == 2:
            self.y += 5   ##down
        elif direction == 3:
            self.x -= 5   ##left

    def rotate(self, direction):
        if direction == 0:
            self.sprite = pg.transform.rotate(self.sprite, self.angle)
        if direction == 1:
            self.sprite = pg.transform.rotate(self.sprite, self.angle)

def main():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    carSprite = pg.image.load("sprites/car-truck1.png")
    car = Car(carSprite, 100, 100, 100, 100, 0)
    clock = pg.time.Clock()
    
    while True:
        
        clock.tick(120)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                break

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            car.move(0)
        elif keys[pg.K_d]:
            car.angle -= 0.25
            car.rotate(0)
        elif keys[pg.K_s]:
            car.move(2)
        elif keys[pg.K_a]:
            car.angle += 0.25
            car.rotate(1)

        screen.fill((255, 255, 255))   
        screen.blit(car.sprite, (car.x, car.y))
        pg.display.update()


if __name__ == "__main__":
    main()
    pg.quit()
