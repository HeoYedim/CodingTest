def solution(players, callings):
    player_dict = {player: rank for rank, player in enumerate(players)}
    
    for calling in callings:
        current_rank = player_dict[calling]
        previous_rank = current_rank - 1
        
        players[current_rank], players[previous_rank] = players[previous_rank], players[current_rank]
        
        player_dict[players[current_rank]] = current_rank
        player_dict[players[previous_rank]] = previous_rank
        
    return players