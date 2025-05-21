def calculate_handicap(score, rating, slope):
    return round((score - rating) * 113 / slope, 1)

