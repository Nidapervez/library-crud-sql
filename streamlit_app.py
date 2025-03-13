import streamlit as st
from library import add_book, get_books

st.title("Library Management System")

# Form to add a book
with st.form("book_form"):
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value=1000, max_value=9999, step=1)
    submit = st.form_submit_button("Add Book")

    if submit:
        add_book(title, author, year)
        st.success(f"Book '{title}' added successfully!")

# Display books
st.subheader("Books in Library")
books = get_books()
for book in books:
    st.write(f"📚 {book[1]} by {book[2]} ({book[3]})")
