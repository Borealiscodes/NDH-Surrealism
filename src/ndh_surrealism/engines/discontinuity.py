import numpy as np


class DiscontinuitySubsystem:

    def __init__(self, drift_scale=45.0, collapse_threshold=0.15):
        """
        Initializes the discontinuity engine.
        drift_scale: Max physical pixel/mm translation shift for Operator 05.
        collapse_threshold: Matrix threshold below which Operator 08 breaks tracking.
        """
        self.drift_scale = drift_scale
        self.collapse_thresh = collapse_threshold
        print("[*] Discontinuity Subsystem Active: Drift & Collapse mechanics operational.")

    def generate_symbolic_drift(self, manifold_vectors, base_paths, canvas_bounds):
        """
        Operator 05: Injects un-rectified coordinate displacements to simulate dream logic.
        """
        c_width, c_height = canvas_bounds
        drift_paths = []
        cumulative_x = 0.0
        cumulative_y = 0.0

        for idx, (x, y) in enumerate(base_paths):
            if idx > 0 and idx < len(manifold_vectors):
                # Calculate the directional variance step
                step_variance = np.std(manifold_vectors[idx] - manifold_vectors[idx - 1])
                if step_variance > 0.8:
                    # Append an un-rectified phase jump
                    cumulative_x += np.sin(idx) * self.drift_scale
                    cumulative_y += np.cos(idx) * self.drift_scale

            new_x = float(np.clip(x + cumulative_x, 0.0, c_width))
            new_y = float(np.clip(y + cumulative_y, 0.0, c_height))
            drift_paths.append((new_x, new_y, 0.35))

        print(f"[+] Operator 05: Compiled {len(drift_paths)} coordinate lines with tracking drift.")
        return drift_paths

    def generate_surface_collapses(self, manifold_vectors, base_paths, canvas_bounds):
        """
        Operator 08: Forces rapid tool lifts when the metric tensor approaches zero.
        """
        c_width, c_height = canvas_bounds
        collapse_paths = []

        for idx, (x, y) in enumerate(base_paths):
            if idx >= len(manifold_vectors):
                norm_val = 1.0
            else:
                # Approximate metric density using local vector bounds
                norm_val = float(np.linalg.norm(manifold_vectors[idx]))

            if norm_val < self.collapse_thresh:
                # Manifold collapse detected. Force fluid throttling to absolute zero
                # The hardware compiler intercepts fluid=0.0 to execute a mechanical rapid tool-lift
                fluid_flow = 0.0
            else:
                fluid_flow = 0.45

            collapse_paths.append((float(np.clip(x, 0.0, c_width)), float(np.clip(y, 0.0, c_height)), fluid_flow))

        print(f"[+] Operator 08: Synthesized {len(collapse_paths)} points containing structural safety floor cuts.")
        return collapse_paths
