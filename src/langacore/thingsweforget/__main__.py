import os
import re
import sys
from time import sleep
import urllib.request, urllib.error, urllib.parse

from lxml import html as etree


CHARSET_REGEX = re.compile(r"charset=(.+)")


def get_content_type(html):
    """Returns a tuple with the content type and its encoding.
    
    :param html: lxml Element obtained for instance by lxml.html.fromstring()
    """
    content_type = None
    encoding = None
    meta = html.xpath('head/meta[translate(@http-equiv, \
                                           "ABCDEFGHIJKLMNOPQRSTUVWXYZ", \
                                           "abcdefghijklmnopqrstuvwxyz")="content-type"]')
    if not meta:
        return content_type, encoding
    attrib = meta[0].attrib
    if 'content' not in attrib:
        msg = "Meta header Content-Type with no content."
        raise ValueError(msg)
    options = attrib['content'].split(';')
    content_type = options[0].strip().lower()
    for opt in options[1:]:
        m = CHARSET_REGEX.match(opt.strip())
        if not m:
            continue
        encoding = m.group(1).lower()
    return content_type, encoding


def get_html_from_bytes(contents_bytes, encoding="utf8", errors="strict"):
    """Converts byte-based contents to Unicode using a specific encoding
    and error treatment method.

    :param contents_bytes: raw bytes
    :param encoding: name of the encoding to use while decoding Unicode
    :param errors: what error handler to use in case of invalid byte sequence.
                   Acceptable values are schemes implemented by ``codecs``, i.e.
                   ``strict``, ``ignore``, ``replace``, etc.
    """
    contents = contents_bytes.decode(encoding, errors)
    return etree.fromstring(contents)


def get_html_from_url(url):
    """Gets a lxml Element for the whole HTML document from the given URL.
    Throws ValueErrors when the URL presents a document of incompatible content
    type.

    :param url: the URL to scan, string"""
    with urllib.request.urlopen(url) as connection:
        contents_bytes = connection.read()
        html = get_html_from_bytes(contents_bytes, errors="replace") 
        content_type, encoding = get_content_type(html)
        if content_type and content_type not in ("text/html",):
            msg = "Invalid content type. "\
                  "Expected HTML but got '{}' instead.".format(content_type)
            raise ValueError(msg)
        if encoding and encoding not in ("utf8", "utf-8"):
            html = get_html_from_bytes(contents_bytes, encoding=encoding)
    return html


def download_img(url, target_dir):
    """Performs the actual image download.

    :param url: source URL, string
    :param target_dir: path to target directory, string. Created if doesn't
                       already exist."""
    def report_progress(blocks_done, block_size, size_total):
        percent = 100.0 * blocks_done * block_size / size_total
        if percent > 100:
            # the last block will most likely be partly empty
            percent = 100
        sys.stdout.write("\r{0}: {1:5.2f}%".format(url, percent))
        sys.stdout.flush()

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    urllib.request.urlretrieve(url,
                               filename=os.path.join(target_dir, url.split('/')[-1]),
                               reporthook=report_progress) 
    sys.stdout.write('\n')
    sys.stdout.flush()


def get_images_from_url(url, target_dir, first_only=True):
    """Gets all images from all posts within the specified URL. Handling is
    specific for the current blogspot theme of ThingsWeForget (as of 2010-06-04).

    :param url: the URL to start the crawling from, string
    :param first_only: if True, only the first image in every post is taken
    :return: a follow-up URL to enable scanning older entries (string), or None"""
    html = get_html_from_url(url)
    for post in html.cssselect('.post'):
        #import pdb; pdb.set_trace()
        for img in post.cssselect('.entry-content img'): 
            if 'src' in img.attrib:
                download_img(img.attrib['src'], target_dir)
            if first_only:
                break
    follow_up_link = html.cssselect('a.blog-pager-older-link')
    if follow_up_link and 'href' in follow_up_link[0].attrib:
        return follow_up_link[0].attrib['href']
    return None


another = get_images_from_url("http://thingsweforget.blogspot.com/", '.')
while another:
    sleep(1)
    another = get_images_from_url(another, '.')
