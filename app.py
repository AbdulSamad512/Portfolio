import streamlit as st
from base64 import b64encode
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import pandas as pd
import numpy as np

# Page configuration should be called only once at the top of the script
st.set_page_config(page_title="Abdul Samad Portfolio", page_icon="★", layout="wide")

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
lottie_contact = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_lt8ter7g.json")
image = Image.open("sentiment.png")

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
    with open("MLCV.pdf", "rb") as pdf_file:
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
    if selected == "Projects":
        with st.container():
            st.header("My Projects")
        # Add subcategories for Dashboards and Data Science Projects
            subcategory = st.radio("Select Project Category:", ["Dashboards", "Data Science Projects"], horizontal=True)

        # Dashboards Section
            if subcategory == "Dashboards":
                st.write("## Dashboards")
            
                # Project 1: Finance Dashboard
                st.write("### Finance Dashboard:")
                col7, col8 = st.columns((1, 2))
                with col7:
                    st.image("Finance.png")
                with col8:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiOWMxYWQ1OTAtYmZmYy00Y2E5LTlmYmUtOTI2YjA3MGU4MTlhIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")  
                    st.markdown("""
                    - The dashboard is a Personal Finance Dashboard summarizing key financial metrics such as income, expenses, and available balance. It tracks performance against target income, with visualizations for income trends and a gauge to highlight target shortfalls.
                    """)

                # Project 2: Sales Dashboard
                st.write("## Sales Dashboard:")
                col13, col14, col15, col16, col17 = st.columns((1, 1, 1, 1,1))  # Add more columns for additional images
                with col13:
                    st.image("Screenshot (237).png")  # First image
                with col14:
                    st.image("Screenshot (238).png")  # Second image
                with col15:
                    st.image("Screenshot (239).png")  # Third image
                with col16:
                    st.image("Screenshot (240).png")  
                with col17:
                    st.image("Screenshot (241).png")
                st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiYWYwOGExMTYtZmJiOC00Zjg0LThlYjItOTIxMjljNzhiMTdiIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                st.markdown("""
                - In this project highlights significant sales and return trends from 2010 to 2013. Over this period, you achieved a total of 61K transactions, resulting in a net sale of $73M and a profit margin of $48M, with 214K units sold across 349 products to 701 customers. The transaction volume increased consistently each year, with notable customer engagement categorized into Diamond, Silver, and Gold ratings. On the return side, 14K units were refunded, amounting to a $6M total refund, representing an 8% return rate. Key customers with the highest return rates include Monster Well and BodyBuild Depart, reflecting areas for improvement in product satisfaction.
                """)

            # Project 3: Income Statement Dashboard
                st.write("### Income Statement Dashboard:")
                col18, col19 = st.columns((1, 2))
                with col18:
                    st.image("Screenshot (242).png")
                with col19:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiNjBiMzViYmEtNDEzYi00MjVkLWJmYzAtMzA0M2I0Y2ZlYTM3IiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                        -  The dashboard provides an income statement analysis for the selected year, comparing current and previous periods across key financial metrics such as revenue, gross profit, net income, and expenses. It highlights percentage changes for each metric and includes visual representations, such as line charts and a donut chart for the net income margin (11.45%). The dashboard is segmented by months and regions, allowing for further filtering and exploration of financial performance over time. Key figures show minor growth in revenue (1%) but a significant drop in net income (34%).
                        """)
            # Project 4: Patient Emergency Room Visit Report 
                st.write("### Patient Emergency Room Visit Report")
                col51,col52 = st.columns((1,2))
                with col51:
                    st.image("Patient.png")
                with col52:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiNDc4MzMzOTItZjBmMC00MmNkLWJhNTAtZjY1MmMyMTQ4MTRlIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - The Patient Emergency Room Visit Report provides an overview of 9,216 total visits, evenly split between administrative and non-administrative appointments. The average patient satisfaction score is 5.47, with 75.10% of services not rated and an average wait time of 35.26 minutes. Most visits occurred during weekdays, with adult patients making up the majority. Referrals primarily lead to general practitioners and orthopedics, while walk-in patients account for 58.59% of the total visits. Patient satisfaction correlates with shorter wait times, as highlighted in the demographic and age group heatmap analysis.
                    """)
            # Project 5: Risk EQUIPMENT DASHBOARD
                st.write("## Risk Equipment Dashboard:")
                col53, col54, col55, col56 = st.columns((1, 1, 1, 1))  # Add more columns for additional images
                with col53:
                    st.image("Risk1.png")  # First image
                with col54:
                    st.image("Risk2.png")  # Second image
                with col55:
                    st.image("Risk3.png")  # Third image
                with col56:
                    st.image("Risk4.png")  
                st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiNGMyZTlhMTMtNDE5Ny00ZjQ5LWFlM2UtYTEyZmU5OTY4N2QyIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                st.markdown("""
                -   Leveraging data visualization tools, I developed interactive dashboards to track and monitor equipment defect
                trends, identify critical issues, and prioritize mitigation efforts. This data-driven approach resulted in a significant
                reduction in equipment failures, improving overall system reliability and operational efficiency. By analyzing defect
                patterns, severity, and likelihood, I was able to implement targeted maintenance strategies and reduce downtime,
                ultimately contributing to increased productivity and cost savings.
                """)
            # Project 6: Fleet Management Dashboard
                st.write("### Fleet Management Dashboard:")
                col57,col58 = st.columns((1,2))
                with col57:
                    st.image("FLEETMANAGEMENT.png")
                with col58:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiNmQwZWUyMGItNDdhNi00NjA3LWE0NWQtYjI0YjhmZTYyMjk5IiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - Fleet Management Dashboard: Designed and developed a dynamic Power BI dashboard to monitor fleet operations and key performance indicators. The dashboard provides insights into metrics such as total fuel consumed, maintenance costs, kilometers traveled, and driver performance. Leveraged data modeling and DAX measures to create intuitive visuals, including trend analysis and comparative metrics, enabling stakeholders to make data-driven decisions. The dashboard integrates multiple data sources and ensures seamless data refresh for up-to-date analysis.
                    """)


        # Data Science Projects Section
            elif subcategory == "Data Science Projects":
                st.write("## Data Science Projects")

                st.write("### Stock Price Prediction")
                col31,col32 = st.columns((1,2))
                with col31:
                    st.video("stock_price.mp4")
                with col32:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/Stovk_Price_Predcition)")
                    st.markdown("""
                        - This project involves building a deep learning model for time-series forecasting using a sequential Long Short-Term Memory (LSTM) network. The model architecture consists of four LSTM layers with increasing units (50, 60, 80, 120) to capture complex temporal dependencies in the data. Dropout layers with rates ranging from 0.2 to 0.5 are incorporated to prevent overfitting. The network is finalized with a Dense layer to output predictions. Designed for input shapes matching the time-series data, the model is trained on preprocessed datasets, leveraging robust recurrent layers. Applications include stock price prediction, weather forecasting, or similar time-series tasks. This architecture is tailored to enhance predictive accuracy while mitigating overfitting risks.
                    """)

                st.write("## Airline Customer Satisfaction MLOPS Projects")
                col33,col34 = st.columns((1,2))
                with col33:
                    st.video("AirlineMLOPS.mp4")
                with col34:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/Airline_Customer_Satisfaction)")
                    st.markdown("""
                        - This project involves building a machine learning model to analyze airline customer   satisfaction, utilizing MLOps technologies to streamline and manage the project workflow efficiently.
                    """)

                # Project 5: HR Employee Attrition
                st.write("## Employee Churn Predicition:")
                col24,col25 = st.columns((1,2))
                with col24:
                    st.image("Employee.png")
                with col25: 
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/HR_Employee_Attrition)")
                    st.markdown("""
                        - Developed an Employee Churn Prediction System that uses machine learning to predict employee turnover. Models like RandomForestClassifier and XGBClassifier were optimized using GridSearchCV for parameters such as n_estimators, max_depth, and learning_rate. The Flask-based interface allows users to input employee data and receive predictions in real time. This project showcases expertise in machine learning, hyperparameter tuning, and full-stack development, providing actionable insights for improving employee retention strategies.
                    """)
                
                # Project 6: HR Employee Attrition
                st.write("## Restaurant Rating Prediction:")
                col26,col27 = st.columns((1,2))
                with col26:
                    st.image("restaurant.png")
                with col27:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/Restaurant_Rating_Prediction)")
                    st.markdown("""
                        - This project predicts restaurant ratings based on user-provided features like votes, reviews, and other parameters using machine learning. The model leverages the Extra Trees Regressor, an ensemble method that builds multiple decision trees for regression. The model is trained using the dataset split into x_train and y_train, then tested with x_test to predict outcomes. The R² score evaluates the model's performance, indicating how well it predicts ratings compared to actual values.
                    """)
                
                # Project 7: Flight Price Prediction
                st.write("## Flight Price Prediction")
                col28,col29 = st.columns((1,2))
                with col28:
                    st.image("Flight_Price_Prediction.png")
                with col29:
                    st.markdown("[Visit Github Repository](https://github.com/AbdulSamad512/Flight_Price_Predicition)")
                    st.markdown("""
                        - This flight price prediction application is a dynamic machine learning-based tool designed to estimate ticket prices based on inputs such as departure and arrival times, airline, and stopover details. Built with a responsive UI, it integrates powerful predictive models like LightGBM to deliver accurate cost estimates in real-time. Developed with a user-friendly interface, this project demonstrates expertise in web development and data science, showcasing the ability to create practical and impactful applications.
                    """)

                # Project 9: Gemini AI Voice Assistant
                st.write("### AI Voice Assistant:")
                col22, col23 = st.columns((1, 2))
                with col22:
                    st.image("AiVoice.png")
                with col23:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/Ai-Voice-Assistant)")
                    st.markdown("""
                        - I developed an AI Voice Assistant enabling interactive voice and text-based queries with a "Speak Now" button for seamless interaction. Built using Python (Flask) and HTML/CSS/JavaScript, it integrates voice-to-text, text-to-speech APIs, and pretrained LLMs to provide accurate, context-aware responses. This project highlights practical AI applications in education, customer support, and learning platforms.
                    """)

            # Project 7: House Price Prediction Using ANN
                st.write("### Housing Price Prediction Using ANN:")
                col20, col21 = st.columns((1, 2))
                with col20:
                    st.image("House.png")
                with col21:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/Housing_Price_Prediction_Using_ANN)")
                    st.markdown("""
                        - The Housing Price Prediction using ANN project uses artificial neural networks to predict house prices based on features like longitude, number of bedrooms, population, and housing median age. It involves data preprocessing, feature engineering, model training, evaluation, and fine-tuning to accurately predict prices for new data.
                    """)

            # Project 8: Sentiment Analysis Using Neural Network
                st.write("### Sentiment Analysis Using Neural Network:")
                col22, col23 = st.columns((1, 2))
                with col22:
                    st.image("NLP-Sentiment.png")
                with col23:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/SentimentAnalysis_with_NeuralNetwork)")
                    st.markdown("""
                        - This project focuses on sentiment analysis using deep neural networks, specifically LSTM (Long Short-Term Memory) layers. It begins with loading a dataset of movie reviews, followed by text preprocessing steps like tokenization, sequence padding, and stopword removal. A sequential model is built with embedding layers and LSTM for extracting temporal patterns, with dense layers for classification. The model is trained and evaluated for accuracy in predicting sentiments (positive or negative). Results are interpreted, and the trained model is ready for deployment in sentiment analysis applications.
                    """)                     
                # Project 3: Winter Forecasting
                st.write("## Winter Sales Forecasting:")
                col9, col10 = st.columns((1, 2))
                with col9:
                    st.image("timeseries.png")  # Replace with actual image path or URL 
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
                    st.image("supermarket.png")
                with col12:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/SuperMarket-Sales-Prediction)")  
                    st.markdown("""
                            - The Sales Prediction System for XYZ Stores uses a trained machine learning model to predict sales based on historical data. It helps store managers and analysts make informed decisions by providing real-time sales predictions, optimizing inventory, planning promotions, and improving product placement efficiency.
                        """)
                    # Project 1 : Sentiment Analysis
                st.write("## Sentiment Analysis:")
                col5,col6 = st.columns((1,2))
                with col5:
                    st.image(image)
                with col6:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/Sentiment_Analysis)")
                    st.markdown("""
                            - To Perform Sentiment Analysis 1-WordCloud of your positive and negative sentences   2-Lets Perform Emoji Analysis 3-Collect the entire data of youtube 4-which category has maximum likes 5-Analyzing relationship between views and likes 6-Whats channel have the largest number of trending videos?
                        """)
                

            # Add other Data Science projects here as needed.

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
    st.download_button(label="📄 Download my CV", data=pdf_bytes, file_name="MLCV.pdf", mime="application/pdf")
    st.write("##")
    st.write(f"""<div class="subtitle" style="text-align: center;">🌟 Have A Wonderful Day!!! 🌟</div>""", unsafe_allow_html=True)

if __name__ == "__main__":
    web_portfolio()

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
lottie_contact = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_lt8ter7g.json")
image = Image.open("sentiment.png")

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
    with open("MLCV.pdf", "rb") as pdf_file:
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
    if selected == "Projects":
        with st.container():
            st.header("My Projects")
        # Add subcategories for Dashboards and Data Science Projects
            subcategory = st.radio("Select Project Category:", ["Dashboards", "Data Science Projects"], horizontal=True)

        # Dashboards Section
            if subcategory == "Dashboards":
                st.write("## Dashboards")
            
                # Project 1: Finance Dashboard
                st.write("### Finance Dashboard:")
                col7, col8 = st.columns((1, 2))
                with col7:
                    st.image("Finance.png")
                with col8:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiOWMxYWQ1OTAtYmZmYy00Y2E5LTlmYmUtOTI2YjA3MGU4MTlhIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")  
                    st.markdown("""
                    - The dashboard is a Personal Finance Dashboard summarizing key financial metrics such as income, expenses, and available balance. It tracks performance against target income, with visualizations for income trends and a gauge to highlight target shortfalls.
                    """)

                # Project 2: Sales Dashboard
                st.write("## Sales Dashboard:")
                col13, col14, col15, col16, col17 = st.columns((1, 1, 1, 1,1))  # Add more columns for additional images
                with col13:
                    st.image("Screenshot (237).png")  # First image
                with col14:
                    st.image("Screenshot (238).png")  # Second image
                with col15:
                    st.image("Screenshot (239).png")  # Third image
                with col16:
                    st.image("Screenshot (240).png")  
                with col17:
                    st.image("Screenshot (241).png")
                st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiYWYwOGExMTYtZmJiOC00Zjg0LThlYjItOTIxMjljNzhiMTdiIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                st.markdown("""
                - In this project highlights significant sales and return trends from 2010 to 2013. Over this period, you achieved a total of 61K transactions, resulting in a net sale of $73M and a profit margin of $48M, with 214K units sold across 349 products to 701 customers. The transaction volume increased consistently each year, with notable customer engagement categorized into Diamond, Silver, and Gold ratings. On the return side, 14K units were refunded, amounting to a $6M total refund, representing an 8% return rate. Key customers with the highest return rates include Monster Well and BodyBuild Depart, reflecting areas for improvement in product satisfaction.
                """)

            # Project 3: Income Statement Dashboard
                st.write("### Income Statement Dashboard:")
                col18, col19 = st.columns((1, 2))
                with col18:
                    st.image("Screenshot (242).png")
                with col19:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiNjBiMzViYmEtNDEzYi00MjVkLWJmYzAtMzA0M2I0Y2ZlYTM3IiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                        -  The dashboard provides an income statement analysis for the selected year, comparing current and previous periods across key financial metrics such as revenue, gross profit, net income, and expenses. It highlights percentage changes for each metric and includes visual representations, such as line charts and a donut chart for the net income margin (11.45%). The dashboard is segmented by months and regions, allowing for further filtering and exploration of financial performance over time. Key figures show minor growth in revenue (1%) but a significant drop in net income (34%).
                        """)
            # Project 4: Patient Emergency Room Visit Report 
                st.write("### Patient Emergency Room Visit Report")
                col51,col52 = st.columns((1,2))
                with col51:
                    st.image("Patient.png")
                with col52:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiNDc4MzMzOTItZjBmMC00MmNkLWJhNTAtZjY1MmMyMTQ4MTRlIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - The Patient Emergency Room Visit Report provides an overview of 9,216 total visits, evenly split between administrative and non-administrative appointments. The average patient satisfaction score is 5.47, with 75.10% of services not rated and an average wait time of 35.26 minutes. Most visits occurred during weekdays, with adult patients making up the majority. Referrals primarily lead to general practitioners and orthopedics, while walk-in patients account for 58.59% of the total visits. Patient satisfaction correlates with shorter wait times, as highlighted in the demographic and age group heatmap analysis.
                    """)
            # Project 5: Risk EQUIPMENT DASHBOARD
                st.write("## Risk Equipment Dashboard:")
                col53, col54, col55, col56 = st.columns((1, 1, 1, 1))  # Add more columns for additional images
                with col53:
                    st.image("Risk1.png")  # First image
                with col54:
                    st.image("Risk2.png")  # Second image
                with col55:
                    st.image("Risk3.png")  # Third image
                with col56:
                    st.image("Risk4.png")  
                st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiNGMyZTlhMTMtNDE5Ny00ZjQ5LWFlM2UtYTEyZmU5OTY4N2QyIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                st.markdown("""
                -   Leveraging data visualization tools, I developed interactive dashboards to track and monitor equipment defect
                trends, identify critical issues, and prioritize mitigation efforts. This data-driven approach resulted in a significant
                reduction in equipment failures, improving overall system reliability and operational efficiency. By analyzing defect
                patterns, severity, and likelihood, I was able to implement targeted maintenance strategies and reduce downtime,
                ultimately contributing to increased productivity and cost savings.
                """)
            # Project 6: Fleet Management Dashboard
                st.write("### Fleet Management Dashboard:")
                col57,col58 = st.columns((1,2))
                with col57:
                    st.image("FLEETMANAGEMENT.png")
                with col58:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiNmQwZWUyMGItNDdhNi00NjA3LWE0NWQtYjI0YjhmZTYyMjk5IiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - Fleet Management Dashboard: Designed and developed a dynamic Power BI dashboard to monitor fleet operations and key performance indicators. The dashboard provides insights into metrics such as total fuel consumed, maintenance costs, kilometers traveled, and driver performance. Leveraged data modeling and DAX measures to create intuitive visuals, including trend analysis and comparative metrics, enabling stakeholders to make data-driven decisions. The dashboard integrates multiple data sources and ensures seamless data refresh for up-to-date analysis.
                    """)


        # Data Science Projects Section
            elif subcategory == "Data Science Projects":
                st.write("## Data Science Projects")

                st.write("### Stock Price Prediction")
                col31,col32 = st.columns((1,2))
                with col31:
                    st.video("stock_price.mp4")
                with col32:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/Stovk_Price_Predcition)")
                    st.markdown("""
                        - This project involves building a deep learning model for time-series forecasting using a sequential Long Short-Term Memory (LSTM) network. The model architecture consists of four LSTM layers with increasing units (50, 60, 80, 120) to capture complex temporal dependencies in the data. Dropout layers with rates ranging from 0.2 to 0.5 are incorporated to prevent overfitting. The network is finalized with a Dense layer to output predictions. Designed for input shapes matching the time-series data, the model is trained on preprocessed datasets, leveraging robust recurrent layers. Applications include stock price prediction, weather forecasting, or similar time-series tasks. This architecture is tailored to enhance predictive accuracy while mitigating overfitting risks.
                    """)

                st.write("## Airline Customer Satisfaction MLOPS Projects")
                col33,col34 = st.columns((1,2))
                with col33:
                    st.video("AirlineMLOPS.mp4")
                with col34:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/Airline_Customer_Satisfaction)")
                    st.markdown("""
                        - This project involves building a machine learning model to analyze airline customer   satisfaction, utilizing MLOps technologies to streamline and manage the project workflow efficiently.
                    """)

                # Project 5: HR Employee Attrition
                st.write("## Employee Churn Predicition:")
                col24,col25 = st.columns((1,2))
                with col24:
                    st.image("Employee.png")
                with col25: 
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/HR_Employee_Attrition)")
                    st.markdown("""
                        - Developed an Employee Churn Prediction System that uses machine learning to predict employee turnover. Models like RandomForestClassifier and XGBClassifier were optimized using GridSearchCV for parameters such as n_estimators, max_depth, and learning_rate. The Flask-based interface allows users to input employee data and receive predictions in real time. This project showcases expertise in machine learning, hyperparameter tuning, and full-stack development, providing actionable insights for improving employee retention strategies.
                    """)
                
                # Project 6: HR Employee Attrition
                st.write("## Restaurant Rating Prediction:")
                col26,col27 = st.columns((1,2))
                with col26:
                    st.image("restaurant.png")
                with col27:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/Restaurant_Rating_Prediction)")
                    st.markdown("""
                        - This project predicts restaurant ratings based on user-provided features like votes, reviews, and other parameters using machine learning. The model leverages the Extra Trees Regressor, an ensemble method that builds multiple decision trees for regression. The model is trained using the dataset split into x_train and y_train, then tested with x_test to predict outcomes. The R² score evaluates the model's performance, indicating how well it predicts ratings compared to actual values.
                    """)
                
                # Project 7: Flight Price Prediction
                st.write("## Flight Price Prediction")
                col28,col29 = st.columns((1,2))
                with col28:
                    st.image("Flight_Price_Prediction.png")
                with col29:
                    st.markdown("[Visit Github Repository](https://github.com/AbdulSamad512/Flight_Price_Predicition)")
                    st.markdown("""
                        - This flight price prediction application is a dynamic machine learning-based tool designed to estimate ticket prices based on inputs such as departure and arrival times, airline, and stopover details. Built with a responsive UI, it integrates powerful predictive models like LightGBM to deliver accurate cost estimates in real-time. Developed with a user-friendly interface, this project demonstrates expertise in web development and data science, showcasing the ability to create practical and impactful applications.
                    """)

                # Project 9: Gemini AI Voice Assistant
                st.write("### AI Voice Assistant:")
                col22, col23 = st.columns((1, 2))
                with col22:
                    st.image("AiVoice.png")
                with col23:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/Ai-Voice-Assistant)")
                    st.markdown("""
                    - I developed an AI Voice Assistant enabling interactive voice and text-based queries with a "Speak Now" button for seamless interaction. Built using Python (Flask) and HTML/CSS/JavaScript, it integrates voice-to-text, text-to-speech APIs, and pretrained LLMs to provide accurate, context-aware responses. This project highlights practical AI applications in education, customer support, and learning platforms.
                    """)

            # Project 7: House Price Prediction Using ANN
                st.write("### Housing Price Prediction Using ANN:")
                col20, col21 = st.columns((1, 2))
                with col20:
                    st.image("House.png")
                with col21:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/Housing_Price_Prediction_Using_ANN)")
                    st.markdown("""
                        - The Housing Price Prediction using ANN project uses artificial neural networks to predict house prices based on features like longitude, number of bedrooms, population, and housing median age. It involves data preprocessing, feature engineering, model training, evaluation, and fine-tuning to accurately predict prices for new data.
                        """)

            # Project 8: Sentiment Analysis Using Neural Network
                st.write("### Sentiment Analysis Using Neural Network:")
                col22, col23 = st.columns((1, 2))
                with col22:
                    st.image("NLP-Sentiment.png")
                with col23:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/SentimentAnalysis_with_NeuralNetwork)")
                    st.markdown("""
                        -This project focuses on sentiment analysis using deep neural networks, specifically LSTM (Long Short-Term Memory) layers. It begins with loading a dataset of movie reviews, followed by text preprocessing steps like tokenization, sequence padding, and stopword removal. A sequential model is built with embedding layers and LSTM for extracting temporal patterns, with dense layers for classification. The model is trained and evaluated for accuracy in predicting sentiments (positive or negative). Results are interpreted, and the trained model is ready for deployment in sentiment analysis applications.
                    """)                     
                # Project 3: Winter Forecasting
                st.write("## Winter Sales Forecasting:")
                col9, col10 = st.columns((1, 2))
                with col9:
                    st.image("timeseries.png")  # Replace with actual image path or URL 
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
                    st.image("supermarket.png")
                with col12:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/SuperMarket-Sales-Prediction)")  
                    st.markdown("""
                        -The Sales Prediction System for XYZ Stores uses a trained machine learning model to predict sales based on historical data. It helps store managers and analysts make informed decisions by providing real-time sales predictions, optimizing inventory, planning promotions, and improving product placement efficiency.
                        """)
                    # Project 1 : Sentiment Analysis
                st.write("## Sentiment Analysis:")
                col5,col6 = st.columns((1,2))
                with col5:
                    st.image(image)
                with col6:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/Sentiment_Analysis)")
                    st.markdown("""
                        - To Perform Sentiment Analysis 1-WordCloud of your positive and negative sentences   2-Lets Perform Emoji Analysis 3-Collect the entire data of youtube 4-which category has maximum likes 5-Analyzing relationship between views and likes 6-Whats channel have the largest number of trending videos?
                        """)
                

            # Add other Data Science projects here as needed.

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
    st.download_button(label="📄 Download my CV", data=pdf_bytes, file_name="MLCV.pdf", mime="application/pdf")
    st.write("##")
    st.write(f"""<div class="subtitle" style="text-align: center;">🌟 Have A Wonderful Day!!! 🌟</div>""", unsafe_allow_html=True)

if __name__ == "__main__":
    web_portfolio()

