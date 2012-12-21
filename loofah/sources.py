from loofah.utils import tmpfile
from loofah.core import get_sources_uri, db, _get_context
from contextlib import contextmanager
import urllib2
import gzip


@contextmanager
def download_sources():
    with tmpfile() as fd:
        f = urllib2.urlopen(get_sources_uri())
        open(fd, 'w').write(f.read())
        yield (fd, _get_context())



@contextmanager
def process_sources():
    with download_sources() as info:
        fd, suite = info
        with tmpfile() as newfd:
            f = gzip.open(fd, 'r')
            try:
                yield (f, suite)
            finally:
                pass
            f.close()


def digest_sources():
    sent = None
    with process_sources() as info:
        fd, suite = info
        sent = Sources(suite)
        ret = {}
        key = None
        for line in fd.readlines():
            if line.strip() == "":
                package = PackageEntry(ret)
                sent.add_entry(package)
                ret = {}
                continue

            if line[0] == " ":
                if ret[key] != "":
                    ret[key] += "\n"
                ret[key] += line.strip()
            else:
                line = line.strip()
                key, val = line.split(":", 1)
                key = key.strip()
                ret[key] = val.strip()
    return sent


class PackageEntry(dict):
    def __init__(self, entry):
        for key in ['Build-Depends', 'Build-Depends-Indep']:
            if key in entry:
                entry[key] = [
                    x.split()[0].strip() for x in entry[key].split(",")
                ]

        if 'Uploaders' in entry:
            entry['Uploaders'] = [
                x.strip() for x in entry['Uploaders'].split(",")
            ]

        if 'Package-List' in entry:
            entry['Package-List'] = [
                {
                    "name": y[0],
                    "type": y[1],
                    "section": y[2],
                    "priority": y[3]
                } for y in [
                    x.split() for x in entry['Package-List'].split("\n")
                ]
            ]
        for key in ["Files", "Checksums-Sha256", "Checksums-Sha1"]:
            entry[key] = [
                {
                    "hash": y[0],
                    "size": y[1],
                    "file": y[2]
                } for y in [x.split() for x in entry[key].split("\n")]
            ]
        for key in entry:
            self[key] = entry[key]


class Sources(dict):
    def __init__(self, info):
        self.base = "{protocol}{base}".format(**info)
        self.suite = info['suite']
        self.dist = info['distro']
        self.version = info['version']

    def add_entry(self, package):
        key = package['Package']
        self[key] = package
        # print "I: New package: %s" % (key)

    def save(self):
        base, suite, dist, version = (
            self.base, self.suite, self.dist, self.version
        )
        print suite, dist, version, base
