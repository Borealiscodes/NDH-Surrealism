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
from ndh_surrealism.hardware.lh_adapter import LeanHallucinationSurrealismAdapter


class NDHSurrealismCompiler:

    def __init__(self, canvas_width=1000.0, canvas_height=1000.0):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        
        # Instantiate the safety enclave intercept shield
        self.safety_shield = LeanHallucinationSurrealismAdapter(tension_ceiling=4.5)
        
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
        """Executes verification intercept audit, spatial projection, leveling, and multi-color G-code compilation."""
        dream_data = self.load_dream_profile(profile_path)
        manifold_space = self.extract_latent_coordinates(dream_data)
        operator = dream_data.get("active_operator", "liquefaction")

        print(f"[*] Ingesting manifold phase space with shape {manifold_space.shape}...")

        # ⚠️ CRITICAL INTERCEPT LAYER: Audit matrix stability via Lean-Hallucination-Guard protocols
        # If the manifold exhibits drift-collapse mimicry, this terminates the execution runtime immediately.
        self.safety_shield.audit_manifold_stream(manifold_space)

        # Step 1: Spatial layout down-projection layer (80D to base 2D plane)
        base_paths = []
        for vector in manifold_space:
            x_proj = float(np.sin(vector) * (self.canvas_width / 2) + (self.canvas_width / 2))
            y_proj = float(np.cos(vector) * (self.canvas_height / 2) + (self.canvas_height / 2))
            base_paths.append((x_proj, y_proj))

        # Step 2: Route structural anomalies through designated modification engine and map Color IDs (0-8)
        if operator == "liquefaction":
            paths_2d = self.liquefaction_engine.generate_melting_paths(manifold_space, base_paths, (self.canvas_width, self.canvas_height))
            compiled_paths = [(x, y, flow, 1) for x, y, flow in paths_2d]  # Assign Tool 1
        elif operator == "holonomy_vortex":
            paths_2d = self.vortex_engine.generate_vortex_paths(manifold_space, base_paths, (self.canvas_width, self.canvas_height))
            compiled_paths = [(x, y, flow, 2) for x, y, flow in paths_2d]  # Assign Tool 2
        elif operator == "hallucination_curvature":
            paths_2d = self.wave_engine.generate_curvature_waves(manifold_space, base_paths, (self.canvas_width, self.canvas_height))
            compiled_paths = [(x, y, flow, 3) for x, y, flow in paths_2d]  # Assign Tool 3
        elif operator == "spectral_cascade":
            paths_2d = self.wave_engine.generate_spectral_cascades(manifold_space, base_paths, (self.canvas_width, self.canvas_height))
            compiled_paths = [(x, y, flow, 4) for x, y, flow in paths_2d]  # Assign Tool 4
        elif operator == "symbolic_drift":
            paths_2d = self.discontinuity_engine.generate_symbolic_drift(manifold_space, base_paths, (self.canvas_width, self.canvas_height))
            compiled_paths = [(x, y, flow, 5) for x, y, flow in paths_2d]  # Assign Tool 5
        elif operator == "collapse_surface":
            paths_2d = self.discontinuity_engine.generate_surface_collapses(manifold_space, base_paths, (self.canvas_width, self.canvas_height))
            compiled_paths = [(x, y, flow, 6) for x, y, flow in paths_2d]  # Assign Tool 6
        elif operator == "conceptual_fusion":
            paths_2d = self.compositional_engine.generate_conceptual_fusion(manifold_space, base_paths, (self.canvas_width, self.canvas_height))
            compiled_paths = [(x, y, flow, 7) for x, y, flow in paths_2d]  # Assign Tool 7
        elif operator == "potential_field":
            paths_2d = self.compositional_engine.generate_potential_fields(manifold_space, base_paths, (self.canvas_width, self.canvas_height))
            compiled_paths = [(x, y, flow, 8) for x, y, flow in paths_2d]  # Assign Tool 8
        elif operator == "dream_diagnostic":
            paths_2d = self.compositional_engine.generate_diagnostic_pipeline(manifold_space, base_paths, (self.canvas_width, self.canvas_height), self)
            compiled_paths = [(x, y, flow, 0) for x, y, flow in paths_2d]  # Dynamic diagnostic cycling
        else:
            print(f"[!] Operator '{operator}' unrecognized. Utilizing uniform fallback baseline loops.")
            compiled_paths = [(x, y, 0.1, 0) for x, y in base_paths]

        # Step 3: Topographic mesh correction adaptation layer
        if enable_leveling:
            self.auto_leveler.load_mesh_telemetry()
            leveled = self.auto_leveler.apply_mesh_leveling([(x, y, flow) for x, y, flow, _ in compiled_paths])
            final_paths = [(leveled[i][0], leveled[i][1], leveled[i][2], leveled[i][3], compiled_paths[i][3]) for i in range(len(compiled_paths))]
        else:
            final_paths = [(x, y, 0.0, flow, color_id) for x, y, flow, color_id in compiled_paths]

        # Step 4: Hardware step translation and multi-color G-code export
        self.hardware_compiler.compile_to_gcode(final_paths, output_gcode_path)
        return final_paths


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NDH-Surrealism Core Compiler with Active Enclave Shield")
    parser.add_argument("--input", type=str, required=True, help="Path to dream profile JSON")
    parser.add_argument("--output", type=str, required=True, help="Path to write compiled G-code")
    parser.add_argument("--no-leveling", action="store_true", help="Bypass topographic mesh adaptations")
    args = parser.parse_args()

    compiler = NDHSurrealismCompiler()
    try:
        compiler.compile_pipeline(args.input, args.output, enable_leveling=not args.no_leveling)
    except Exception as e:
        print(f"[-] Execution halted by security monitor: {e}")
