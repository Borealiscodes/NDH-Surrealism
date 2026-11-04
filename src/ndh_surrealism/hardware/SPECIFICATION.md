
🎛️ Hardware Pinout & Wiring Specifications

This specification maps standard open-source control architecture (such as a BigTreeTech SKR, Duet3D, or an Arduino RAMPS setup) directly to the NDH-Surrealism robotic toolhead and fluid distribution mechanics.
========================================================================
NDH-SURREALISM STUDIO CONTROLLER ELECTRICAL INTERFACE SPECS (v1.0)
========================================================================

[ PRIMARY POWER & DATA BUS ]
Power Supply Rails ───> 24V DC / 10A (Enforces high torque under fluid load)
Primary Data Input ───> USB Serial / Raspberry Pi Local Stream Interface

[ STEPPER MOTOR OUTPUT CHANNEL ALLOCATIONS ]
X-Driver Port ────────> Robotic Arm Base Rotation Motor
Y-Driver Port ────────> Articulating Shoulder/Elbow Extension Motor
Z-Driver Port ────────> Toolhead Linear Z-Axis Lift Motor
E0-Driver Port ───────> Peristaltic Fluid Pump Stepper Motor (⚠️ CRITICAL)

[ AUXILIARY TELESKOP / VOLTAGE REGISTER CONTROL ]
PWM Output Slot ──────> Solid-State Relay ───> 24V Electronic Paint Solenoid
Fan Output Slot ──────> Optocoupler Relay ───> Air-Compressor Splatter Line

[ SIGNAL & LIMIT SENSOR REGISTER ]
Endstop Pin X_MIN ────> Mechanical / Optical Microswitch (Homing Target Base)
Endstop Pin Y_MIN ────> Mechanical / Optical Microswitch (Homing Target Arm)
Endstop Pin Z_MIN ────> Inductive Proximity Probe (Canvas Plane Deflection Safeguard)
========================================================================

📏 Step-by-Step Fluidics Calibration Instructions

To ensure that the volumetric extrusion parameter (E) inside your compiled G-code translates perfectly to physical fluid volume on canvas, you must calibrate the pump's steps-per-milliliter calculation.

Step 1: Calculate the Mathematical Baseline

Before running fluid through the line, calculate your theoretical steps-per-rev baseline using your motor and driver values:
Total Steps per Revolution=Base Motor Steps (e.g., 200)×Microstepping Multiplier (e.g., 16)=3200 pulsesTotal Steps per Revolution equals Base Motor Steps (e.g., 200) cross Microstepping Multiplier (e.g., 16) equals 3200  pulses
Total Steps per Revolution=Base Motor Steps (e.g., 200)×Microstepping Multiplier (e.g., 16)=3200 pulses

Step 2: Perform the Physical 10mL Draw Test

1. Fill your peristaltic pump line with your chosen painting medium (acrylic, oil, or ink mixture).
2. Send command G92 E0 via your serial terminal to clear the extrusion tracker register.
3. Place a clean, empty graduated cylinder directly beneath the toolhead brush nozzle.
4. Execute an absolute test extrusion command block to drive the pump motor for what should theoretically equal 10.0 mL of fluid volume:gcode
G1 E10.0 F100 ; Feed 10 units at a controlled speed of 100mm/min
Use code with caution.

Step 3: Measure and Calculate the Correction Factor

Measure the exact volume of paint delivered into the graduated cylinder. If the output does not match 10.0 mL exactly, use the correction formula below to update your step configuration:
New Extrusion Steps=(Target Volume (10.0 mL)Measured Volume (mL))×Current Extrusion StepsNew Extrusion Steps equals open paren the fraction with numerator Target Volume (10.0 mL) and denominator Measured Volume (mL) end-fraction close paren cross Current Extrusion Steps
New Extrusion Steps=Target Volume (10.0 mL)Measured Volume (mL)×Current Extrusion Steps

Step 4: Flash Configuration Updates

Once the corrected value is determined, save it directly to the controller board's non-volatile memory storage register using standard G-code configuration commands:
gcode
M92 E325.40 ; Set the newly calculated steps-per-milliliter variable 
M500        ; Save changes securely to the controller's onboard EEPROM
