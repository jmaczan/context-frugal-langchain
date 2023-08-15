from langchain.memory import ConversationSummaryMemory
from langchain.llms import OpenAI
import dotenv
dotenv.load_dotenv()


llm = OpenAI(temperature=0)
memory = ConversationSummaryMemory(llm=llm)
memory.save_context({"input": "hi"}, {"output": "whats up"})
memory.save_context({"input": "im working on better docs for chatbots"}, {
                    "output": "oh, that sounds like a lot of work"})
memory.save_context({"input": "yes, but it's worth the effort"}, {
                    "output": "agreed, good docs are important!"})
memory.load_memory_variables({})
print(memory)