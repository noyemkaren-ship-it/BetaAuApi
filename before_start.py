from base import Base, engine
from repository.User import UserRepository
from repository.Lesson import LessonRepository
from schemas.lesson import LessonSchema
from models import *
from utils.before_start.create_all_french_lessons import *
from utils.before_start.english import *
from utils.before_start.metall_data import *

Base.metadata.create_all(engine)

LessonRepository.create_new(LessonSchema(
    title="Приветствие и знакомство",
    html_code=LESSON_1_HTML,
    subs=1,
    subject="french",
    xp=5,
))
LessonRepository.create_new(LessonSchema(
    title="Местоимения и глаголы",
    html_code=LESSON_2_HTML,
    subs=2,
    subject="french",
    xp=10,
))
LessonRepository.create_new(LessonSchema(
    title="Существительные и контрольная",
    html_code=LESSON_3_HTML,
    subs=3,
    subject="french",
    xp=15,
))
LessonRepository.create_new(LessonSchema(
    title="Числа, дни недели и время",
    html_code=LESSON_4_HTML,
    subs=4,
    subject="french",
    xp=20,
))
LessonRepository.create_new(LessonSchema(
    title="Вопросы и отрицания",
    html_code=LESSON_5_HTML,
    subs=5,
    subject="french",
    xp=25,
))
LessonRepository.create_new(LessonSchema(
    title="Passé composé — прошедшее время",
    html_code=LESSON_6_HTML,
    subs=6,
    subject="french",
    xp=30,
))
LessonRepository.create_new(LessonSchema(
    title="Futur — будущее время",
    html_code=LESSON_7_HTML,
    subs=7,
    subject="french",
    xp=35,
))
LessonRepository.create_new(LessonSchema(
    title="Модальные глаголы",
    html_code=LESSON_8_HTML,
    subs=8,
    subject="french",
    xp=40,
))
LessonRepository.create_new(LessonSchema(
    title="Возвратные глаголы",
    html_code=LESSON_9_HTML,
    subs=9,
    subject="french",
    xp=45,
))
LessonRepository.create_new(LessonSchema(
    title="Практика и итоговая контрольная",
    html_code=LESSON_10_HTML,
    subs=10,
    subject="french",
    xp=50,
))
LessonRepository.create_new(LessonSchema(
    title="Введение в алхимию и базовую химию",
    html_code=METTAL_FIRST_LESSON,
    subs=1,
    subject="metall",
    xp=5,
))
LessonRepository.create_new(LessonSchema(
    title="Атомы и их устройство",
    html_code=METTAL_SECOND_LESSON,
    subs=2,
    subject="metall",
    xp=10,
))
LessonRepository.create_new(LessonSchema(
    title="Соединения металлов и сплавы",
    html_code=METTAL_THIRD_LESSON,
    subs=3,
    subject="metall",
    xp=15,
))
LessonRepository.create_new(LessonSchema(
    title="Свойства и соединения металлов",
    html_code=METTAL_FOURTH_LESSON,
    subs=4,
    subject="metall",
    xp=20,
))
LessonRepository.create_new(LessonSchema(
    title="Плавка металлов и получение золота",
    html_code=METTAL_FIFTH_LESSON,
    subs=5,
    subject="metall",
    xp=25,
))
LessonRepository.create_new(LessonSchema(
    title="Основы алхимии: Великое Делание",
    html_code=METTAL_SIXTH_LESSON,
    subs=6,
    subject="metall",
    xp=30,
))
LessonRepository.create_new(LessonSchema(
    title="Практическая алхимия: лаборатория",
    html_code=METTAL_SEVENTH_LESSON,
    subs=7,
    subject="metall",
    xp=35,
))
LessonRepository.create_new(LessonSchema(
    title="Алхимический символизм",
    html_code=METTAL_EIGHTH_LESSON,
    subs=8,
    subject="metall",
    xp=40,
))
LessonRepository.create_new(LessonSchema(
    title="Великие алхимики и их наследие",
    html_code=METTAL_NINTH_LESSON,
    subs=9,
    subject="metall",
    xp=45,
))
LessonRepository.create_new(LessonSchema(
    title="Алхимия сегодня: от магии к науке",
    html_code=METTAL_TENTH_LESSON,
    subs=10,
    subject="metall",
    xp=50,
))
LESSONS = [
    ("Greetings and Introductions",          ENGLISH_FIRST_LESSON),
    ("Pronouns and the verb to be",          ENGLISH_SECOND_LESSON),
    ("Nouns and Articles",                   ENGLISH_THIRD_LESSON),
    ("Numbers, Days and Time",               ENGLISH_FOURTH_LESSON),
    ("Questions and Negations",              ENGLISH_FIFTH_LESSON),
    ("Present Simple",                       ENGLISH_SIXTH_LESSON),
    ("Past Simple",                          ENGLISH_SEVENTH_LESSON),
    ("Future Simple",                        ENGLISH_EIGHTH_LESSON),
    ("Modal Verbs",                          ENGLISH_NINTH_LESSON),
    ("Practice and Final Test",              ENGLISH_TENTH_LESSON),
]

for i, (title, html) in enumerate(LESSONS, start=1):
    LessonRepository.create_new(LessonSchema(
        title=title,
        html_code=html,
        subs=i,
        subject="english",
        xp=i * 3,
    ))

password = str(input("Введите пароль админа: "))

UserRepository.create(
    name="admin",
    email="noyemkaren@gmail.com",
    phone="+79060122100",
    password=password,
    is_admin=True
)

