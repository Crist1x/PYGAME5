import pygame
import os
import sys


def load_image(name):
    fullname = os.path.join("images", name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением {fullname} не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

def main():
    pygame.init()
    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Спрайты')
    screen.fill("white")
    image = load_image("bomb.png")
    running = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приёма и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            # РЕАКЦИЯ НА ОСТАЛЬНЫЕ СОБЫТИЯ
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.blit(image, (event.pos[0] - image.get_width()//2,
                                    event.pos[1] - image.get_width()//2))
        # отрисовка и изменение свойств объектов
        # ...
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
