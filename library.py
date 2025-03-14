from db_connection import get_connection

# ✅ Add a New Book
def add_book(title, author, year):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, year, status) VALUES (%s, %s, %s, 'available')", 
                   (title, author, year))
    conn.commit()
    conn.close()

# ✅ Get All Books
def get_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books

# ✅ Update Book
def update_book(book_id, title, author, year):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title=%s, author=%s, year=%s WHERE id=%s", 
                   (title, author, year, book_id))
    conn.commit()
    conn.close()

# ✅ Delete Book
def delete_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=%s", (book_id,))
    conn.commit()
    conn.close()

# ✅ Lend Book (Mark as Borrowed)
def lend_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET status='borrowed' WHERE id=%s", (book_id,))
    conn.commit()
    conn.close()

# ✅ Return Book (Mark as Available)
def return_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET status='available' WHERE id=%s", (book_id,))
    conn.commit()
    conn.close()

# ✅ Get Borrowed Books
def get_borrowed_books():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE status='borrowed'")
    books = cursor.fetchall()
    conn.close()
    return books
