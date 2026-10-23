import pytest
from validator.modules import UrlRequest

def test_valid_urls():
    req = UrlRequest(urls=["https://google.com"])
    assert len(req.urls) == 1

def test_invalid_urls_should_fail():
    with pytest.raises(Exception):
        UrlRequest(urls=["not-a-url"]) # should fail