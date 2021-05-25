import pygame  
  
pygame.init()  
surface = pygame.Surface((400,500))
surface=pygame.Surface(
done = False  
  
while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
    pygame.display.flip()
