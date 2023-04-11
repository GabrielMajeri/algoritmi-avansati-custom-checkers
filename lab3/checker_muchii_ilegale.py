import io

from dmoj.result import CheckerResult

VALID_ANSWERS = (
    'LEGAL',
    'ILLEGAL',
)

def check(process_output, judge_output, **kwargs):
    judge_output = io.StringIO(judge_output.decode('utf-8'))
    expected_answers = [line.strip() for line in judge_output]
    first_expected_answer = expected_answers[0][3:].strip()
    second_expected_answer = expected_answers[1][3:].strip()

    process_output = io.StringIO(process_output.decode('utf-8'))
    answers = [line.strip() for line in process_output]

    # See how many lines the output has
    if len(answers) != 2:
        return CheckerResult(False, 0, f'expected 2 output lines, got {len(answers)}')

    line = answers[0]
    segment = line[:3]
    if segment != 'AC:':
        return CheckerResult(False, 0, "first line should start with the string 'AC:'")

    answer = line[3:].strip()
    if answer not in VALID_ANSWERS:
        return CheckerResult(False, 0, f"edge type must be 'LEGAL' or 'ILLEGAL'")

    if first_expected_answer != answer:
        return CheckerResult(False, 0, f"expected '{first_expected_answer}' for first edge")

    line = answers[1]
    segment = line[:3]
    if segment != 'BD:':
        return CheckerResult(False, 0, "second line should start with the string 'BD:'")

    answer = line[3:].strip()
    if answer not in VALID_ANSWERS:
        return CheckerResult(False, 0, f"edge type must be 'LEGAL' or 'ILLEGAL'")

    if second_expected_answer != answer:
        return CheckerResult(False, 0, f"expected answer '{second_expected_answer}' for second edge")

    return True
