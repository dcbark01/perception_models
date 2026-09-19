import subprocess
import sys

import torch

import perception_models
import perception_models.core.vision_encoder.pe as pe
from perception_models.core.audio_visual_encoder import PEAudioVisual, PEAudioVisualTransform  # noqa: F401
from perception_models.core.vision_encoder.config import PE_VISION_CONFIG
from perception_models.core.vision_encoder.tokenizer import SimpleTokenizer


def test_version():
    assert perception_models.__version__ != "0.0.0"


def test_packaged_bpe_vocab_loads():
    assert SimpleTokenizer().encode("a photo of a cat")


def test_vision_encoder_forward():
    model = pe.VisionTransformer(**vars(PE_VISION_CONFIG["PE-Core-T16-384"])).eval()
    with torch.no_grad():
        out = model(torch.randn(1, 3, 384, 384))
    assert out.shape == (1, 512)


def test_encoders_import_without_xformers():
    # xformers is a `train`-only extra (no macOS wheels); the encoders must not need it.
    code = (
        "import sys; sys.modules['xformers'] = None\n"
        "import perception_models.core.vision_encoder.pe\n"
        "import perception_models.core.audio_visual_encoder\n"
    )
    subprocess.run([sys.executable, "-c", code], check=True)
