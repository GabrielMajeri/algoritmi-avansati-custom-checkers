import io

from dmoj.result import CheckerResult

def check(process_output, judge_output, **kwargs):
    process_output = io.StringIO(process_output.decode('utf-8'))
    judge_output = io.StringIO(judge_output.decode('utf-8'))

    # See how long the produced convex hull is.
    try:
        raw_convex_hull_size = next(process_output)
    except:
        return CheckerResult(False, 0, 'could not read first line of solution')

    try:
        convex_hull_size = int(raw_convex_hull_size)
    except:
        return CheckerResult(False, 0, f"first line of solution is not a valid integer: '{raw_convex_hull_size}'")

    expected_convex_hull_size = int(next(judge_output))

    # If it doesn't even have the right length, it's definitely wrong.
    if convex_hull_size != expected_convex_hull_size:
        return CheckerResult(False, 0, 'wrong number of points in convex hull')

    # Now check if the solution is correct.
    expected_points = []
    for _ in range(expected_convex_hull_size):
        x, y = map(int, judge_output.readline().split())
        expected_points.append((x, y))

    points = []
    try:
        for _ in range(convex_hull_size):
            x, y = map(int, process_output.readline().split())
            points.append((x, y))
    except:
        return CheckerResult(False, 0, 'could not read points of the convex hull')


    sync_point = expected_points[0]

    try:
        sync_point_index = points.index(sync_point)
    except ValueError:
        return CheckerResult(False, 0, 'could not find first expected point of convex hull in solution')

    reordered_points = points[sync_point_index:] + points[:sync_point_index]

    return expected_points == reordered_points
