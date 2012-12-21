import loofah.core
loofah.core.SOURCES_URI = "http://localhost/Sources.gz"

from loofah.sources import digest_sources
sources = digest_sources()
sources.save()
