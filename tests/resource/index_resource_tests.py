# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

from unittest import TestCase

import mock
from nose.tools import *

from api.resource.index_resource import *


class IndexResourceTestCase(TestCase):
    def test_a_message_is_returned(self):
        result = FakeResult('hello')
        bus = mock.Mock()
        bus.send_and_wait_response.return_value = result

        response = IndexResource(query_bus=bus).get()

        assert_equals('hello', response)


class FakeResult:
    def __init__(self, response):
        self.response = response
