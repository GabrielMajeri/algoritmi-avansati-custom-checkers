import io

from dmoj.result import CheckerResult

def check(process_output, judge_output, **kwargs):
    judge_input = kwargs['judge_input']
    judge_input = io.StringIO(judge_input.decode('utf-8'))
    left, right = map(float, next(judge_input).strip().split())
    precision = int(next(judge_input).strip())
    # Read and skip the number of cases in this test
    next(judge_input)

    EPSILON = 10 ** (-precision)

    judge_output = io.StringIO(judge_output.decode('utf-8'))
    expected_answers = [line.strip() for line in judge_output]

    process_output = io.StringIO(process_output.decode('utf-8'))
    answers = [line.strip() for line in process_output]

    # See how many lines the output has
    if len(expected_answers) != len(answers):
        return CheckerResult(False, 0, f'expected {len(expected_answers)} output lines, got {len(answers)}')

    for idx, (expected_answer, answer) in enumerate(zip(expected_answers, answers)):
        kind = next(judge_input).strip()
        next(judge_input)

        if kind == 'TO':
            if expected_answer != answer:
                return CheckerResult(False, 0, f"line {idx + 1}: expected '{expected_answer}', got '{answer}'")
        elif kind == 'FROM':
            float_expected_answer = float(expected_answer)

            try:
                float_answer = float(answer)
            except ValueError:
                return CheckerResult(False, 0, f'line {idx + 1}: invalid floating-point number')

            if not (left <= float_answer <= right):
                return CheckerResult(False, 0, f"line {idx + 1}: number outside of interval")

            if abs(float_expected_answer - float_answer) > EPSILON:
                return CheckerResult(False, 0, f"line {idx + 1}: expected '{round(float_expected_answer, precision)}', got '{answer}'")
        else:
            raise NotImplementedError(f"Unexpected test case type: '{kind}'")

    return True
