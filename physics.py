import pygame

pygame.init()
h_res, v_res = 1280,720
screen = pygame.display.set_mode((h_res, v_res))

clock = pygame.time.Clock()
x,y = 0.5,0
delta_x, delta_y = 0.05,0.02
gravity = 0.001
damper = 0.9
while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

    screen.fill("purple")  # Fill the display with a solid color
    color = (255,255,255)

    if x<0:
        delta_x *= -1
        delta_x *= damper
        x = 0

    if x>1:
        delta_x *= -1
        delta_x *= damper
        x = 1
    
    if y<0:
        delta_y *= -1
        delta_y *= damper
        y = 0

    if y>1:
        delta_y *= -1
        delta_y *= damper
        y = 1
    
    

    x += delta_x
    y += delta_y
    
        

    delta_y += gravity

    print(delta_y)


    rectangle = pygame.Rect((x*h_res,y*v_res),(20,20)) # left, top, width, height
    pygame.draw.rect(screen,color,rectangle)
    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)