import numpy as np


class LiquefactionFluidicsCompiler:

    def __init__(self, viscosity_floor=0.1, gravity_vector=(0.0, -1.0)):
        """
        Initializes the melting engine.
        viscosity_floor: Safety threshold preventing the paint flow from halting entirely.
        gravity_vector: Directional vector for fluid bleed simulation on a vertical canvas.
        """
        self.viscosity_floor = viscosity_floor
        self.gravity_vector = np.array(gravity_vector)
        print("[*] Liquefaction Engine Active: Calibrated for viscous fluidic mapping.")

    def calculate_metric_degradation(self, manifold_vectors):
        """
        Simulates metric tensor collapse across the 80D manifold arrays.
        Returns a 1D array of degradation factors scaling between 0.0 (solid) and 1.0 (liquid).
        """
        # Compute variances across the 80 dimensions to locate structural instabilities
        variances = np.var(manifold_vectors, axis=1)
        if len(variances) == 0:
            return np.array([])

        max_v = np.max(variances) if np.max(variances) > 0 else 1.0
        degradation = variances / max_v
        return degradation

    def generate_melting_paths(self, manifold_vectors, base_paths, canvas_bounds):
        """
        Transforms clean layout points into sagging, melting tool paths.
        Returns a list of tuples: (X, Y, Fluid_Flow_Rate)
        """
        degradation_factors = self.calculate_metric_degradation(manifold_vectors)
        c_width, c_height = canvas_bounds

        melted_paths = []
        for idx, (x, y) in enumerate(base_paths):
            if idx >= len(degradation_factors):
                factor = 0.0
            else:
                factor = degradation_factors[idx]

            # Calculate gravitational sag based on the local metric degradation factor
            # Higher degradation pulls the coordinate further down the gravity vector
            sag_magnitude = factor * 75.0  # Maximum pixel/mm displacement per point
            sag_offset = self.gravity_vector * sag_magnitude

            # Apply offsets while enforcing rigid boundary containment floors
            new_x = float(np.clip(x + sag_offset[0], 0.0, c_width))
            new_y = float(np.clip(y + sag_offset[1], 0.0, c_height))

            # Fluid flow parameter directly corresponds to metric fluidity
            # High degradation = open fluid valve to allow physical paint dripping
            fluid_flow = float(max(factor, self.viscosity_floor))

            melted_paths.append((new_x, new_y, fluid_flow))

        print(
            f"[+] Liquefaction mapping complete. Synthesized {len(melted_paths)} continuous fluid strokes."
        )
        return melted_paths
