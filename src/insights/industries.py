from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Return a list of unique industries from the provided jobs data file.

    Note:
        Must call `read`.

    Args:
        path (str): The file path of the jobs data file to read.

    Returns:
        list of str: A list of unique industries present in the jobs data file.

    Raises:
        FileNotFoundError: If the specified file path does not exist.
        ValueError: If the specified file does not have a valid format.
    """
    jobs = read(path)
    unique_industries = []

    for job in jobs:
        industry = job['industry']
        if industry and industry not in unique_industries:
            unique_industries.append(industry)

    return unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filter a list of job dictionaries by industry.

    Args:
        jobs (List[Dict]): A list of job dictionaries.
        industry (str): The industry to filter by.

    Returns:
        List[Dict]: A filtered list of job dictionaries
        with the specified industry.

    """
    filtered_industries = []

    for job in jobs:
        if job['industry'] == industry:
            filtered_industries.append(job)

    return filtered_industries
