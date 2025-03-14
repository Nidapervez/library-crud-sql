import streamlit as st
from library import add_book, get_books, update_book, delete_book, lend_book, return_book, get_borrowed_books

st.set_page_config(page_title="📚 Library Management", layout="wide")

st.title("📚 Library Management System")

# ✅ Add a Book Section
st.sidebar.header("➕ Add a New Book")
with st.sidebar.form("add_book_form"):
    title = st.text_input("📖 Book Title")
    author = st.text_input("✍️ Author")
    year = st.number_input("📅 Year", min_value=1000, max_value=9999, step=1)
    submit = st.form_submit_button("Add Book")

    if submit:
        add_book(title, author, year)
        st.success(f"✅ Book '{title}' added successfully!")
        st.rerun()

# ✅ Display Available Books
st.subheader("📚 Available Books")
books = get_books()

for book in books:
    book_id, book_title, book_author, book_year, book_status = book

    # Only show available books
    if book_status == "available":
        col1, col2, col3, col4, col5 = st.columns([3, 3, 2, 2, 2])

        with col1:
            st.write(f"📖 **{book_title}**")
        with col2:
            st.write(f"✍️ {book_author}")
        with col3:
            st.write(f"📅 {book_year}")
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

# ✅ Display Borrowed Books
st.subheader("📕 Borrowed Books")
borrowed_books = get_borrowed_books()

if borrowed_books:
    for book in borrowed_books:
        book_id, book_title, book_author, book_year, book_status = book

        col1, col2, col3, col4 = st.columns([3, 3, 2, 2])

        with col1:
            st.write(f"📕 **{book_title}**")
        with col2:
            st.write(f"✍️ {book_author}")
        with col3:
            st.write(f"📅 {book_year}")
        with col4:
            if st.button(f"🔄 Return", key=f"return_{book_id}"):
                return_book(book_id)
                st.success(f"🔄 '{book_title}' returned!")
                st.rerun()
else:
    st.write("✅ No borrowed books!")

