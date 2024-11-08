
from crewai import Task
from agents import planner,writer,editor, industry_analyst,copywriter


plan = Task(
    description=(
        "1. Prioritize the latest trends, key players, "
            "and noteworthy news on {topic}.\n"
        "2. Identify the target audience, considering "
            "their interests and pain points.\n"
        "3. Develop a detailed content outline including "
            "an introduction, key points, and a call to action.\n"
        "4. Include SEO keywords and relevant data or sources."
    ),
    expected_output="A comprehensive content plan document "
        "with an outline, audience analysis, "
        "SEO keywords, and resources.",
    agent=planner,
)

write = Task(
    description=(
        "1. Use the content plan to craft a compelling "
            "blog post on {topic}.\n"
        "2. Incorporate SEO keywords naturally.\n"
  "3. Sections/Subtitles are properly named "
            "in an engaging manner.\n"
        "4. Ensure the post is structured with an "
            "engaging introduction, insightful body, "
            "and a summarizing conclusion.\n"
        "5. Proofread for grammatical errors and "
            "alignment with the brand's voice.\n"
    ),
    expected_output="A well-written blog post "
        "in markdown format, ready for publication, "
        "each section should have 2 or 3 paragraphs.",
    agent=writer,
)

edit = Task(
    description=("Proofread the given blog post for "
                 "grammatical errors and "
                 "alignment with the brand's voice."),
    expected_output="A well-written blog post in markdown format, "
                    "ready for publication, "
                    "each section should have 2 or 3 paragraphs.",
    agent=editor
)

# Task for the Industry Analyst to cover latest industry topics
industry_analysis = Task(
    description=(
        "1. Research and summarize the latest industry trends, innovations, and news on {topic}.\n"
        "2. Identify key players, new technologies, and recent changes impacting the industry.\n"
        "3. Highlight relevant statistics, case studies, or examples to support analysis.\n"
        "4. Provide context on how these developments may affect the target audience."
    ),
    expected_output="A concise industry analysis document summarizing recent trends, key players, "
                    "and their potential impact on {topic}.",
    agent=industry_analyst
)

# Task to create social media posts
social_media_copy = Task(
    description=(
        "1. Create concise and engaging social media posts based on the blog article on {topic}.\n"
        "2. Include relevant hashtags and a call-to-action to drive engagement.\n"
        "3. Adjust tone and style for each platform (e.g., Twitter, LinkedIn)."
    ),
    expected_output="A series of social media posts tailored for different platforms (Twitter, LinkedIn, etc.).",
    agent=copywriter
)

# Task for headline and tagline options
headline_tagline = Task(
    description=(
        "1. Generate a list of compelling headline options for the blog article on {topic}.\n"
        "2. Create 2-3 taglines that succinctly capture the essence of the article.\n"
        "3. Ensure each option aligns with the brand’s tone and engages the target audience."
    ),
    expected_output="A list of 5-10 headlines and 2-3 taglines for the article on {topic}.",
    agent=copywriter
)

# Task for email marketing copy
email_copy = Task(
    description=(
        "1. Write a brief and engaging email promoting the blog post on {topic}.\n"
        "2. Include a compelling introduction, key points, and a call-to-action.\n"
        "3. Use a friendly and persuasive tone to encourage readers to click and read more."
    ),
    expected_output="An email draft that introduces the blog post, highlights key points, and encourages readers to engage.",
    agent=copywriter
)