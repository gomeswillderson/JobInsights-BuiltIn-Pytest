from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    job_list = read(path)
    max_salary = 0
    for job in job_list:
        salary = job.get('max_salary')
        # https://www.w3schools.com/python/ref_dictionary_get.asp
        if salary and salary.isdigit():
            salary = int(salary)
            if salary > max_salary:
                max_salary = salary
    return max_salary

    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    raise NotImplementedError


def get_min_salary(path: str) -> int:
    job_list = read(path)
    min_salary = 10000000
    for job in job_list:
        salary = job.get('min_salary')
        if salary and salary.isdigit():
            salary = int(salary)
            if salary < min_salary:
                min_salary = salary
    return min_salary

    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job.get('min_salary'))
        max_salary = int(job.get('max_salary'))
        if min_salary is None or max_salary is None:
            raise ValueError
        if min_salary > max_salary:
            raise ValueError
        salary = int(salary)
        return min_salary <= salary <= max_salary
    except (TypeError, ValueError):
        raise ValueError

    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    filtered_jobs = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            # https://www.w3schools.com/python/ref_keyword_continue.asp
            continue

    return filtered_jobs

    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
