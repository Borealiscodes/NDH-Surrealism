import numpy as np


class CanvasAutoLeveler:

    def __init__(self, grid_size=3, canvas_bounds=(1000.0, 1000.0)):
        """
        grid_size: Number of probe points per axis (3x3 = 9 sampling nodes)
        """
        self.grid_size = grid_size
        self.bounds = canvas_bounds
        # Initialize a flat terrain map baseline (all heights at 0.0mm)
        self.height_map = np.zeros((grid_size, grid_size))
        print(f"[*] Auto-Leveling Subsystem Armed: Configured for {grid_size}x{grid_size} mesh mapping.")

    def load_mesh_telemetry(self, simulated_matrix=None):
        """
        Simulates reading height probe deflections from the sensor grid.
        Positive variables mean the canvas bows outward; negative values mean a sag.
        """
        if simulated_matrix is not None:
            self.height_map = np.array(simulated_matrix)
        else:
            # Emulate slight center warping (+1.4mm warp in the middle of the canvas)
            self.height_map = np.array([
                [0.0,  0.2,  0.0],
                [0.3,  1.4,  0.2],
                [0.0,  0.1,  0.0]
            ])
        print("[+] Canvas topographic height-map registered successfully.")

    def apply_mesh_leveling(self, compiled_paths):
        """
        Applies bilinear interpolation to dynamically adjust Z height 
        relative to the toolhead's absolute X/Y positions.
        Returns a list of tuples: (X, Y, Z_Corrected, Fluid_Flow)
        """
        leveled_paths = []
        c_width, c_height = self.bounds
        
        # Calculate spacing grid intervals
        x_ticks = np.linspace(0.0, c_width, self.grid_size)
        y_ticks = np.linspace(0.0, c_height, self.grid_size)

        for x, y, flow in compiled_paths:
            if flow == 0.0:
                # Retain structural rapid lifts without modification
                leveled_paths.append((x, y, flow))
                continue

            # Locate position indices inside the mesh grid cells
            x_idx = np.searchsorted(x_ticks, x) - 1
            y_idx = np.searchsorted(y_ticks, y) - 1
            
            x_idx = int(np.clip(x_idx, 0, self.grid_size - 2))
            y_idx = int(np.clip(y_idx, 0, self.grid_size - 2))

            # Fetch the 4 corner height coordinates for bilinear interpolation
            z00 = self.height_map[y_idx, x_idx]
            z10 = self.height_map[y_idx, x_idx + 1]
            z01 = self.height_map[y_idx + 1, x_idx]
            z11 = self.height_map[y_idx + 1, x_idx + 1]

            # Calculate relative distance parameters inside the current cell grid
            x_ratio = (x - x_ticks[x_idx]) / (x_ticks[x_idx + 1] - x_ticks[x_idx])
            y_ratio = (y - y_ticks[y_idx]) / (y_ticks[y_idx + 1] - y_ticks[y_idx])

            # Bilinear interpolation equation mapping
            z_offset = (1 - x_ratio) * (1 - y_ratio) * z00 + \
                       x_ratio * (1 - y_ratio) * z10 + \
                       (1 - x_ratio) * y_ratio * z01 + \
                       x_ratio * y_ratio * z11

            # Append the corrected Z coordinate vector path
            leveled_paths.append((x, y, float(z_offset), flow))

        print(f"[+] Topographic leveling applied. Warped {len(leveled_paths)} vectors to canvas surface profiles.")
        return leveled_paths
