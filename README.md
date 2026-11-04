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

The repository organizes all nine automated execution modules from the geometry lab, pairing specific high-dimensional failure states with physical canvas rendering modes:

Spatial Wave Subsystem

* 🟥 Curvature-Breathing Compiler (src/ndh_surrealism/engines/spatial_wave.py — Op 01): Translates latent curvature tensor spikes into expanding, pulsating stroke concentricity that mimics the aesthetic of "breathing walls."
* 🟪 Spectral Cascade Observatory (src/ndh_surrealism/engines/spatial_wave.py — Op 06): Tracks high-dimensional eigenvalue step transformations to inject nested sub-strokes and fractal recursive paths.

Fluidic & Rotational Subsystem

* 🟩 Liquefaction Fluidics Controller (src/ndh_surrealism/engines/manifold_melting.py — Op 04): Controls the velocity and pressure of fluid delivery systems to physically simulate the melting, dripping, and dissolving of a degrading metric tensor.
* 🟫 Rotational Vortex Drive (src/ndh_surrealism/engines/holonomy_vortex.py — Op 07): Maps accumulated rotational holonomy twist to 2D polar space coordinates, forcing the toolhead into precise, non-terminating spiral trajectories.

Discontinuity Subsystem

* 🟦 Volumetric Drift Planner (src/ndh_surrealism/engines/discontinuity.py — Op 05): Accumulates un-rectified tracking offsets across sequential semantic updates, creating jarring, dream-logic composition offsets.
* ⬛ Collapse-Surface Interrupter (src/ndh_surrealism/engines/discontinuity.py — Op 08): Detects sudden metric dimension drops (\(\det(g) \to 0\)) and issues absolute zero fluid signals to trigger automated rapid Z-axis hardware lifts, creating whitespace structural voids.

Compositional Subsystem

* 🟧 Chimera Fusion Renderer (src/ndh_surrealism/engines/compositional.py — Op 02): Averages symmetrical layout nodes across overlapping matrix boundaries to melt disparate concepts into unified physical shapes.
* 🟨 Dream Potential Field Mapper (src/ndh_surrealism/engines/compositional.py — Op 03): Projects multi-field attraction forces onto baseline coordinates, pulling layout nodes toward high-density attractor wells to cluster the composition.
* ⬜ Full Dream Diagnostic Pipeline (src/ndh_surrealism/engines/compositional.py — Op 09): Sequentially segments and routes input matrices through the entire multi-operator suite to output a unified topological canvas fingerprint.

🛠 Repository Structure

<pre> 

NDH-Surrealism/
├── .github/
│   └── workflows/           # Localized CI/CD validation suites
│       └── verify.yml
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
│           ├── gcode.py
│           ├── leveling.py  # Bilinear canvas surface-mesh leveler
│           └── streamer.py  # Serial communication hardware streaming interface
├── tests/
│   ├── test_geometry.py    # Pytest suites for boundary containment metrics
│   └── Verification.lean   # Lean 4 formal verification for boundary safety
├── lakefile.toml           # Lean 4 dependency configuration
├── pyproject.toml          # Python environmental dependency specifications
├── run_pipeline.sh         # Master automation orchestration shell utility
├── Makefile                # Localized pipeline runtime orchestration
└── README.md

</pre>

🚀 Localized Pipeline Execution

To preserve total workspace sovereignty and keep creative systems self-contained, the runtime operates entirely on local hardware with zero network dependencies.
bash
# Initialize the local virtual environment and install tracking dependencies
make env

# Run the pytest suite to validate geometric boundaries and fluidics scales
make test

# Execute the Lean 4 formal verification to mathematically prove coordinate containment
make verify-proofs

# Run the complete pipeline end-to-end (Compilation, Validation, Calibration, and Stream)
./run_pipeline.sh dream_diagnostic /dev/ttyUSB0
Use code with caution.

📜 Ethical Licensing & Operational Boundary

This software is released under a strict, protective open-source license. It is purpose-built exclusively for deterministic studio practice, artistic experimentation, and geometric interpretability. It is expressly prohibited from deployment in kinetic targeting systems, autonomous weapon navigation, or aerospace flight control surfaces.

📑 Provenance

* Artifact-Class: Automated Studio Substrate (Surrealist Mechanics)
* Design Track: NDH-RESEARCH-PILOT / Sub-Track: Autonomic Canvas Execution
* Maintainer: Borealis S. Hedling & The Studio Compiler Network
* Seal: [ NDH . SURREALISM . v1_0 ]
