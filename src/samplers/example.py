application = 'example'


###############################################################################
def getDetails(env=None):
    return [
        {'env': 'preprod', 'release': '2.4', 'url': "http://www.google.com"},
        {'env': 'prod', 'release': '2.3a', 'notes': "But wait, there's more"},
        ]

# EOF
