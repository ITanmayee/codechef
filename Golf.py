"""

It's a lockdown. You’re bored in your house and are playing golf in the hallway.

The hallway has N+2 tiles numbered from 0 to N+1 from left to right. There is a hole on tile number x. You hit the ball standing on tile 0. When you hit the ball, it bounces at lengths of k, i.e. the tiles covered by it are 0,k,2k,…, and so on until the ball passes tile N+1.

If the ball doesn't enter the hole in the first trial, you try again but this time standing on the tile N+1. When you hit the ball, it bounces at lengths of k, i.e. the tiles covered by it are (N+1),(N+1−k),(N+1−2k),…, and so on until the ball passes tile 0.

Find if the ball will enter the hole, either in its forward journey or backward journey.

"""
# cook your dish here
def check(no_of_tiles, check_tile, jumps):
    if check_tile % jumps == 0:
        return "YES"
    if (no_of_tiles + 1 - check_tile) % jumps == 0:
        return "YES"
    return "NO"

for _ in range(int(input())):
    no_of_tiles, check_tile, jumps = map(int, input().split())
    
    print(check(no_of_tiles, check_tile, jumps))
