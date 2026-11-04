import numpy as np


class SpatialWaveSubsystem:

    def __init__(self, wave_frequency=5.0, recursion_depth=3):
        """
        Initializes the spatial wave subsystem.
        wave_frequency: Throttles the concentric pulse density for Operator 01.
        recursion_depth: Sets the maximum nested fractional splits for Operator 06.
        """
        self.wave_freq = wave_frequency
        self.rec_depth = recursion_depth
        print("[*] Spatial Wave Subsystem Engaged: Curvature & Spectral Cascade loops active.")

    def generate_curvature_waves(self, manifold_vectors, base_paths, canvas_bounds):
        """
        Operator 01: Maps manifold metric spikes to expanding concentric breathing lines.
        """
        c_width, c_height = canvas_bounds
        center_x, center_y = c_width / 2.0, c_height / 2.0
        
        # Determine global tension spikes via vector norms
        tension_factors = np.linalg.norm(manifold_vectors, axis=1)
        max_tension = np.max(tension_factors) if np.max(tension_factors) > 0 else 1.0

        wave_paths = []
        for idx, (x, y) in enumerate(base_paths):
            factor = tension_factors[idx] / max_tension if idx < len(tension_factors) else 0.5
            
            dx, dy = x - center_x, y - center_y
            radius = np.sqrt(dx**2 + dy**2)
            
            # Apply a harmonic radial expansion factor mimicking 'breathing' walls
            pulse = np.sin(radius * (self.wave_freq / 100.0) * factor) * (50.0 * factor)
            new_radius = radius + pulse

            # Re-project coordinate paths out from the canvas center
            theta = np.arctan2(dy, dx) if radius > 0 else 0.0
            new_x = float(np.clip(center_x + new_radius * np.cos(theta), 0.0, c_width))
            new_y = float(np.clip(center_y + new_radius * np.sin(theta), 0.0, c_height))
            
            # Modulate line thickness (fluid flow) with breathing velocity
            fluid_flow = float(0.3 + 0.5 * np.abs(np.cos(theta)))
            wave_paths.append((new_x, new_y, fluid_flow))

        print(f"[+] Operator 01: Compiled {len(wave_paths)} pulsating curvature points.")
        return wave_paths

    def generate_spectral_cascades(self, manifold_vectors, base_paths, canvas_bounds):
        """
        Operator 06: Implements eigenvalue chain reactions as recursive sub-stroke offsets.
        """
        c_width, c_height = canvas_bounds
        cascade_paths = []

        # Simulate secondary eigenmode splits using differential differences
        for idx, (x, y) in enumerate(base_paths):
            cascade_paths.append((x, y, 0.4))
            
            if idx == 0 or idx >= len(manifold_vectors):
                continue

            # Compute local high-dimensional perturbation step
            diff = np.linalg.norm(manifold_vectors[idx] - manifold_vectors[idx - 1])
            if diff > 1.5:  # High cascade split threshold triggered
                for depth in range(1, self.rec_depth + 1):
                    # Inject nested sub-strokes scaled inversely by recursion depth
                    fractal_offset = (diff * 10.0) / depth
                    cx = float(np.clip(x + np.sin(depth) * fractal_offset, 0.0, c_width))
                    cy = float(np.clip(y + np.cos(depth) * fractal_offset, 0.0, c_height))
                    cascade_paths.append((cx, cy, float(0.2 / depth)))

        print(f"[+] Operator 06: Expanded baseline to {len(cascade_paths)} points via fractal recursion loops.")
        return cascade_paths
