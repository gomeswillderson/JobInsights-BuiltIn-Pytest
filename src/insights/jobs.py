from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents.

    :args:
        path (str): Full path to file.

    :returns:
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

    :note:
        Must call `read`.

    :args:
        path (str): Must be passed to `read`.

    :returns:
        list: List of unique job types.
    """
    jobs = read(path)
    unique_jobs = []

    for job in jobs:
        if job['job_type'] not in unique_jobs:
            unique_jobs.append(job['job_type'])

    return unique_jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type.

    :args:
        jobs (list): List of jobs to be filtered.
        job_type (str): Job type for the list filter.

    :returns:
        list: List of jobs with provided job_type.
    """
    filtered_jobs = []

    for job in jobs:
        if job['job_type'] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs
