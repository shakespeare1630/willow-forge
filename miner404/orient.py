"""The renderer interface the pipeline uses, and the judge's four front-view angles (30 degrees left and right of +Z,
the front from slightly below and from slightly above), shared with the photo-match score in match.py."""

from __future__ import annotations

from typing import Protocol

from witness_client import RenderOptions

FRONT_THETAS = (30.0, 330.0, 0.0, 0.0)
FRONT_PHIS = (0.0, 0.0, 15.0, -30.0)


class Renderer(Protocol):
    def render(self, source: str, options: RenderOptions) -> bytes: ...
