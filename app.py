import streamlit as st
from create_column import create_column_gen , create_column_test
from vote_avg_relation import recommend_gen_vote_avg , recommend_crew_vote_avg ,recommend_prod_vote_avg
from Tabs import create_tabs , create_select_menu
from fetch_poster import fetch_poster
import pandas as pd
import pickle
import requests
import numpy as np


st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)
# Tab
create_tabs()
st.title('Movie Recommender System')


def recommend(movie):
  movie_index = movies[movies['title'].str.contains(movie,case=False)].index[0]
  distance = list(enumerate(similarity [movie_index]))
  movies_list = sorted(distance,key=lambda x:x[1], reverse=True)[1:7]

  recommend_movies = []
  recommended_movies_poster = []
  for i in movies_list:
    movie_id = movies.iloc[i[0]].movie_id
    # Fetch poster from API
    recommend_movies.append(movies.iloc[i[0]].title)
    recommended_movies_poster.append(fetch_poster(movie_id))
  return recommend_movies , recommended_movies_poster

# Content base
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

new_df = pickle.load(open('recommend_relation_vote_avg.pkl','rb'))

### Relation ###

### Genres ###
def recommend_gen_relation(names_gen):
   movie = []
   movie_poster = []
   ref_index = movies[movies['title']== names_gen].index[0]
   gen = movies['genres'].iloc[ref_index]
   rec_gen = movies[movies['genres']==gen]
   if len(rec_gen) < 6:
      limit = len(rec_gen)
   else:
      limit = 6
   for i in range(limit):
      movie.append(rec_gen['title'].iloc[i])
      movie_poster.append(fetch_poster(rec_gen['movie_id'].iloc[i]))
   return movie,movie_poster

def recommend_crew_relation(names_gen):
   movie = []
   movie_poster = []
   ref_index = movies[movies['title']== names_gen].index[0]
   gen = movies['crew'].iloc[ref_index]
   rec_gen = movies[movies['crew']==gen]
   if len(rec_gen) < 6:
      limit = len(rec_gen)
   else:
      limit = 6
   for i in range(limit):
      movie.append(rec_gen['title'].iloc[i])
      movie_poster.append(fetch_poster(rec_gen['movie_id'].iloc[i]))
   return movie,movie_poster

def recommend_cast_relation(names_cast):
    movie_cast = []
    movie_poster = []
    ref_index = movies[movies['title'] == names_cast].index[0]
    ref = movies['cast'].iloc[ref_index]
    text_split = ref.split()
    cast_4 = text_split[:1]
    cast_4 = ' '.join(cast_4)
    rec_cast = movies[movies['cast'].str.contains(cast_4)]
    if len(rec_cast) < 6:
        limit = len(rec_cast)
    else:
        limit = 6
    for i in range(limit):
        movie_cast.append(rec_cast['title'].iloc[i])
        movie_poster.append(fetch_poster(rec_cast['movie_id'].iloc[i]))
    return movie_cast,movie_poster

def recommend_year_relation(year):
   movie = []
   movie_poster = []
   ref_index = movies[movies['title']== year].index[0]
   gen = movies['year'].iloc[ref_index]
   rec_gen = movies[movies['year']==gen]
   if len(rec_gen) < 6:
      limit = len(rec_gen)
   else:
      limit = 6
   for i in range(limit):
      movie.append(rec_gen['title'].iloc[i])
      movie_poster.append(fetch_poster(rec_gen['movie_id'].iloc[i]))
   return movie,movie_poster

def recommend_prod_relation(country):
   movie = []
   movie_poster = []
   ref_index = movies[movies['title']== country].index[0]
   gen = movies['production_countries'].iloc[ref_index]
   rec_gen = movies[movies['production_countries'].str.contains(gen,case=False)]
   if len(rec_gen) < 6:
      limit = len(rec_gen)
   else:
      limit = 6
   for i in range(limit):
      movie.append(rec_gen['title'].iloc[i])
      movie_poster.append(fetch_poster(rec_gen['movie_id'].iloc[i]))
   return movie,movie_poster




select_movie_name = select_crew_relation = select_gen_relation = select_cast = select_year = select_prod = select_gen_vote = select_crew_vote = select_prod_vote = st.selectbox(
'What movie would you like to recommend?',
movies['title'].values
)
names,poster1   =  recommend(select_movie_name)
name_gen,poster_gen_relation = recommend_gen_relation(select_gen_relation)
name_crew,poster_crew_relation = recommend_crew_relation(select_crew_relation)
name_cast,poster_cast_relation = recommend_cast_relation(select_cast)
name_year,poster_year_relation = recommend_year_relation(select_year)
name_prod,poster_prod_relation = recommend_prod_relation(select_prod)
name_gen_vote,poster_gen_vote = recommend_gen_vote_avg(new_df,select_gen_vote)
name_crew_vote,poster_crew_vote =  recommend_crew_vote_avg(new_df,select_gen_vote)
name_prod_vote,poster_prod_vote = recommend_prod_vote_avg(new_df,select_gen_vote)

if st.button('Play'):
    create_column_test(names,poster1)
    st.subheader('หนังของผู้กำกับเดียวกัน: {}'.format(select_movie_name))
    create_column_test(name_crew,poster_crew_relation)
    st.subheader('ภาพยนตร์ประเภทเดียวกันกับ: {}'.format(select_movie_name))
    create_column_test(name_gen,poster_gen_relation)
    if len(name_cast) < 1 or len(name_year) < 1 or len(name_prod) <1:
       pass
    else:
      st.subheader('ภาพยนตร์ของนักแสดง: {}'.format(select_movie_name))
      create_column_test(name_cast,poster_cast_relation)
      st.subheader('ภาพยนตร์ปีเดียวกันกับ: {}'.format(select_movie_name))
      create_column_test(name_year,poster_year_relation)
      st.subheader('ภาพยนตร์ผลิตประเทศเดียวกันกับ: {}'.format(select_movie_name))
      create_column_test(name_prod,poster_prod_relation)
      st.subheader('หนังที่มีประเภทคล้าย ที่มีความนิยมสูง: {}'.format(select_movie_name))
      create_column_test(name_gen_vote,poster_gen_vote)
      st.subheader('หนังที่มีผู้กำกับ  ที่มีความนิยมสูง: {}'.format(select_movie_name))
      create_column_test(name_crew_vote,poster_crew_vote)
      st.subheader('หนังที่ผลิตประเทศเดียวกันกับ ที่มีความนิยมสูง: {}'.format(select_movie_name))
      create_column_test(name_prod_vote,poster_prod_vote)




# New Movies
new_movie_dict = pickle.load(open('new_movie_dict.pkl','rb'))
new_movie = pd.DataFrame(new_movie_dict) 

def recommend_new_movie(new_movie):
    movie = []
    movie_poster = []
    num_rows = len(new_movie)  # Get the number of rows in the DataFrame
    for i in range(min(6, num_rows)):  # Ensure we don't go out of bounds
        movie.append(new_movie['title'].iloc[i])
        movie_poster.append(fetch_poster(new_movie['movie_id'].iloc[i]))
    return movie , movie_poster
st.subheader('หนังใหม่')
st.link_button('See more','app3.py')
names2 ,poster_new_movie = recommend_new_movie(new_movie)
create_column_test(names2,poster_new_movie)


### Top movies ###

top_movie = pickle.load(open('top_movie.pkl','rb'))

def recommend_top_movie(top_movie,top_n=6):
   movie = []
   movie_poster = []
   num_rows = len(top_movie)
   for i in range(min(top_n,num_rows)):
      movie.append(top_movie['original_title'].iloc[i])
      movie_poster.append(fetch_poster(top_movie['movie_id'].iloc[i]))
   return movie , movie_poster

st.subheader('หนังยอดฮิต') 
st.link_button('See more','app4.py')
names3 ,poster_top_movie = recommend_top_movie(top_movie)
create_column_test(names3,poster_top_movie)


def recommend_random_movie(data):
   movie = []
   movie_poster = []
   random_index = np.random.randint(0,len(data)-1,6)
   for i in random_index:
      movie.append(data['title'].iloc[i])
      movie_poster.append(fetch_poster(data['movie_id'].iloc[i]))
   return movie , movie_poster

st.subheader('ภาพยนตร์')
st.link_button('See more','app2.py')
random_movie , poster_random = recommend_random_movie(movies)
create_column_test(random_movie,poster_random)


### Crew  recommend ###

recommend_cg_dict = pickle.load(open('recommend_crew.pkl','rb'))
recommend_cg = pd.DataFrame(recommend_cg_dict)

def recommend_crew_movie(recommend_crew,select_crew):
   movie = []
   movie_poster = []
   num_rows = len(recommend_crew)
   ref_index = recommend_crew[recommend_crew['crew'].str.contains(select_crew,case=False)]
   for i in range(min(6,num_rows)):
      movie.append(ref_index['title'].iloc[i])
      movie_poster.append(fetch_poster(ref_index['movie_id'].iloc[i]))
   return movie , movie_poster

st.subheader('Director')
select_crew = st.selectbox(
  'Select movie Director',
  recommend_cg['crew'].values
)
st.link_button('See more','app2.py')
names4 , poster_crew = recommend_crew_movie(recommend_cg,select_crew)
create_column_test(names4,poster_crew)


### Genres ###
def recommend_gen_movie(recommend_gen,select_gen):
   movie = []
   movie_poster = []
   num_rows = len(recommend_gen)
   ref_index = recommend_gen[recommend_gen['genres'].str.contains(select_gen,case=False)]
   for i in range(min(6,num_rows)):
      movie.append(ref_index['title'].iloc[i])
      movie_poster.append(fetch_poster(ref_index['movie_id'].iloc[i]))
   return movie , movie_poster

st.subheader('Genres')
select_gen = st.selectbox(
   'Select Genres movie',
   recommend_cg['genres'].values
)
st.link_button('See more','app2.py')
names5,poster_gen = recommend_gen_movie(recommend_cg,select_gen)
create_column_test(names5,poster_gen)

## Recommend Crew movie
df_cast = pickle.load(open('df_cast.pkl','rb'))

def recommend_cast(names_cast):
   movie = []
   movie_poster = []
   ref = df_cast[df_cast['cast'].str.contains(names_cast,case=False)]
   if len(ref) < 6:
      limit = len(ref)
   else:
      limit = 6
   for i in range(limit):
      movie.append(ref['title'].iloc[i])
      movie_poster.append(fetch_poster(ref['movie_id'].iloc[i]))
   return movie, movie_poster

st.subheader('Cast')
select_cast = st.selectbox(
   'Select actors ',
   df_cast['cast'].values
)
st.link_button('See more','app2.py')
names8,poster_cast = recommend_cast(select_cast)
create_column_test(names8,poster_cast)


## Recommend Hybrid Movie ###

hybrid_df = pickle.load(open('hybrid2.pkl','rb'))
similarity_hybrid = pickle.load(open('similarity2.pkl','rb'))

def recommend_hybrid(title,similarity_weight=0.7,top_n=6):
    movie = []
    movie_poster = []
    data = hybrid_df
    index_movie = data[data['original_title'] == title].index
    similarity = similarity_hybrid[index_movie].T
    sim_df = pd.DataFrame(similarity, columns=['similarity'])
    final_df = pd.concat([data, sim_df], axis=1)
    # You can also play around with the number
    final_df['final_score'] = final_df['score']*(1-similarity_weight) + final_df['similarity']*similarity_weight
    final_df_sorted = final_df.sort_values(by='final_score', ascending=False).head(top_n)
    #final_df_sorted.set_index('original_title', inplace=True)
    #return final_df_sorted[['original_title','movie_id_x','score', 'similarity', 'final_score']]
    for i in range(min(top_n,len(final_df_sorted))):
       movie.append(final_df_sorted['original_title'].iloc[i])
       movie_poster.append(fetch_poster(final_df_sorted['movie_id_x'].iloc[i]))
    return movie,movie_poster

st.subheader('เนื้อหาที่คุณอาจสนใจ')
select_hybrid = st.selectbox(
   "How would like movie hot rating",
   hybrid_df['original_title'].values
)

st.link_button('See more','app5.py')
names6,poster_hybrid = recommend_hybrid(select_hybrid)
create_column_test(names6,poster_hybrid)


 
 # Product Country
product_country  = pickle.load(open('./product_country.pkl','rb'))
prod_country_value = product_country['production_countries'].value_counts()

   
def recommend_country_movie(recommend_country,select_country):
   movie = []
   movie_poster = []
   ref_index = recommend_country[recommend_country['production_countries'].str.contains(select_country,case=False)]
   if len(ref_index) < 6:
      limit = len(ref_index)
   else:
      limit = 6
   for i in range(limit):
      movie.append(ref_index['title'].iloc[i])
      movie_poster.append(fetch_poster(ref_index['movie_id'].iloc[i]))
   return movie, movie_poster

st.subheader('Production Country')
select_country = st.selectbox(
   'Select Production of Country?',
   prod_country_value.index
)
st.link_button('See more','app6.py')
names7,poster_prod = recommend_country_movie(product_country,select_country)
create_column_test(names7,poster_prod)


# Initialize list_collect if it doesn't exist in session_state
if 'list_collect' not in st.session_state:
    st.session_state.list_collect = []
    st.session_state.list_poster = []

st.subheader('รายการที่สนใจ')
option = st.selectbox("How would you like to be contacted?",
                     movies['title'].values,
                     index=None,
                     placeholder='Select Interested movies')
st.write('You selected:', option)

def optional(option):
    ref_index= movies[movies['title'].str.contains(option)].index[0]
    st.session_state.list_collect.append(movies['title'].iloc[ref_index])
    st.session_state.list_poster.append(fetch_poster(movies['movie_id'].iloc[ref_index]))
if st.button('เพิ่มเป็นรายการที่สนใจ'):
    optional(option)  # Call the function to append the option to list_collect
    #st.write(st.session_state.list_collect)  Display the updated list_collect
    create_column_test(st.session_state.list_collect,st.session_state.list_poster)
    name_mycollect1,poster_mycollect = recommend(st.session_state.list_collect[-1])
    selected_item = st.session_state.list_collect[-1]
    st.header('เนื่องจากคุณสนใจ: {}'.format(str(selected_item)))
    create_column_test(name_mycollect1,poster_mycollect)

       
       
       