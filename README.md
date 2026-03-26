[dl_readme.md](https://github.com/user-attachments/files/26286748/dl_readme.md)
# Sampling-Constrained Perception Theory
**Author:** Mike Kaman — Byron Center, Michigan
**Contact:** Kamaninc@yahoo.com

---

## The Central Result

This repository contains the working paper, mathematical derivations,
and simulation code for a geometric framework proposing that quantum
mechanics, gravity, and the Standard Model gauge forces all emerge
from the topology of stable folds in a 4D membrane.

The headline result is a derivation of the fine structure constant
to 0.007% accuracy from pure geometry:

    α = (φ + (2/3)(2+φ)/(4π)) / (8π³)  =  0.007296...

    Observed: α = 0.007297...    Error: −0.007%

where φ = (1+√5)/2 is the golden ratio. No free parameters.
No fitting. Every symbol has a geometric origin.

The formula comes from the self-linking number of the Clifford
torus projection curve — the trajectory of a particle in 4D
space projected onto the 3D observer's slice. The writhe of
that curve is φ (forced by the golden ratio parametrization).
The S³ curvature correction is weighted by 2/3 (the fraction
of S³ accessible to a 3D observer: dim(S²)/dim(S³)). The
normalization is 8π³ = Vol(S³) × 4π.

---

## What the Theory Derives

From two medium properties (surface tension T and curvature
stiffness κ), with no additional assumptions:

- Quantum mechanics — Schrödinger and Dirac equations
- Born rule P = |ψ|²
- Wavefunction collapse
- Special relativity
- Spin-½, spin-statistics, Pauli exclusion
- Linearized general relativity and Newton's law
- Standard Model gauge groups U(1) × SU(2) × SU(3)
- Fine structure constant α (0.007% accuracy)
- Coupling ratios g_w/g_em = 2, g_s/g_em = 3 (tree level)
- Color confinement (topological)
- Proton stability (topological)
- Exactly three fermion generations
- Parity violation (geometric — Chern-Simons handedness)
- Charge quantization (integer winding)

---

## The Core Idea

There is a flow.

We didn't find it by looking harder. We found it by asking what happens
when you stop the flow, freeze it, and try to read it as a static thing.

Imagine a skin cell. At the molecular level it is a blur of motion —
proteins folding, ions crossing membranes, water molecules colliding
millions of times a second. Take a photograph of it. Freeze it in time.
Now you have a static particle. You have lost the flow. And if that
photograph were the only thing you ever had, you would never know the
cell was alive. You would call it a particle and write down its position
and wonder why it behaves so strangely.

That is what I think we have done with quantum mechanics.

The shape is just the stage. What matters is the quantum current
flowing on it. The geometry never changes but the current has a
direction, a handedness. That's where the asymmetry comes from.
The shape doesn't break the symmetry — the current does. And it
doesn't have to be a torus. Different stable shapes, same idea.
The current is the thing.

---

## Testable Predictions

**P1 — CHSH degrades with measurement resolution (novel)**
In a Bell test where the coincidence timing window is varied
from sub-nanosecond to microsecond, the CHSH value should
decrease smoothly from 2√2 toward 2.0 as resolution degrades.
Standard QM predicts CHSH stays flat at 2√2. Testable with
existing equipment.

**P2 — Fine structure constant from geometry**
α = (φ + (2/3)(2+φ)/(4π)) / (8π³) to within higher-order
corrections. Currently accurate to 0.007%.

**P3 — Exactly three fermion generations**
Confirmed by LEP Z-boson decay width measurements.

**P4 — No stable fourth gauge force**
The N=3 stability cap in 4D forbids a fourth gauge group.

**P5 — Branching degree conservation**
A new conservation law — branching degree of Whitney folds
is preserved in all interactions.

---

## Files

| File | Description |
|------|-------------|
| `paper.md` | Full paper in plain language |
| `mathematical_derivations.md` | Complete derivation chain |
| `alpha_derivation.md` | Standalone α derivation — the central result |
| `sampling_theory_simulation.py` | Original Bell test simulation |
| `geometry_first_chsh.py` | Geometry-first CHSH — no circular formula |
| `whitney_pinch_profile.py` | Numerical verification of r^(1/2) vanishing |
| `fn_numerical.py` | Coupling constant computation from fold topology |

---

## How to Run

```
pip install numpy scipy matplotlib pandas
python geometry_first_chsh.py
python whitney_pinch_profile.py
python fn_numerical.py
```

---

## What I'm Looking For

A physicist or mathematician in quantum foundations, differential
geometry, or singularity theory willing to check three things:

1. Is the writhe of the Clifford torus projection curve exactly φ?
2. Is the S³ curvature correction formula L²/(4π·Vol(S³)) correct
   at leading order for this embedding?
3. Is the 2/3 accessibility weight dim(S²)/dim(S³) derivable from
   the action rather than just from dimension counting?

If all three hold, the fine structure constant is derived from
first principles to within higher-order corrections.

---

## Status

This is not a finished theory. It is an honest account of how far
a geometric idea can be pushed by someone without formal physics
training. Some results are rigorous. Some are structural arguments
that need tightening. The derivations document is explicit about
which is which.

I'm not a physicist. I'm a curious person who couldn't stop thinking
about this. If it's wrong I'd rather know. If it's right I'd rather
not be the only one thinking about it.

— Mike Kaman, Byron Center MI
