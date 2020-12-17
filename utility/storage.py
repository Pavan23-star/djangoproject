from whitenoise.storage import CompressedManifestStaticFilesStorage

class WhiteNoiseStaticFileStorage(CompressedManifestStaticFilesStorage):
    manifest_strict = False
