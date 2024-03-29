#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Union, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ getting deletion resisting page
            """
        assert type(index) == int
        assert type(page_size) == int
        ids = self.__indexed_dataset
        length = len(ids)
        idxx = index
        if index is None:
            index = 0
        assert index < length and index >= 0
        data = []
        count = 0
        for a in range(index, length):
            if ids.get(a):
                count += 1
                data.append(ids.get(a))
            if count == page_size:
                break
        return {
            "index": idxx,
            "data": data,
            "next_index": a + 1,
            "page_size": page_size
        }
