# -*- coding: utf-8 -*-

from typing import Generator
from faker.providers import BaseProvider
from lib.nonbinary_names import nonbinary_names


class Provider(BaseProvider):
    """
    A Faker provider for real nonbinary names
    """

    def __init__(self, generator: Generator):
        self.generator = generator

    def real_name_nonbinary(self) -> str:
        """
        Returns a truly neutral name from baby names
        assigned equally between male and female babies in 2018.
        From https://www.ssa.gov/oact/babynames/
        """
        return self.random_element(nonbinary_names)
