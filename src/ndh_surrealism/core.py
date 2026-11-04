import os
import json
import argparse
import numpy as np
from ndh_surrealism.engines.manifold_melting import LiquefactionFluidicsCompiler
from ndh_surrealism.engines.holonomy_vortex import RotationalVortexDrive
from ndh_surrealism.engines.spatial_wave import SpatialWaveSubsystem
from ndh_surrealism.hardware.gcode import NDHGCodeCompiler


class NDHSurrealismCompiler:

    def __init__(self, canvas_width=1000.0, canvas_height=1000.0):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        
        # Initialize processing subsystems
        self.liquefaction_engine = LiquefactionFluidicsCompiler()
        self.vortex_engine = RotationalVortexDrive()
        self.wave_engine = SpatialWaveSubsystem()
        self.hardware_compiler = NDHGCodeCompiler()
        print(f"[*] NDH-Surrealism Engine Initialized. Bounds: {canvas_width}x{canvas_height}")

    def load_dream_profile(self, profile_path):
        if not os.path.exists(profile_path):
            raise FileNotFoundError(f"Dream profile not found at {profile_path}")
        with open(profile_path, "r") as f:
            data = json.load(f)
        return data

    def extract_latent_coordinates(self, dream_data):
        raw_coords = dream_data.get("latent_coordinates", [])
        if not raw_coords:
            return np.random.randn(100, 80)
        return np.array(raw_coords)

    def compile_pipeline(self, profile_path, output_gcode_path):
        dream_data = self.load_dream_profile(profile_path)
        manifold_space = self.extract_latent_coordinates(dream_data)
        operator = dream_data.get("active_operator", "liquefaction")

        print(f"[*] Processing manifold with shape {manifold_space.shape} via '{operator}'...")

        # Step 1: Spatial layout down-projection layer
        base_paths = []
        for vector in manifold_space:
            x_proj = float(np.sin(vector) * (self.canvas_width / 2) + (self.canvas_width / 2))
            y_proj = float(np.cos(vector) * (self.canvas_height / 2) + (self.canvas_height / 2))
            base_paths.append((x_proj, y_proj))

        # Step 2: Route structural anomalies through designated modification engine
        if operator == "liquefaction":
            compiled_paths = self.liquefaction_engine.generate_melting_paths(
                manifold_space, base_paths, (self.canvas_width, self.canvas_height)
            )
        elif operator == "holonomy_vortex":
            compiled_paths = self.vortex_engine.generate_vortex_paths(
                manifold_space, base_paths, (self.canvas_width, self.canvas_height)
            )
        elif operator == "hallucination_curvature":
            compiled_paths = self.wave_engine.generate_curvature_waves(
                manifold_space, base_paths, (self.canvas_width, self.canvas_height)
            )
        elif operator == "spectral_cascade":
            compiled_paths = self.wave_engine.generate_spectral_cascades(
                manifold_space, base_paths, (self.canvas_width, self.canvas_height)
            )
        else:
            print(f"[!] Operator '{operator}' not explicitly compiled. Using uniform fallback.")
            compiled_paths = [(x, y, 0.1) for x, y in base_paths]

        # Step 3: Hardware step translation and G-code export block compilation
        self.hardware_compiler.compile_to_gcode(compiled_paths, output_gcode_path)
        return compiled_paths


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NDH-Surrealism Core Compiler")
    parser.add_argument("--input", type=str, required=True, help="Path to dream profile JSON")
    parser.add_argument("--output", type=str, required=True, help="Path to write compiled G-code")
    args = parser.parse_args()

    compiler = NDHSurrealismCompiler()
    try:
        compiler.compile_pipeline(args.input, args.output)
    except Exception as e:
        print(f"[-] Execution halted: {e}")
