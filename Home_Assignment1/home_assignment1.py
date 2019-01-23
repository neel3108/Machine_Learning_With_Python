# # Ex-1 Pawn BrotherHood
def checkio(game_result: List[str]) -> str:
    
    for i in range(3):
        if (game_result[i][0] in ['O', 'X']) and (game_result[i][0] == game_result[i][1] == game_result[i][2]):
            return game_result[i][0]
        if (game_result[0][i] in ['O', 'X']) and (game_result[0][i] == game_result[1][i] == game_result[2][i]):
            return game_result[0][i]
    if (game_result[1][1] in ['O', 'X']) and ((game_result[0][0] == game_result[1][1] == game_result[2][2]) or (game_result[0][2] == game_result[1][1] == game_result[2][0])):
        return game_result[1][1]
    return "D" 


      
# Ex-2 Refree
def safe_pawns(pawns):
    ploc = set()
    safeCount = 0
    for p in pawns:
        row  = int(p[1]) - 1
        col = ord(p[0]) - 97
        ploc.add((row, col))
    for row, col in ploc:
        safe = safe = any(((row - 1, col - 1) in ploc, (row - 1, col + 1) in ploc))
        if safe:
            safeCount += 1
    return safeCount  

#Ex-3 Long Reapet 

def long_repeat(line):
    count = 0
    countList = []
    for i in range(len(line) - 1):
        if line[i] == line[i+1]:
            count += 1    
            countList.append(count)
        else:
             countList.append(count)
            count = 0    
    return max(countList) + 1

print (long_repeat("dddsssdddssss"))