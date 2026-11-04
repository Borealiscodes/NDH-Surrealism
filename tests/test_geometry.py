import pytest
import numpy as np
from ndh_surrealism.engines.manifold_melting import LiquefactionFluidicsCompiler
from ndh_surrealism.engines.holonomy_vortex import RotationalVortexDrive
from ndh_surrealism.engines.spatial_wave import SpatialWaveSubsystem


@pytest.fixture
def mock_manifold_data():
    np.random.seed(42)
    return np.random.randn(5, 80)


@pytest.fixture
def mock_base_paths():
    return [(250.0, 250.0), (500.0, 500.0), (750.0, 750.0), (100.0, 900.0), (900.0, 100.0)]


def test_liquefaction_bounds_and_fluidics(mock_manifold_data, mock_base_paths):
    bounds = (1000.0, 1000.0)
    compiler = LiquefactionFluidicsCompiler(viscosity_floor=0.1)
    melted_output = compiler.generate_melting_paths(mock_manifold_data, mock_base_paths, bounds)
    assert len(melted_output) == len(mock_base_paths)
    for x, y, fluid in melted_output:
        assert 0.0 <= x <= bounds[0]
        assert 0.0 <= y <= bounds[1]
        assert 0.1 <= fluid <= 1.0


def test_vortex_spiral_transformation(mock_manifold_data, mock_base_paths):
    bounds = (1200.0, 1200.0)
    compiler = RotationalVortexDrive(twist_intensity=3.0)
    vortex_output = compiler.generate_vortex_paths(mock_manifold_data, mock_base_paths, bounds)
    assert len(vortex_output) == len(mock_base_paths)
    for x, y, fluid in vortex_output:
        assert 0.0 <= x <= bounds[0]
        assert 0.0 <= y <= bounds[1]
        assert fluid > 0.0


def test_curvature_breathing_bounds(mock_manifold_data, mock_base_paths):
    """Audits Operator 01 expanding waveforms to verify boundary containment."""
    bounds = (1000.0, 1000.0)
    engine = SpatialWaveSubsystem(wave_frequency=8.0)
    wave_output = engine.generate_curvature_waves(mock_manifold_data, mock_base_paths, bounds)
    assert len(wave_output) == len(mock_base_paths)
    for x, y, fluid in wave_output:
        assert 0.0 <= x <= bounds[0]
        assert 0.0 <= y <= bounds[1]


def test_spectral_cascade_expansion(mock_manifold_data, mock_base_paths):
    """Audits Operator 06 nested subdivisions to verify tracking path growth."""
    bounds = (1000.0, 1000.0)
    engine = SpatialWaveSubsystem(recursion_depth=2)
    cascade_output = engine.generate_spectral_cascades(mock_manifold_data, mock_base_paths, bounds)
    # The output length should be greater than or equal to the input due to fractal splits
    assert len(cascade_output) >= len(mock_base_paths)
    for x, y, fluid in cascade_output:
        assert 0.0 <= x <= bounds[0]
        assert 0.0 <= y <= bounds[1]


def test_empty_manifold_fallback():
    empty_manifold = np.array([])
    empty_paths = []
    bounds = (1000.0, 1000.0)
    compiler = LiquefactionFluidicsCompiler()
    melted_output = compiler.generate_melting_paths(empty_manifold, empty_paths, bounds)
    assert len(melted_output) == 0
