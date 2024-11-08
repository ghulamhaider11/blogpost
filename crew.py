#__import__('pysqlite3')
#import sys
#sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
#import sqlite3

import streamlit as st
from crewai import Crew
from agents import planner, writer, editor, industry_analyst, copywriter  # Import copywriter
from tasks import plan, write, edit, industry_analysis  # Basic tasks
from tasks import social_media_copy, headline_tagline, email_copy  # Copywriting tasks

# Define custom tasks for specific copy types
sales_copy_task = Task(
    description="Create persuasive sales copy for {topic} that targets the buyer’s needs and emphasizes benefits.",
    expected_output="Sales copy that includes a headline, benefits section, and a call-to-action.",
    agent=copywriter
)

ad_copy_task = Task(
    description="Write a compelling ad copy for {topic} that is short, impactful, and suitable for digital ads.",
    expected_output="Ad copy with a catchy headline, main message, and call-to-action.",
    agent=copywriter
)

email_copy_task = Task(
    description="Craft a promotional email for {topic} that is engaging, includes key information, and prompts the reader to take action.",
    expected_output="Email copy with a subject line, greeting, main content, and call-to-action.",
    agent=copywriter
)

# Create a Streamlit interface
def main():
    st.title("Multi-Agent Workflow with CrewAI and Groq")

    # Display introductory text
    st.markdown("""
    **CHATGROQ API USING OPEN SOURCE MODEL BY META : "llama3-70b-8192"**
    """)

    # Text input for the topic
    topic = st.text_input("Enter a topic for the AI crew", "")

    # Button to generate a blog
    if st.button("Generate blog"):
        with st.spinner('Generating blog content...'):
            try:
                # Initialize the crew with blog-related agents and tasks
                crew = Crew(
                    agents=[planner, writer, editor],
                    tasks=[plan, write, edit],
                    verbose=2
                )

                # Kick off the crew with the input topic
                result = crew.kickoff(inputs={"topic": topic})
                st.markdown(result, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"An error occurred: {e}")

    # Radio button selection for copy type
    copy_type = st.radio(
        "Select the type of copy you want to generate:",
        ("Sales Copy", "Ad Copy", "Email Copy")
    )

    # Button for additional copywriting tasks
    if st.button("Generate copywriting materials"):
        with st.spinner(f'Generating {copy_type}...'):
            try:
                # Choose the task based on user selection
                if copy_type == "Sales Copy":
                    selected_task = sales_copy_task
                elif copy_type == "Ad Copy":
                    selected_task = ad_copy_task
                else:
                    selected_task = email_copy_task

                # Initialize the crew with the copywriter agent and selected task
                crew_copywriter = Crew(
                    agents=[copywriter],
                    tasks=[selected_task],
                    verbose=2
                )

                # Kick off the selected copywriting task with the input topic
                copywriting_result = crew_copywriter.kickoff(inputs={"topic": topic})
                st.markdown(copywriting_result, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
