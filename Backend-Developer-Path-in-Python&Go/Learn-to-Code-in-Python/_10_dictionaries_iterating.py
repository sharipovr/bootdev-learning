def get_most_common_enemy(enemies_dict):
    # if enemies_dict == None:
    #   return None
    
    most_common_name = None
    most_common_qty = float("-inf")

    for k in enemies_dict:
        if enemies_dict[k] > most_common_qty:
            most_common_qty = enemies_dict[k]
            most_common_name = k

    return most_common_name