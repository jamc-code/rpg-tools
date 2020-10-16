# -*- coding: utf-8 -*-

from faker.providers import BaseProvider
from lib.common_names import nonbinary_names


class Provider(BaseProvider):
    """
    A Faker provider for real nonbinary names
    """

    def __init__(self, generator):
        self.generator = generator

    def real_name_nonbinary(self):
        """
        Returns a truly neutral name from baby names
        assigned equally between male and female babies in 2018.
        From https://www.ssa.gov/oact/babynames/
        """

        return self.random_element(nonbinary_names)
