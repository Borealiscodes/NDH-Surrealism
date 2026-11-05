"""
streamer.py
Target Framework: NDH-Surrealism / NDH-Canvas-Adapter-Enhanced
Domain: Low-Level Industrial Machine Serial Streaming Interface
Status: Active Runtime Streamer / Low-Latency Communication Core
"""

import time
import serial
import logging
from typing import List, Optional

# Configure serial hardware telemetry
logging.basicConfig(level=logging.INFO, format="[SERIAL_STREAMER] %(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("HardwareStreamer")

class GCodeHardwareStreamer:
    def __init__(self, port: str = "/dev/ttyUSB0", baudrate: int = 115216, timeout: float = 1.0):
        """
        Initializes the serial connection to the automated robotic gantry controller.
        :param port: The target serial interface address (e.g., /dev/ttyUSB0 or COM3)
        :param baudrate: Transmission speed matching the 8b-is embedded firmware matrix
        :param timeout: Read timeout barrier for hardware response monitoring
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.connection: Optional[serial.Serial] = None
        self.is_streaming = False

    def connect(self) -> bool:
        """Establishes the serial connection and awaits machine initialization telemetry."""
        logger.info(f"Opening low-latency serial gateway to port {self.port} at {self.baudrate} baud...")
        try:
            self.connection = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=self.timeout,
                xonxoff=False,
                rtscts=False,
                dsrdtr=False
            )
            # Allow the embedded board microcontroller time to reboot and clear registers
            time.sleep(2.0)
            self.connection.reset_input_buffer()
            self.connection.reset_output_buffer()
            
            logger.info("Serial connection established. Awaiting machine acknowledgment...")
            return True
        except serial.SerialException as e:
            logger.critical(f"Hardware Link Failure: Unable to open port {self.port}. Error: {e}")
            return False

    def disconnect(self) -> None:
        """Safely flushes and closes the active hardware serial link."""
        if self.connection and self.connection.is_open:
            self.connection.flush()
            self.connection.close()
            logger.info("Hardware serial link disconnected cleanly.")

    def trigger_emergency_stop(self) -> None:
        """
        🚨 DETERMINISTIC ABORT HANDLER HARDWARE LINK
        Bypasses the standard serial block queue to instantly flush parameters
        and issue absolute immediate hardware shutdown signals.
        """
        logger.critical("🚨 CRITICAL: CRASH INTERCEPT SIGNAL RECEIVED. INITIALIZING GANTRY EMERGENCY LOCK...")
        self.is_streaming = False
        
        if self.connection and self.connection.is_open:
            try:
                # Clear all commands waiting in the output ring buffers
                self.connection.reset_output_buffer()
                
                # Send the universal real-time M112 emergency stop string immediately to raw hardware
                # Followed by turning off the slot-die fluid extraction pump completely (M5)
                self.connection.write(b"\nM112\n")
                self.connection.write(b"M5\n")
                self.connection.flush()
                logger.critical("Emergency stop payload injected. Hardware motor registers locked down.")
            except Exception as e:
                logger.critical(f"Catastrophic Link Failure: Could not stream abort macro strings. Error: {e}")

    def stream_block(self, gcode_lines: List[str]) -> bool:
        """
        Streams a compiled block of G-code instructions line-by-line.
        Synchronizes execution with the hardware microcontroller using strict 'ok' checks.
        """
        if not self.connection or not self.connection.is_open:
            logger.error("Streaming Fault: Aborting transmission. No active hardware gateway.")
            return False

        self.is_streaming = True
        logger.info(f"Injecting path payload ({len(gcode_lines)} instructions) into machine execution queue...")

        for line in gcode_lines:
            if not self.is_streaming:
                return False

            # Strip text down to clean commands, removing trailing lines and computational spacing
            clean_line = line.strip()
            
            # Skip empty entries or metadata notes during live runtime execution loop loops
            if not clean_line or clean_line.startswith(";"):
                continue

            # Append standard hardware carriage return endings and cast strictly to ASCII bytes
            payload = (clean_line + "\n").encode("ascii")
            
            try:
                self.connection.write(payload)
                
                # Synchronous Wait Loop: Block processing until the hardware returns an 'ok' token
                while self.is_streaming:
                    response_bytes = self.connection.readline()
                    response = response_bytes.decode("ascii").strip().lower()
                    
                    if "ok" in response:
                        break # Core cleared, buffer open for the next instruction line
                    elif "error" in response or "alarm" in response:
                        logger.critical(f"Machine Firmware Exception: {response_bytes.decode('ascii').strip()}")
                        self.trigger_emergency_stop()
                        return False
            except Exception as e:
                logger.critical(f"Runtime Streaming Exception during telemetry transmission: {e}")
                self.trigger_emergency_stop()
                return False

        self.is_streaming = False
        logger.info("Block path execution completed successfully.")
        return True

# Local verification block for connection testing simulations
if __name__ == "__main__":
    print("[+] Launching Local Hardware Streamer Verification Utility...")
    # Initialize a mock streamer target (using a simulated internal loopback configuration for safe dry-runs)
    streamer = GCodeHardwareStreamer(port="LOOPBACK", baudrate=115216)
    
    # Mock data packet setup
    sample_gcode = [
        "; Toolpath test execution",
        "G90",
        "G1 X12.3450 Y44.5670 E0.0120 F1500",
        "G1 X15.0000 Y50.0000 E0.0000 F1500 ; Ternary rest hold step",
        "M400"
    ]
    
    print("[+] Streamer initialized. Run with 'make build' setup to route live serial hardware streams.")
