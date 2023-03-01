from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents.

    Args:
        path (str): Full path to file.

    Returns:
        list: List of rows as dicts.
    """
    with open(path, mode="r") as file:
        csv_file = csv.DictReader(file)
        job_list = []
        for job in csv_file:
            job_list.append(job)

    return job_list


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them.

    Note:
        Must call `read`.

    Args:
        path (str): Must be passed to `read`.

    Returns:
        list: List of unique job types.
    """
    jobs = read(path)
    unique_jobs = []

    for job in jobs:
        job = job['job_type']
        if job and job not in unique_jobs:
            unique_jobs.append(job)

    return unique_jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type.

    Args:
        jobs (list): List of jobs to be filtered.
        job_type (str): Job type for the list filter.

    Returns:
        list: List of jobs with provided job_type.
    """
    filtered_jobs = []

    for job in jobs:
        if job['job_type'] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs
