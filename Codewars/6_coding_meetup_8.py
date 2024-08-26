def all_continents(lst):
    zones = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
    for ele in lst:
        if ele['continent'] in zones:
            zones.remove(ele['continent'])
        if len(zones) == 0: return True
    return False