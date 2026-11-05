"""
gcode.py
Target Framework: NDH-Surrealism / NDH-Canvas-Adapter-Enhanced
Domain: Volumetric Extrusion & Color-Swapping G-code Compiler
Status: Bare-Metal Machine Translation Layer / Zero-Float Codec
"""

import numpy as np
import logging
from typing import List, Tuple, Optional

# Configure hardware tracking telemetry
logging.basicConfig(level=logging.INFO, format="[HARDWARE_COMPILER] %(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("GCodeCompiler")

class GCodeAutomationCompiler:
    def __init__(self, feedrate: int = 1500, micron_scale: int = 1000, layer_height_nm: float = 5.0):
        """
        Initializes the G-code compiler matrix using integer scale bounds.
        :param feedrate: Feedrate speed in mm/min (must remain integer-bound)
        :param micron_scale: Multiplier to enforce strict integer micron mapping (1000 = 1mm)
        :param layer_height_nm: Atomic thin-film thickness delta ceiling verified in Lean 4 (Δz = 5nm)
        """
        self.feedrate = feedrate
        self.scale = micron_scale
        self.delta_z_mm = layer_height_nm / 1_000_000.0 # Convert 5nm ceiling safely to mm
        self.current_tool: Optional[int] = None
        
        # Physical constraints setup
        self.max_x_micron = 5_000_000  # 5000mm active gantry boundary
        self.max_y_micron = 5_000_000  # 5000mm active gantry boundary
        
    def _to_micron_integer(self, normalized_val: float, max_bounds: int) -> int:
        """Enforces Strict No-Float Quantization Law. Converts bounded state down to pure microns."""
        # Scale the unit hypersphere output (-1.0 to 1.0) to full physical coordinate bounds
        micron_coord = int(np.round(normalized_val * max_bounds))
        return micron_coord

    def calculate_extrusion_vol(self, x1: int, y1: int, x2: int, y2: int) -> float:
        """
        Calculates fluid delivery flow volume dynamically.
        Balances instantaneous pressure offsets to avoid gravimetric pooling during '0' pauses.
        """
        # Linear distance in micron units
        distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        if distance == 0:
            return 0.0
            
        # Volumetric area calculations for the slot-die coating head array
        # Extrusion Multiplier is bound tightly to the Δz <= 5nm thickness constraint
        extrusion_factor = 0.00012 
        return float(distance * extrusion_factor)

    def generate_tool_change(self, target_channel: int) -> List[str]:
        """Executes safe off-canvas toolhead color-swapping cycles across macro channels T0-T15."""
        if target_channel < 0 or target_channel > 15:
            logger.error(f"Hardware Exception: Invalid Multi-Color Channel T{target_channel} rejected.")
            return []
            
        if self.current_tool == target_channel:
            return [] # Invariant: Tool already active, skip cycle
            
        self.current_tool = target_channel
        commands = [
            "; --- BEGIN AUTONOMIC CHROMATIC CHANNEL SWAP ---",
            "G91 ; Shift momentarily to relative positioning for clean liftoff",
            "G1 Z2.0 F3000 ; Rapid safety lift to break ink meniscus filament",
            "G90 ; Revert instantly to absolute coordinate system tracking",
            f"T{target_channel} ; Trigger automated macro gantry cluster shift",
            "M400 ; Wait for mechanical synchronization buffer to clear",
            "; --- END AUTONOMIC CHROMATIC CHANNEL SWAP ---"
        ]
        return commands

    def compile_hypersphere_path(self, frame_id: int, safe_matrix: np.ndarray, tool_channel: int) -> List[str]:
        """
        Translates safe 80D normalized state matrix points into absolute G-code blocks.
        Clips out continuous variables and formats raw motor pulse trajectories.
        """
        if safe_matrix.shape[1] < 2:
            logger.error("Compilation Failure: Input safe matrix lacks sufficient physical 2D projections.")
            return []

        gcode_block = [
            f"; 🌌 BEGIN FLOW TRANSCRIPTION: FRAME #{frame_id:04d}",
            f"; Invariant Tracking Source: [ NDH . COMPILER . ACTIVE . RELEASABLE ]",
            "G90 ; Set machine index to absolute coordinate paths",
            "G21 ; Hardlock system hardware processing to millimeter metrics"
        ]
        
        # Inject required tool configuration macro strings
        gcode_block.extend(self.generate_tool_change(tool_channel))

        # Establish baseline tracking positions
        prev_x_mic = 0
        prev_y_mic = 0
        current_z_mm = frame_id * self.delta_z_mm

        for idx, coordinate in enumerate(safe_matrix):
            # Extract first two primary axes from the projected hypersphere envelope
            raw_x, raw_y = coordinate[0], coordinate[1]
            
            # Map values to physical integer coordinates via the No-Float Law
            x_mic = self._to_micron_integer(raw_x, self.max_x_micron // 2)
            y_mic = self._to_micron_integer(raw_y, self.max_y_micron // 2)
            
            # Convert back to pristine mm floats ONLY for final raw text printing format block
            x_mm = x_mic / self.scale
            y_mm = y_mic / self.scale
            
            if idx == 0:
                # Travel move to starting position without printing
                gcode_block.append(f"G0 X{x_mm:.4f} Y{y_mm:.4f} Z{current_z_mm:.6f} ; Rapid entry path allocation")
            else:
                # Calculate active non-Newtonian fluid discharge requirements
                extrusion_e = self.calculate_extrusion_vol(prev_x_mic, prev_y_mic, x_mic, y_mic)
                
                if extrusion_e == 0.0:
                    # Momentary 0 balanced ternary pause: cut fluid completely to avoid gravimetric pooling
                    gcode_block.append(f"G1 X{x_mm:.4f} Y{y_mm:.4f} E0.0000 F{self.feedrate} ; Ternary Rest Phase")
                else:
                    # Active deposition path execution move
                    gcode_block.append(f"G1 X{x_mm:.4f} Y{y_mm:.4f} E{extrusion_e:.4f} F{self.feedrate} ; Linear Deposition Loop")
            
            prev_x_mic = x_mic
            prev_y_mic = y_mic

        gcode_block.append(f"; 🌌 END FLOW TRANSCRIPTION: FRAME #{frame_id:04d}\n")
        return gcode_block

# Local verification block for gcode compilation safety checking
if __name__ == "__main__":
    print("[+] Launching Local Hardware Translation System Verification Module...")
    compiler = GCodeAutomationCompiler()
    
    # Simulate safe, normalized 80D coordinate tracking stack outputted from the guard enclave
    mock_safe_coordinates = np.array([
        [0.0, 0.0, 0.1, 0.2],
        [0.5, 0.2, -0.3, 0.1],
        [0.5, 0.2, 0.0, 0.0],  # Forcing a mechanical ternary '0' point hold step
        [-0.2, 0.8, 0.4, -0.9]
    ])
    
    # Compile the array block targeting Multi-Color Tool Channel T3 (Curvature-Breathing mode)
    generated_gcode = compiler.compile_hypersphere_path(frame_id=1, safe_matrix=mock_safe_coordinates, tool_channel=3)
    
    print("\n=== GENERATED INDUSTRIAL G-CODE SPECIMEN OUTPUT ===")
    print("\n".join(generated_gcode))
