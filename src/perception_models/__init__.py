"""Perception Models: Perception Encoder (PE, PE-AV) and Perception Language Model (PLM).

Model code lives in :mod:`perception_models.core`, e.g.::

    import perception_models.core.vision_encoder.pe as pe
    from perception_models.core.audio_visual_encoder import PEAudioVisual
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("perception_models")
except PackageNotFoundError:  # pragma: no cover - running from an uninstalled checkout
    __version__ = "0.0.0"
