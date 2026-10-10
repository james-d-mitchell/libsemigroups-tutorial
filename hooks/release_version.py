"""Expose the release being built to the site header."""

import os
from urllib.parse import quote


def on_config(config):
    version = os.environ.get("TUTORIAL_VERSION", "").strip() or "dev"
    release_tag = os.environ.get("TUTORIAL_RELEASE_TAG", "").strip()
    config.extra["tutorial_version"] = version
    config.extra["tutorial_release_url"] = (
        "https://github.com/libsemigroups/tutorial/releases/tag/"
        + quote(release_tag, safe="")
        if release_tag
        else None
    )
    return config
