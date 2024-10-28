import openai
import json
import streamlit as st
from langchain.llms import OpenAIChat
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI
from langchain_core.documents import Document
import os
import time
import re

st.markdown(
    """
    <style>
    .jazzee-title {
                    display: inline;
                    background: linear-gradient(93.59deg, orange 3.13%, #f6be58 85.77%);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-size: 1em;
                    font-weight: bold;
    }
    </style>
    """, 
    unsafe_allow_html=True
)
st.markdown('<h1><span class="jazzee-title">Jazzee</span> Assist</h1>', unsafe_allow_html=True)
waste=st.text_input("Product/Category:",placeholder="eg: JAMF")
specific=st.text_input("Specific Feature:", placeholder="eg: Device Management",value="")
company_name = st.text_input("Company:", placeholder="eg: www.greenlight.com",value="")
domain=st.text_input("Sector:", placeholder="eg: Fintech",value="")
company_size = st.selectbox(
    "Number Of Employees:",
    ["", "1-100", "101-1000", "1000+"],
    format_func=lambda x: "Select" if x == "" else str(x)
)
role=st.text_input("Your Role:", placeholder="eg: IT Manager",value="")




# st.subheader("💬 **Suggested Queries**")
# # Initialize session states for each button to track if they were clicked
# if "review_buttons" not in st.session_state:
#     st.session_state.review_buttons = {
#         "IT Manager for JAMF": False,
#         "Marketing Head for Mixpanel": False,
#         "CISO for Vanta Software": False,
#         "CTO for New Relic": False,
#     }

# if "fetch_button_clicked" not in st.session_state:
#     st.session_state.fetch_button_clicked = False

# # Function to mark a specific review button as clicked
# def set_review_button_red(button_name):
#     st.session_state.review_buttons[button_name] = True

# # CSS to ensure consistent button size across all buttons
# button_css = """
# <style>
# button {
#     width: 100%;  /* Make the button take full width of the column */
#     height: 50px;
#     font-size: 16px;
#     border-radius: 8px;
#     border: 2px solid red;
#     cursor: pointer;
#     color: black;
#     transition: 0s;
# }

# button:hover {
#     background-color: white;
#     color: white;
# }
# </style>
# """
# # Inject CSS into the app
# st.markdown(button_css, unsafe_allow_html=True)

# # Create four columns (one for each button) to align them horizontally
# cols = st.columns(len(st.session_state.review_buttons))

# # Display the buttons in their respective columns
# for (button_name, clicked), col in zip(st.session_state.review_buttons.items(), cols):
#     with col:
#         if clicked:
#             # Render as a red-styled HTML button
#             st.markdown(f'<button>{button_name}</button>', unsafe_allow_html=True)
#         else:
#             # Render a Streamlit button and set it as clicked when pressed
#             if st.button(button_name, key=button_name, on_click=set_review_button_red, args=(button_name,)):
#                 st.session_state.review_buttons[button_name] = True

def read_json_file(file_path):
    """Read the input JSON file and return its contents."""
    with open(file_path, 'r',encoding='utf-8') as f:
        return json.load(f)

def linkify_numbers(numbers):
    return ", ".join([f"[{num}](#{num})" for num in numbers])

if st.button("Fetch the relevant reviews"):
    with st.spinner('⏳ Fetching reviews matching the profile'):
        time.sleep(5)
    st.markdown("""
##### Fitment Rating: 8/10""")
    st.markdown(f'<a name="{0}"></a>', unsafe_allow_html=True)  # Create an anchor for each review
    with st.expander("##### Rationale for the Rating:"):
        st.markdown("""
    Jamf is a powerful MDM solution for managing Apple devices, offering extensive features and strong integration capabilities. However, its steep learning curve, inconsistent support, and scalability issues may pose challenges for larger organizations or those with complex compliance needs. While it excels in remote management and security, potential customers should weigh these pros and cons against their specific organizational requirements and consider the competitive landscape before making a decision.
    """)
    
    
    col1, col2 = st.columns(2)
    
    with col1:
        # st.markdown(f"""
        #                 **Pros**
        #     - **Comprehensive Apple Device Management** {linkify_numbers([1, 3, 8])}.
        #     - **High Reliability in Large-Scale Environments** {linkify_numbers([4, 5, 8])}.
        #     - **Strong Customer Support and Community** {linkify_numbers([6, 12, 36])}
        #     - **Efficient Zero-Touch Deployment** {linkify_numbers([1, 4, 6])}.
        #     - **Integrated Security Features** {linkify_numbers([3, 5, 11])}.
        #     """)
        # Displaying each "Pro" point separately in green
        # st.markdown("<span style='color: green; font-weight: bold;'>**Pros**</span>", unsafe_allow_html=True)
        # st.markdown(f"<span style='color: green;'>- **Comprehensive Apple Device Management** {linkify_numbers([1, 3, 8])}</span>", unsafe_allow_html=True)
        # st.markdown(f"<span style='color: green;'>- **High Reliability in Large-Scale Environments** {linkify_numbers([4, 5, 8])}</span>", unsafe_allow_html=True)
        # st.markdown(f"<span style='color: green;'>- **Strong Customer Support and Community** {linkify_numbers([6, 12, 36])}</span>", unsafe_allow_html=True)
        # st.markdown(f"<span style='color: green;'>- **Efficient Zero-Touch Deployment** {linkify_numbers([1, 4, 6])}</span>", unsafe_allow_html=True)
        # st.markdown(f"<span style='color: green;'>- **Integrated Security Features** {linkify_numbers([3, 5, 11])}</span>", unsafe_allow_html=True)
        
        # Summaries for each reference link
        summaries = {
            1: "This review highlights the ease of use and comprehensive management features.",
            3: "Focuses on the seamless integration with other Apple services.",
            4: "Points out the reliability and scalability for enterprise environments.",
            5: "Describes the robustness of the system under large-scale use.",
            6: "Praised for its responsive customer support and active community.",
            8: "Mentions the intuitive interface for Apple device management.",
            11: "Details the integrated security features and compliance support.",
            12: "Highlights the active user community and shared resources.",
            36: "Discusses the comprehensive documentation and support network."
        }
        
        st.markdown("<span style='color: green; font-weight: bold;'>**Pros**</span>", unsafe_allow_html=True)
        
        # List of pros with reference links
        pros = [
            ("Comprehensive Apple Device Management", [1, 3, 8]),
            ("High Reliability in Large-Scale Environments", [4, 5, 8]),
            ("Strong Customer Support and Community", [6, 12, 36]),
            ("Efficient Zero-Touch Deployment", [1, 4, 6]),
            ("Integrated Security Features", [3, 5, 11]),
        ]
        
        # Display each pro in an expander with reference summaries
        for pro, refs in pros:
            with st.expander(f"**{pro}** {linkify_numbers(refs)}"):
                for ref in refs:
                    st.markdown(f"- {summaries.get(ref, 'No summary available')}")

    with col2:
        # st.markdown(f"""
        #                 **Cons**
        #     - **Steep Learning Curve** {linkify_numbers([3, 12, 18])}.
        #     - **High Cost for Advanced Features** {linkify_numbers([1, 6, 15])}.
        #     - **Outdated User Interface** {linkify_numbers([5, 12, 25])}.
        #     - **Inconsistent Patch Management** {linkify_numbers([2, 16, 24])}.
        #     - **Limited Remote Assistance Capabilities** {linkify_numbers([15, 16, 29])}.
        #     """)
        # Displaying each "Con" point separately in red
        st.markdown("<span style='color: red; font-weight: bold;'>**Cons**</span>", unsafe_allow_html=True)
        st.markdown(f"<span style='color: red;'>- **Steep Learning Curve** {linkify_numbers([3, 12, 18])}</span>", unsafe_allow_html=True)
        st.markdown(f"<span style='color: red;'>- **High Cost for Advanced Features** {linkify_numbers([1, 6, 15])}</span>", unsafe_allow_html=True)
        st.markdown(f"<span style='color: red;'>- **Outdated User Interface** {linkify_numbers([5, 12, 25])}</span>", unsafe_allow_html=True)
        st.markdown(f"<span style='color: red;'>- **Inconsistent Patch Management** {linkify_numbers([2, 16, 24])}</span>", unsafe_allow_html=True)
        st.markdown(f"<span style='color: red;'>- **Limited Remote Assistance Capabilities** {linkify_numbers([15, 16, 29])}</span>", unsafe_allow_html=True)



    st.markdown("______________________")
    st.header("Reviews that matches your profile")
    st.markdown("______________________")
    with open("final_clean_rev.json", "r") as json_file:
        file = json.load(json_file)
    for idx, elem in enumerate(file):
        flag=0
        if elem['useful'] == '0' and elem['customer_useful'] == '0':  # Display reviews marked as '0'
            st.markdown(f'<a name="{idx+1}"></a>', unsafe_allow_html=True)  # Create an anchor for each review
        if elem['body']=="":
            flag=1
        if 'title' in elem and flag==0:
            st.subheader(elem['title'])
        if 'platform' in elem:
            if 'upvotes' in elem:
                st.markdown(f"Platform : {elem['platform']} | {elem['created'].split()[0]} | [Open Review]({elem['url']}) | Upvotes : {elem['upvotes']} | [Go Back](#{0})")
            else:
                st.markdown(f"Platform : {elem['platform']} | [Open Review]({elem['url']}) | [Go Back](#{0})")
        else:   
            st.markdown(f"Platform : Reddit/{elem['subreddit']} | {elem['created'].split()[0]} | [Open Review]({elem['url']}) | Upvotes : {elem['upvotes']} | [Go Back](#{0})")
        sample_para=elem['body']
        if flag==1:
            sample_para=elem['title']
        para = sample_para.replace('\n', '<br>')
        if elem['sentiment']=='2':
            st.markdown(
                            f"""
                            <div style="background-color: #d4edda; padding: 10px; border-radius: 5px; margin-bottom: 15px;">
                                <p style="color: #155724; font-size: 16px; margin: 0;">{elem['summary']}</p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
            with st.expander("View Full Review"):
                st.markdown(
                            f"""
                            <div style="background-color: #d4edda; padding: 10px; border-radius: 5px; margin-bottom: 15px;">
                                <p style="color: #155724; font-size: 16px; margin: 0;">{para}</p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
        elif elem['sentiment']=='4':
            st.markdown(
                            f"""
                            <div style="background-color: #cce5ff; padding: 10px; border-radius: 5px;">
                                <p style="color: #004085; font-size: 16px;">{elem['summary']}</p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
            with st.expander("View Full Review"):
                st.markdown(
                            f"""
                            <div style="background-color: #cce5ff; padding: 10px; border-radius: 5px;">
                                <p style="color: #004085; font-size: 16px;">{para}</p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
        else:
            st.markdown(
                            f"""
                            <div style="background-color: #f8d7da; padding: 10px; border-radius: 5px;">
                                <p style="color: #721c24; font-size: 16px;">{elem['summary']}</p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
            with st.expander("View Full Review"):
                st.markdown(
                            f"""
                            <div style="background-color: #f8d7da; padding: 10px; border-radius: 5px;">
                                <p style="color: #721c24; font-size: 16px;">{para}</p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
        st.markdown("**********")
