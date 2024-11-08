from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq

llm = ChatGroq(temperature=0,
               model_name="llama3-70b-8192",
               api_key='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')

planner = Agent(
    llm=llm,  # LLM model you are using
    role="content planner",  # Define the role
    goal="Plan engaging and factually accurate content on {topic}",  # Set the goal
    backstory=(
        "You're working on planning a blog article "
        "about the topic: {topic}. "
        "You collect information that helps the "
        "audience learn something and make informed decisions. "
        "Your work is the basis for the Content Writer to write an article on this topic."
    ),  # Backstory that sets the context
    verbose=True,  # Enable verbose mode for detailed output
    allow_delegation=False  # Disable delegation of tasks
)
#
writer = Agent(
    llm=llm,
    role="Content Writer",
    goal="Write insightful and factually accurate "
         "opinion piece about the topic: {topic}",
    backstory="You're working on a writing "
              "a new opinion piece about the topic: {topic}. "
              "You base your writing on the work of "
              "the Content Planner, who provides an outline "
              "and relevant context about the topic. "
              "You follow the main objectives and "
              "direction of the outline, "
              "as provide by the Content Planner. "
              "You also provide objective and impartial insights "
              "and back them up with information "
              "provide by the Content Planner. "
              "You acknowledge in your opinion piece "
              "when your statements are opinions "
              "as opposed to objective statements.",
    allow_delegation=False,
    verbose=True
)

editor = Agent(
    llm=llm,    
    role="Editor",
    goal="Edit a given blog post to align with "
         "the writing style of the organization. ",
    backstory="You are an editor who receives a blog post "
              "from the Content Writer. "
              "Your goal is to review the blog post "
              "to ensure that it follows journalistic best practices,"
              "provides balanced viewpoints "
              "when providing opinions or assertions, "
              "and also avoids major controversial topics "
              "or opinions when possible.",
    allow_delegation=False,
    verbose=True
)

# Define the industry-focused agent
industry_analyst = Agent(
    llm=llm,  
    role="Industry Analyst",  # Define the role
    goal="Provide the latest industry insights and trends on {topic}",  # Set the goal
    backstory=(
        "You're working as an industry analyst focusing on {topic}. "
        "Your role is to provide the latest information on industry trends, "
        "emerging technologies, competitor strategies, and relevant news that can impact the content. "
        "You provide data, analyses, and well-rounded insights to help the team stay up-to-date with industry developments."
    ),
    verbose=True,  # Enable verbose mode for detailed output
    allow_delegation=False  # Disable delegation of tasks
)
# Define the Copywriter agent
copywriter = Agent(
    llm=llm,
    role="Copywriter",
    goal="Generate captivating and persuasive copy on {topic} for different formats (headline, tagline, social media, etc.)",
    backstory=(
        "You are a skilled copywriter tasked with creating short, impactful copy "
        "that highlights the key messages in a memorable and engaging way. "
        "Your work is used for headlines, social media posts, and promotional material "
        "to draw in readers and increase engagement."
    ),
    verbose=True,
    allow_delegation=False
)