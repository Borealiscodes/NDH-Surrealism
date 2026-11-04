import os
import json
import argparse
import numpy as np
from ndh_surrealism.engines.manifold_melting import LiquefactionFluidicsCompiler


class NDHSurrealismCompiler:

    def __init__(self, canvas_width=1000.0, canvas_height=1000.0):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        # Initialize sub-engines
        self.liquefaction_engine = LiquefactionFluidicsCompiler()
        print(
            f"[*] NDH-Surrealism Engine Initialized. Canvas Bounds: {canvas_width}x{canvas_height}"
        )

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

    def compile_pipeline(self, profile_path):
        """Executes full transformation and routing sequence."""
        dream_data = self.load_dream_profile(profile_path)
        manifold_space = self.extract_latent_coordinates(dream_data)
        operator = dream_data.get("active_operator", "liquefaction")

        print(f"[*] Processing manifold with shape {manifold_space.shape} via '{operator}'...")

        # Step 1: Base projection layer (Spatial mapping)
        base_paths = []
        for vector in manifold_space:
            x_proj = float(np.sin(vector[0]) * (self.canvas_width / 2) + (self.canvas_width / 2))
            y_proj = float(np.cos(vector[1]) * (self.canvas_height / 2) + (self.canvas_height / 2))
            base_paths.append((x_proj, y_proj))

        # Step 2: Route through designated hallucination modifier
        if operator == "liquefaction":
            compiled_paths = self.liquefaction_engine.generate_melting_paths(
                manifold_space, base_paths, (self.canvas_width, self.canvas_height)
            )
        else:
            # Fallback uniform pathing with neutral flow rate
            print(f"[!] Operator '{operator}' not explicitly compiled. Using uniform output.")
            compiled_paths = [(x, y, 0.1) for x, y in base_paths]

        return compiled_paths


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NDH-Surrealism Core Compiler")
    parser.add_argument("--input", type=str, required=True, help="Path to dream profile JSON")
    args = parser.parse_args()

    compiler = NDHSurrealismCompiler()
    try:
        compiler.compile_pipeline(args.input)
    except Exception as e:
        print(f"[-] Execution halted: {e}")
