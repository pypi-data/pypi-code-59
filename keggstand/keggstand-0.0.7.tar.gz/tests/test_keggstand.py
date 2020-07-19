#!/usr/bin/env python

"""Tests for `keggstand` package."""

import mock

import pytest

from requests.exceptions import RequestException

from keggstand.api import Kegg, NestedDictionary


class MockResponse:
    def __init__(self, content=b"", status_code=200):
        self.content = content
        self.status_code = status_code

    @property
    def ok(self):
        return False


class TestNestedDictionary:
    def test_splits_dunder_string_key(self):
        d = NestedDictionary()
        d["hello__world"] = 1
        assert d["hello"]["world"] == 1

    def test_list_of_keys_recursively_nests(self):
        d = NestedDictionary()
        d[["hello", "world"]] = 1
        assert d["hello"]["world"] == 1

    def test_regular_string_are_top_level(self):
        d = NestedDictionary()
        d["hello"] = 1
        assert d["hello"] == 1


class TestKeggAPI:
    def test_url_builder_joins_arguments_with_fwd_slash(self):
        url = Kegg().url_builder("hsa", ["1", "2"])
        assert url == Kegg.BASE_URL + "hsa/1/2/"

    def test_url_builder_accepts_string_argument(self):
        url = Kegg().url_builder("hsa", "1")
        assert url == Kegg.BASE_URL + "hsa/1/"

    def test_url_builder_value_error_if_no_arguments(self):
        with pytest.raises(ValueError):
            Kegg().url_builder("hsa", [])

    @mock.patch("keggstand.api.requests.get", return_value=MockResponse())
    def test_get_reraises_request_exception_on_fail(self, patch):
        with pytest.raises(RequestException):
            Kegg().get(Kegg.BASE_URL)
        patch.assert_called()

    @mock.patch("keggstand.api.pd.read_csv")
    def parse_dataframe_calls_read_with_tab_delim_and_no_header(self, patch):
        response = MockResponse(content=b"1\t2\t3")
        Kegg().parse_dataframe(response)
        patch.assert_called_with(delimiter="\t", header=False)
