import requests
import time
import uuid
import json

from gfycat.constants import (
    FETCH_URL_ENDPOINT, FETCH_URL_LAZY_ENDPOINT,
    FETCH_URL_STATUS_ENDPOINT, FILE_UPLOAD_ENDPOINT,
    FILE_UPLOAD_STATUS_ENDPOINT, ACL, AWS_ACCESS_KEY_ID,
    POLICY, SUCCESS_ACTION_STATUS, SIGNATURE, CONTENT_TYPE,
    QUERY_ENDPOINT, CHECK_LINK_ENDPOINT, OAUTH_ENDPOINT, ERROR_KEY
)
from gfycat.error import GfycatClientError


class GfycatClient(object):
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

        self.get_token()

    def upload_from_url(self, url):
        """
        Upload a GIF from a URL.
        """
        self.check_token()

        # md5 which is used by default, returns an error if gfyCat detects the content is already on GfyCat.
        # noMd5 skips this check, and uploads the content anyway.
        params = {'fetchUrl': url, "noMd5": "true"}
        r = requests.post(FETCH_URL_ENDPOINT, params=params)
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
        self.check_token()

        r = requests.get(QUERY_ENDPOINT + gfyname, headers=self.headers)

        response = r.json()

        if r.status_code != 200 and not ERROR_KEY in response:
            raise GfycatClientError('Bad response from Gfycat',
                                    r.status_code)
        elif ERROR_KEY in response:
            raise GfycatClientError(response[ERROR_KEY], r.status_code)

        return response

    def check_link(self, link):
        """
        Check if a link has been already converted.
        """
        r = requests.get(CHECK_LINK_ENDPOINT + link)
        if r.status_code != 200:
            raise GfycatClientError('Unable to check the link',
                                    r.status_code)

        return r.json()

    def check_token(self):
        """
        Checks if Token is still valid and updates if it's not
        """
        if time.time() > self.expires_at:
            self.get_token()

    def get_token(self):
        """
        Gets the authorization token
        """

        payload = {'grant_type': 'client_credentials', 'client_id': self.client_id, 'client_secret': self.client_secret}
        r = requests.get(OAUTH_ENDPOINT, data=json.dumps(payload), headers={'content-type': 'application/json'})

        response = r.json()

        if r.status_code != 200 and not ERROR_KEY in response:
            raise GfycatClientError('Error fetching the OAUTH URL', r.status_code)
        elif ERROR_KEY in response:
            raise GfycatClientError(response[ERROR_KEY], r.status_code)

        self.token_type = response['token_type']
        self.access_token = response['access_token']
        self.expires_in = response['expires_in']
        self.expires_at = time.time() + self.expires_in - 5
        self.headers = {'content-type': 'application/json', 'Authorization': self.token_type + ' ' + self.access_token}
