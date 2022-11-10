from behave import *
from quiz_game import QuizGame, QuizAPI, QUIZ_URL, ConsolePlayer, BaseAPI, Question, Answer

# Vi behöver
# Kunna skapa ett quiz-program
# Styra över vilka frågor det har
# Syra över vilka svar som är korrekt på en fråga
# Kontrollera vad som skrivs ut på terminalen


class TestAPI(BaseAPI):
    questions: list[Question]

    def __init__(self):
        self.questions = []

    def get_questions(self) -> list[Question]:
        return self.questions

    def post_answer(self, question: Question, correct: bool):
        pass


@given(u'A quiz program')
def step_impl(context):
    context.quiz_api = TestAPI()
    context.quiz_player = ConsolePlayer()
    context.quiz_game = QuizGame(context.quiz_api, context.quiz_player)


@given(u'There is one question')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given There is one question')


@given(u'Answer 1 is correct')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Answer 1 is correct')


@when(u'The user answers 1')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The user answers 1')


@when(u'The program is run')
def step_impl(context):
    raise NotImplementedError(u'STEP: When The program is run')


@then(u'The result should be 1 of 1 questions correct')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The result should be 1 of 1 questions correct')
