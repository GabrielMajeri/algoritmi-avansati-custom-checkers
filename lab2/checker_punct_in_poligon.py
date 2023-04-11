import io

from dmoj.result import CheckerResult

VALID_ANSWERS = (
    'INSIDE',
    'OUTSIDE',
    'BOUNDARY',
)

def check(process_output, judge_output, **kwargs):
    judge_output = io.StringIO(judge_output.decode('utf-8'))
    expected_answers = [line.strip() for line in judge_output]

    process_output = io.StringIO(process_output.decode('utf-8'))
    answers = [line.strip() for line in process_output]

    # See how many lines the output has
    if len(expected_answers) != len(answers):
        return CheckerResult(False, 0, f'expected {len(expected_answers)} output lines, got {len(answers)}')

    for idx, (expected_answer, answer) in enumerate(zip(expected_answers, answers)):
        if answer not in VALID_ANSWERS:
            return CheckerResult(False, 0, f"invalid output on line {idx + 1}: '{answer}'")

        if expected_answer != answer:
            return CheckerResult(False, 0, f"line {idx + 1}: expected '{expected_answer}', got '{answer}'")

    return True
