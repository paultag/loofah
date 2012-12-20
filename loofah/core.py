#

from pymongo import Connection

connection = Connection('localhost', 27017)
db = connection.loofah


MIRROR_URL = "ftp.us.debian.org"
DISTRO_NAME = "debian"
VERSION_NAME = "unstable"
SUITE = "main"

SOURCES_URI = "http://{base}/{distro}/dists/{version}/{suite}/source/Sources.gz"


def _get_context():
    return {
        "base": MIRROR_URL,
        "distro": DISTRO_NAME,
        "version": VERSION_NAME,
        "suite": SUITE
    }


def get_sources_uri():
    return SOURCES_URI.format(**_get_context())
