import requests
import time
import uuid

from gfycat.constants import (FETCH_URL_ENDPOINT, FETCH_URL_LAZY_ENDPOINT,
                       FETCH_URL_STATUS_ENDPOINT, FILE_UPLOAD_ENDPOINT,
                       FILE_UPLOAD_STATUS_ENDPOINT, ACL, AWS_ACCESS_KEY_ID,
                       POLICY, SUCCESS_ACTION_STATUS, SIGNATURE, CONTENT_TYPE,
                       QUERY_ENDPOINT, CHECK_LINK_ENDPOINT)
from gfycat.error import GfycatClientError


class GfycatClient(object):
    def __init__(self):
        # Will hold access tokens and auth credentials when Gfycat decides to
        # implement them.
        pass

    def upload_from_url(self, url):
        """
        Upload a GIF from a URL.
        """
        params = {'fetchUrl': url}
        r = requests.get(FETCH_URL_ENDPOINT, params=params)

        if r.status_code != 200:
            raise GfycatClientError('Error fetching the URL', r.status_code)

        response = r.json()
        if 'error' in response:
            raise GfycatClientError(response['error'])

        return response

    def upload_from_file(self, filename):
        """
        Upload a local file to Gfycat
        """
        key = str(uuid.uuid4())[:8]

        form = [('key', key),
                ('acl', ACL),
                ('AWSAccessKeyId', AWS_ACCESS_KEY_ID),
                ('success_action_status', SUCCESS_ACTION_STATUS),
                ('signature', SIGNATURE),
                ('Content-Type', CONTENT_TYPE),
                ('policy', POLICY)]
        data = dict(form)

        files = {'file': open(filename, 'rb')}
        r = requests.post(FILE_UPLOAD_ENDPOINT, data=data, files=files)

        if r.status_code != 200:
            raise GfycatClientError('Error uploading the GIF', r.status_code)

        info = self.uploaded_file_info(key)
        while 'timeout' in info.get('error', '').lower():
            time.sleep(2)
            info = self.uploaded_file_info(key)
        if 'error' in info:
            raise GfycatClientError(info['error'])

        return info

    def uploaded_file_info(self, key):
        """
        Get information about an uploaded GIF.
        """
        r = requests.get(FILE_UPLOAD_STATUS_ENDPOINT + key)
        if r.status_code != 200:
            raise GfycatClientError('Unable to check the status',
                                    r.status_code)

        return r.json()

    def query_gfy(self, gfyname):
        """
        Query a gfy name for URLs and more information.
        """
        r = requests.get(QUERY_ENDPOINT + gfyname)
        if r.status_code != 200:
            raise GfycatClientError('Unable to query for the GIF',
                                    r.status_code)

        return r.json()

    def check_link(self, link):
        """
        Check if a link has been already converted.
        """
        r = requests.get(CHECK_LINK_ENDPOINT + link)
        if r.status_code != 200:
            raise GfycatClientError('Unable to check the link',
                                    r.status_code)

        return r.json()

