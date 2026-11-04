import os
import json
import argparse
import numpy as np
from ndh_surrealism.engines.manifold_melting import LiquefactionFluidicsCompiler
from ndh_surrealism.engines.holonomy_vortex import RotationalVortexDrive
from ndh_surrealism.engines.spatial_wave import SpatialWaveSubsystem
from ndh_surrealism.engines.discontinuity import DiscontinuitySubsystem
from ndh_surrealism.engines.compositional import CompositionalSubsystem
from ndh_surrealism.hardware.gcode import NDHGCodeCompiler
from ndh_surrealism.hardware.leveling import CanvasAutoLeveler


class NDHSurrealismCompiler:

    def __init__(self, canvas_width=1000.0, canvas_height=1000.0):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        
        # Instantiate complete 9-operator suite
        self.liquefaction_engine = LiquefactionFluidicsCompiler()
        self.vortex_engine = RotationalVortexDrive()
        self.wave_engine = SpatialWaveSubsystem()
        self.discontinuity_engine = DiscontinuitySubsystem()
        self.compositional_engine = CompositionalSubsystem()
        
        # Instantiate industrial hardware driver modules
        self.auto_leveler = CanvasAutoLeveler(grid_size=3, canvas_bounds=(canvas_width, canvas_height))
        self.hardware_compiler = NDHGCodeCompiler()
        print(f"[*] NDH-Surrealism Engine Initialized. Bounds: {canvas_width}x{canvas_height}")

    def load_dream_profile(self, profile_path):
        if not os.path.exists(profile_path):
            raise FileNotFoundError(f"Dream profile not found at {profile_path}")
        with open(profile_path, "r") as f:
            return json.load(f)

    def extract_latent_coordinates(self, dream_data):
        raw_coords = dream_data.get("latent_coordinates", [])
        return np.array(raw_coords) if raw_coords else np.random.randn(100, 80)

    def compile_pipeline(self, profile_path, output_gcode_path, enable_leveling=True):
        """Executes full high-dimensional projection, operator routing, terrain leveling, and G-code export."""
        dream_data = self.load_dream_profile(profile_path)
        manifold_space = self.extract_latent_coordinates(dream_data)
        operator = dream_data.get("active_operator", "liquefaction")

        print(f"[*] Processing manifold with shape {manifold_space.shape} via '{operator}'...")

        # Step 1: Spatial layout down-projection layer (80D to base 2D plane)
        base_paths = []
        for vector in manifold_space:
            x_proj = float(np.sin(vector) * (self.canvas_width / 2) + (self.canvas_width / 2))
            y_proj = float(np.cos(vector) * (self.canvas_height / 2) + (self.canvas_height / 2))
            base_paths.append((x_proj, y_proj))

        # Step 2: Route structural anomalies through designated modification engine
        if operator == "liquefaction":
            compiled_paths = self.liquefaction_engine.generate_melting_paths(manifold_space, base_paths, (self.canvas_width, self.canvas_height))
        elif operator == "holonomy_vortex":
            compiled_paths = self.vortex_engine.generate_vortex_paths(manifold_space, base_paths, (self.canvas_width, self.canvas_height))
        elif operator == "hallucination_curvature":
            compiled_paths = self.wave_engine.generate_curvature_waves(manifold_space, base_paths, (self.canvas_width, self.canvas_height))
        elif operator == "spectral_cascade":
            compiled_paths = self.wave_engine.generate_spectral_cascades(manifold_space, base_paths, (self.canvas_width, self.canvas_height))
        elif operator == "symbolic_drift":
            compiled_paths = self.discontinuity_engine.generate_symbolic_drift(manifold_space, base_paths, (self.canvas_width, self.canvas_height))
        elif operator == "collapse_surface":
            compiled_paths = self.discontinuity_engine.generate_surface_collapses(manifold_space, base_paths, (self.canvas_width, self.canvas_height))
        elif operator == "conceptual_fusion":
            compiled_paths = self.compositional_engine.generate_conceptual_fusion(manifold_space, base_paths, (self.canvas_width, self.canvas_height))
        elif operator == "potential_field":
            compiled_paths = self.compositional_engine.generate_potential_fields(manifold_space, base_paths, (self.canvas_width, self.canvas_height))
        elif operator == "dream_diagnostic":
            compiled_paths = self.compositional_engine.generate_diagnostic_pipeline(manifold_space, base_paths, (self.canvas_width, self.canvas_height), self)
        else:
            print(f"[!] Operator '{operator}' unrecognized. Utilizing uniform fallback baseline loops.")
            compiled_paths = [(x, y, 0.1) for x, y in base_paths]

        # Step 3: Topographic mesh correction adaptation layer
        if enable_leveling:
            self.auto_leveler.load_mesh_telemetry() # Pull sensor calibration variables
            final_paths = self.auto_leveler.apply_mesh_leveling(compiled_paths)
        else:
            # Flatten Z dimension natively if terrain adaptations are bypassed
            final_paths = [(x, y, 0.0, flow) for x, y, flow in compiled_paths]

        # Step 4: Hardware step translation and G-code export block compilation
        self.hardware_compiler.compile_to_gcode(final_paths, output_gcode_path)
        return final_paths


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NDH-Surrealism Core Compiler")
    parser.add_argument("--input", type=str, required=True, help="Path to dream profile JSON")
    parser.add_argument("--output", type=str, required=True, help="Path to write compiled G-code")
    parser.add_argument("--no-leveling", action="store_true", help="Bypass topographical terrain leveling adaptations")
    args = parser.parse_args()

    compiler = NDHSurrealismCompiler()
    try:
        compiler.compile_pipeline(args.input, args.output, enable_leveling=not args.no_leveling)
    except Exception as e:
        print(f"[-] Execution halted: {e}")
