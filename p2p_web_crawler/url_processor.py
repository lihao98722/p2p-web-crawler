__author__ = 'Howie'
import hashlib
from urlparse import urlparse


def get_domain_checksum(url):
    domain = get_domain(url)
    return hashlib.md5(domain).digest()


def get_url_checksum(url):
    ret = urlparse(url)
    hostname = ret.hostname[4:] if ret.hostname.startswith("www.") else ret.hostname
    url_reduced = hostname + ret.path
    return hashlib.sha1(url_reduced).digest()


def get_domain(url):
    hostname = urlparse(url).hostname
    return '.'.join(hostname.split('.')[-2:])