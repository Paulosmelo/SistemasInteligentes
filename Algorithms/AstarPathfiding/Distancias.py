#O grafo de estações é representado por uma matriz onde cada direta[i][j] é a distancia direta entre os vertices i e j
#direta[0][1] = 10 0,0> distancia entre as estações E1 e E2
# Distancia real talvez seja melhor representado usando lista de adjacencia

direta = [
    [0.0,	10.0,	18.5,	24.8,	36.4,	38.8,	35.8,	25.4,	17.6,	9.1,	16.7,	27.3,	27.6,	29.8],
    [10.0,	0.0,	8.5,	14.8,	26.6,	29.1,	26.1,	17.3,	10.0,	3.5,	15.5,	20.9,	19.1,	21.8],
    [18.5,	8.5,	0.0,	6.3,	18.2,	20.6,	17.6,	13.6,	9.4,	10.3,	19.5,	19.1,	12.1,	16.6],
    [24.8,	14.8,	6.3,	0.0,	12.0,	14.4,	11.5,	12.4,	12.6,	16.7,	23.6,	18.6,	10.6,	15.4],
    [36.4,	26.6,	18.2,	12.0,	0.0,	3.0,	2.4,	19.4,	23.3,	28.2,	34.2,	24.8,	14.5,	17.9],
    [38.8,	29.1,	20.6,	14.4,	3.0,	0.0,	3.3,	22.3,	25.7,	30.3,	36.7,	27.6,	15.2,	18.2],
    [35.8,	26.1,	17.6,	11.5,	2.4,	3.3,	0.0,	20.0,	23.0,	27.3,	34.2,	25.7,	12.4,	15.6],
    [25.4,	17.3,	13.6,	12.4,	19.4,	22.3,	20.0,	0.0,	8.2,	20.3,	16.1,	6.4,	22.7,	27.6],
    [17.6,	10.0,	9.4,	12.6,	23.3,	25.7,	23.0,	8.2,	0.0,	13.5,	11.2,	10.9,	21.2,	26.6],
    [9.1,	3.5,	10.3,	16.7,	28.2,	30.3,	27.3,	20.3,	13.5,	0.0,	17.6,	24.2,	18.7,	21.2],
    [16.7,	15.5,	19.5,	23.6,	34.2,	36.7,	34.2,	16.1,	11.2,	17.6,	0.0,	14.2,	31.5,	35.5],
    [27.3,	20.9,	19.1,	18.6,	24.8,	27.6,	25.7,	6.4,	10.9,	24.2,	14.2,	0.0,	28.8,	33.6],
    [27.6,	19.1,	12.1,	10.6,	14.5,	15.2,	12.4,	22.7,	21.2,	18.7,	31.5,	28.8,	0.0,	5.1],
    [29.8,	21.8,	16.6,	15.4,	17.9,	18.2,	15.6,	27.6,	26.6,	21.2,	35.5,	33.6,	5.1,	0.0]
]

real = [ 
[(1, 10.0)],
[(0, 10.0),(2,8.5), (8,10.0), (9,3.5)],
[(1,8.5), (3,6.3),(8,9.4),(12,18.7)],
[(2,6.3), (4,13.0), (7,15.3), (12,12.8)],
[(3,13.0),(5,3), (6,2.4), (7,30)],
[(4,3)],
[(4,2.4)],
[(4,30), (3,15.3), (8, 9.6), (11, 6.4)],
[(2,9.4), (1,10.0),(7, 9.6),(10, 12.2)],
[(1,3.5)],
[(8,12.2)],
[(7,6.4)],
[(3,12.8), (2,18.7),(13,  5.1)],
[(12,5.1)],
]

# linha 1 -> azul
# linha 2 -> amarelo
# linha 3 -> vermelho
# linha 4 -> verde
lines = [ 
    [1, 1,  1, 1, 1,  1, 0, 0,  0,  0, 0,  0, 0, 0],
    [0, 1,  0, 0, 1,  0, 1, 1,  1,  1, 0,  0, 0, 0],
    [0, 0,  1, 0, 0,  0, 0, 0,  1,  0, 1,  0, 1, 0],
    [0, 0,  0, 1, 0,  0, 0, 1,  0,  0, 0,  1, 1, 1],
]