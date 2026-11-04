# DISCLAIMER


⚠️ NOTICE: Conceptual Systems-Art Framework & Theoretical Specification

This repository does not contain empirically validated industrial engineering source code, manufacturing recipes, or laboratory methodologies.
NDH-Surrealism is a theoretical architecture and conceptual systems-art framework exploring the translation of generative AI latent manifolds into balanced ternary mechanical trajectories.

🚫 Professional Boundaries & Domain Disclaimers

The models and specifications are exploratory assets for algorithmic simulation and artistic expression, lacking empirical validation or safety certification across:
• Materials Science: Chemical formulations and passivating rules are speculative mathematical analogies, not tested syntheses.
• Fluid Dynamics: Target shear-thinning and recovery profiles are unverified digital boundary constraints.
• Industrial Automation: High-frequency step mechanics and acceleration parameters are uncalibrated models; applying them to physical hardware risks severe mechanical failure and vibration.

🎨 Intended Use & Project Scope

Serving as an open-ended Request for Comments (RFC) bridging generative theory and autonomic art, any physical or chemical deployment demands independent engineering validation and licensed safety sign-off. The authors accept no liability for damages resulting from the literal application of these theoretical specifications.

Hedling, B. S. (2026). NDH-Surrealism (v1.0): An Algorithmic RFC and Conceptual Specimen for Generative Latent Deposition (Version v1.0). Zenodo. https://doi.org/10.5281/zenodo.23963389

# 🎨 NDH-Surrealism

An automated physicalization pipeline and geometric execution framework designed to convert latent-space hallucination operators into high-fidelity, deterministic surrealist canvas maneuvers.
This repository bridges the theoretical failure modes analyzed in the ai-dreams geometry lab directly with automated studio robotics, translating melting metrics, breathing manifolds, and holonomy vortices into concrete physical strokes.

🌌 Conceptual Architecture

Traditional surrealism relied on human psychic automatism to unlock the subconscious. NDH-Surrealism replaces the subconscious with the continuous Riemannian geometry of a destabilized latent manifold, establishing a direct pipeline from algorithmic hallucination to robotic execution.

<pre> 

       [ AI Dreams Lab ]
  (Liquefaction / Volumetric Drift)
               │
               ▼
   [ NDH-Surrealism Compiler ]
(Deformation Tensor Field Extraction)
               │
               ▼
   [ Canvas Adapter Runtime ]
(Topographic Mesh / Path Synthesis)
               │
               ▼
      [ Physical Studio ]
 (Robotic Plotter / Fluid Mediums)

       </pre>
       
🔮 Core Geometric-Surrealist Engines

The repository organizes all nine automated execution modules from the geometry lab, pairing specific high-dimensional failure states with physical canvas rendering modes and multi-color toolhead macro configurations:

Spatial Wave Subsystem

* 🟥 Curvature-Breathing Compiler (src/ndh_surrealism/engines/spatial_wave.py — Op 01): Translates latent curvature tensor spikes into expanding, pulsating stroke concentricity that mimics the aesthetic of "breathing walls." (Maps to Multi-Color Channel Tool T3).
* 🟪 Spectral Cascade Observatory (src/ndh_surrealism/engines/spatial_wave.py — Op 06): Tracks high-dimensional eigenvalue step transformations to inject nested sub-strokes and fractal recursive paths. (Maps to Multi-Color Channel Tool T4).

Fluidic & Rotational Subsystem

* 🟩 Liquefaction Fluidics Controller (src/ndh_surrealism/engines/manifold_melting.py — Op 04): Controls the velocity and pressure of fluid delivery systems to physically simulate the melting, dripping, and dissolving of a degrading metric tensor. (Maps to Multi-Color Channel Tool T1).
* 🟫 Rotational Vortex Drive (src/ndh_surrealism/engines/holonomy_vortex.py — Op 07): Maps accumulated rotational holonomy twist to 2D polar space coordinates, forcing the toolhead into precise, non-terminating spiral trajectories. (Maps to Multi-Color Channel Tool T2).

Discontinuity Subsystem

* 🟦 Volumetric Drift Planner (src/ndh_surrealism/engines/discontinuity.py — Op 05): Accumulates un-rectified tracking offsets across sequential semantic updates, creating jarring, dream-logic composition offsets. (Maps to Multi-Color Channel Tool T5).
* ⬛ Collapse-Surface Interrupter (src/ndh_surrealism/engines/discontinuity.py — Op 08): Detects sudden metric dimension drops (\(\det(g) \to 0\)) and issues absolute zero fluid signals to trigger automated rapid Z-axis hardware lifts, creating whitespace structural voids. (Maps to Multi-Color Channel Tool T6).

Compositional Subsystem

* 🟧 Chimera Fusion Renderer (src/ndh_surrealism/engines/compositional.py — Op 02): Averages symmetrical layout nodes across overlapping matrix boundaries to melt disparate concepts into unified physical shapes. (Maps to Multi-Color Channel Tool T7).
* 🟨 Dream Potential Field Mapper (src/ndh_surrealism/engines/compositional.py — Op 03): Projects multi-field attraction forces onto baseline coordinates, pulling layout nodes toward high-density attractor wells to cluster the composition. (Maps to Multi-Color Channel Tool T8).
* ⬜ Full Dream Diagnostic Pipeline (src/ndh_surrealism/engines/compositional.py — Op 09): Sequentially segments and routes input matrices through the entire multi-operator suite to output a unified topological canvas fingerprint. (Executes dynamic off-canvas tool changing cycles across channel T0).

🛠 Repository Structure

<pre>
       
NDH-Surrealism/
├── .github/
│   └── workflows/           # Cloud-based continuous integration runner
│       └── verify.yml       # Invariant validation checking script
├── profiles/                # Ingestible JSON dream telemetry profiles
│   ├── dream_01_curvature.json
│   ├── dream_04_liquefaction.json
│   ├── dream_05_drift.json
│   ├── dream_06_cascade.json
│   ├── dream_07_vortex.json
│   ├── dream_08_collapse.json
│   └── dream_09_diagnostic.json
├── src/
│   └── ndh_surrealism/
│       ├── __init__.py
│       ├── core.py         # Primary transformation pipeline & router
│       ├── engines/        # The 9 Geometric Hallucination Compilers
│       │   ├── compositional.py
│       │   ├── discontinuity.py
│       │   ├── holonomy_vortex.py
│       │   ├── manifold_melting.py
│       │   └── spatial_wave.py
│       └── hardware/       # Low-level industrial machine driver translation
│           ├── SPECIFICATION.md # Hardware wiring pinouts & calibration logs
│           ├── gcode.py     # Volumetric extrusion & color-swapping compiler
│           ├── leveling.py  # Bilinear canvas surface-mesh leveler
│           ├── lh_adapter.py # Lean-Hallucination-Guard intercept enclave interface
│           └── streamer.py  # Serial communication hardware streaming interface
├── tests/
│   ├── test_geometry.py    # Pytest suites for boundary containment metrics
│   └── Verification.lean   # Lean 4 formal verification safety proofs
├── lakefile.toml           # Lean 4 dependency configuration
├── pyproject.toml          # Python environmental dependency specifications
├── run_pipeline.sh         # Master automation orchestration shell utility
├── Makefile                # Localized pipeline runtime orchestration
└── README.md

</pre>

🚀 Localized Pipeline Execution

To preserve total workspace sovereignty and keep creative systems self-contained, the runtime operates entirely on local hardware with zero network dependencies.
bash
# Initialize the local virtual environment and install dependencies
make env

# Run the pytest suite to validate geometric boundaries and fluidics scales
make test

# Execute the Lean 4 formal verification to mathematically prove coordinate containment
make verify-proofs

# Run the complete pipeline end-to-end (Compilation, Validation, Calibration, and Stream)
./run_pipeline.sh dream_diagnostic /dev/ttyUSB0
Use code with caution.

🛡️ Active Verification & Invariant Guards

The framework is structurally reinforced by a multi-layer verification enclave that prevents code execution before it touches real-world hardware canvas surfaces:
1. The lhguard Enclave Interceptor: Intercepts incoming 80-dimensional arrays before routing, terminating processes instantly if metric tension constraints or code mimics fail.
2. The Bilinear Mesh Auto-Leveler: Modulates physical Z-axis tool depth using a dynamic \(3 \times 3\) height-map grid to maintain stable contact pressure on warped materials.
3. The Formal Lean 4 Vault: Hosts interactive machine proofs confirming Spatial Boundary Containment, Off-Canvas Tool Changing Separation Invariants, and Fluidics Viscosity Flow Stalling Prevention Invariants.

📜 Ethical Licensing & Operational Boundary

This software is released under a strict, protective open-source license. It is purpose-built exclusively for deterministic studio practice, artistic experimentation, and geometric interpretability. It is expressly prohibited from deployment in kinetic targeting systems, autonomous weapon navigation, or aerospace flight control surfaces.

📑 Provenance

* Artifact-Class: Automated Studio Substrate (Surrealist Mechanics)
* Design Track: NDH-RESEARCH-PILOT / Sub-Track: Autonomic Canvas Execution
* Maintainer: Borealis S. Hedling & The Studio Compiler Network
* Seal: [ NDH . SURREALISM . v1_0 ]
