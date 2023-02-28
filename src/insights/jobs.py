from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, mode="r") as file:
        csv_file = csv.DictReader(file)
        job_list = []
        for job in csv_file:
            job_list.append(job)

    return job_list

    """Reads a file from a given path and returns its contents

    Parameters
    ---------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    unique_jobs = []

    for job in jobs:
        if job['job_type'] not in unique_jobs:
            unique_jobs.append(job['job_type'])

    return unique_jobs

    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_jobs = []

    for job in jobs:
        if job['job_type'] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
