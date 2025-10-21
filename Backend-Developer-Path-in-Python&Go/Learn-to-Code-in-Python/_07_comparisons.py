def does_attack_hit(attack_roll, armor_class):
    result = (attack_roll != 1 and attack_roll >= armor_class) or attack_roll == 20
    return result