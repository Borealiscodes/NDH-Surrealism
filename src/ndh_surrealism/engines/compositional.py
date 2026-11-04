import numpy as np


class CompositionalSubsystem:

    def __init__(self, attraction_strength=0.4, blend_ratio=0.5):
        self.attraction_strength = attraction_strength
        self.blend_ratio = blend_ratio
        print("[*] Compositional Subsystem Active: Multi-Field clustering initialized.")

    def generate_conceptual_fusion(self, manifold_vectors, base_paths, canvas_bounds):
        """
        Operator 02: Blends disparate coordinates into a singular chimera path.
        """
        c_width, c_height = canvas_bounds
        fused_paths = []
        num_points = len(base_paths)

        for idx, (x, y) in enumerate(base_paths):
            # Mirror blend coordinates from the tail end of the path array
            alt_idx = num_points - 1 - idx
            alt_x, alt_y = base_paths[alt_idx]

            new_x = float(np.clip((1 - self.blend_ratio) * x + self.blend_ratio * alt_x, 0.0, c_width))
            new_y = float(np.clip((1 - self.blend_ratio) * y + self.blend_ratio * alt_y, 0.0, c_height))
            fused_paths.append((new_x, new_y, 0.4))

        print(f"[+] Operator 02: Synthesized {len(fused_paths)} blended conceptual fusion strokes.")
        return fused_paths

    def generate_potential_fields(self, manifold_vectors, base_paths, canvas_bounds):
        """
        Operator 03: Attracts tool-paths toward high-density attractor wells.
        """
        c_width, c_height = canvas_bounds
        attractor_well = np.array([c_width * 0.5, c_height * 0.5])  # Center gravitational well
        field_paths = []

        for idx, (x, y) in enumerate(base_paths):
            current_pos = np.array([x, y])
            # Pull coordinates toward the localized attractor center point
            pull_vector = attractor_well - current_pos
            adjusted_pos = current_pos + (pull_vector * self.attraction_strength)

            new_x = float(np.clip(adjusted_pos[0], 0.0, c_width))
            new_y = float(np.clip(adjusted_pos[1], 0.0, c_height))
            field_paths.append((new_x, new_y, 0.5))

        print(f"[+] Operator 03: Grouped {len(field_paths)} nodes within the core potential field.")
        return field_paths

    def generate_diagnostic_pipeline(self, manifold_vectors, base_paths, canvas_bounds, core_compiler):
        """
        Operator 09: Unified fingerprint loop aggregating multiple operators sequentially.
        """
        print("[*] Operator 09: Running multi-kernel dream diagnostics sequence...")
        chunk_size = max(1, len(base_paths) // 4)
        diagnostic_paths = []

        # Segment the pathing array into distinct sub-operator profiles
        for i in range(0, len(base_paths), chunk_size):
            chunk_m = manifold_vectors[i:i + chunk_size]
            chunk_b = base_paths[i:i + chunk_size]
            segment_id = i // chunk_size

            if segment_id == 0:
                diagnostic_paths.extend(core_compiler.liquefaction_engine.generate_melting_paths(chunk_m, chunk_b, canvas_bounds))
            elif segment_id == 1:
                diagnostic_paths.extend(core_compiler.vortex_engine.generate_vortex_paths(chunk_m, chunk_b, canvas_bounds))
            elif segment_id == 2:
                diagnostic_paths.extend(core_compiler.wave_engine.generate_curvature_waves(chunk_m, chunk_b, canvas_bounds))
            else:
                diagnostic_paths.extend(self.generate_potential_fields(chunk_m, chunk_b, canvas_bounds))

        return diagnostic_paths
