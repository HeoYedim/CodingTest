def solution(players, callings):
    
    player_dic = {player : rank for rank, player in enumerate(players)}
    
    for call in callings:
        
        winner = player_dic[call]
        loser =  winner - 1
        
        players[winner], players[loser] = players[loser], players[winner]
        
        player_dic[players[winner]] += 1
        player_dic[players[loser]] -= 1
        
        
    return players