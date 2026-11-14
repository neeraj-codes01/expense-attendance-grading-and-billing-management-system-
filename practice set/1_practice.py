watched = ["Action", "Comedy", "Action", "Drama", "Comedy","Action", "Action"]
frequency = {}
for genre in watched:
    if genre in frequency:
        frequency[genre] += 1
    else:
        frequency[genre] = 1
print("frequency:", frequency)

distinct = set(watched)
print("distinct genre:", distinct)

most_watched = max(frequency, key = frequency.get)
print("most watched:", most_watched)
print("count:", frequency[most_watched])

report = ",".join(genre.upper() for genre in watched)
print("report:",report)