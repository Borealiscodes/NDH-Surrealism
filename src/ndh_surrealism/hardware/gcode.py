import os


class NDHGCodeCompiler:

    def __init__(self, safe_travel_height=5.0, print_feedrate=1200, travel_feedrate=3000):
        self.safe_z = safe_travel_height
        self.p_feed = print_feedrate
        self.t_feed = travel_feedrate
        print("[*] G-Code Production Core Ready: Volumetric fluid scaling active.")

    def compile_to_gcode(self, compiled_paths, target_output_path):
        gcode_blocks = [
            "; --- START OF UPGRADED NDH-SURREALISM AUTOMATED PLOT ---",
            "G21 ; Set units to millimeters",
            "G90 ; Absolute positioning mode",
            "M82 ; Set fluid extrusion to absolute mode",
            f"G0 Z{self.safe_z} F{self.t_feed} ; Lift tool-head to safety ceiling",
            "G28 ; Home all axes safely",
            "M3 ; Engage toolhead fluid pump driver telemetry",
            "G92 E0.0 ; Reset fluid extrusion tracking baseline",
        ]

        is_painting = False
        cumulative_e = 0.0

        for idx, (x, y, z, flow) in enumerate(compiled_paths):
            x_str = f"{x:.3f}"
            y_str = f"{y:.3f}"
            z_str = f"{z:.3f}" # Parse the leveled surface contour depth metric

            if flow == 0.0:
                if is_painting:
                    cumulative_e -= 1.5
                    gcode_blocks.extend([
                        f"G1 E{cumulative_e:.4f} F1800 ; Retract fluid to prevent drips",
                        f"G0 Z{self.safe_z} F{self.t_feed} ; Rapid lift to safety clear",
                    ])
                    is_painting = False
                gcode_blocks.append(f"G0 X{x_str} Y{y_str} F{self.t_feed} ; Travel over void space")
                continue

            if not is_painting:
                cumulative_e += 1.5
                gcode_blocks.extend([
                    f"G0 X{x_str} Y{y_str} F{self.t_feed} ; Transit to entry node",
                    f"G1 Z{z_str} F600 ; Lower brush to calculated terrain height",
                    f"G1 E{cumulative_e:.4f} F1200 ; Prime fluid valve back to surface baseline",
                ])
                is_painting = True

            e_step = flow * 2.0  
            cumulative_e += e_step
            dynamic_feed = int(self.p_feed * (1.2 - flow))

            # Upgraded Feature: Dynamic spatial trajectory trace containing active mesh leveling Z coordinates
            gcode_blocks.append(f"G1 X{x_str} Y{y_str} Z{z_str} E{cumulative_e:.4f} F{dynamic_feed}")

        cumulative_e -= 2.0
        gcode_blocks.extend([
            f"G1 E{cumulative_e:.4f} F1800 ; Final fluid retract check",
            f"G0 Z{self.safe_z} F{self.t_feed} ; Extraction lift clear of canvas",
            "M5 ; Disengage toolhead fluid pump driver telemetry",
            "M30 ; Absolute program reset",
            "; --- END OF UPGRADED NDH-SURREALISM AUTOMATED PLOT ---"
        ])

        os.makedirs(os.path.dirname(target_output_path), exist_ok=True)
        with open(target_output_path, "w") as f:
            f.write("\n".join(gcode_blocks))
            
        print(f"[+] Compiled upgraded leveled G-code file -> {target_output_path}")
        return target_output_path
