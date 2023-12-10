import streamlit as st
import pandas as pd
import pickle 
from fetch_poster import fetch_poster

new_df = pickle.load(open('recommend_relation_vote_avg.pkl','rb'))

def recommend_gen_vote_avg(new_df,name_movie):
    movie = []
    movie_poster = []
    ref_index = new_df[new_df['title']==name_movie].index[0]
    check_gen = new_df['genres'].iloc[ref_index]
    find_similar_gen = new_df[new_df['genres']==check_gen]
    sort_vote_average = find_similar_gen.sort_values('vote_average',ascending=False)
    if len(sort_vote_average)<6:
        limit = len(sort_vote_average)
    else:
        limit = 6
    for i in range(limit):
        movie.append(sort_vote_average['title'].iloc[i])
        movie_poster.append(fetch_poster(sort_vote_average['movie_id'].iloc[i]))
    return movie,movie_poster

def recommend_crew_vote_avg(new_df,name_movie):
    movie = []
    movie_poster = []
    ref_index = new_df[new_df['title']==name_movie].index[0]
    check_gen = new_df['crew'].iloc[ref_index]
    find_similar_gen = new_df[new_df['crew']==check_gen]
    sort_vote_average = find_similar_gen.sort_values('vote_average',ascending=False)
    if len(sort_vote_average)<6:
        limit = len(sort_vote_average)
    else:
        limit = 6
    for i in range(limit):
        movie.append(sort_vote_average['title'].iloc[i])
        movie_poster.append(fetch_poster(sort_vote_average['movie_id'].iloc[i]))
    return movie,movie_poster

def recommend_prod_vote_avg(new_df,name_movie):
    movie = []
    movie_poster = []
    ref_index = new_df[new_df['title']==name_movie].index[0]
    check_gen = new_df['production_countries'].iloc[ref_index]
    find_similar_gen = new_df[new_df['production_countries']==check_gen]
    sort_vote_average = find_similar_gen.sort_values('vote_average',ascending=False)
    if len(sort_vote_average)<6:
        limit = len(sort_vote_average)
    else:
        limit = 6
    for i in range(limit):
        movie.append(sort_vote_average['title'].iloc[i])
        movie_poster.append(fetch_poster(sort_vote_average['movie_id'].iloc[i]))
    return movie,movie_poster