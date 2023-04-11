import io

from dmoj.result import CheckerResult

VALID_ANSWERS = (
    'NO',
    'YES',
)

EPSILON = 1e-6

def check(process_output, judge_output, **kwargs):
    judge_output = io.StringIO(judge_output.decode('utf-8'))
    expected_answers = [line.strip() for line in judge_output]

    process_output = io.StringIO(process_output.decode('utf-8'))
    answers = [line.strip() for line in process_output]

    expected_answers_index = 0
    answers_index = 0
    while expected_answers_index < len(expected_answers):
        expected_answer = expected_answers[expected_answers_index]
        expected_answers_index += 1

        if len(answers) < answers_index + 1:
            return CheckerResult(False, 0, 'output too short, expected more lines')

        answer = answers[answers_index]

        if answer not in VALID_ANSWERS:
            return CheckerResult(False, 0, f'line {answers_index + 1}: expected line with "YES" or "NO"')

        answers_index += 1

        if expected_answer != answer:
            return CheckerResult(False, 0, f'line {answers_index + 1}: expected "{expected_answer}", got "{answer}"')

        if expected_answer == 'YES':
            expected_area = float(expected_answers[expected_answers_index])
            expected_answers_index += 1

            if len(answers) < answers_index + 1:
                return CheckerResult(False, 0, 'expected line with area of interesting rectangle')

            answer = answers[answers_index]
            try:
                area = float(answer)
            except ValueError:
                return CheckerResult(False, 0, f'line {answers_index + 1}: could not convert value "{answer}" to a float')

            answers_index += 1

            if abs(area - expected_area) > EPSILON:
                return CheckerResult(False, 0, f'line {answers_index + 1}: output area different from expected area')

    return True
