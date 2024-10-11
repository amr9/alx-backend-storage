#!/usr/bin/env python3
"""uses the requests module to obtain the HTML
content of a particular URL and returns it."""

from typing import List
import requests


def get_list_of_words(subdomains: List[str]) -> List[str]:
    """get_list_of_words: function that takes a list of subdomains
    and returns a list of words"""
    words = []
    for subdomain in subdomains:
        url = f"http://www.{subdomain}.com"
        page = get_page(url)
        words.extend(page.split())
    return words


def get_page(url: str) -> str:
    """get_page: function that takes a URL and returns the content
    of that URL"""
    response = requests.get(url)
    return response.text
