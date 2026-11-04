import numpy as np


class RotationalVortexDrive:

    def __init__(self, twist_intensity=2.5):
        """
        Initializes the vortex engine.
        twist_intensity: Controls how tightly wrapped the generated spiral trajectories are.
        """
        self.twist_intensity = twist_intensity
        print("[*] Rotational Vortex Drive Active: Calibrated for holonomy spiral mapping.")

    def calculate_cumulative_holonomy(self, manifold_vectors):
        """
        Calculates the rotational twist accumulated between sequential 80D vectors.
        Returns a 1D array of cumulative angular offsets in radians.
        """
        num_vectors = len(manifold_vectors)
        if num_vectors < 2:
            return np.zeros(num_vectors)

        angles = [0.0]
        cumulative_twist = 0.0

        for i in range(1, num_vectors):
            v1 = manifold_vectors[i - 1]
            v2 = manifold_vectors[i]

            # Calculate the cosine similarity between sequential high-dimensional states
            denom = np.linalg.norm(v1) * np.linalg.norm(v2)
            dot_prod = np.dot(v1, v2)
            cos_sim = np.clip(dot_prod / denom if denom > 0 else 1.0, -1.0, 1.0)

            # Angular drift acts as the local geometric phase change (twist)
            angular_drift = np.arccos(cos_sim)
            cumulative_twist += angular_drift * self.twist_intensity
            angles.append(cumulative_twist)

        return np.array(angles)

    def generate_vortex_paths(self, manifold_vectors, base_paths, canvas_bounds):
        """
        Transforms standard linear coordinate layouts into swirling holonomy vortices.
        Returns a list of tuples: (X, Y, Fluid_Flow_Rate)
        """
        angular_twists = self.calculate_cumulative_holonomy(manifold_vectors)
        c_width, c_height = canvas_bounds
        center_x, center_y = c_width / 2.0, c_height / 2.0

        vortex_paths = []
        for idx, (x, y) in enumerate(base_paths):
            theta = angular_twists[idx] if idx < len(angular_twists) else 0.0

            # Calculate the initial distance (radius) from the canvas center point
            dx, dy = x - center_x, y - center_y
            radius = np.sqrt(dx**2 + dy**2)

            # Apply a 2D rotational matrix transformation driven by the accumulated 80D holonomy
            new_x = center_x + radius * np.cos(theta)
            new_y = center_y + radius * np.sin(theta)

            # Secure coordinates inside physical canvas frame boundaries
            clamped_x = float(np.clip(new_x, 0.0, c_width))
            clamped_y = float(np.clip(new_y, 0.0, c_height))

            # Flow rate correlates with the rotational velocity (faster twist = thicker lines)
            local_velocity = np.abs(np.sin(theta))
            fluid_flow = float(0.2 + (local_velocity * 0.6))

            vortex_paths.append((clamped_x, clamped_y, fluid_flow))

        print(
            f"[+] Vortex spiral compilation complete. Transformed {len(vortex_paths)} points into spiral trajectories."
        )
        return vortex_paths
