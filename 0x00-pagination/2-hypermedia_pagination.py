#!/usr/bin/env python3
""" a module that gets start and end index of a page """
from typing import Tuple, Union, List, Any, Dict
import csv
import math
from typing import List
from math import ceil


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ gets start and end index of a page"""
    start_index = ((page - 1) * page_size)
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get content by page
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        self.dataset()
        if self.__dataset is None:
            return []
        start, end = index_range(page, page_size)

        length = len(self.__dataset) - 1
        if length < start:
            return []
        if length < end:
            end = length
        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[Any, Any]:
        """ get next, current, prev and total pages"""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        self.dataset()
        length = len(self.__dataset) - 1 if self.__dataset is not None else 0
        result = dict()
        data = self.get_page(page, page_size)
        result['data'] = data
        result['page_size'] = len(data)
        result['page'] = page
        if page > 1:
            result['prev_page'] = page - 1
        else:
            result['prev_page'] = None
        next_start, next_end = index_range(page + 1, page_size)
        if next_start <= length:
            result['next_page'] = page + 1
        else:
            result['next_page'] = None
        result['total_pages'] = ceil((length + 1) / page_size)
        return result
