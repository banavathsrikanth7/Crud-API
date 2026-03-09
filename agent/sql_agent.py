from langchain_community.utilities import SQLDatabase
from langchain.agents import create_sql_agent
from langchain_openai import ChatOpenAI
from langchain.agents.agent_toolkits import SQLDatabaseToolkit

db = SQLDatabase.from_uri(
    "postgresql://postgres:password@localhost:5432/video_db"
)

llm = ChatOpenAI()

toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)

agent.run("Show all videos")