
import streamlit as st
import pandas as pd
import pickle

movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)


def create_columns(names):
    # Create 6 columns
    n = 6
    cols = st.columns(n,gap='small')

    for i in range(n-1):
        with cols[i]:
            st.text(names[i])
            st.image("https://static.streamlit.io/examples/owl.jpg")

def create_columns2(names2):

   col1, col2, col3, col4 , col5, col6 = st.columns(6)

   with col1:
      st.text(names2[0])
      st.image("https://static.streamlit.io/examples/owl.jpg")
   with col2:
      st.text(names2[1])
      st.image("https://static.streamlit.io/examples/owl.jpg")
   with col3:
      st.text(names2[2])
      st.image("https://static.streamlit.io/examples/owl.jpg")
   with col4:
      st.text(names2[3])
      st.image("https://static.streamlit.io/examples/owl.jpg")
   with col5:
      st.text(names2[4])
      st.image("https://static.streamlit.io/examples/owl.jpg")
   with col6:
      st.text(names2[5])
      st.image("https://static.streamlit.io/examples/owl.jpg")


def create_column_gen(names1):
   num_rows = 1
   num_cols = 6

   for row in range(num_rows):
      cols = st.columns(num_cols)
      for col_index, col in enumerate(cols):
         movie_index = row * num_cols + col_index
         if movie_index < len(names1):
            # You can add images to each column using st.image
            image_url = "https://static.streamlit.io/examples/owl.jpg"  # Replace with your image URL
                
            # Use HTML to overlay text on the image
            col.image(image_url, use_column_width=True)
            col.markdown(f"<p style='text-align: center; font-size: 18px;'>{names1[movie_index]}</p>", unsafe_allow_html=True)

def create_column_test(names1,poster):
   num_rows = 1
   num_cols = 6

   for row in range(num_rows):
      cols = st.columns(num_cols)
      for col_index, col in enumerate(cols):
         movie_index = row * num_cols + col_index
         if movie_index < len(names1):
            # You can add images to each column using st.image
            image_url = poster[movie_index] # Replace with your image URL
                
            # Use HTML to overlay text on the image
            col.image(image_url, use_column_width=True)
            col.markdown(f"<p style='text-align: center; font-size: 18px;'>{names1[movie_index]}</p>", unsafe_allow_html=True)




# Example list of names
#names = ["Name 1", "Name 2", "Name 3", "Name 4", "Name 5", "Name 6"]

# Call the function to create columns

'''
import streamlit as st

# List of image URLs
image_urls = [
    "https://static.streamlit.io/examples/cat.jpg",
    "https://static.streamlit.io/examples/dog.jpg",
    "https://static.streamlit.io/examples/cat.jpg",
]

# Create a Streamlit app
def main():
    st.title("Image Slider")

    # Create a column for the buttons
    col1, col2 = st.columns(2)

    current_index = st.session_state.get("current_index", 0)

    with col1:
        if st.button("Previous") and current_index > 0:
            current_index -= 1

    with col2:
        if st.button("Next") and current_index < len(image_urls) - 1:
            current_index += 1

    st.image(image_urls[current_index], caption="Current Image")
    print(current_index)

if __name__ == "__main__":
    main()
'''

'''
tab1 = st.tabs(["Cat", "Dog", "Owl"])

with tab1[0]:
   st.header('A Cat')
   st.image("https://static.streamlit.io/examples/cat.jpg", width=150)

with tab1[1]:
   st.header('A Dog')
   st.image("https://static.streamlit.io/examples/dog.jpg", width=150)

with tab1[2]:
   st.header('An Owl')
   st.image("https://static.streamlit.io/examples/owl.jpg", width=150)

'''
