import os


class NDHGCodeCompiler:

    def __init__(self, safe_travel_height=5.0, print_feedrate=1200, travel_feedrate=3000):
        self.safe_z = safe_travel_height
        self.p_feed = print_feedrate
        self.t_feed = travel_feedrate
        # Define a physical off-canvas clean station coordinate zone
        self.rinse_station_x = -50.0
        self.rinse_station_y = -50.0
        print("[*] Upgraded Multi-Color G-Code Core Ready: Tool-changing macros active.")

    def compile_to_gcode(self, compiled_paths, target_output_path):
        """
        Translates multi-operator paths into color-swapped G-code sequences.
        Paths are expected to include a color index parameter: (X, Y, Z, Flow, Color_ID)
        """
        gcode_blocks = [
            "; --- START OF MULTI-COLOR NDH-SURREALISM PLOT ---",
            "G21 ; Set units to millimeters",
            "G90 ; Absolute positioning mode",
            "M82 ; Set fluid extrusion to absolute mode",
            f"G0 Z{self.safe_z} F{self.t_feed} ; Lift tool-head to safety ceiling",
            "G28 ; Home all axes safely",
            "T0 ; Select baseline default tool head channel",
            "G92 E0.0 ; Reset fluid extrusion tracking",
        ]

        current_tool = 0
        is_painting = False
        cumulative_e = 0.0

        for idx, (x, y, z, flow, color_id) in enumerate(compiled_paths):
            x_str = f"{x:.3f}"
            y_str = f"{y:.3f}"
            z_str = f"{z:.3f}"

            # ⚠️ CRITICAL UPGRADE: Automated Off-Canvas Tool Changing Macro
            if color_id != current_tool:
                if is_painting:
                    # Retract current paint line before lifting
                    cumulative_e -= 2.0
                    gcode_blocks.append(f"G1 E{cumulative_e:.4f} F1800 ; Retract current color tool")
                    gcode_blocks.append(f"G0 Z{self.safe_z} F{self.t_feed} ; Clear canvas surface")
                    is_painting = False
                
                # Transit rapidly to the off-canvas cleaning basin coordinates
                gcode_blocks.extend([
                    f"G0 X{self.rinse_station_x:.3f} Y{self.rinse_station_y:.3f} F{self.t_feed} ; Transit to clean tank",
                    f"T{color_id} ; Execute hardware toolhead/pump channel switch",
                    "G92 E0.0 ; Reset extrusion coordinate baseline for the new line",
                ])
                cumulative_e = 0.0
                current_tool = color_id

            if flow == 0.0:
                if is_painting:
                    cumulative_e -= 1.5
                    gcode_blocks.extend([
                        f"G1 E{cumulative_e:.4f} F1800 ; Retract paint to clear void",
                        f"G0 Z{self.safe_z} F{self.t_feed} ; Rapid lift",
                    ])
                    is_painting = False
                gcode_blocks.append(f"G0 X{x_str} Y{y_str} F{self.t_feed} ; Air travel")
                continue

            if not is_painting:
                cumulative_e += 1.5
                gcode_blocks.extend([
                    f"G0 X{x_str} Y{y_str} F{self.t_feed} ; Transit to edge entry",
                    f"G1 Z{z_str} F600 ; Lower brush onto terrain",
                    f"G1 E{cumulative_e:.4f} F1200 ; Prime new color channel",
                ])
                is_painting = True

            e_step = flow * 2.0  
            cumulative_e += e_step
            dynamic_feed = int(self.p_feed * (1.2 - flow))

            gcode_blocks.append(f"G1 X{x_str} Y{y_str} Z{z_str} E{cumulative_e:.4f} F{dynamic_feed}")

        # Safe extraction wind-down sequence
        cumulative_e -= 2.0
        gcode_blocks.extend([
            f"G1 E{cumulative_e:.4f} F1800 ; Final fluid retract check",
            f"G0 Z{self.safe_z} F{self.t_feed} ; Extraction lift clear of canvas",
            "M30 ; Absolute program reset",
            "; --- END OF MULTI-COLOR NDH-SURREALISM PLOT ---"
        ])

        os.makedirs(os.path.dirname(target_output_path), exist_ok=True)
        with open(target_output_path, "w") as f:
            f.write("\n".join(gcode_blocks))
            
        print(f"[+] Compiled multi-color G-code file -> {target_output_path}")
        return target_output_path
