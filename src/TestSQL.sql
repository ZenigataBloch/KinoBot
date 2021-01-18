create table movie
(
    titolo varchar(50),
    anno varchar(4),
    trama varchar(500),
    poster varchar(50),
    trailer varchar(50),
    download varchar(100)
);
LOAD DATA LOCAL INFILE 'H:/#CorsoJava/#ProgrammiPersonali/KinoBot/src/Movies.txt' INTO TABLE movie
FIELDS TERMINATED BY '/--/' LINES TERMINATED BY '\n';

select movie.titolo
from movie