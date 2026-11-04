# Developer Note: Architectural Realities of Primitive Floating-Point Verification in Lean 4

1. The Core Limitation: The Opaque Floating-Point Box

In Lean 4, the primitive Float type directly wraps the host processor's hardware IEEE 754 floating-point operations. Because these operations are defined as opaque, low-level calls for raw execution performance, they lack structural algebraic properties within the core logic system.
Standard automated decision procedures—such as linarith (linear arithmetic) or omega (Presburger arithmetic)—operate entirely on types with well-behaved, exact algebraic structures (like Nat, Int, or Real). When presented with Float, these solvers fail immediately. They cannot automatically deduce basic inequality chains, nor can they verify standard boundary-containment expressions.

2. Resolution Strategies for Production Pipelines

To achieve total formal proof closure without sorry placeholders in an engineering framework like NDH-Surrealism, developers must use one of two primary architectural patterns:
• Pattern A: Postulated Order Axioms (Axiomatic Modeling)
Introduce explicit computational axioms matching the target hardware's properties. By postulating foundational laws for Float.min, Float.max, and transitivity, the compiler can close proofs using purely deductive tactics (intro, dsimp, constructor, exact, apply). This treats the underlying floating-point engine as an idealized order-theoretic structure.
• Pattern B: Exact Domain Refinement (The Real Mapping)
Redefine the core studio structures (StudioConfig, RobotState) to use exact mathematical real numbers (Real from Mathlib) for all mathematical proofs. Once the high-level boundary containment theorems are completely verified using exact arithmetic, a separate, unverified translation layer projects these values down to physical Float coordinates at the hardware serialization border.

3. Current Pipeline Status

The mathematical design specifications detailed in tensor_choreography_v1.tex assume an error-clamped framework. The companion python stream engine (lh_adapter.py) supplements this logic at runtime by executing physical metric verification checks (such as Singular Value Decomposition ratio auditing via NumPy) before coordinate sets are allowed to pass to the motor lines.
