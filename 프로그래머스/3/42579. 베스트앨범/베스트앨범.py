def solution(genres, plays):
    
    genre_play = {}
    for idx, (g, p) in enumerate(zip(genres, plays)):
        if g not in genre_play:
            genre_play[g] = [(p, idx)]
        else:
            genre_play[g].append((p, idx))
    
    genre_sum = {genre: sum(p for p, idx in play) for genre, play in genre_play.items()}
    
    sorted_genres = sorted(genre_sum.keys(), key=lambda x:genre_sum[x], reverse=True)
    
    answer = []
    for genre in sorted_genres:
        songs = sorted(genre_play[genre], key=lambda x:(-x[0], x[1]))
        answer.extend([idx for _, idx in songs[:2]])
    
    return answer
        