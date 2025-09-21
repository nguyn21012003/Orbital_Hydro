set terminal qt size 600,600
set datafile separator ","

set palette defined (\
0 '#604860',\
1 '#784860',\
2 '#a86060',\
3 '#c07860',\
4 '#f0a848',\
5 '#f8ca8c',\
6 '#feecae',\
7 '#fff4c2',\
8 '#fff7db',\
9 '#fffcf6')



unset tics
unset border
unset title
unset colorbox


splot "orbital.csv" using 1:2:3:4 with points pt 7 ps 0.5 palette notitle

