# import streamlit as st
# import os
# import cv2
# from tempfile import NamedTemporaryFile
# from main import process_video  # Import your existing processing function

# # Set up the Streamlit app
# st.title("Tennis Analysis Video Upload")

# # User authentication (simplified)
# def check_credentials(username, password):
#     # Replace this with actual authentication logic
#     return username == 'Ankith' and password == 'Ankith@13'

# # Authentication form
# with st.sidebar.form("login_form"):
#     st.header("Login")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
#     login_button = st.form_submit_button("Login")

#     if login_button:
#         if check_credentials(username, password):
#             st.session_state.authenticated = True
#             st.success("Logged in successfully!")
#         else:
#             st.session_state.authenticated = False
#             st.error("Incorrect username or password")

# # Check if the user is authenticated
# if 'authenticated' in st.session_state and st.session_state.authenticated:

#     # Upload video
#     uploaded_file = st.file_uploader("Choose a video...", type=["mp4", "avi", "mov","webm"])
    
#     if uploaded_file is not None:
#         with NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_file:
#             tmp_file.write(uploaded_file.read())
#             tmp_file_path = tmp_file.name

#         st.video(tmp_file_path)  # Display the uploaded video

#         if st.button('Process Video'):
#             with st.spinner('Processing video...'):
#                 output_path = process_video(tmp_file_path)
#                 st.success('Video processed successfully!')
#                 st.video(output_path)  # Display the processed video

# else:
#     st.warning("Please log in to use the application.")




# import streamlit as st
# import os
# from tempfile import NamedTemporaryFile
# from main import process_video  # Import your existing processing function

# # Set up the Streamlit app
# st.title("Tennis Analysis App")

# # Function to check user credentials
# def check_credentials(username, password):
#     # Replace this with actual authentication logic
#     return username == 'Ankith' and password == 'Ankith@13'

# # Function to handle navigation between pages
# def show_login_page():
#     st.header("Login")
#     with st.form("login_form"):
#         username = st.text_input("Username")
#         password = st.text_input("Password", type="password")
#         login_button = st.form_submit_button("Login")

#         if login_button:
#             if check_credentials(username, password):
#                 st.session_state.authenticated = True
#                 st.session_state.page = "upload"
#                 st.success("Logged in successfully!")
#             else:
#                 st.session_state.authenticated = False
#                 st.error("Incorrect username or password")

# def show_upload_page():
#     st.header("Tennis Analysis Video Upload")
    
#     # Upload video
#     uploaded_file = st.file_uploader("Choose a video...", type=["mp4", "avi", "mov", "webm"])
    
#     if uploaded_file is not None:
#         with NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_file:
#             tmp_file.write(uploaded_file.read())
#             tmp_file_path = tmp_file.name
        
#         st.video(tmp_file_path)  # Display the uploaded video
        
#         if st.button('Process Video'):
#             with st.spinner('Processing video...'):
#                 output_path = process_video(tmp_file_path)
                
#                 if output_path:
#                     st.success('Video processed successfully!')
#                     st.video(output_path)  # Display the processed video
#                 else:
#                     st.error('Failed to process video.')

# # Initialize session state
# if 'authenticated' not in st.session_state:
#     st.session_state.authenticated = False
# if 'page' not in st.session_state:
#     st.session_state.page = "login"

# # Page navigation
# if st.session_state.page == "login":
#     show_login_page()
# elif st.session_state.page == "upload":
#     if st.session_state.authenticated:
#         show_upload_page()
#     else:
#         st.warning("Please log in to access the upload page.")


# import streamlit as st
# import os
# from tempfile import NamedTemporaryFile
# from main import process_video  # Import your existing processing function

# # Set up the Streamlit app
# st.title("Tennis Analysis App")

# # Function to check user credentials
# def check_credentials(username, password):
#     # Replace this with actual authentication logic
#     return username == 'Ankith' and password == 'Ankith@13'

# # Function to handle navigation between pages
# def show_login_page():
#     st.header("Login")
#     with st.form("login_form"):
#         username = st.text_input("Username")
#         password = st.text_input("Password", type="password")
#         login_button = st.form_submit_button("Login")

#         if login_button:
#             if check_credentials(username, password):
#                 st.session_state.authenticated = True
#                 st.session_state.page = "upload"
#                 st.success("Logged in successfully!")
#             else:
#                 st.session_state.authenticated = False
#                 st.error("Incorrect username or password")

# def show_upload_page():
#     st.header("Tennis Analysis Video Upload")
    
#     # Upload video
#     uploaded_file = st.file_uploader("Choose a video...", type=["mp4", "avi", "mov", "webm"])
    
#     if uploaded_file is not None:
#         with NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_file:
#             tmp_file.write(uploaded_file.read())
#             tmp_file_path = tmp_file.name
        
#         st.video(tmp_file_path)  # Display the uploaded video
        
#         if st.button('Process Video'):
#             with st.spinner('Processing video...'):
#                 try:
#                     output_path = process_video(tmp_file_path)
                    
#                     # Check if the output_path is a tuple
#                     if isinstance(output_path, tuple):
#                         output_path = output_path[0]  # Extract the file path
                    
#                     # Debugging output path
#                     st.write(f"Output path type: {type(output_path)}")
#                     st.write(f"Output path value: {output_path}")
                    
#                     if isinstance(output_path, str) and os.path.isfile(output_path):
#                         st.success('Video processed successfully!')
#                         st.video(output_path)  # Display the processed video
#                     else:
#                         st.error('Processed video file path is invalid.')
#                 except Exception as e:
#                     st.error(f'Error during processing: {e}')
#                 finally:
#                     # Cleanup
#                     if os.path.exists(tmp_file_path):
#                         os.remove(tmp_file_path)

# # Initialize session state
# if 'authenticated' not in st.session_state:
#     st.session_state.authenticated = False
# if 'page' not in st.session_state:
#     st.session_state.page = "login"

# # Page navigation
# if st.session_state.page == "login":
#     show_login_page()
# elif st.session_state.page == "upload":
#     if st.session_state.authenticated:
#         show_upload_page()
#     else:
#         st.warning("Please log in to access the upload page.")




import streamlit as st
import os
from tempfile import NamedTemporaryFile
from main import process_video  


st.title("Court Vision")

def check_credentials(username, password):
    
    return username == 'Ankith' and password == 'Ankith@13'

def local_css(file_path):
    try:
        with open(file_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file not found: {file_path}")


local_css("C:/Users/ankit/OneDrive/Desktop/Tennis/style.css")


def show_login_page():
    st.header("Login")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Login")

        if login_button:
            if check_credentials(username, password):
                st.session_state.authenticated = True
                st.session_state.page = "upload"
                st.success("Logged in successfully!")
            else:
                st.session_state.authenticated = False
                st.error("Incorrect username or password")

def show_upload_page():
    st.header("Tennis Analysis Video Upload")
    
    # Upload video
    uploaded_file = st.file_uploader("Choose a video...", type=["mp4", "avi", "mov", "webm"])
    
    if uploaded_file is not None:
        with NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file_path = tmp_file.name
        
        st.video(tmp_file_path)  
        
        if st.button('Process Video'):
            with st.spinner('Processing video...'):
                try:
                    output_path = process_video(tmp_file_path)
                    
                    # Check if the output_path is a tuple
                    if isinstance(output_path, tuple):
                        output_path = output_path[0]  # Extract the file path
                    
                    # Debugging output path
                    st.write("Check  output video folders for processed video")
                    # st.write(f"Output path value: {output_path}")
                    
                    if isinstance(output_path, str) and os.path.isfile(output_path):
                        st.success('Video processed successfully!')
                        # st.video(output_path)  # Display the processed video
                    else:
                        st.error('Processed video file path is invalid.')
                except Exception as e:
                    st.error(f'Error during processing: {e}')
                finally:
                    # Cleanup
                    if os.path.exists(tmp_file_path):
                        os.remove(tmp_file_path)

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'page' not in st.session_state:
    st.session_state.page = "login"

# Page navigation
if st.session_state.page == "login":
    show_login_page()
elif st.session_state.page == "upload":
    if st.session_state.authenticated:
        show_upload_page()
    else:
        st.warning("Please log in to access the upload page.")
