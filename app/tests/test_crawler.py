import sys
import os
import pytest

# Ensure the root directory is in the sys.path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Now, you can import from the app package
from app.crawler import crawl_domain

def test_valid_url():
    url = "http://example.com"
    result = crawl_domain(url)
    assert isinstance(result, dict), "Sitemap should be a dictionary"

def test_invalid_url():
    url = "http://invalid-url"
    result = crawl_domain(url)
    assert result == {}, "Crawling an invalid URL should return an empty sitemap"

def test_domain_restriction():
    url = "http://example.com"
    result = crawl_domain(url)
    for page in result:
        assert "example.com" in page, "Crawler should restrict to the same domain"

def test_recursive_structure():
    url = "http://example.com"
    result = crawl_domain(url)
    assert isinstance(result, dict), "Sitemap should be nested dictionaries"
