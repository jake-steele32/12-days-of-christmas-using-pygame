import pygame
import time

pygame.init()

BLACK = (0,0,0)
GOLD   = (255,215,0)

SCREENWIDTH = 500
SCREENHEIGHT = 500

font = pygame.font.Font(None, 25)

window = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT ))
pygame.display.set_caption("12 days of christmas")

def partridge(message):
    partridge_pic = pygame.image.load('day 1.JPG').convert()
    partridge_pic = pygame.transform.scale(partridge_pic, (SCREENWIDTH,SCREENHEIGHT ))

    window.blit(partridge_pic, (0,0))
    text = font.render(str(message), 1, BLACK)
    window.blit(text, (150,475))

def doves():
    doves_pic = pygame.image.load('day 2.JPG').convert()
    doves_pic = pygame.transform.scale(doves_pic, (SCREENWIDTH,SCREENHEIGHT ))

    window.blit(doves_pic, (0,0))
    text = font.render(str('two turtle doves'), 1, BLACK)
    window.blit(text, (175,475))

def hens():
    hens_pic = pygame.image.load('day 3.JPG').convert()
    hens_pic = pygame.transform.scale(hens_pic, (SCREENWIDTH,SCREENHEIGHT ))

    window.blit(hens_pic, (0,0))
    text = font.render(str('three french hens'), 1, BLACK)
    window.blit(text, (175,475))

def birds():
    birds_pic = pygame.image.load('day 4.PNG').convert()
    birds_pic = pygame.transform.scale(birds_pic, (SCREENWIDTH,SCREENHEIGHT ))

    window.blit(birds_pic, (0,0))
    text = font.render(str('four calling birds'), 1, BLACK)
    window.blit(text, (175,475))

def rings():
    rings_pic = pygame.image.load('day 5.JPG').convert()
    rings_pic = pygame.transform.scale(rings_pic, (SCREENWIDTH,SCREENHEIGHT ))

    window.blit(rings_pic, (0,0))
    text = font.render(str('five gold rings'), 1, BLACK)
    window.blit(text, (175,475))

def geese():
    geese_pic = pygame.image.load('day 6.PNG').convert()
    geese_pic = pygame.transform.scale(geese_pic, (SCREENWIDTH,SCREENHEIGHT ))

    window.blit(geese_pic, (0,0))
    text = font.render(str('six geese a-laying'), 1, BLACK)
    window.blit(text, (175,475))

def swans():
    swans_pic = pygame.image.load('day 7.JPG').convert()
    swans_pic = pygame.transform.scale(swans_pic, (SCREENWIDTH,SCREENHEIGHT ))

    window.blit(swans_pic, (0,0))
    text = font.render(str('seven swans a-swimming'), 1, BLACK)
    window.blit(text, (150,475))

def maids():
    maids_pic = pygame.image.load('day 8.JPG').convert()
    maids_pic = pygame.transform.scale(maids_pic, (SCREENWIDTH,SCREENHEIGHT ))

    window.blit(maids_pic, (0,0))
    text = font.render(str('eight maids a-milking'), 1, BLACK)
    window.blit(text, (150,475))

def ladies():
    ladies_pic = pygame.image.load('day 9.JPG').convert()
    ladies_pic = pygame.transform.scale(ladies_pic, (SCREENWIDTH,SCREENHEIGHT ))

    window.blit(ladies_pic, (0,0))
    text = font.render(str('nine ladies dancing'), 1, BLACK)
    window.blit(text, (150,475))

def lords():
    lords_pic = pygame.image.load('day 10.JPG').convert()
    lords_pic = pygame.transform.scale(lords_pic, (SCREENWIDTH,SCREENHEIGHT ))

    window.blit(lords_pic, (0,0))
    text = font.render(str('ten lords a-leaping'), 1, BLACK)
    window.blit(text, (150,475))

def pipers():
    pipers_pic = pygame.image.load('day 11.PNG').convert()
    pipers_pic = pygame.transform.scale(pipers_pic, (SCREENWIDTH,SCREENHEIGHT ))

    window.blit(pipers_pic, (0,0))
    text = font.render(str('eleven pipers piping'), 1, BLACK)
    window.blit(text, (150,475))

def drummers():
    drummers_pic = pygame.image.load('day 12.JPG').convert()
    drummers = pygame.transform.scale(drummers_pic, (SCREENWIDTH,SCREENHEIGHT ))

    window.blit(drummers_pic, (0,0))
    text = font.render(str('twelve drummers drumming'), 1, BLACK)
    window.blit(text, (150,475))

def day1(message, dates):
    partridge(message)    
    header = font.render(str(dates), 1, BLACK)
    window.blit(header, (25,10))
    pygame.display.update()
    time.sleep(5)
    window.fill(GOLD)
    pygame.display.update()
    time.sleep(3)

def day2(message, dates):
    doves()    
    header = font.render(str(dates), 1, BLACK)
    window.blit(header, (25,10))
    pygame.display.update()
    time.sleep(5)
    day1(message, dates)

def day3(message, dates):
    hens()
    header = font.render(str(dates), 1, BLACK)
    window.blit(header, (25,10))
    pygame.display.update()
    time.sleep(5)
    day2(message, dates)

def day4(message, dates):
    birds()
    header = font.render(str(dates), 1, BLACK)
    window.blit(header, (25,10))
    pygame.display.update()
    time.sleep(5)
    day3(message, dates)

def day5(message, dates):
    rings()
    header = font.render(str(dates), 1, BLACK)
    window.blit(header, (25,10))
    pygame.display.update()
    time.sleep(5)
    day4(message, dates)

def day6(message, dates):
    geese()
    header = font.render(str(dates), 1, BLACK)
    window.blit(header, (25,10))
    pygame.display.update()
    time.sleep(5)
    day5(message, dates)

def day7(message, dates):
    swans()
    header = font.render(str(dates), 1, BLACK)
    window.blit(header, (25,10))
    pygame.display.update()
    time.sleep(5)
    day6(message, dates)

def day8(message, dates):
    maids()
    header = font.render(str(dates), 1, BLACK)
    window.blit(header, (25,10))
    pygame.display.update()
    time.sleep(5)
    day7(message, dates)

def day9(message, dates):
    ladies()
    header = font.render(str(dates), 1, BLACK)
    window.blit(header, (25,10))
    pygame.display.update()
    time.sleep(5)
    day8(message, dates)

def day10(message, dates):
    lords()
    header = font.render(str(dates), 1, BLACK)
    window.blit(header, (25,10))
    pygame.display.update()
    time.sleep(5)
    day9(message, dates)

def day11(message, dates):
    pipers()
    header = font.render(str(dates), 1, BLACK)
    window.blit(header, (25,10))
    pygame.display.update()
    time.sleep(5)
    day10(message, dates)

def day12(message, dates):
    drummers()
    header = font.render(str(dates), 1, BLACK)
    window.blit(header, (25,10))
    pygame.display.update()
    time.sleep(5)
    day11(message, dates)

message = "A partridge in a pear tree"
dates = 'on the first day of christmas my true love gave to me:'
day1(message, dates)
message = "And a partridge in a pear tree"
dates = 'on the second day of christmas my true love gave to me:'
day2(message, dates)
dates = 'on the third day of christmas my true love gave to me:'
day3(message, dates)
dates = 'on the fourth day of christmas my true love gave to me:'
day4(message, dates)
dates = 'on the fifth day of christmas my true love gave to me:'
day5(message, dates)
dates = 'on the sixth day of christmas my true love gave to me:'
day6(message, dates)
dates = 'on the seventh day of christmas my true love gave to me:'
day7(message, dates)
dates = 'on the eigth day of christmas my true love gave to me:'
day8(message, dates)
dates = 'on the ninth day of christmas my true love gave to me:'
day9(message, dates)
dates = 'on the tenth day of christmas my true love gave to me:'
day10(message, dates)
dates = 'on the eleventh day of christmas my true love gave to me:'
day11(message, dates)
dates = 'on the twelth day of christmas my true love gave to me:'
day12(message, dates)
