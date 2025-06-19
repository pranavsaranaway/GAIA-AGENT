from smolagents import CodeAgent, OpenAIServerModel
from tools import youtube_video_analyzer, search_tool, string_reversal_tool, file_format_handler, wiki_search, python_interpreter_tool, calc_square_integers
from dotenv import load_dotenv
import os

load_dotenv()
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")


agent = CodeAgent(
    model = OpenAIServerModel(model_id="gpt-4o"),
    tools =[youtube_video_analyzer, search_tool, string_reversal_tool, file_format_handler, wiki_search, python_interpreter_tool, calc_square_integers],
    add_base_tools = True,
    additional_authorized_imports=['pandas', 'cv2', 'numpy', 'requests', 'csv']
)

agent.run('How many studio albums were published by Mercedes Sosa between 2000 and 2009 (included)? You can use the latest 2022 version of english wikipedia.')