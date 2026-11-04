import os


class NDHGCodeCompiler:

    def __init__(self, safe_travel_height=5.0, print_feedrate=1200, travel_feedrate=3000):
        self.safe_z = safe_travel_height
        self.p_feed = print_feedrate
        self.t_feed = travel_feedrate
        print("[*] G-Code Production Core Ready: Configured for industrial serial plotting.")

    def compile_to_gcode(self, compiled_paths, target_output_path):
        gcode_blocks = [
            "; --- START OF NDH-SURREALISM AUTOMATED PLOT ---",
            "G21 ; Set units to millimeters",
            "G90 ; Absolute positioning mode",
            f"G0 Z{self.safe_z} F{self.t_feed} ; Lift tool-head clear",
            "G28 ; Home all axes safely",
            "M3 ; Engage tracking loop",
        ]

        is_painting = False

        for idx, (x, y, flow) in enumerate(compiled_paths):
            x_str = f"{x:.3f}"
            y_str = f"{y:.3f}"

            # Intercept topological collapse states
            if flow == 0.0:
                if is_painting:
                    gcode_blocks.append(f"G0 Z{self.safe_z} F{self.t_feed} ; Lift tool-head: Surface Collapse Encountered")
                    is_painting = False
                gcode_blocks.append(f"G0 X{x_str} Y{y_str} F{self.t_feed} ; Air travel past void boundary")
                continue

            # Return to painting domain if previously lifted
            if not is_painting:
                gcode_blocks.append(f"G0 X{x_str} Y{y_str} F{self.t_feed}")
                gcode_blocks.append("G1 Z0.0 F600 ; Lower paintbrush back onto canvas")
                is_painting = True

            e_str = f"{flow * 10.0:.4f}"
            gcode_blocks.append(f"G1 X{x_str} Y{y_str} E{e_str} F{self.p_feed}")

        gcode_blocks.extend([
            f"G0 Z{self.safe_z} F{self.t_feed} ; Final extraction lift",
            "M5 ; Disengage tracking loop",
            "M30 ; Reset program",
            "; --- END OF NDH-SURREALISM AUTOMATED PLOT ---"
        ])

        os.makedirs(os.path.dirname(target_output_path), exist_ok=True)
        with open(target_output_path, "w") as f:
            f.write("\n".join(gcode_blocks))
            
        return target_output_path
