'''
def main():
    current_index = st.session_state.get('current_index', 0)

    col1, col2 = st.columns(2)

    with col1:
        if st.button('Previous'):
            if current_index > 0:
                current_index -= 1
            else:
                current_index = 2  # Loop back to the last tab when at index 0

    with col2:
        if st.button('Next'):
            if current_index < 2:
                current_index += 1
            else:
                current_index = 0  # Loop back to the first tab when at index 2

    st.session_state['current_index'] = current_index  # Update the session state

    st.write(current_index)


if __name__ == "__main__":
    main()

'''