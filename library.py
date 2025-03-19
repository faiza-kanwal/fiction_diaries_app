import streamlit as st
import json
import os

# 🌟 CSS Styles for UI
st.markdown("""
    <style>
    body {
        background-color: #1E90FF;
    }
    .main-title {
        text-align: center;
        font-size: 80px;
        font-family : "Georgia";
        font-weight: bold;
        color: #1E90FF;
        padding: 10px;
        text-transform: uppercase;
        letter-spacing : 2px;
    }
    .book-card {
        background-color: #ffffff;
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .book-title {
        font-size: 18px;
        font-weight: bold;
        color: #2980b9;
    }
    .book-author {
        font-size: 14px;
        color: #7f8c8d;
    }
    .read-link {
        text-decoration: none;
        font-weight: bold;
        color: #e74c3c;
    }
    .read-link:hover {
        color: #c0392b;
    }
    .sidebar .block-container {
        font-size: 18px; /* Increase sidebar text size */
    }
    </style>
""", unsafe_allow_html=True)

# 📚 Function to Load JSON File

def load_library():
    if os.path.exists("library.json"):  
        with open("library.json", "r") as file:
            return json.load(file)
    else:
        default_books = [
            {"title": "Peer-e-Kamil", "author": "Umera Ahmed", "link": "https://www.mediafire.com/file/0n5kbbfd75o0677/Pir+e+Kamil+By+Umera+Ahmed.pdf/file"},
            {"title": "Jannat Ke Pattay", "author": "Nimra Ahmed", "link": "https://example.com/jannat-ke-pattay"},
            {"title": "Namal", "author": "Nemrah Ahmed", "link": "https://example.com/namal"},
            {"title": "Mala", "author": "Nimra Ahmed", "link": "https://kitabnagri.xyz/mala.pdf"},
            {"title": "Aks", "author": "Umera Ahmed", "link": "https://kitabnagri.xyz/aks.pdf"},
            {"title": "Mushaf", "author": "Nemrah Ahmed", "link": "https://kitabnagri.xyz/mushaf.pdf"},
            {"title": "Usri Yusra", "author": "Nemrah Ahmed", "link": "https://kitabnagri.xyz/usri-yusra.pdf"},
            {"title": "Qarqaram Ka Taj Mehal", "author": "Nemrah Ahmed", "link": "https://kitabnagri.xyz/qarqaram-ka-taj-mehal.pdf"}
        ]
        save_library(default_books)  
        return default_books  

# 📂 Function to Save Books to JSON File
def save_library(library):
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)

# 📖 Load Library
library = load_library()

# 🎉 Beautiful Title
st.markdown('<p class="main-title">🖤 Fiction Diaries By Faiza</p>', unsafe_allow_html=True)

# 📌 ✅ Sidebar Menu
menu = st.sidebar.radio("📌 Menu", ["📚 View Library", "➕ Add Book", "❌ Remove Book", "🔍 Search Book"])

# 📌 ✅ View Library
if menu == "📚 View Library":
    st.subheader("📖 Available Books:")
    if library:
        for book in library:
            st.markdown(f"""
                <div class="book-card">
                    <p class="book-title">{book['title']}</p>
                    <p class="book-author">by {book['author']}</p>
                    <a class="read-link" href="{book['link']}" target="_blank">📖 Read Online</a>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("🚫 No books found in your library!")

# 📌 ✅ Add Book Section
elif menu == "➕ Add Book":
    st.subheader("➕ Add a New Book")
    title = st.text_input("📖 Enter Book Title:")
    author = st.text_input("✍ Enter Author Name:")
    link = st.text_input("🔗 Enter Online Link:")
    
    if st.button("✅ Add Book"):
        if title and author and link:
            library.append({"title": title, "author": author, "link": link})
            save_library(library)
            st.success(f"🎉 '{title}' by {author} added successfully!")
            st.experimental_rerun()
        else:
            st.warning("⚠ Please enter all details!")

# 📌 ✅ Remove Book Section
elif menu == "❌ Remove Book":
    st.subheader("🗑 Remove a Book")
    book_titles = [book["title"] for book in library]
    book_to_remove = st.selectbox("📖 Select a Book to Remove", book_titles)
    
    if st.button("🗑 Remove Book"):
        library = [book for book in library if book["title"] != book_to_remove]
        save_library(library)
        st.success(f"🗑 '{book_to_remove}' has been removed!")
        st.experimental_rerun()

# 📌 ✅ Search Book Section
elif menu == "🔍 Search Book":
    st.subheader("🔍 Search for a Book")
    search_query = st.text_input("🔎 Enter book title or author name:")
    
    if search_query:
        results = [book for book in library if search_query.lower() in book["title"].lower() or search_query.lower() in book["author"].lower()]
        if results:
            for book in results:
                st.markdown(f"""
                    <div class="book-card">
                        <p class="book-title">{book['title']}</p>
                        <p class="book-author">by {book['author']}</p>
                        <a class="read-link" href="{book['link']}" target="_blank">📖 Read Online</a>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("🚫 No matching books found!")
