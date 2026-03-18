The Perception of Order Beyond Human Time-Scale Resolution
A Speculative Framework from an Independent Researcher
Mike Kaman Byron Center, Michigan Kamaninc@yahoo.com github.com/MikeKaman/sampling-perception-theory
This paper is not a finished scientific proof. It is an honest account of an idea I cannot get out of my head, developed as far as I am able to take it without formal training, and offered to the scientific community in the hope that someone with the right tools will tell me whether it stands up.

A Note Before You Read
I am not a physicist. I have no university degree in any related field.
What I have is a persistent intuition — one that arrived partly through dreams, partly
through years of thinking about perception and reality at odd hours — that the
"weirdness" of quantum mechanics might have a simpler explanation than we've been
assuming. Not simpler as in easy. Simpler as in: we might be looking at the shadow of
something, and calling the shadow fundamental.
I've done my best to connect this intuition to real mathematics and real physics. Some
of those connections I'm confident in. Others I'm not. I've tried to be clear throughout
about which is which.
If you're a physicist reading this and you see an obvious flaw — I genuinely want to
know. If you see something interesting — I'd love to talk.

The Core Idea (Plain Language First)
Imagine filming a spinning fan with a camera that's too slow. The fan looks frozen, or
reversed, or like it's doing something strange. The strangeness isn't in the fan. It's in
the gap between how fast the fan is moving and how fast your camera can see.
Now imagine that quantum particles are like that fan — moving in a real, structured,
deterministic way — but at frequencies so far beyond what any of our instruments can
sample that we can't reconstruct the true motion. What we see instead is the aliased
version: probabilistic, uncertain, weird.
That's the hypothesis. The "randomness" of quantum mechanics might be an artifact of
under-sampling, not a feature of reality itself.
This is not a new category of idea. Hidden variable theories have been around since
Einstein. What I think might be new is the specific mechanism I'm proposing — applying
the Nyquist-Shannon sampling theorem formally to the act of quantum measurement —
and the specific prediction it generates, which I'll get to near the end.

1. Where This Came From
I've spent a long time thinking about perception — about how every sense we have is
a filter, not a window. Eyes only see a narrow band of electromagnetic frequency. Ears
only hear a narrow band of pressure waves. We build our entire picture of reality from
a sliver of what's actually there.
This is obvious when you think about it, and it bothered me. If we only experience a
slice of the available information, how do we know our physics — built entirely from
what we can measure — describes reality, rather than describing our slice of it?
The Nyquist-Shannon theorem is a result from signal processing that says something
precise about this problem. It says: if you want to faithfully reconstruct a signal, you
need to sample it at least twice as fast as its highest frequency. Sample slower than
that, and you don't just lose information — you create false information. Patterns that
look real but aren't. Frequencies that appear to be there but are artifacts.
My question became: what if quantum measurement is sampling below the Nyquist rate
for some underlying physical process? What would that look like from the inside?
It would look, I think, exactly like quantum mechanics.

2. The Signal Processing Connection
I am reasonably confident in this section. The mathematics of sampling theory is
well-established and I've been careful here.
The Nyquist-Shannon theorem states: a signal containing frequency components up to frequency f must be sampled at a rate greater than 2f to be reconstructed without distortion. Below this rate, aliasing occurs.
Aliasing produces specific artifacts:
	•	Patterns that appear to move in the wrong direction (spinning wheels on film)
	•	Frequencies that appear lower than they actually are
	•	Apparent randomness from perfectly structured signals
The hypothesis is that these artifacts, when they appear in the domain of quantum
measurement, look like: wavefunction spreading, positional uncertainty, probabilistic
collapse.
A particle that moves deterministically at frequency f_r — observed by an instrument with sampling rate f_s — would appear, to that instrument, as a probability distribution rather than a trajectory, if f_s < 2f_r.
This is not a metaphor. It is a direct application of a mathematical theorem to a
physical situation. Whether the physical situation actually applies — whether quantum
particles really do move at some true frequency that we undersample — is the part I
cannot prove. That is an empirical question.

3. The Heisenberg Connection
I want to be careful here. This section makes a bolder claim and I'm less certain of it.
The Heisenberg uncertainty principle says: the more precisely you know a particle's
position, the less precisely you can know its momentum, and vice versa. Formally:
Δx · Δp ≥ ħ/2.
Standard quantum mechanics treats this as a fundamental feature of nature — not a
limitation of our instruments, but a property of reality itself.
My suggestion is that this might be a sampling theorem in disguise.
Here's the sketch of the argument — and I want to be honest that this is a sketch, not a proof: if a particle moves with a true frequency f_r, then by the de Broglie relation, its momentum is p = hf_r/v. An observer sampling at rate f_s cannot resolve positions more finely than about v/(2f_s). The uncertainty in inferred momentum scales inversely. When you multiply those two uncertainties together, you get something that looks like ħ/2.
I've worked through this calculation several times and it seems to come out right. But
I've also learned enough to know that "seems to come out right" is not the same as
"is correct." The step where I convert from sampling interval to momentum uncertainty
involves assumptions I'm not fully confident in. A physicist would need to check this
carefully.
If it does hold up — if Heisenberg's inequality really does fall out of Nyquist's theorem
when applied to de Broglie waves — that would be significant. It would mean the
uncertainty principle is an epistemological limit (a limit of what observers can know)
rather than an ontological one (a limit of what exists). The particle always has a
definite position and momentum. We just can't sample fast enough to see both at once.

4. The Bell Problem — and Why I Think There's a Path Through It
This is where most hidden variable theories die, and I want to be honest that I don't
have a full solution here.
Bell's theorem, confirmed experimentally by Aspect in 1982 and Zeilinger in 2022, shows that no local hidden variable theory can reproduce all the predictions of quantum mechanics. This is one of the most robustly established results in all of physics.
My theory is a hidden variable theory. So does Bell kill it?
My argument for why it might not: my proposed hidden structure — the high-frequency
field through which particles move — is not local. It is a shared four-dimensional
manifold. Two entangled particles are not two separate things that happen to be
correlated. They are two intersection points of a single structure. Their correlations
don't travel between them — the correlations are baked into the geometry they share.
This is similar in spirit to the de Broglie-Bohm pilot wave interpretation, which also
survives Bell by being explicitly non-local.
I've tried to work out whether the shared-manifold model reproduces the specific
correlations quantum mechanics predicts — the cosine relationship between measurement
angles that produces what's called the CHSH value of 2√2. For a Clifford torus
trajectory in 4D space, I believe it does, because that trajectory has uniform
orientation in all directions. But I have to be honest: I derived this with significant
help from an AI assistant, and while the geometric reasoning feels right to me, I have
not had a mathematician verify it.
This is the thing I most need checked.

5. The Prediction
Here is the part I feel most confident about — not because the math is fully derived,
but because it follows directly from the core idea with minimal assumptions.
If quantum indeterminacy is a sampling artifact, then it should get worse as measurement precision decreases. Specifically: the degree to which entangled particles violate Bell's inequality — measured by the CHSH value — should be a function of the measurement instrument's effective resolution.
Standard quantum mechanics predicts the CHSH value is fixed: approximately 2.828
for ideal measurements, independent of how the measurement is made.
Local hidden variable theories predict it's fixed at or below 2.0.
My theory predicts something different from both: as measurement precision degrades
below a threshold (the Nyquist rate for the relevant field frequency), the CHSH value
should decrease smoothly from ~2.828 toward ~2.0. The better your instrument, the
more quantum it looks. The coarser your instrument, the more classical.
I believe this prediction is genuinely novel — I haven't found it in the literature —
but I could simply not know where to look. If anyone is aware of a theory that makes
a similar prediction, I'd genuinely like to know.
A practical experiment: a Bell test using entangled photons, where the measurement
integration window is varied systematically from sub-nanosecond to microsecond.
If the CHSH value drops as the window widens, my theory is supported. If it stays
flat (corrected for known noise sources), the theory is in trouble.

6. The Computational Work
I've built a simulation in Python (available at the link at the top of this document)
that models deterministic systems sampled at varying rates and measures whether they
produce quantum-like statistics.
The results show that deterministic undersampled trajectories do produce statistics
that look quantum — rising positional entropy, loss of autocorrelation, Bell scores
that approach the QM prediction at high sampling rates and degrade toward the
classical limit at low ones.
I want to be clear about what this proves and doesn't prove. It proves that the mechanism is internally consistent — that undersampling could produce this kind of apparent randomness. It doesn't prove that it actually does in nature. That's the empirical question the Bell experiment above would address.
The simulation is fully reproducible (seed=42). Every assumption is documented in
comments. I welcome scrutiny.

7. What I'm Asking For
I'm not asking anyone to believe this theory. I'm asking for honest engagement with it.
Specifically, I would find it valuable if someone with the relevant expertise could
tell me:
	1	Is the Nyquist-to-Heisenberg derivation in Section 3 worth formalizing, or is there an obvious gap I've missed?
	2	Does the Clifford torus argument in Section 4 actually produce the QM cosine correlation, or is my geometric reasoning flawed?
	3	Is the prediction in Section 5 genuinely novel, or does it already appear somewhere in the literature on quantum foundations?
	4	If none of the formal physics holds up — if there are fatal flaws throughout — is the core intuition (Nyquist applied to quantum observation) still worth anything as a conceptual framework, even if not as a physical theory?
I've been sitting with this idea for long enough that I genuinely can't tell anymore
whether it's something or nothing. I suspect the answer requires someone who can hold
both the intuition and the mathematics at the same time — which is not something I
can do alone.

References
Bell, J.S. (1964). On the Einstein-Podolsky-Rosen paradox. Physics, 1(3), 195–200.
Aspect, A., Dalibard, J., & Roger, G. (1982). Experimental test of Bell's inequalities using time-varying analyzers. Physical Review Letters, 49, 1804.
Bohm, D. (1952). A suggested interpretation of the quantum theory in terms of hidden variables. Physical Review, 85(2), 166.
Nyquist, H. (1928). Certain topics in telegraph transmission theory. Transactions of the AIEE, 47, 617–644.
Shannon, C.E. (1949). Communication in the presence of noise. Proceedings of the IRE, 37(1), 10–21.
Zeilinger, A. (2022). Nobel Prize lecture: Experiment and the foundations of quantum
physics.

I wrote this paper because I couldn't stop thinking about it. If it turns out to be wrong, I'd rather know. If it turns out to be right, I'd rather not be the only one thinking about it.
— Mike Kaman, Byron Center MI — Kamaninc@yahoo.com
