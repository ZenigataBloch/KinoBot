import sys

lbreak = '/--/'
loop = True

f = open('src/Movies.txt', 'a')
while(loop == True):
    titolo = input('Titolo: ')
    ttrad = input('Titolo tradotto: ')
    anno = input('Anno: ')
    trama = input('Trama: ')
    poster = input('Poster: ')
    trailer = input('Trailer: ')
    download = input('Magnet: ')
    x = input('Continua? ')

    f.write(titolo + lbreak + ttrad + lbreak + anno + lbreak + trama + lbreak + poster + lbreak + trailer + lbreak + download)

    if(x.lower() == 'y'):
        loop == True
        f.write('\n')
    else:
        loop == False
        f.write('\n')
        break   