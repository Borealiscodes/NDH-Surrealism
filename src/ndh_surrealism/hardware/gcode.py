import os


class NDHGCodeCompiler:

    def __init__(self, safe_travel_height=5.0, print_feedrate=1200, travel_feedrate=3000):
        """
        Initializes machine translation parameters.
        safe_travel_height: Z-axis height (mm) to lift tool-head when repositioning.
        print_feedrate: Movement speed (mm/min) while executing painting paths.
        travel_feedrate: Movement speed (mm/min) during air travels.
        """
        self.safe_z = safe_travel_height
        self.p_feed = print_feedrate
        self.t_feed = travel_feedrate
        print("[*] G-Code Production Core Ready: Configured for industrial serial plotting.")

    def compile_to_gcode(self, compiled_paths, target_output_path):
        """
        Translates continuous geometric paths into structured G-code.
        compiled_paths: List of tuples (X, Y, Fluid_Flow_Rate)
        """
        gcode_blocks = [
            "; --- START OF NDH-SURREALISM AUTOMATED PLOT ---",
            "; System Architecture: Deterministic Robotic Canvas Interface",
            "G21 ; Set units to millimeters",
            "G90 ; Absolute positioning mode",
            f"G0 Z{self.safe_z} F{self.t_feed} ; Lift tool-head to initialization safety ceiling",
            "G28 ; Home all axes safely",
            "M3 ; Engage toolhead telemetry tracking loop",
        ]

        # Tracking state to minimize redundant state commands
        is_painting = False

        for idx, (x, y, flow) in enumerate(compiled_paths):
            # Format numeric variables cleanly to preserve fractional physical precision
            x_str = f"{x:.3f}"
            y_str = f"{y:.3f}"
            
            # Map fluid flow rate directly to an extrusion or valve open command variable 'E'
            # Higher fluid values force more material throughput down the brush manifold
            e_str = f"{flow * 10.0:.4f}"

            if idx == 0:
                # Fast travel to initial boundary layout node without dropping fluid
                gcode_blocks.append(f"G0 X{x_str} Y{y_str} F{self.t_feed} ; Rapid transit to entry node")
                gcode_blocks.append("G1 Z0.0 F600 ; Lower paintbrush onto canvas surface")
                is_painting = True
                continue

            # Active continuous execution line with automated material extrusion calculation
            gcode_blocks.append(f"G1 X{x_str} Y{y_str} E{e_str} F{self.p_feed}")

        # Wind down sequence to arrest motor drive current and isolate hardware safely
        gcode_blocks.extend([
            f"G0 Z{self.safe_z} F{self.t_feed} ; Extraction lift clear of wet paint surface",
            "M5 ; Disengage toolhead telemetry tracking loop",
            "M30 ; Program end and absolute software stack reset",
            "; --- END OF NDH-SURREALISM AUTOMATED PLOT ---"
        ])

        # Write output matrix file securely to disk environment
        os.makedirs(os.path.dirname(target_output_path), exist_ok=True)
        with open(target_output_path, "w") as f:
            f.write("\n".join(gcode_blocks))
            
        print(f"[+] Hardware translation complete. Written {len(gcode_blocks)} G-code instructions securely to: {target_output_path}")
        return target_output_path
