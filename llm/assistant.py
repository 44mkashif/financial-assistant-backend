import os
import openai
import traceback
from urllib.parse import urlparse

from config import Config
from constants import PROMPT_TEMPLATE

class Assistant:
    def __init__(self):
        self.client = openai.OpenAI()

    def create_assistant(self, w2_data):
        prompt = PROMPT_TEMPLATE.format(w2_data=w2_data)
        return self.client.beta.assistants.create(
            instructions=prompt,
            model=Config.MODEL_NAME,
            name="Financial Assistant",
        )

    def create_thread(self):
        return self.client.beta.threads.create()
    
    def retrieve_thread(self, gpt_thread_id):
        return self.client.beta.threads.retrieve(gpt_thread_id)
    
    def retrieve_thread_messages(self, gpt_thread_id):
        return self.client.beta.threads.messages.list(thread_id=gpt_thread_id)

    def answer_question(
        self, question, gpt_assistant_id, gpt_thread_id
    ):
        self.client.beta.threads.messages.create(
            thread_id=gpt_thread_id,
            role="user",
            content=question
        )
        run = self.client.beta.threads.runs.create(
            thread_id=gpt_thread_id,
            assistant_id=gpt_assistant_id
        )

        while run.status not in ["completed", "failed"]:
            run = self.client.beta.threads.runs.retrieve(
                thread_id=gpt_thread_id, run_id=run.id
            )

        messages = self.client.beta.threads.messages.list(
            thread_id=gpt_thread_id
        )
        return messages

