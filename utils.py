"""
set of utils (templates)
"""


def collect() -> list[dict[str, str | int]]:
    """
    Template for lun array
    """
    example = [
        {
            'name': 'd500-137',
            'vendor': 'Huawei'
        },  # rest
        {
            'instance_id': 1,
            'name': 'd500-137',
            'vendor': 'Hitachi',
            'proxy': 'd500-137r',  # instance_id == port???
        },  # util
        {
            'name': 'd500-137',
            'vendor': 'IBM'
        },  # ssh | rest
    ]
    return example


def request_to_array() -> list[dict[str, str | int]]:
    """
    Template for disc array
    """
    example = [
        {
            'name': "1",
            'uid': "1",
            'size': 1
        },
        {
            'name': "2",
            'uid': "2",
            'size': 2
        },
        {
            'name': "3",
            'uid': "3",
            'size': 3
        }
    ]
    return example
