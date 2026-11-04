
Execution Blueprint: Achieving 100% Formal Proof Closure in Lean 4

To transition your robotic canvas execution pipeline from an unverified prototype to a fully machine-checked, safety-clamped system, follow this step-by-step roadmap. This plan addresses the core challenge of Lean 4’s raw Float types by utilizing a verified tracking layer, stepping from base configuration bounds to an end-to-end continuous integration pipeline.
[Phase 1: Typestate Modeling] ──> [Phase 2: Float Boundary Axiomatization] 
                                                    │
                                                    ▼
[Phase 4: Automatic CI Enforcer] <── [Phase 3: Theorem Proof Refinement]

Phase 1: Establish the Geometric and Typestate Foundations

Define the structural envelopes and invariant boundaries of your physical studio environment.
• Action item: Construct your spatial structures and operating predicates. Group parameters into distinct records (StudioConfig and RobotState) to encapsulate physical parameters.
• Target files: tests/Verificationrefined.lean
• Logical bounds:
	• Ensure canvas boundaries (width, height) and fluid safety thresholds (viscosity_floor) are strictly constrained to positive spaces.
	• Formally define the physical coordinate space of the rinse/tool-change station outside the valid painting envelope.

Phase 2: Structural Axiomatization of Floating-Point Operations

Because Lean 4’s Float type wraps hardware IEEE 754 operations, standard decision procedures (like omega or linarith) cannot solve inequality chains directly. You must explicitly build the order theory axioms for floating-point calculations.
• Action item: Declare explicit parameters and operational rules for Float.min and Float.max.
• Target files: tests/Verificationrefined.lean (Axioms block)
• Key constraints to formalize:
	• Lower Bounding: Prove that Float.max A B ≥ A and Float.max A B ≥ B.
	• Upper Bounding: Prove that Float.min A B ≤ A and Float.min A B ≤ B.
	• Transitivity: Provide manual inequality chaining lemmas (∀ a b c : Float, a ≤ b → b ≤ c → a ≤ c).

Phase 3: Theorem Proof Refinement

With the order foundations laid, write out the explicit deductive proofs for your three core hardware execution safeguards. Avoid using automated tactics that break on floating-point structures; rely strictly on core constructive tactics (intro, dsimp, constructor, exact, cases).

Milestone 3.1: Theorem 1 — Spatial Clamping Invariant Guarantee

• Objective: Mathematically prove that the canvas hardware adapter's hardware coordinate clamping function (Float.max 0.0 (Float.min raw cfg.canvas_width)) will always generate a position inside the legal bounds of the canvas, preventing axis collision.
• Tactic Flow: Apply structural axioms step-by-step to show that the output coordinate sits between 0.0 and the upper configuration maximums.

Milestone 3.2: Theorem 2 — Tool Change Separation Invariant Guarantee

• Objective: Prove that when the robot switches tools at the rinse station, it is physically impossible to simultaneously be within the active painting envelope. This prevents the robot from dripping active fluid or solvent on a clear canvas during transit.
• Tactic Flow: Construct a proof by contradiction using the rinse station coordinate constraints (X < 0, Y < 0) against the canvas painting constraints (X ≥ 0, Y ≥ 0).

Milestone 3.3: Theorem 3 — Fluidics Viscosity Flow Safety Invariant

• Objective: Guarantee that the command runtime cannot issue fluid rates below the mechanical stalling floor while the toolhead is actively engaged with the canvas, preventing clogging.
• Tactic Flow: Verify structural initialization properties to enforce flow constraints whenever contact pressure is active (Z ≤ 0.0).

Phase 4: Construct the Automated Continuous Integration Enforcer

Ensure that every subsequent commit to the NDH-Surrealism pipeline is automatically checked, blocking unverified code from deployment onto the physical robotics array.
• Action item: Set up local build configurations and cloud continuous integration workflows.
• Target files: lakefile.toml, .github/workflows/verify.yml
• Execution Strategy: Configure a Lean 4 build environment using GitHub Actions to automatically run lake build and execute the full proof validation suite on every repository push or pull request.
