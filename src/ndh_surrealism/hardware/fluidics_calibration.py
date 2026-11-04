class FluidicsCalibration:

    def __init__(self, internal_diameter_mm=4.0, steps_per_rev=200, microstepping=16):
        """
        Calculates fluid displacement for a peristaltic pump head.
        internal_diameter_mm: Inner diameter of the silicone tubing.
        steps_per_rev: Base steps of the stepper motor (usually 1.8 degrees = 200 steps).
        microstepping: Driver microstepping multiplier (e.g., 16x).
        """
        self.id_mm = internal_diameter_mm
        self.total_steps_per_rev = steps_per_rev * microstepping
        
        # Calculate volume displaced per complete revolution of the roller head
        # Assuming a standard 3-roller head compressing a 30mm track segment
        import math
        self.track_length_mm = 30.0
        self.volume_per_rev_mm3 = math.pi * ((self.id_mm / 2.0) ** 2) * self.track_length_mm
        
        # 1 mm3 = 0.001 mL (milliliters)
        self.ml_per_rev = self.volume_per_rev_mm3 * 0.001
        
        # Calculate how many motor pulses are required to deliver exactly 1.0 mL of paint
        self.steps_per_ml = self.total_steps_per_rev / self.ml_per_rev
        print(f"[*] Calibration Vector Calculated: {self.steps_per_ml:.2f} steps required per mL of fluid.")

    def get_extrusion_multiplier(self, paint_viscosity_factor=1.0):
        """
        Returns a tuning scalar. Thicker mediums require higher step steps to offset line lag.
        """
        return float(self.steps_per_ml * paint_viscosity_factor)
