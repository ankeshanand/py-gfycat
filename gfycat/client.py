import requests
import uuid

from constants import (FETCH_URL_ENDPOINT, FETCH_URL_LAZY_ENDPOINT,
    FETCH_URL_STATUS_ENDPOINT, FILE_UPLOAD_ENDPOINT,
    FILE_UPLOAD_STATUS_ENDPOINT, ACL, AWS_ACCESS_KEY_ID, POLICY,
    SUCCESS_ACTION_STATUS, SIGNATURE, CONTENT_TYPE, QUERY_ENDPOINT,
    CHECK_LINK_ENDPOINT)
from error import GfycatClientError


class GfycatClient(object):
    def __init__(self):
        # Will hold access tokens and auth credentials when Gfycat decides to
        # implement them.
        pass

    def fetch_url(self, url):
        params = {'fetchUrl': url}
        r = requests.get(FETCH_URL_ENDPOINT, params=params)

        if r.status_code != 200:
            raise GfycatClientError('Error fetching the URL', r.status_code)

        response = r.json()
        return response

    def fetch_url_lazy(self, url, random_string=None):
        if not random_string:
            random_string = str(uuid.uuid4())[:8]

        params = {'fetchUrl': url}
        r = requests.get(FETCH_URL_LAZY_ENDPOINT + random_string,
                         params=params)

        if r.status_code != 200:
            raise GfycatClientError('Error fetching the URL', r.status_code)

        return random_string

    def check_fetch_status(self, random_string):
        pass

    def upload_file(self, filename, key=None):
        """
        Upload a local file to Gfycat
        :param filename:
        :param key: A unique string to later check the status of file upload
        :return:
        """
        if not key:
            key = str(uuid.uuid4())[:8]

        form = [('key', key),
                ('acl', ACL),
                ('AWSAccessKeyId', AWS_ACCESS_KEY_ID),
                ('success_action_status', SUCCESS_ACTION_STATUS),
                ('signature', SIGNATURE),
                ('Content-Type', CONTENT_TYPE),
                ('policy', POLICY)]

        with open(filename, 'rb') as upfile:
            form.append(('file', upfile))
            r = requests.post(FILE_UPLOAD_ENDPOINT, files=form)

        if r.status_code != 200:
            raise GfycatClientError('Error uploading the GIF', r.status_code)

        return key

    def check_upload_status(self, key):
        pass

    def query_gfy(self, gfyname):
        pass

    def check_link(self, link):
        pass

