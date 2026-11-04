import pytest
import numpy as np
from ndh_surrealism.engines.manifold_melting import LiquefactionFluidicsCompiler
from ndh_surrealism.engines.holonomy_vortex import RotationalVortexDrive


@pytest.fixture
def mock_manifold_data():
    """Generates an evaluation matrix conforming to the 80D Riemannian manifold specification."""
    np.random.seed(42)
    # Generate 5 coordinates across 80 high-dimensional dimensions
    return np.random.randn(5, 80)


@pytest.fixture
def mock_base_paths():
    """Generates localized initial layout points inside a standard 1000x1000 canvas area."""
    return [(250.0, 250.0), (500.0, 500.0), (750.0, 750.0), (100.0, 900.0), (900.0, 100.0)]


def test_liquefaction_bounds_and_fluidics(mock_manifold_data, mock_base_paths):
    """Audits Operator 04 to ensure spatial containment floors and dynamic fluid throttling."""
    bounds = (1000.0, 1000.0)
    compiler = LiquefactionFluidicsCompiler(viscosity_floor=0.1)

    melted_output = compiler.generate_melting_paths(
        mock_manifold_data, mock_base_paths, bounds
    )

    assert len(melted_output) == len(mock_base_paths)
    for x, y, fluid in melted_output:
        # Spatial Containment Assertions
        assert 0.0 <= x <= bounds[0], f"X coordinate {x} broke canvas boundary containment ceilings."
        assert 0.0 <= y <= bounds[1], f"Y coordinate {y} broke canvas boundary containment ceilings."
        
        # Fluidics Regulation Assertions
        assert 0.1 <= fluid <= 1.0, f"Fluid throttling engine dropped below the calibrated safety floor: {fluid}"


def test_vortex_spiral_transformation(mock_manifold_data, mock_base_paths):
    """Audits Operator 07 to confirm rotational drift matrix projections stay bounded."""
    bounds = (1200.0, 1200.0)  # Evaluate against alternative studio configurations
    compiler = RotationalVortexDrive(twist_intensity=3.0)

    vortex_output = compiler.generate_vortex_paths(
        mock_manifold_data, mock_base_paths, bounds
    )

    assert len(vortex_output) == len(mock_base_paths)
    for x, y, fluid in vortex_output:
        assert 0.0 <= x <= bounds[0]
        assert 0.0 <= y <= bounds[1]
        assert fluid > 0.0, "Fluid flow delivery stalled during angular spiral displacement."


def test_empty_manifold_fallback():
    """Validates structural safety fallbacks when structural arrays encounter null input data."""
    empty_manifold = np.array([])
    empty_paths = []
    bounds = (1000.0, 1000.0)

    compiler = LiquefactionFluidicsCompiler()
    melted_output = compiler.generate_melting_paths(empty_manifold, empty_paths, bounds)
    
    assert len(melted_output) == 0, "Fallback routing structural checks failed to return a zero-length matrix frame."
