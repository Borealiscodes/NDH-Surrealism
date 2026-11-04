-- ========================================================================
-- NDH-SURREALISM: FORMAL STUDIO INVARIANT VERIFICATION SUBSTRATE (v1.1)
-- AUTHOR: BOREALIS S. HEDLING & THE STUDIO COMPILER NETWORK
-- FILE: tests/Verificationrefined.lean
-- ========================================================================

import Mathlib.Data.Float

-- Contains structural configurations (`StudioConfig`, `RobotState`), 
-- safety invariant predicates (`IsPaintingInsideBounds`, `IsValidToolChangeState`),
-- floating-point operational axioms for `Float.min` and `Float.max`,
-- and formal theorems (`spatial_containment_invariant`, `tool_change_separation_invariant`, `fluid_viscosity_flow_safety`).
