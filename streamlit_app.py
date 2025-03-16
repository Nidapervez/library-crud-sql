import streamlit as st
import base64
from library import add_book, get_books, update_book, delete_book, lend_book, return_book, get_borrowed_books

# Set page configuration
st.set_page_config(page_title="📚 Library Management", layout="wide")

# Apply background image
def set_background(image_file):
    with open(image_file, "rb") as img:
        encoded_string = base64.b64encode(img.read()).decode()
    
    bg_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .text-container {{
        background: rgba(255, 255, 255, 0.7);
        padding: 10px;
        border-radius: 10px;
        color: #4B0082;
    }}
    .header-container {{
        background: rgba(255, 255, 255, 0.8);
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #4B0082;
        margin-bottom: 20px;
    }}
    </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)

set_background("11.jpg")  # Background image file

# Title with white background
st.markdown("<div class='header-container'>📚 Library Management System</div>", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("<div class='text-container'><b>📖 Navigation</b></div>", unsafe_allow_html=True)
menu = st.sidebar.radio("Go to:", ["🏠 Home", "📚 Available Books", "📕 Borrowed Books", "➕ Add a Book"])

# ➕ Add a Book Section
if menu == "➕ Add a Book":
    st.sidebar.markdown("<div class='text-container'><b>➕ Add a New Book</b></div>", unsafe_allow_html=True)
    with st.sidebar.form("add_book_form"):
        title = st.text_input("📖 Book Title")
        author = st.text_input("✍️ Author")
        year = st.number_input("📅 Year", min_value=1000, max_value=9999, step=1)
        submit = st.form_submit_button("Add Book")

        if submit:
            add_book(title, author, year)
            st.success(f"✅ Book '{title}' added successfully!")
            st.rerun()

# 📚 Display Available Books
if menu == "📚 Available Books":
    st.markdown("<div class='header-container'>📚 Available Books</div>", unsafe_allow_html=True)
    
    search_query = st.text_input("🔍 Search by Title or Author", "")
    books = get_books()
    
    for book in books:
        book_id, book_title, book_author, book_year, book_status = book

        # Search filter
        if search_query.lower() in book_title.lower() or search_query.lower() in book_author.lower():
            if book_status == "available":
                col1, col2, col3, col4, col5 = st.columns([3, 3, 2, 2, 2])

                with col1:
                    st.markdown(f"<div class='text-container'>📖 <b>{book_title}</b></div>", unsafe_allow_html=True)
                with col2:
                    st.markdown(f"<div class='text-container'>✍️ {book_author}</div>", unsafe_allow_html=True)
                with col3:
                    st.markdown(f"<div class='text-container'>📅 {book_year}</div>", unsafe_allow_html=True)
                with col4:
                    if st.button(f"📚 Borrow", key=f"borrow_{book_id}"):
                        lend_book(book_id)
                        st.success(f"📚 '{book_title}' borrowed!")
                        st.rerun()
                with col5:
                    if st.button(f"🗑 Delete", key=f"delete_{book_id}"):
                        delete_book(book_id)
                        st.warning(f"🗑 '{book_title}' deleted!")
                        st.rerun()

st.divider()

# 📕 Display Borrowed Books
if menu == "📕 Borrowed Books":
    st.markdown("<div class='header-container'>📕 Borrowed Books</div>", unsafe_allow_html=True)
    borrowed_books = get_borrowed_books()

    if borrowed_books:
        for book in borrowed_books:
            book_id, book_title, book_author, book_year, book_status = book

            col1, col2, col3, col4 = st.columns([3, 3, 2, 2])

            with col1:
                st.markdown(f"<div class='text-container'>📕 <b>{book_title}</b></div>", unsafe_allow_html=True)
            with col2:
                st.markdown(f"<div class='text-container'>✍️ {book_author}</div>", unsafe_allow_html=True)
            with col3:
                st.markdown(f"<div class='text-container'>📅 {book_year}</div>", unsafe_allow_html=True)
            with col4:
                if st.button(f"🔄 Return", key=f"return_{book_id}"):
                    return_book(book_id)
                    st.success(f"🔄 '{book_title}' returned!")
                    st.rerun()
    else:
        st.markdown("<div class='text-container'>✅ No borrowed books!</div>", unsafe_allow_html=True)
