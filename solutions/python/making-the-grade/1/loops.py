"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    Parameters:
        student_scores (list[float]): Student exam scores.

    Returns:
        list[int]: Student scores *rounded* to the nearest integer value.
    """

    int_scores = []
    for score in student_scores:
        int_scores.append(round(score))
    return int_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    Parameters:
        student_scores (list[int]): Student scores as ints.

    Returns:
        int: The count of student scores at or below 40.
    """

    count = 0
    for score in student_scores:
        if score <= 40:
            count += 1
    return count


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    Parameters:
        student_scores (list[int]): Integer scores.
        threshold (int): The threshold to cross to be the "best" score.

    Returns:
        list[int]: Integer scores that are at or above the "best" threshold.
    """

    best = []
    for score in student_scores:
        if score >= threshold:
            best.append(score)
    return best


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    Parameters:
        highest (int): The value of the highest exam score.

    Returns:
        list[int]: Lower threshold scores for each D-A letter grade interval.

        For example, where the highest score is 100, and failing is <= 40,
        The result would be [41, 56, 71, 86]:
            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    grade_range = highest - 41
    half = round(grade_range / 2)
    quarter = round(half / 2)
    return [41, 41 + quarter, 41 + half, 41 + half + quarter]


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    Parameters:
        student_scores (list): Scores in descending order.
        student_names (list[str]): Student names by exam score in descending order.

    Returns:
        list[str]: Strings in format ["<rank>. <student name>: <score>"].
    """

    results_list = []
    for i in range(0, len(student_scores)):
        rank = str(i + 1)
        name = str(student_names[i])
        score = str(student_scores[i])
        results_list.append(rank + ". " + name + ": " + score)
    return results_list


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    Parameters:
        student_info (list[list[str, int]]): List of [<student name>, <score>] lists.

    Returns:
        list: First `[<student name>, 100]` found OR `[]` if no student score of 100 is found.
    """

    # results_list = []
    # for student in student_info:
    #     for name, grade in student_info[student]:
    #         if grade == 100:
    #             results_list.append(name)
    #             results_list.append(grade)
    # return results_list

    for student in student_info:
        name, grade = student
        if grade == 100:
            return [name, grade]
    return []
            
