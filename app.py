import streamlit as st
from base64 import b64encode
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# Set page configuration at the top
st.set_page_config(page_title="Abdul Samad Portfolio", page_icon='★', layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load local CSS (ensure style.css is in the same directory or specify the correct relative path)
local_css("style.css")

# Load animations
lottie_coder = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_UBiAADPga8.json")
lottie_contact = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_lt8ter7g.json")

# Load images using relative paths (ensure images are in the repo when deploying to Streamlit Cloud)
image = Image.open("sentiment.png")

def web_portfolio():
    # Title and profile image
    st.write(f"""
    <div class="title" style="text-align:center;">
    <span style='font-size: 32px;'>Tech365 Developer</span>
    </div>            
    """, unsafe_allow_html=True)

    st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)

    # Load profile image (relative path)
    with open("abdul.jpg", "rb") as img_file:
        img = "data:image/jpg;base64," + b64encode(img_file.read()).decode()

    # Load certificate images
    cert_img_paths = ["certificate.png", "download.png", "down.png"]
    cert_imgs = []
    for cert_path in cert_img_paths:
        with open(cert_path, "rb") as cert_file:
            cert_imgs.append("data:image/jpg;base64," + b64encode(cert_file.read()).decode())

    # Load CV file
    with open("DACV.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    # Display profile with slight tilt animation
    st.write(f"""
    <style>
    @keyframes slowTilt {{
    0%, 100% {{ transform: rotate(0deg); }}
    50% {{ transform: rotate(1deg); }}
    }}
    .box img {{
    width: 300px;
    height: 200px;
    border-radius: 30%;
    animation: slowTilt 3s ease-in-out infinite;
    }}
    </style>
    <div style="display: flex; justify-content: center;">
    <div class="box">
    <img src="{img}">
    </div>
    </div>
    """, unsafe_allow_html=True)

    # Subtitle
    st.write(f"""
             <div class="subtitle" style="text-align: center;">Data Analyst & BI-Consultant</div>""",
              unsafe_allow_html=True)
    
    # Social icons
    social_icons_data = {
        "LinkedIn": ["https://www.linkedin.com/in/abdul-samad-ali-abbasi-40859926a/", "https://cdn-icons-png.flaticon.com/128/3536/3536505.png"],
        "GitHub": ["https://github.com/AbdulSamad512?tab=repositories", "https://cdn-icons-png.flaticon.com/128/5968/5968866.png"]
    }

    social_icons_html = [
        f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'>"
        f"<img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'"
        f" style='width: 25px; height: 25px;'></a>"
        for platform in social_icons_data
    ]
    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
    {''.join(social_icons_html)}
    </div>""", 
    unsafe_allow_html=True)

    st.write('----')

    # Menu options
    selected = option_menu(
        menu_title=None,
        options=['About', 'Projects', 'Contact'],
        icons=['person', 'code-slash', 'chat-left-text-fill'],
        orientation='horizontal'
    )

    # About Section
    if selected == 'About':
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("I am Abdul Samad")
                st.title("Undergraduate at BSAI 7th Semester")
                st.markdown("""
                - 🧑‍💻 Mid Level Data Analyst and BI-Consultant at Diamond Supermarket HO.
                - ❤️ Passionate about Machine Learning/Deep Learning, MLOps, and Data Science.
                - 🏂 In my free time, I enjoy sports like Cricket and Cycling.
                - 🪧 Reach me at tech365developer@gmail.com.
                - 🏠 Based in Pakistan.
                """)
            with col2:
                st_lottie(lottie_coder)
            
            st.write("---")
            col3, col4 = st.columns(2)
            with col3:
                st.write("## Education:")
                st.markdown("""
                - Bachelor Of Science In Artificial Intelligence.
                - Certified Artificial Intelligence Developer at PIAIC.
                - Certified Machine-Learning, AI & Data Science at Ehunar.
                - Certified Python For Everyone at Ehunar.
                """)
                
            with col4:
                st.write("## My Certificates:")
                cert_cols = st.columns(3)
                for idx, cert_img in enumerate(cert_imgs):
                    cert_cols[idx].write(f"""
                    <div style="text-align:center;">
                    <img src="{cert_img}" alt="Certificate {idx+1}" style='width: 150px; height: 150px; margin: 10px;'>
                    </div>
                    """, unsafe_allow_html=True)

    # Projects Section
    elif selected == "Projects":
        st.header("My Projects")

        # Example project
        st.write("## Sentiment Analysis:")
        col5, col6 = st.columns((1, 2))
        with col5:
            st.image(image)
        with col6:
            st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/Sentiment_Analysis)")
            st.markdown("""
            - Performs Sentiment Analysis with emoji analysis, category analysis, and trend analysis.
            """)

        # Additional projects (use relative paths for images)
        # Repeat similar structure for each project

    # Contact Section
    elif selected == 'Contact':
        st.header("Get in touch!")
        contact_form = """
        <form action="https://formsubmit.co/abdul.samad.ali.abbasi.r678@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message" required></textarea>
            <button type="submit">Send</button>
        </form>
        """            
        left_col, right_col = st.columns((2,1))
        with left_col:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_col:
            st_lottie(lottie_contact, height=400)

    # Download CV button
    st.download_button(label="📄 Download my CV", data=pdf_bytes, file_name="AbdulSamad_linkedin_cv.pdf", mime="application/pdf")
    st.write("##")
    st.write(f"""<div class="subtitle" style="text-align: center;">🌟 Have A Wonderful Day!!! 🌟</div>""", unsafe_allow_html=True)

if __name__ == "__main__":
    web_portfolio()
