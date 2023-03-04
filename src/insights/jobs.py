from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    data = []
    with open(path, encoding="utf8") as file:
        reader = csv.DictReader(file, delimiter=",")
        for row in reader:
            data.append(row)
    return data


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    job_types_repeated = []
    for job in data:
        job_types_repeated.append(job["job_type"])
    job_types_set = set(job_types_repeated)
    job_types = list(job_types_set)
    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
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
