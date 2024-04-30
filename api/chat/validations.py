from pydantic import BaseModel


class AskQuestionSchema(BaseModel):
    question: str
    w2_form_id: int
    gpt_thread_id: str
    gpt_assistant_id: str
