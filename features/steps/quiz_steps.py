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

    def print_questions(self):
        print("-"*80)
        for q in self.questions:
            print(q.prompt)
            for a in q.answers:
                print(a.answer, a.correct)
        print("-" * 80)


class TestPlayer(Player):
    last_message: str
    next_answer: list[int]

    def __init__(self):
        self.next_answer = []

    def ask_num(self, n: int) -> int:
        return self.next_answer.pop(0)

    def add_answer(self, n: int):
        self.next_answer.append(n)

    def send_message(self, message: str):
        self.last_message = message


@given(u'A quiz program')
def step_impl(context):
    context.quiz_api = TestAPI()
    context.quiz_player = TestPlayer()
    context.quiz_game = QuizGame(context.quiz_api, context.quiz_player)


@given(u'a question "{prompt}"')
def step_impl(context, prompt):
    answers = []
    for row in context.table:
        answer = row['answer']
        correct = True if row['correct'] == 'True' else False
        answers.append(Answer(answer, correct))
    context.quiz_api.questions.append(Question(1, prompt, 10, 5, answers))


@given(u'There is one question')
def step_impl(context):
    context.question = Question(1, "", 0, 0, [])
    context.quiz_api.questions.append(context.question)


@given(u'Answer 1 is correct')
def step_impl(context):
    context.answer = Answer("", True)
    context.question.answers.append(context.answer)


@when(u'The user answers {ans}')
def step_impl(context, ans):
    context.quiz_player.add_answer(int(ans))


@when(u'The program is run')
def step_impl(context):
    context.quiz_game.run()


@then(u'The result should be {expected_result}')
def step_impl(context, expected_result):
    assert context.quiz_player.last_message == expected_result, f"got {context.quiz_player.last_message}"

