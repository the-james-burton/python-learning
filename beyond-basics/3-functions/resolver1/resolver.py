#!/usr/bin/env python3
"""Demostrate functions"""


import socket


class Resolver:

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        """this special method is syntactic sugar for
        directly calling this with Resolver(...)"""
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        self._cache.clear()

    def has(self, host):
        return host in self._cache