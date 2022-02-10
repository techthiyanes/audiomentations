from .augmentations.spectrogram_transforms import SpecFrequencyMask, SpecChannelShuffle
from .augmentations.transforms import (
    AddBackgroundNoise,
    AddGaussianNoise,
    AddGaussianSNR,
    AddImpulseResponse,
    ApplyImpulseResponse,
    AddShortNoises,
    BandPassFilter,
    BandStopFilter,
    Clip,
    ClippingDistortion,
    FrequencyMask,
    Gain,
    HighPassFilter,
    LowShelfFilter,
    HighShelfFilter,
    LoudnessNormalization,
    LowPassFilter,
    Mp3Compression,
    Normalize,
    PeakingFilter,
    PitchShift,
    PolarityInversion,
    Resample,
    Reverse,
    Shift,
    TanhDistortion,
    TimeMask,
    TimeStretch,
    Trim,
)
from .core.composition import Compose, SpecCompose, OneOf, SomeOf

__version__ = "0.21.0"
