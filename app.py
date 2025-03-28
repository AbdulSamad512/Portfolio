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
    cert_img_paths = ["certificate.png", "download.png", "down.png", "MLIntern.png"]
    cert_imgs = []
    for cert_path in cert_img_paths:
        with open(cert_path, "rb") as cert_file:
            cert_imgs.append("data:image/jpg;base64," + b64encode(cert_file.read()).decode())

    # Reading Profile
    with open("UpdatedDaSc.pdf", "rb") as pdf_file:
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
                st.title("Undergraduate at BSAI 8th Semester")
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
                    cert_cols = st.columns(4)
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
            subcategory = st.radio("Select Project Category:", ["Dashboards", "Data Science Projects", "Data base & ETL Projects","MLOPS PROJECT"], horizontal=True)

        # Dashboards Section
            if subcategory == "Dashboards":
                st.write("## Dashboards:")

                st.write("### 🚀 Optimizing Ticket Performance with Power BI! 📊:")
                col1,col2 = st.columns((1,2))
                with col1:
                    st.video("Ticket.mp4")
                with col2:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiNDczMjg1ZDktMmM5MC00ZjU0LTk1ZjMtYThiZDhmMWM4ZTZhIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - I recently developed an interactive Ticket Performance Dashboard in Power BI to analyze  SLA compliance, and resolution trends. The dashboard provides data-driven insights into key metrics such as ticket volume, agent performance, and issue categories, helping businesses improve efficiency and decision-making.
                    """)

                st.write("### 🚀 Optimizing SALES DASHBOARD with Power BI! 📊:")
                col3,col4 = st.columns((1,2))
                with col3:
                    st.video("SalesDashboard.mp4")
                with col4:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiY2I1YzJjMzAtM2U1OS00NWUxLWE0OGEtOWViMDY0OWU1MTU0IiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - This Power BI Sales Dashboard provides insights into transactions, revenue, and sales performance across different channels. It breaks down performance by managers, supervisors, and salespersons while comparing revenue trends against the budget. With interactive filters, it helps businesses track trends, identify top performers, and make data-driven decisions efficiently.
                    """)

                # Project 1: Finance Dashboard
                st.write("### 🚀 Optimizing Finance Dashboard with Power BI! 📊:")
                col5, col6 = st.columns((1, 2))
                with col5:
                    st.image("Finance.png")
                with col6:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiOWMxYWQ1OTAtYmZmYy00Y2E5LTlmYmUtOTI2YjA3MGU4MTlhIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")  
                    st.markdown("""
                    - The dashboard is a Personal Finance Dashboard summarizing key financial metrics such as income, expenses, and available balance. It tracks performance against target income, with visualizations for income trends and a gauge to highlight target shortfalls.
                    """)

                # Project 2: Sales Dashboard
                st.write("### 🚀 Optimizing Sales Dashboard with Power BI! 📊:")
                col7, col8 =   st.columns((1, 2)) # Add more columns for additional images
                with col7:
                    st.video("HPN_Dashboard.mp4")  # First image
                with col8:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiYWYwOGExMTYtZmJiOC00Zjg0LThlYjItOTIxMjljNzhiMTdiIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - In this project highlights significant sales and return trends from 2010 to 2013. Over this period, you achieved a total of 61K transactions, resulting in a net sale of $73M and a profit margin of $ 48M, with 214K units sold across 349 products to 701 customers. The transaction volume increased consistently each year, with notable customer engagement categorized into Diamond, Silver, and Gold ratings. On the return side, 14K units were refunded, amounting to a $6M total refund, representing an 8% return rate. Key customers with the highest return rates include Monster Well and BodyBuild Depart, reflecting areas for improvement in product satisfaction.
                    """)

            # Project 3: Income Statement Dashboard
                st.write("### 🚀 Optimizing Income Statement Dashboard with Power BI! 📊:")
                col9, col10 = st.columns((1, 2))
                with col9:
                    st.image("Screenshot (242).png")
                with col10:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiNjBiMzViYmEtNDEzYi00MjVkLWJmYzAtMzA0M2I0Y2ZlYTM3IiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                        -  The dashboard provides an income statement analysis for the selected year, comparing current and previous periods across key financial metrics such as revenue, gross profit, net income, and expenses. It highlights percentage changes for each metric and includes visual representations, such as line charts and a donut chart for the net income margin (11.45%). The dashboard is segmented by months and regions, allowing for further filtering and exploration of financial performance over time. Key figures show minor growth in revenue (1%) but a significant drop in net income (34%).
                        """)


            # Project 4: Patient Emergency Room Visit Report 
                st.write("### 🚀 Optimizing Patient Emergency Room Visit Report with Power BI! 📊")
                col11,col12 = st.columns((1,2))
                with col11:
                    st.image("Patient.png")
                with col12:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiNDc4MzMzOTItZjBmMC00MmNkLWJhNTAtZjY1MmMyMTQ4MTRlIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - The Patient Emergency Room Visit Report provides an overview of 9,216 total visits, evenly split between administrative and non-administrative appointments. The average patient satisfaction score is 5.47, with 75.10% of services not rated and an average wait time of 35.26 minutes. Most visits occurred during weekdays, with adult patients making up the majority. Referrals primarily lead to general practitioners and orthopedics, while walk-in patients account for 58.59% of the total visits. Patient satisfaction correlates with shorter wait times, as highlighted in the demographic and age group heatmap analysis.
                    """)


            # Project 5: Risk EQUIPMENT DASHBOARD
                st.write("### 🚀 Optimizing Risk Equipment Dashboard with Power BI! 📊:")
                col13, col14, col15, col16 = st.columns((1, 1, 1, 1))  # Add more columns for additional images
                with col13:
                    st.image("Risk1.png")  # First image
                with col14:
                    st.image("Risk2.png")  # Second image
                with col15:
                    st.image("Risk3.png")  # Third image
                with col16:
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
                st.write("### 🚀 Optimizing Fleet Management Dashboard with Power BI! 📊:")
                col17,col18 = st.columns((1,2))
                with col17:
                    st.image("FLEETMANAGEMENT.png")
                with col18:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiNmQwZWUyMGItNDdhNi00NjA3LWE0NWQtYjI0YjhmZTYyMjk5IiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - Fleet Management Dashboard: Designed and developed a dynamic Power BI dashboard to monitor fleet operations and key performance indicators. The dashboard provides insights into metrics such as total fuel consumed, maintenance costs, kilometers traveled, and driver performance. Leveraged data modeling and DAX measures to create intuitive visuals, including trend analysis and comparative metrics, enabling stakeholders to make data-driven decisions. The dashboard integrates multiple data sources and ensures seamless data refresh for up-to-date analysis.
                    """)


                st.write("### 🚀 Call Center Dashboard with Power BI! 📊:")
                col17,col18 = st.columns((1,2))
                with col17:
                    st.video("Call_Center_Dashboard.mp4")
                with col18:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiMjQ5YTNmMTQtMjQyMy00MTZmLWFiOTctOTc3NTA1M2RhZmQ5IiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - Developed an interactive Power BI dashboard to monitor call center performance. Visualized key metrics such as call volume, average handling time, and customer satisfaction. Provided actionable insights to enhance operational efficiency and optimize resource allocation. Enabled real-time decision-making through intuitive visualizations.
                    """)

                st.write("### 🚀 Expense Analysis Dashboard with Power BI! 📊:")
                col19,col20 = st.columns((1,2))
                with col19:
                    st.video("Expense_Analysis_Dashboard.mp4")
                with col20:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiNTgyMzA0ZWYtNzU5OS00NWQ0LWJlNzktNzNmNDdhYzVlN2RkIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - Designed a comprehensive Power BI dashboard to track and analyze expenses across categories. Visualized spending patterns, identified cost-saving opportunities, and provided detailed financial insights. Enabled stakeholders to make data-driven budgeting decisions through clear and interactive visualizations.
                    """)

                st.write("### 🚀 Energy Consumption Dashboard with Power BI! 📊:")
                col20,col21 = st.columns((1,2))
                with col20:
                    st.video("Energy_Consumption_Dashboard.mp4")
                with col21:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiODA4Zjk5ZDMtMGRjOS00ZTQ0LTgzMTgtNTlkYTIzODdkMWYxIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - Developed an interactive Power BI dashboard to monitor energy consumption patterns across various sectors. Provided actionable insights through detailed visualizations, facilitating energy optimization and cost management. Empowered decision-makers to reduce wastage and enhance energy efficiency.
                    """)

                st.write("### 🚀 Ecommerce Sales Dashboard with Power BI! 📊:")
                col22,col23 = st.columns((1,2))
                with col22:
                    st.video("Ecommerce_Sales_Dashboard.mp4")
                with col23:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiMjhlNzA1ZDMtMzhhZi00ZTcxLTlkZWItZGU5MzVlYjE0ZGMwIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - Designed an intuitive Power BI dashboard to analyze ecommerce sales performance. Visualized key metrics such as revenue, sales trends, and product performance. Delivered actionable insights to optimize sales strategies and drive business growth.
                    """)

                st.write("### 🚀 Sales Performance Dashboard with Power BI! 📊:")
                col24,col25 = st.columns((1,2))
                with col24:
                    st.video("Sales_Performance_Dashboard.mp4")
                with col25:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiZjYwNDUwYWQtZTcxMS00Y2IxLWIzMDUtNjAwNmZlMGE3ZTdmIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - Developed a dynamic sales performance dashboard in Power BI. Provided real-time insights into sales trends, regional performance, and product analysis. Enabled stakeholders to make data-driven decisions for improved sales outcomes.
                    """)
                    
                st.write("### 🚀 Employee Performance Dashboard with Power BI! 📊:")
                col26,col27 = st.columns((1,2))
                with col26:
                    st.video("Employee_Performance_Dashboard.mp4")
                with col27:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiNjMzZjcxZDQtODEzNS00OWFlLThiMjQtZGE1NjFiOGUzYTc2IiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - Developed a Power BI dashboard to assess employee performance using key metrics like productivity, attendance, and task completion. Provided actionable insights for HR and management to identify top performers and support employee development.
                    """)

                st.write("### 🚀 Sales Win Loss Ratio Dashboard with Power BI! 📊:")
                col28,col29 = st.columns((1,2))
                with col28:
                    st.video("Salaes_Win_Loss_Ratio_Dashboard.mp4")
                with col29:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiNDZkODcxOTEtMTk4MS00MzUzLTk5OTUtY2NmMjdkNTU5Njc5IiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - Built a dynamic Power BI dashboard to track sales performance by analyzing win-loss ratios. Provided detailed insights into deal outcomes, helping sales teams refine strategies and improve conversion rates.
                    """)

                st.write("### 🚀 Sales and Inventory Dashboard with Power BI! 📊:")
                col30,col31 = st.columns((1,2))
                with col30:
                    st.video("Sales_And_Inventory_Dashboard.mp4")
                with col31:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiMTRiNzkxNjUtMWYzYi00NGU2LThhOTctYzkwYTFmOWE2MTA0IiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - Developed a Power BI dashboard to monitor real-time sales and inventory levels. Provided actionable insights for inventory management, reducing stockouts and overstocking, and improving operational efficiency.
                    """)

                st.write("### 🚀 Supply Chain Dashboard with Power BI! 📊:")
                col32,col33 = st.columns((1,2))
                with col32:
                    st.video("Supply_Chain_Analytics.mp4")
                with col33:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiM2MxZjlkNTAtZmZmZi00NzM3LWJiNmYtNmNmNzQ2MzNiZTMyIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - Designed a comprehensive Power BI dashboard to analyze supply chain performance, monitor key metrics, and identify bottlenecks. Enabled data-driven decision-making, improving overall operational efficiency and reducing costs.
                    """)

                st.write("### 🚀 Customer Analytics Dashboard with Power BI! 📊:")
                col32,col33 = st.columns((1,2))
                with col32:
                    st.video("Customer_Analytics_Dashboard.mp4")
                with col33:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiMmM5ZDliMmYtNzFlZS00MmVjLWEzNWYtNjdiNGM1M2Q2ZjI0IiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - Developed a dynamic Power BI dashboard to analyze customer behavior, segment audiences, and track key performance indicators. Provided actionable insights to enhance customer retention and personalize marketing strategies.
                    """)

                st.write("### 🚀 Balance Sheet Dashboard with Power BI! 📊:")
                col34,col35 = st.columns((1,2))
                with col34:
                    st.video("Balance_Statment_Analytics.mp4")
                with col35:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiNzg5YTQ2OTYtMDIxNC00YTBiLTk1ZjYtODRkZjQ4ZTVlOGVkIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - Designed an interactive Power BI dashboard to visualize financial data, track revenue, expenses, and profit trends. Enabled stakeholders to make informed financial decisions with real-time insights and comprehensive reports.
                    """)
                
                st.write("### 🚀 Car Sale Dashboard with Power BI! 📊:")
                col34,col35 = st.columns((1,2))
                with col34:
                    st.video("Car_Sales_Dashboard.mp4")
                with col35:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiYmUzMDk3YjMtNzg2Zi00NDA5LTg0MDgtYjE2ZTk4ZTZjOGM5IiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - Developed a comprehensive Power BI dashboard to monitor car sales performance, analyze trends, and assess dealership profitability. Provided actionable insights using visualized KPIs, regional comparisons, and sales growth metrics.
                    """)

                st.write("### 🚀 Adidas Sales Dashboard with Power BI! 📊:")
                col34,col35 = st.columns((1,2))
                with col34:
                    st.video("ADDIDAS_SALES_VIDEO.mp4")
                with col35:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiNDA4ZDhjMGQtY2MxOS00MjUzLTlhY2ItM2IyYjhiZWJlMTNmIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - Created an interactive Power BI dashboard to analyze Adidas sales data, track revenue growth, and evaluate regional performance. Delivered data-driven insights into product sales, customer preferences, and market trends.
                    """)
                
                st.write("### 🚀 Toman Bike Shop Dashboard with Power BI! 📊:")
                col34,col35 = st.columns((1,2))
                with col34:
                    st.video("Toman_Bike_Shop.mp4")
                with col35:
                    st.markdown("[Visit Project](https://app.powerbi.com/view?r=eyJrIjoiOGNhZjBjZjYtYjQzOC00ZWJlLThlZDQtMjgyMjM0NTgxZjJjIiwidCI6IjI0MWNlN2VlLTVjYmUtNDczNi1hYWM0LWZkOWZmM2NjMWRkMSIsImMiOjl9)")
                    st.markdown("""
                    - Developed a comprehensive Power BI dashboard for Toman Bike Shop, analyzing sales performance, inventory levels, and customer preferences. Provided actionable insights to optimize product offerings and enhance operational efficiency.
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

                # Project : Customer Churn Prediction   
                st.write("## Customer Churn Prediction:")
                col31,col32 = st.columns((1,2))
                with col31:
                    st.image("CHURNN.png")
                with col32:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/Customer_Churn-Prediction)")
                    st.markdown("""
                        - This repository contains a Customer Churn Prediction project aimed at identifying customers likely to leave a business. The project leverages machine learning techniques to analyze customer behavior and predict churn, enabling data-driven decision-making. It includes data preprocessing, feature engineering, and model training using algorithms like Logistic Regression, Random Forest, and XGBoost. The repository provides a clear workflow, Python code, and visualizations to ensure reproducibility and understanding. This solution is particularly useful for businesses in improving customer retention strategies.
                        """)
                # Project : Movie Recommendation System 
                st.write("## Movie Recommendation System:")
                col27,col28 = st.columns((1,2))
                with col27:
                    st.image("Movie.png")
                with col28:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/Movie_Recommendation_System)")
                    st.markdown("""
                        - This repository showcases a Movie Recommendation System designed to suggest movies based on user preferences. The project employs content-based filtering techniques, utilizing features such as genres, cast, and keywords to recommend similar movies. It includes data preprocessing, feature extraction, and vectorization using TF-IDF and cosine similarity for recommendation generation. The repository provides Python code, detailed explanations, and visualizations to ensure clarity and usability. This system can be applied to enhance user experience in entertainment platforms.
                        """)
                # Project : Chest X-Ray 
                st.write("## Chest Xray Analysis:")
                col29,col30 = st.columns((1,2)) 
                with col29:
                    st.image("chestxray.png")
                with col30:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/Chest_Xray_Detection)")
                    st.markdown("""
                        - This repository contains a Chest X-ray Detection project aimed at diagnosing lung diseases such as pneumonia from chest X-ray images. The project leverages deep learning techniques, utilizing Convolutional Neural Networks (CNNs) for image classification. It includes steps such as data preprocessing, data augmentation, model training, and evaluation to ensure high accuracy. The repository provides well-structured Python code and visualizations for easy understanding and reproducibility. This solution has potential applications in healthcare for early disease detection and diagnosis.
                        """)
                    
            elif subcategory == "Data base & ETL Projects":
                st.write("## Data base & ETL Projects")

                st.write("### Data Warehousing with SQL Server")
                col41, col42 = st.columns((1, 2))
                with col41:
                    st.image("data_architecture.png")
                with col42:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/Sql-Data-Warehouse-Project)")
                    st.markdown("""
                        💡 **Project Highlights**:
                        ✅ Designed a Modern Data Warehouse with Medallion Architecture (Bronze, Silver, Gold layers)  
                        ✅ Built robust ETL pipelines to process sales data from ERP & CRM sources  
                        ✅ Implemented Data Modeling with Fact & Dimension tables for analytics  
                        ✅ Developed SQL-based business insights on Customer Behavior, Sales Trends & Product Performance  
                        ✅ Created clear documentation & architecture diagrams to guide stakeholders  
                    """)

                st.write("### Multi-Location Weather ETL Pipeline")
                col89,col90,col91 = st.columns((1,1,2))
                with col89:
                    st.image("Apache_Airflow1.png")
                with col90:
                    st.image("Apache_Airfloe2.png")
                with col91:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/Multi-Location-Weather-ETL-Pipeline#)")
                    st.markdown("""
                    - Developed an automated ETL pipeline using Apache Airflow to extract, transform, and load weather data from multiple geographic locations into a PostgreSQL database. The pipeline collects real-time weather data via APIs, processes and cleans it using Python (Pandas, NumPy), and loads it into a structured database for analysis. Scheduled daily DAG runs ensure timely updates, while logging and error-handling mechanisms help track failures and automate retries. The system improves data reliability and accessibility, supporting advanced analytics and reporting. Technologies used include Apache Airflow, PostgreSQL, Python, and SQL.
                    """)


            elif subcategory == "MLOPS PROJECT":
                st.write("## MLOPS PROJECT")

                st.write("## MLOps-based Airline Customer Analytics System")
                col33,col34 = st.columns((1,2))
                with col33:
                    st.video("AirlineMLOPS.mp4")
                with col34:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/MLOPS-PROJECT-AIRLINE)")
                    st.markdown("""
                        - This project is an MLOps-based Airline Customer Analytics System that streamlines data processing, model training, and deployment. It integrates data versioning (DVC) and CI/CD pipelines (Jenkins) to ensure robust model lifecycle management. The pipeline includes data ingestion, preprocessing, feature engineering, and model deployment using Docker for containerization. Custom exception handling, as shown in the image, enhances debugging by capturing and formatting detailed error messages. Logging and monitoring are incorporated using MLflow, enabling real-time tracking of model performance. The project ensures scalability and reproducibility, making it suitable for airline customer behavior analysis and predictive modeling. 🚀
                    """)

                st.write("## Vehicle Insurance Risk Prediction using MLOps")
                col33,col34 = st.columns((1,2))
                with col33:
                    st.image("MlopsVehicle.png")
                with col34:
                    st.markdown("[Visit Github Repo](https://github.com/AbdulSamad512/VEHICLE-INSURANCE-MLOPS-PROJECT1)")
                    st.markdown("""
                        - This project aims to automate the end-to-end machine learning lifecycle for vehicle insurance risk prediction using MLOps practices. The system leverages Python, Scikit-learn, and TensorFlow/PyTorch for building predictive models, along with Docker, Git, and CI/CD pipelines for deployment. The architecture follows a modular structure with components for data ingestion, validation, transformation, model training, evaluation, and deployment. The project utilizes FastAPI or Flask for serving the model, integrates Power BI for visualization, and employs Cloud platforms (AWS/Azure/GCP) for scalable deployment.
                                
                        💡 Key Tools & Technologies:
                        ✅ Machine Learning: Python, Pandas, NumPy, Scikit-learn, TensorFlow/PyTorch
                        ✅ MLOps: Docker, GitHub Actions, DVC, MLflow
                        ✅ Backend & Deployment: FastAPI/Flask, Kubernetes, Cloud Services
                        ✅ Data Processing: SQL, Power BI, Azure Data Factory
                        ✅ Automation: CI/CD Pipelines, Power Automate
                    """)


            else:
                st.write("Please select a valid project category.")     
           
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
    st.download_button(label="📄 Download my CV", data=pdf_bytes, file_name="DSCV.pdf", mime="application/pdf")
    st.write("##")
    st.write(f"""<div class="subtitle" style="text-align: center;">🌟 Have A Wonderful Day!!! 🌟</div>""", unsafe_allow_html=True)

if __name__ == "__main__":
    web_portfolio()
