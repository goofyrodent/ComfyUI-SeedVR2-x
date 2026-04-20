"""
ComfyUI-SeedVR2_VideoUpscaler
Official SeedVR2 integration for ComfyUI
"""

# Patch for transformers>=5.5.0 bug: 'flash_attn' missing from PACKAGE_DISTRIBUTION_MAPPING
# but accessed unconditionally in is_flash_attn_2_available(), causing KeyError on import.
try:
    from transformers.utils.import_utils import PACKAGE_DISTRIBUTION_MAPPING
    if "flash_attn" not in PACKAGE_DISTRIBUTION_MAPPING:
        PACKAGE_DISTRIBUTION_MAPPING["flash_attn"] = ["flash_attn", "flash-attn"]
except Exception:
    pass

from .src.optimization.compatibility import ensure_triton_compat  # noqa: F401
from .src.interfaces import comfy_entrypoint, SeedVR2Extension

__all__ = ["comfy_entrypoint", "SeedVR2Extension"]
