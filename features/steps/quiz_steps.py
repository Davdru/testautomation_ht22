from behave import *
from quiz_game import QuizGame, QuizAPI, QUIZ_URL, ConsolePlayer, BaseAPI, Question, Answer, Player

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


class TestPlayer(Player):
    last_message: str

    def ask_num(self, n: int) -> int:
        return 1

    def send_message(self, message: str):
        self.last_message = message


@given(u'A quiz program')
def step_impl(context):
    context.quiz_api = TestAPI()
    context.quiz_player = TestPlayer()
    context.quiz_game = QuizGame(context.quiz_api, context.quiz_player)


@given(u'There is one question')
def step_impl(context):
    context.question = Question(1, "", 0, 0, [])
    context.quiz_api.questions.append(context.question)


@given(u'Answer 1 is correct')
def step_impl(context):
    context.answer = Answer("", True)
    context.question.answers.append(context.answer)


@when(u'The user answers 1')
def step_impl(context):
    pass


@when(u'The program is run')
def step_impl(context):
    context.quiz_game.run()


@then(u'The result should be You answered 1 of 1 correct!')
def step_impl(context):
    assert context.quiz_player.last_message == "You answered 1 of 1 correct!", f"got {context.quiz_player.last_message}"
