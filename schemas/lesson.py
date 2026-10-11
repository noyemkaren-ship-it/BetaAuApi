import pydantic

class LessonSchema(pydantic.BaseModel):
    title: str
    html_code: str
    subs: int
    subject: str
    xp: float