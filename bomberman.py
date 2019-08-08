import time, sys
from os import system

bomberman_field = [ "....0.0.0....",
                    ".0.........0.",
                    "......0......",
                    "...0.....0...",
                    "0.....0.....0",
                    "...0.....0...",
                    "0.....0.....0",
                    "...0.....0...",
                    "......0......",
                    ".0.........0.",
                    "....0.0.0...." ]

for i in range(len(bomberman_field)):
    bomberman_field[i] = list(bomberman_field[i])

def find_all_crates():
    crates = []
    for y in range(len(bomberman_field)):
        for x in range(len(bomberman_field[y])):
            if(bomberman_field[y][x] == '0'):
                crates.append([y,x])
    return crates

def calculate_distance(a,b):
    if(b):
        return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
    return False

def find_nearest_crate(p_loc, crates): #p_loc[0] = y, p_loc[1] = x
    min_distance = 100
    nearest_crate = []
    for i in crates:
        distance = ((i[0]-p_loc[0])**2 + (i[1]-p_loc[1])**2)**0.5
        #print(distance)
        if(distance < min_distance):
            min_distance = distance
            nearest_crate = [i[0], i[1]]
    #print(min_distance, nearest_crate)
    return nearest_crate

def simulate_bomb(radius, bomb_place):
    #Radius + bomb_location will give you the amount of crates hit and which crates got hit.
    directions = [[-1,0], [1,0], [0,-1], [0,1]]
    hit = 0
    hit_coors = []
    #for instance, radius==3 and bomb_place==[y,x]==[4,3]
    for dir in directions:
        for a in range(1, radius+1):
            y = bomb_place[0] + a*dir[0]
            x = bomb_place[1] + a*dir[1]
            if(y >= 0 and y < len(bomberman_field) and x >= 0 and x < len(bomberman_field[0])):
                if(bomberman_field[y][x] == '0'):
                    hit += 1
                    hit_coors.append([y,x])
                    break
                else:
                    continue
            else:
                break
    return hit, hit_coors

def find_best_place(player_place, crates):
    min_hits = 0
    final_coors = []
    bomb_coors = []
    arr = []
    for y in range(len(bomberman_field)):
        for x in range(len(bomberman_field[y])):
            if(bomberman_field[y][x] != '0'):
                hits, coors = simulate_bomb(3, [y,x])
                if(min_hits <= hits):
                    if(min_hits != hits):
                        arr = []
                    min_hits = hits
                    #if(len(final_coors) == 0 or calculate_distance(player_place, [y,x]) < calculate_distance(player_place, final_coors)):
                    final_coors = [y,x]
                    bomb_coors = coors
                    arr.append(final_coors)
    final_coors = (find_nearest_crate(player_place, arr))
    throwaway, bomb_coors = simulate_bomb(3, final_coors)
    #print(find_nearest_crate(player_place, arr))
    return min_hits, final_coors, bomb_coors

def remove_crate(crate, all_crates):
    #Removes the crate from the board and from the array where all the crates are in stored
    bomberman_field[crate[0]][crate[1]] = '.'
    all_crates.remove(crate)


def show_field():
    #shows the field
    _ = system('cls') 
    for i in bomberman_field:
        for x in i:
            print(x, end='')
        print('')

def possible_direction(p, d):
    y = p[0] + d[0]
    x = p[1] + d[1]
    if(x>=0 and x<len(bomberman_field[0]) and y>=0 and y<len(bomberman_field) and bomberman_field[y][x] != '0'):
        return True
    return False

def new_place(p, d, i):
    return [p[0] + d[0], p[1] + d[1], i]

def show_path(path, i):
    if i <= 0:
        path.append(path_tw[i])
        return True
    else:
        show_path(path, path_tw[i][2])
        path.append(path_tw[i])

def walking_path(player_place, end_goal):
    arr = [player_place]
    i = 0
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    # while(player_place != goal_place):
    while(i < len(arr)):
        for dir in directions:
            if(possible_direction(arr[i],dir)):
                new_location = new_place(arr[i], dir, i)
                arr.append(new_location)
                if(new_location[0] == end_goal[0] and new_location[1] == end_goal[1]):
                    return arr
        i += 1
c = find_all_crates()

player_location = [0,0]
for i in range(12):
    hits, l, x = find_best_place(player_location ,c)

    path_tw = (walking_path(player_location, l))
    final_path = []
    show_path(final_path, path_tw[-1][2])
    final_path.append(l)
    for p in range(1,len(final_path)):
        bomberman_field[final_path[p][0]][final_path[p][1]] = 'x'
        bomberman_field[final_path[p-1][0]][final_path[p-1][1]] = '.'
        show_field()

    player_location = l
    for crates in x:
        remove_crate(crates,c)
    show_field()
