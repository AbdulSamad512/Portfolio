import streamlit as st
from base64 import b64encode
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image


# Page configuration should be called only once at the top of the script
st.set_page_config(page_title="Abdul Samad Portfolio", page_icon='★', layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("style.css")

lottie_coder = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_UBiAADPga8.json")
lottie_contact = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_lt8ter7g.json")
image = Image.open("C:\\Users\\Tesla Laptops\\Desktop\\portfolio\\sentiment.png")

def web_portfolio():
    # Remove the second set_page_config call here

    st.write(f"""
    <div class="title" style="text-align:center;">
    <span style='font-size: 32px;'>Tech365 Developer</span>
    </div>            
    """, unsafe_allow_html=True)

    st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)

    # Get Profile Image
    with open("abdul.jpg", "rb") as img_file:
        img = "data:image/jpg;base64," + b64encode(img_file.read()).decode()

    # Get Certificate Images
    cert_img_paths = ["certificate.png", "download.png", "down.png"]
    cert_imgs = []
    for cert_path in cert_img_paths:
        with open(cert_path, "rb") as cert_file:
            cert_imgs.append("data:image/jpg;base64," + b64encode(cert_file.read()).decode())

    # Reading Profile
    with open("DACV.pdf", "rb") as pdf_file:
       pdf_bytes = pdf_file.read()

    # Add animation on the DP
    st.write(f"""
    <style>
    @keyframes slowTilt {{
    0%, 100% {{
    transform: rotate(0deg);
    }}
    50% {{
    transform: rotate(1deg);
    }}
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
    """, 
    unsafe_allow_html=True)

    # Set the title
    st.write(f"""
             <div class= "subtitle" style="text-align: center;">Data Analyst & BI-Consultant</div>""",
              unsafe_allow_html=True)
    
    # Add Social Icons
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

    with st.container():
        selected = option_menu(
            menu_title=None,
            options=['About','Projects','Contact'],
            icons=['person','code-slash','chat-left-text-fill'],
            orientation='horizontal'
        )
    if selected == 'About':
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.write("##")
                st.subheader("I am Abdul Samad")
                st.title("Undergraduate at BSAI 7th Semester")
                st.markdown("""
                - 🧑‍💻 I am a **Mid Level Data Analyst and BI-Consultant** at [Diamond Supermarket HO], 
                where I am currently working on a Data Science& Machine Learning project for Keep Learning.
                - ❤️ I am passionate about *Machine Learning/Deep Learning, MLOps, Data Science, Software Engineering, 
                Computer Vision, Data Analytics, Data Engineering, Automation*, and more!
                - 🏂 In my free time, I enjoy practicing sports such as Cricket and Cycling.
                - 🪧 You can reach me at tech365developer@gmail.com.
                - 🏠 Based in Pakistan.
                """)
            with col2:
                st_lottie(lottie_coder)
            
            st.write("---")
            with st.container():
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
                    # Display 3 certificate images side by side
                    st.write("## My Certificates:")
                    cert_cols = st.columns(3)
                    for idx, cert_img in enumerate(cert_imgs):
                        cert_cols[idx].write(f"""
                        <div style="text-align:center;">
                        <img src="{cert_img}" alt="Certificate {idx+1}" style='width: 150px; height: 150px; margin: 10px;'>
                        </div>
                        """, unsafe_allow_html=True)
    if selected =="Projects":
        with st.container():
            st.header("My Projects")
            st.write("## Sentiment Analysis:")
            col5,col6 = st.columns((1,2))
            with col5:
                st.image(image)
            with col6:
                st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/Sentiment_Analysis)")
                st.markdown("""
                - To Perform Sentiment Analysis 1-WordCloud of your positive and negative sentences   2-Lets Perform Emoji Analysis 3-Collect the entire data of youtube 4-which category has maximum likes 5-Analyzing relationship between views and likes 6-Whats channel have the largest number of trending videos?
                """)
             # Project 2: Sales Forecasting
            st.write("## Finance DashBoard:")
            col7, col8 = st.columns((1, 2))
            with col7:
                st.image("C:\\Users\\Tesla Laptops\\Desktop\\portfolio\\Finance.png")
            with col8:
                st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiOWMxYWQ1OTAtYmZmYy00Y2E5LTlmYmUtOTI2YjA3MGU4MTlhIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")  
                st.markdown("""
                - The dashboard is a Personal Finance Dashboard summarizing key financial metrics such as income, expenses, and available balance. It tracks performance against target income, with visualizations for income trends and a gauge to highlight target shortfalls. The dashboard also includes an alert system for upcoming debts and a monthly selection panel for easy filtering. It provides a clear overview of financial health, helping users track their income and expenses effectively.
                """)
            # Project 4: Winter Forecasting
            st.write("## Winter Sales Forecasting:")
            col9, col10 = st.columns((1, 2))
            with col9:
                st.image("C:\\Users\\Tesla Laptops\\Desktop\\portfolio\\timeseries.png")  # Replace with actual image path or URL 
            with col10:
                st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/Time-Series-Forecasting-Multi-Category-Sales/blob/main/Winter_SALES_FORECASTING.ipynb)") 
                st.markdown("""
                - Built a time-series forecasting model to predict future sales.
                - Applied SARIMAX model for time-series data.
                - Visualized forecast results and performance metrics using Matplotlib and Seaborn.
                """)
            # Project 4: Supermarket Sales Price Prediction
            st.write("## Supermarket Sales Prediction:")
            col11, col12 = st.columns((1, 2))
            with col11:
                st.image("C:\\Users\\Tesla Laptops\\Desktop\\portfolio\\supermarket.png")
            with col12:
                st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/SuperMarket-Sales-Prediction)")  
                st.markdown("""
                -The Sales Prediction System for XYZ Stores uses a trained machine learning model to predict sales based on historical data. It helps store managers and analysts make informed decisions by providing real-time sales predictions, optimizing inventory, planning promotions, and improving product placement efficiency.
                """)
            # Project 5: Sales Dashboard
            st.write("## Sales Dashboard:")
            col13, col14, col15, col16, col17 = st.columns((1, 1, 1, 1, 1))  # Add more columns for additional images
            with col13:
                st.image("C:\\Users\\Tesla Laptops\\Desktop\\portfolio\\Screenshot (237).png")  # First image
            with col14:
                st.image("C:\\Users\\Tesla Laptops\\Desktop\\portfolio\\Screenshot (238).png")  # Second image
            with col15:
                st.image("C:\\Users\\Tesla Laptops\\Desktop\\portfolio\\Screenshot (239).png")  # Third image
            with col16:
                st.image("C:\\Users\\Tesla Laptops\\Desktop\\portfolio\\Screenshot (240).png")
            with col17:
                st.image("C:\\Users\\Tesla Laptops\\Desktop\\portfolio\\Screenshot (241).png")
            st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiYWYwOGExMTYtZmJiOC00Zjg0LThlYjItOTIxMjljNzhiMTdiIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
            st.markdown("""
            - In this project highlights significant sales and return trends from 2010 to 2013. Over this period, you achieved a total of 61K transactions, resulting in a net sale of $73M and a profit margin of $48M, with 214K units sold across 349 products to 701 customers. The transaction volume increased consistently each year, with notable customer engagement categorized into Diamond, Silver, and Gold ratings. On the return side, 14K units were refunded, amounting to a $6M total refund, representing an 8% return rate. Key customers with the highest return rates include Monster Well and BodyBuild Depart, reflecting areas for improvement in product satisfaction.
            """)
            # Project 6: Income Statment Dashboard
            st.write("## Income Statment Dashboard:")
            col18, col19= st.columns((1, 2))  # Add more columns for additional images
            with col18:
                st.image("C:\\Users\\Tesla Laptops\\Desktop\\portfolio\\Screenshot (242).png")
            with col19:
                st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiNjBiMzViYmEtNDEzYi00MjVkLWJmYzAtMzA0M2I0Y2ZlYTM3IiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                st.markdown("""
                - The dashboard provides an income statement analysis for the selected year, comparing current and previous periods across key financial metrics such as revenue, gross profit, net income, and expenses. It highlights percentage changes for each metric and includes visual representations, such as line charts and a donut chart for the net income margin (11.45%). The dashboard is segmented by months and regions, allowing for further filtering and exploration of financial performance over time. Key figures show minor growth in revenue (1%) but a significant drop in net income (34%).
                """)
    if selected=='Contact':
        st.header("Get in touch!")
        st.write("##")
        contact_form = """
        <form action="https://formsubmit.co/abdul.samad.ali.abbasi.r678@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder = "Your name" required>
            <input type="email" name="email" placeholder = "Your email" required>
            <textarea name = "message" placeholder = "Your message" required></textarea>
            <button type="submit">Send</button>
        </form>
        """            
        left_col, right_col = st.columns((2,1))
        with left_col:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_col:
            st_lottie(lottie_contact,height=400)    
        

    # Download CV button
    st.download_button(label="📄 Download my CV", data=pdf_bytes, file_name="AbdulSamad_linkedin_cv.pdf", mime="application/pdf")
    st.write("##")
    st.write(f"""<div class="subtitle" style="text-align: center;">🌟 Have A Wonderful Day!!! 🌟</div>""", unsafe_allow_html=True)

if __name__ == "__main__":
    web_portfolio()
