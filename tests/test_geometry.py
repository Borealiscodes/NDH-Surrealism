import pytest
import numpy as np
from ndh_surrealism.core import NDHSurrealismCompiler
from ndh_surrealism.engines.manifold_melting import LiquefactionFluidicsCompiler
from ndh_surrealism.engines.holonomy_vortex import RotationalVortexDrive
from ndh_surrealism.engines.spatial_wave import SpatialWaveSubsystem
from ndh_surrealism.engines.discontinuity import DiscontinuitySubsystem
from ndh_surrealism.engines.compositional import CompositionalSubsystem


@pytest.fixture
def mock_manifold_data():
    np.random.seed(42)
    return np.random.randn(8, 80)


@pytest.fixture
def mock_base_paths():
    return [(250.0, 250.0), (500.0, 500.0), (750.0, 750.0), (100.0, 900.0), 
            (900.0, 100.0), (300.0, 600.0), (600.0, 300.0), (400.0, 400.0)]


def test_liquefaction_bounds_and_fluidics(mock_manifold_data, mock_base_paths):
    bounds = (1000.0, 1000.0)
    compiler = LiquefactionFluidicsCompiler(viscosity_floor=0.1)
    melted_output = compiler.generate_melting_paths(mock_manifold_data, mock_base_paths, bounds)
    assert len(melted_output) == len(mock_base_paths)
    for x, y, fluid in melted_output:
        assert 0.0 <= x <= bounds[0] and 0.0 <= y <= bounds[1]
        assert 0.1 <= fluid <= 1.0


def test_vortex_spiral_transformation(mock_manifold_data, mock_base_paths):
    bounds = (1200.0, 1200.0)
    compiler = RotationalVortexDrive(twist_intensity=3.0)
    vortex_output = compiler.generate_vortex_paths(mock_manifold_data, mock_base_paths, bounds)
    assert len(vortex_output) == len(mock_base_paths)
    for x, y, fluid in vortex_output:
        assert 0.0 <= x <= bounds[0] and 0.0 <= y <= bounds[1]


def test_conceptual_fusion_averaging(mock_manifold_data, mock_base_paths):
    """Audits Operator 02 boundary blending to ensure containment."""
    bounds = (1000.0, 1000.0)
    engine = CompositionalSubsystem(blend_ratio=0.5)
    fused_output = engine.generate_conceptual_fusion(mock_manifold_data, mock_base_paths, bounds)
    assert len(fused_output) == len(mock_base_paths)
    for x, y, _ in fused_output:
        assert 0.0 <= x <= bounds[0] and 0.0 <= y <= bounds[1]


def test_potential_field_attraction(mock_manifold_data, mock_base_paths):
    """Audits Operator 03 clustering toward canvas center wells."""
    bounds = (1000.0, 1000.0)
    engine = CompositionalSubsystem(attraction_strength=0.6)
    field_output = engine.generate_potential_fields(mock_manifold_data, mock_base_paths, bounds)
    assert len(field_output) == len(mock_base_paths)
    for x, y, _ in field_output:
        assert 0.0 <= x <= bounds[0] and 0.0 <= y <= bounds[1]


def test_full_diagnostic_pipeline(mock_manifold_data, mock_base_paths):
    """Audits Operator 09 sequential chunk modulation routing loops."""
    bounds = (1000.0, 1000.0)
    core_compiler = NDHSurrealismCompiler(canvas_width=bounds[0], canvas_height=bounds[1])
    engine = CompositionalSubsystem()
    
    diagnostic_output = engine.generate_diagnostic_pipeline(
        mock_manifold_data, mock_base_paths, bounds, core_compiler
    )
    assert len(diagnostic_output) >= len(mock_base_paths)
    for x, y, _ in diagnostic_output:
        assert 0.0 <= x <= bounds[0] and 0.0 <= y <= bounds[1]
