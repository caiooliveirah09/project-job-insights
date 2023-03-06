from src.pre_built.sorting import sort_by

criteria_mock = [
    {"min_salary": 1, "max_salary": 3, "date_posted": "2001-01-01"},
    {"min_salary": 2, "max_salary": 2, "date_posted": "2002-01-01"},
    {"min_salary": 3, "max_salary": 1, "date_posted": "2003-01-01"},
]

criteria_mock_sorted_by_min_salary = [
    {"min_salary": 1, "max_salary": 3, "date_posted": "2001-01-01"},
    {"min_salary": 2, "max_salary": 2, "date_posted": "2002-01-01"},
    {"min_salary": 3, "max_salary": 1, "date_posted": "2003-01-01"},
]

criteria_mock_sorted_by_max_salary = [
    {"min_salary": 1, "max_salary": 3, "date_posted": "2001-01-01"},
    {"min_salary": 2, "max_salary": 2, "date_posted": "2002-01-01"},
    {"min_salary": 3, "max_salary": 1, "date_posted": "2003-01-01"},
]

criteria_mock_sorted_by_date_posted = [
    {"min_salary": 3, "max_salary": 1, "date_posted": "2003-01-01"},
    {"min_salary": 2, "max_salary": 2, "date_posted": "2002-01-01"},
    {"min_salary": 1, "max_salary": 3, "date_posted": "2001-01-01"},
]


def test_sort_by_criteria():
    sort_by(criteria_mock, "min_salary")
    assert criteria_mock == criteria_mock_sorted_by_min_salary

    sort_by(criteria_mock, "max_salary")
    assert criteria_mock == criteria_mock_sorted_by_max_salary

    sort_by(criteria_mock, "date_posted")
    assert criteria_mock == criteria_mock_sorted_by_date_posted
