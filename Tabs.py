import streamlit as st
from  streamlit_option_menu import option_menu
import pickle 
import pandas as pd

recommend_cg_dict = pickle.load(open('recommend_crew.pkl','rb'))
recommend_cg = pd.DataFrame(recommend_cg_dict)

def create_tabs():
    st.write(
    f'<span style="font-size: 70px; font-weight: bold; color: red;">NETFLIX</span>',
    unsafe_allow_html=True
    )
    tab1 = st.tabs(["หน้าหลัก","หนังมาใหม่","ยอดฮิต", "ภาพยนตร์","หมวดหมู่","เนื้อหาคล้ายกับที่คุณสนใจ", "รายการของฉัน"])

    with tab1[0]:
        pass

    with tab1[1]:
        st.link_button('Go to new movies',"app3.py")
    

    with tab1[2]:
        st.link_button("Go to Top movies", "app.4py")

    with tab1[3]:
        st.link_button("Go to movies", "app2.py")

    with tab1[4]:
        option = st.selectbox(
        "How would you like to be contacted?",
        recommend_cg['genres'].values,
        index=None,
        placeholder="Select genres movies...",
        )

        st.write('You selected:', option)

    with tab1[5]:
        st.link_button("Hybrid", "app5.py")
    
    with tab1[6]:
        st.link_button("รายการที่คุณสนใจ", "app5.py")




# Define your options and other parameters
def create_select_menu():
    st.write(
        f'<span style="font-size: 70px; font-weight: bold; color: red;">NETFLIX</span>',
        unsafe_allow_html=True
        )
    options = ['Home', 'New movie', 'Top movie', 'Movies', 'Genres', 'Hybrid', 'My collection']
    icons = ['house', 'bi-alarm', 'fire', 'book', 'camera-reels', 'envelope', 'bag-heart']
    default_index = 0

    # Set the padding/margin to expand the option_menu edge
    selected = option_menu(
        menu_title=None,
        options=options,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
        orientation='horizontal',
        styles={'margin': '20px'}  # Adjust the margin as needed
    )
    if selected == 'Home':
        pass
    if selected == options[1]:
        st.link_button('Go to new movies',"app3.py")
    if selected == options[2]:
        st.link_button("Go to Top movies", "app.4py")
    if selected == options[3]:
        st.link_button("Go to movies", "app2.py")
    if selected == options[4]:
        option = st.selectbox(
        "How would you like to be contacted?",
        recommend_cg['genres'].values,
        index=None,
        placeholder="Select genres movies...",
        )

        st.write('You selected:', option)
    if selected == options[5]:
        st.link_button("Hybrid", "app5.py")
    if selected == options[6]:
        st.link_button("My Collection", "app5.py")