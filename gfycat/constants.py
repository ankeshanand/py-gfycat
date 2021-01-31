# Gfycat does not yet have a full fledged API with
# access credentials and advanced access control.
# These parameters are explicitly mentioned at
# http://gfycat.com/api

# Fetching from a URL
FETCH_URL_ENDPOINT = 'https://upload.gfycat.com/transcode'
FETCH_URL_LAZY_ENDPOINT = 'https://upload.gfycat.com/transcodeRelease/'
FETCH_URL_STATUS_ENDPOINT = 'https://upload.gfycat.com/status/'

# File Upload
FILE_UPLOAD_ENDPOINT = 'https://gifaffe.s3.amazonaws.com/'
FILE_UPLOAD_STATUS_ENDPOINT = 'https://upload.gfycat.com/transcode/'
ACL = 'private'
AWS_ACCESS_KEY_ID = 'AKIAIT4VU4B7G2LQYKZQ'
POLICY = "eyAiZXhwaXJhdGlvbiI6ICIyMDIwLTEyLTAxVDEyOjAwOjAwLjAwMFoiLAogICAgICAgICAgICAiY29uZGl0aW9ucyI6IFsKICAgICAgICAgICAgeyJidWNrZXQiOiAiZ2lmYWZmZSJ9LAogICAgICAgICAgICBbInN0YXJ0cy13aXRoIiwgIiRrZXkiLCAiIl0sCiAgICAgICAgICAgIHsiYWNsIjogInByaXZhdGUifSwKCSAgICB7InN1Y2Nlc3NfYWN0aW9uX3N0YXR1cyI6ICIyMDAifSwKICAgICAgICAgICAgWyJzdGFydHMtd2l0aCIsICIkQ29udGVudC1UeXBlIiwgIiJdLAogICAgICAgICAgICBbImNvbnRlbnQtbGVuZ3RoLXJhbmdlIiwgMCwgNTI0Mjg4MDAwXQogICAgICAgICAgICBdCiAgICAgICAgICB9"
SUCCESS_ACTION_STATUS = 200
SIGNATURE = 'mk9t/U/wRN4/uU01mXfeTe2Kcoc='
CONTENT_TYPE = 'image/gif'

# Query
QUERY_ENDPOINT = 'https://api.gfycat.com/v1/gfycats/'
QUERY_FALLBACK = 'https://api.redgifs.com/v1/gfycats/'

# Check Link
CHECK_LINK_ENDPOINT = 'https://gfycat.com/cajax/checkUrl/'

# OAuth
OAUTH_ENDPOINT = 'https://api.gfycat.com/v1/oauth/token'

# Error
ERROR_KEY = 'errorMessage'
