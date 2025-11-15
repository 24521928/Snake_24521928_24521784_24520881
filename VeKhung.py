import pygame


#define MINX 2
#define MINY 2
#define MAXX 35
#define MAXY 20
void VeKhung(){
    for (int i = MINX ; i<=MAXX ; i++)
        for (int j = MINY ; j<=MAXY ; j++)
            if ((i==MINX) || (i==MAXX) || (j==MINY) || (j==MAXY)){
                gotoxy(i,j);
                printf("+");
            }
}

def VeKhung(screen, width, height):
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, width, height), 10)
