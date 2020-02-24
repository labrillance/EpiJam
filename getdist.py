def get_distance(player, planete):
    xdist = (all_planete[player.position].x - all_planete[planete].x) * infoObject.current_w / 1600
    ydist = (all_planete[player.position].y - all_planete[planete].y) * infoObject.current_h / 1080
    return round(math.sqrt(math.pow(xdist, 2) + math.pow(ydist, 2)))