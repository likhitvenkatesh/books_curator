import streamlit as st
import requests


st.set_page_config(layout="wide")

container_style = """
    <style>
    body{
        text-align: center;
    }
        .container {
            position: absolute;
            top: 10px;
            right: 10px;
            background-color: #262631;
            padding: 10px;
            border-radius: 15px;
            border: 0.5px solid gray;
            
        }
        .link-button {
            text-decoration: none;
            color: white !important;  /* Button color */
            font-weight: bold;
            # background-color: transparent !important;
            border: none !important;
            cursor: pointer;
            outline: none !important;
            
        }
        .container:hover {
            border: 1px solid white;
            border-radius: 15px;
            
        }
    </style>
"""

# Apply the CSS style
st.markdown(container_style, unsafe_allow_html=True)

# Create the container with the link button
st.markdown("""
<div class='container'>
    <a class='link-button' href='https://streamlit.io/gallery'>Log Out</a>
</div>
""", unsafe_allow_html=True)
# CSS for center-aligning the header and styling the line
page_bg_img = '''
<style>

[data-testid="stAppViewContainer"] > .main {
    background-image: url(https://ibb.co/K0wT2JZ);
 
    background-position: center;
   
    background-attachment: local, fixed;
}

</style>
'''


st.markdown(page_bg_img, unsafe_allow_html=True)

header_style = """
    <style>

     .header {
            color: #fff;
            padding: 0;
            margin-top: 0;
            text-align: center;
        }
        .caption {
            color: #fff;
            text-align: center;
            margin-top: 0;
            padding-top: 100px:
            font-size: 60px;
        }
        .line {
           
            border-bottom: 2px dashed #f85a40 #ccc;
            margin-bottom: 20px;
            padding-bottom: 40px;
        }
        .block-container st-emotion-cache-z5fcl4 ea3mdgi2 {
            padding: 0;
        }
        
        
            
    </style>
"""
# st.set_page_config(layout="wide")

# Adding the CSS to the Streamlit app
st.markdown(header_style, unsafe_allow_html=True)

# Header with center alignment and line separator
st.markdown("<h1 class='header'>The Curator<span style='color: #f85a40;'>.</span></h1>", unsafe_allow_html=True)


st.markdown("<h1 class='caption'>Book Recommendation Tool</h1>", unsafe_allow_html=True)
st.markdown("<div class='line'></div>", unsafe_allow_html=True)
# Function to search books by genre
def search_books_by_genre(genres, api_key):
    url = 'https://www.googleapis.com/books/v1/volumes'
    params = {
        'q': 'subject:' + '+'.join(genres),  # Search by genre
        'orderBy': 'relevance',  # Order by relevance (popularity)
        'maxResults': 5,  # Get the top 5 results
        'key': api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

# Function to search books by author
def search_books_by_author(authors, api_key):
    url = 'https://www.googleapis.com/books/v1/volumes'
    params = {
        'q': 'inauthor:' + '+'.join(authors),  # Search by author
        'orderBy': 'relevance',  # Order by relevance (popularity)
        'maxResults': 5,  # Get the top 5 results
        'key': api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

# Streamlit app
def main():
    

    search_option = st.selectbox("Search by:", ('Genre', 'Author'))

    if search_option == 'Genre':
        selected_genres = st.multiselect('Select Genre(s)', ['Fiction', 'Science Fiction', 'Fantasy', 'Mystery', 'Thriller', 'Horror', 'Romance', 'Biography', 'History', 'Self-Help', 'Cooking', 'Travel'])

        if st.button('Search'):
            if len(selected_genres) > 0:
                api_key = 'AIzaSyArTvhMGlt1AAbo2FGhSO-tj2_6eriZAIk'  # Use provided API key
                for genre in selected_genres:
                    st.subheader(genre)
                    result = search_books_by_genre([genre], api_key)
                    if 'items' in result:
                        for item in result['items']:
                            volume_info = item.get('volumeInfo', {})
                            title = volume_info.get('title', 'No title available')
                            authors = volume_info.get('authors', ['Unknown'])
                            description = volume_info.get('description', 'No description available')
                            cover_image_link = volume_info.get('imageLinks', {}).get('thumbnail', 'No cover available')
                            preview_link = volume_info.get('previewLink', 'No preview available')

                            st.markdown(f'<div style="background-color: black; padding: 10px; text-align: center; text-transform: uppercase; color: white;">Title: {title}</div>', unsafe_allow_html=True)
                            st.markdown("")
                            st.markdown(f'<div style="text-align: center; text-transform: uppercase; color: white;">Author: {", ".join(authors)}</div>', unsafe_allow_html=True)
                            st.markdown("")
                            st.write("**Description:**", description)
                            if cover_image_link != 'No cover available':
                                st.image(cover_image_link, caption='Cover Image', width=150)
                            else:
                                st.write("Cover Image not available")
                            st.write("**Preview Link:**", preview_link)
                            st.write("---")

    elif search_option == 'Author':
        authors = st.multiselect("Select Author(s)", ['J.K. Rowling', 'Stephen King', 'George R.R. Martin', 'Agatha Christie', 'Tolkien', 'Haruki Murakami', 'Neil Gaiman', 'Dan Brown', 'Margaret Atwood', 'Ernest Hemingway',
        'J.K. Rowling', 'Stephen King', 'George R.R. Martin', 'Agatha Christie', 'J.R.R. Tolkien','R. L. Stine','H. C. Verma','R. D.Sharma', 
        'Haruki Murakami', 'Neil Gaiman', 'Dan Brown', 'Margaret Atwood', 'Ernest Hemingway', 
        'Jane Austen', 'Leo Tolstoy', 'Terry Pratchett', 'Mark Twain', 'John Grisham',
        'Jodi Picoult', 'Gabriel Garcia Marquez', 'Fyodor Dostoevsky', 'George Orwell', 'Virginia Woolf',
        'Herman Melville', 'Ray Bradbury', 'Kurt Vonnegut', 'Charles Dickens', 'Emily Dickinson',
        'Toni Morrison', 'H.G. Wells', 'Homer', 'Oscar Wilde', 'William Faulkner', 
        'Ayn Rand', 'Victor Hugo', 'Philip K. Dick', 'Edgar Allan Poe', 'H.P. Lovecraft',
        'Murasaki Shikibu', 'F. Scott Fitzgerald', 'Ernest Hemingway', 'James Joyce', 'Charlotte Bronte','G . Tewani',
        'Kazuo Ishiguro', 'Roald Dahl', 'Aldous Huxley', 'Stephenie Meyer', 'Yukio Mishima',
        'Margaret Mitchell', 'George Eliot', 'Ian McEwan', 'Michel Houellebecq', 'Douglas Adams'
    ])

        if st.button('Search'):
            if authors:
                api_key = 'AIzaSyArTvhMGlt1AAbo2FGhSO-tj2_6eriZAIk'  # Use provided API key
                result = search_books_by_author(authors, api_key)
                if 'items' in result:
                    for item in result['items']:
                        volume_info = item.get('volumeInfo', {})
                        title = volume_info.get('title', 'No title available')
                        authors = volume_info.get('authors', ['Unknown'])
                        description = volume_info.get('description', 'No description available')
                        cover_image_link = volume_info.get('imageLinks', {}).get('thumbnail', 'No cover available')
                        preview_link = volume_info.get('previewLink', 'No preview available')

                        st.markdown(f'<div style="background-color: black; padding: 10px; text-align: center; text-transform: uppercase; color: white;">Title: {title}</div>', unsafe_allow_html=True)
                        st.markdown("")
                        st.markdown(f'<div style="text-align: center; text-transform: uppercase; color: white;">Author: {", ".join(authors)}</div>', unsafe_allow_html=True)
                        st.markdown("")
                        st.write("**Description:**", description)
                        if cover_image_link != 'No cover available':
                            st.image(cover_image_link, caption='Cover Image', width=150)
                        else:
                            st.write("Cover Image not available")
                        st.write("**Preview Link:**", preview_link)
                        st.write("---")

if __name__ == '__main__':
    main()
