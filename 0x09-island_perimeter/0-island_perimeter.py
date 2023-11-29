#!/usr/bin/python3
# island perimeter script


def island_perimeter(grid):
    length = 1
    width = 0

    for i in grid:
        for j in i:
            if i[j] == 1:
                width += 1

    le = len(grid)
    j = len(i)
    if le * j <= 100:
        per = (2*(length + width))
        return(per)
