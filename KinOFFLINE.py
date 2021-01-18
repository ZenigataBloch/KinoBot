from classes import Cinema

file =  open('src/Movies.txt', 'r')  #unpacks the file
f = file.readlines()
for line in f:
    rd = line.strip().split('/--/')
    movie = Cinema.Film(rd[0],rd[1],rd[2],rd[3],rd[4],rd[5],rd[6])
    print(movie.title_ita)