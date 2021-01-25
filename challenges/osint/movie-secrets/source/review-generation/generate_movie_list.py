#!/usr/bin/env python3

import random

def create_format(movie_name, meta_rank):
    rank = int(meta_rank % 10 + random.randint(1, 10))
    if meta_rank > 10:  rank += random.randint(0, 3)
    if meta_rank < 80 or not random.randint(0, 100): rank -= random.randint(0, 4)
    while(rank > 10): rank -= random.randint(-1, 4)
  
    if movie_name == "The Goonies": rank = 10
    return f"<tr><td><a href=\"missing-review.html\">{movie_name}</a></td><td>{rank}/10</td></tr>\n"

def main():
    movies = []
    rankings = []
    final_html = ""

    with open("movies", "r") as movie_list: movies = movie_list.read().split(', ')
    with open("rankings", "r") as rank_list: rankings = rank_list.read().split(', ')

    for index, movie in enumerate(movies):
        final_html += create_format(movie, float(rankings[index]))

    print(final_html)
    return

if __name__ == "__main__": main()
