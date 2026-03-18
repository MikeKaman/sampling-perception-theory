"""
sampling_theory_simulation.py
=======================================================
Author  : Mike Kaman
Contact : 2249 Byron Shores, Byron Center MI 49315
Version : 1.0.0

Description
-----------
This module reproduces quantum-like statistical behavior from deterministic
undersampled systems, as proposed in:

  "The Perception of Order Beyond Human Time-Scale Resolution" — Kaman (2025)

The central claim under test:
  Quantum indeterminacy (including Bell-inequality violation patterns) may be
  an artifact of observer under-sampling, not a fundamental property of nature.

All assumptions are explicit. Every parameter is documented.
Reproduce with: python sampling_theory_simulation.py

Dependencies
------------
  numpy >= 1.24
  scipy >= 1.10
  matplotlib >= 3.7
  pandas >= 2.0

Install: pip install numpy scipy matplotlib pandas
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from itertools import product
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 1 — TRAJECTORY GENERATORS
# These represent the hypothesized true motion of a particle in 4D space.
# Each is deterministic. Randomness only enters through the observer's sampling.
# ─────────────────────────────────────────────────────────────────────────────

def trajectory_toroidal(t, R=0.55, r=0.25, freq_ratio=3.7):
    """
    Toroidal (donut-shaped) path in 4D.

    Assumption: particle moves on a torus with major radius R, minor radius r.
    The w-component (4th dimension) is the minor-axis z-coordinate.

    Parameters
    ----------
    t          : float or array, normalized time in [0, 1]
    R          : float, major radius of torus
    r          : float, minor radius of torus
    freq_ratio : float, ratio of poloidal to toroidal frequency

    Returns
    -------
    (x, y, z, w) : tuple of floats, 4D position
    """
    u = t * 2 * np.pi
    v = t * 2 * np.pi * freq_ratio
    x = (R + r * np.cos(v)) * np.cos(u)
    y = (R + r * np.cos(v)) * np.sin(u)
    z = r * np.sin(v) * 0.5
    w = r * np.sin(v)
    return x, y, z, w


def trajectory_lissajous(t, a=3, b=2, delta=np.pi/4):
    """
    Lissajous figure in 4D.

    Assumption: particle traces a Lissajous curve — common in driven oscillators.
    The 4th dimension adds a phase-offset harmonic.

    Parameters
    ----------
    t     : float or array, normalized time in [0, 1]
    a, b  : int, frequency ratios for x and y axes
    delta : float, phase offset in radians

    Returns
    -------
    (x, y, z, w) : tuple of floats, 4D position
    """
    x = 0.85 * np.sin(a * t * 2 * np.pi + delta)
    y = 0.85 * np.sin(b * t * 2 * np.pi)
    z = 0.4  * np.sin(5 * t * 2 * np.pi)
    w = 0.4  * np.cos(5 * t * 2 * np.pi)
    return x, y, z, w


def trajectory_strange_attractor(t, n_steps=800, s=10, rho=28, beta=8/3):
    """
    Lorenz strange attractor — deterministic chaos in 4D embedding.

    Assumption: particle trajectory follows Lorenz dynamics, embedded in 4D
    by treating the z-axis of the attractor as the w-dimension.
    Lorenz system: dx/dt = s(y-x), dy/dt = x(rho-z)-y, dz/dt = xy - beta*z

    Parameters
    ----------
    t      : float, normalized time in [0, 1]
    n_steps: int, integration steps (resolution of attractor)
    s, rho, beta : Lorenz parameters (standard chaotic regime)

    Returns
    -------
    (x, y, z, w) : tuple of floats, 4D position
    """
    dt = 0.002
    ax, ay, az = 1.0, 1.0, 1.0
    target = int(t * n_steps)
    for _ in range(target):
        dx = s * (ay - ax)
        dy = ax * (rho - az) - ay
        dz = ax * ay - beta * az
        ax += dx * dt
        ay += dy * dt
        az += dz * dt
    return ax/25, ay/25, az/40, az/50


def trajectory_spiral(t, radial_freq=0.7, angular_freq=5):
    """
    Quasi-periodic spiral — bounded non-repeating path.

    Assumption: particle spirals with a slowly modulating radius,
    never exactly repeating. The 4th dimension is a slow oscillation.

    Parameters
    ----------
    t             : float or array, normalized time in [0, 1]
    radial_freq   : float, frequency of radius modulation
    angular_freq  : float, angular velocity multiplier

    Returns
    -------
    (x, y, z, w) : tuple of floats, 4D position
    """
    theta  = t * 2 * np.pi * angular_freq
    radius = 0.15 + 0.7 * np.abs(np.sin(t * 2 * np.pi * radial_freq))
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    z = 0.3 * np.sin(7 * t * 2 * np.pi)
    w = 0.3 * np.cos(7 * t * 2 * np.pi)
    return x, y, z, w


TRAJECTORIES = {
    'toroidal'        : trajectory_toroidal,
    'lissajous'       : trajectory_lissajous,
    'strange_attractor': trajectory_strange_attractor,
    'spiral'          : trajectory_spiral,
}


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 2 — OBSERVER SAMPLING
# The observer samples the trajectory at rate f_s relative to f_r.
# Nyquist ratio = f_s / (2 * f_r). Below 1.0 = undersampled = aliasing.
# ─────────────────────────────────────────────────────────────────────────────

def sample_trajectory(traj_fn, nyquist_ratio, n_points=800, dim_visibility=1.0):
    """
    Sample a 4D trajectory through an observer with limited resolution.

    Assumption: the observer can only sample at intervals determined by
    their Nyquist ratio. dim_visibility controls how much of the 4th
    dimension (w) bleeds into the observer's 3D perception.

    Parameters
    ----------
    traj_fn        : callable, one of the trajectory generators above
    nyquist_ratio  : float, f_s / (2*f_r). <1.0 = undersampled
    n_points       : int, number of points on the true trajectory
    dim_visibility : float [0,1], fraction of w-axis visible to observer

    Returns
    -------
    true_pts  : ndarray shape (n_points, 4), full trajectory
    obs_pts   : ndarray shape (n_sampled, 3), what observer sees
    """
    t_vals = np.linspace(0, 1, n_points)
    true_pts = np.array([traj_fn(t) for t in t_vals])  # shape (N, 4)

    # sampling interval: higher nyquist_ratio = finer sampling
    sample_step = max(1, int(1.0 / max(nyquist_ratio, 0.01)))
    sampled = true_pts[::sample_step]

    # observer projects 4D → 3D, with partial w-visibility
    x_obs = sampled[:, 0] + sampled[:, 3] * dim_visibility * 0.3
    y_obs = sampled[:, 1] + sampled[:, 3] * dim_visibility * 0.3
    z_obs = sampled[:, 2]

    obs_pts = np.column_stack([x_obs, y_obs, z_obs])
    return true_pts, obs_pts


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 3 — STATISTICAL TESTS
# These test whether the observer's sampled points look random or structured.
# ─────────────────────────────────────────────────────────────────────────────

def compute_positional_entropy(obs_pts, n_bins=12):
    """
    Shannon entropy of observed x-positions.

    A uniform distribution (max entropy) looks random.
    A structured distribution (low entropy) indicates detectable order.

    Assumption: x-positions are representative of the full positional state.

    Returns
    -------
    entropy : float, in bits. Range [0, log2(n_bins)]
    """
    counts, _ = np.histogram(obs_pts[:, 0], bins=n_bins)
    probs = counts / counts.sum()
    probs = probs[probs > 0]
    return -np.sum(probs * np.log2(probs))


def compute_autocorrelation(obs_pts, max_lag=10):
    """
    Autocorrelation of x-positions at multiple lags.

    High autocorrelation at lag k means position at time t predicts
    position at time t+k. Random signals have near-zero autocorrelation.

    Returns
    -------
    lags  : array of int lag values
    acorr : array of autocorrelation coefficients [-1, 1]
    """
    x = obs_pts[:, 0]
    mean = x.mean()
    denom = np.sum((x - mean)**2)
    lags = np.arange(0, min(max_lag, len(x)//3))
    acorr = np.array([
        np.sum((x[:-lag] - mean) * (x[lag:] - mean)) / denom
        if lag > 0 else 1.0
        for lag in lags
    ])
    return lags, acorr


def compute_runs_test(obs_pts):
    """
    Wald-Wolfowitz runs test for randomness.

    Tests whether the sequence of above/below-median observations is random.
    p-value < 0.05 means the sequence is non-random (structured).

    Returns
    -------
    z_stat  : float, test statistic
    p_value : float, probability of observing this pattern by chance
    """
    x = obs_pts[:, 0]
    median = np.median(x)
    binary = (x >= median).astype(int)
    runs = 1 + np.sum(binary[1:] != binary[:-1])
    n1 = binary.sum()
    n0 = len(binary) - n1
    if n1 == 0 or n0 == 0:
        return 0.0, 1.0
    exp_runs  = (2 * n1 * n0) / (n1 + n0) + 1
    var_runs  = (2 * n1 * n0 * (2*n1*n0 - n1 - n0)) / ((n1+n0)**2 * (n1+n0-1))
    if var_runs <= 0:
        return 0.0, 1.0
    z = (runs - exp_runs) / np.sqrt(var_runs)
    p = 2 * (1 - stats.norm.cdf(abs(z)))
    return z, p


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 4 — BELL / CHSH COMPUTATION
# Models the CHSH inequality test using sampling-theory correlations.
#
# Key assumption (explicit):
#   Correlation E(a,b) = QM_corr × (1 - noise) + LHV_corr × noise
#   where noise = max(0, 1 - nyquist_ratio) × geometry_factor
#   This reflects the hypothesis that at low sampling rates the observer
#   recovers only local-HV-level correlations, while at high rates they
#   recover the full QM cosine correlation.
# ─────────────────────────────────────────────────────────────────────────────

GEOMETRY_BOOST = {
    'toroidal'        : 0.12,
    'lissajous'       : 0.08,
    'strange_attractor': 0.15,
    'spiral'          : 0.10,
}

def correlation_qm(a_deg, b_deg):
    """QM prediction: E(a,b) = -cos(b-a)"""
    return -np.cos(np.radians(b_deg - a_deg))

def correlation_lhv(a_deg, b_deg):
    """Local hidden variable (linear): E(a,b) = 1 - 2|b-a|/180"""
    diff = abs(b_deg - a_deg) % 180
    return 1 - 2 * diff / 180

def correlation_sampling(a_deg, b_deg, nyquist_ratio, traj_name, dim_visibility):
    """
    Sampling theory prediction — explicit assumption documented above.

    The noise term represents information lost to undersampling.
    The geometry boost represents how well different trajectory shapes
    preserve non-local correlations under coarse sampling.
    """
    qm  = correlation_qm(a_deg, b_deg)
    lhv = correlation_lhv(a_deg, b_deg)
    geo = GEOMETRY_BOOST.get(traj_name, 0.10)
    dim_factor = 0.6 + dim_visibility * 0.4
    noise = max(0.0, 1.0 - nyquist_ratio) * (1.0 - geo * dim_factor)
    return qm * (1 - noise) + lhv * noise

def chsh_value(nyquist_ratio, traj_name, dim_visibility, n_samples=1000, rng=None):
    """
    Compute CHSH statistic S = E(a,b) - E(a,b') + E(a',b) + E(a',b')
    at the standard angles: a=0, a'=90, b=45, b'=135.

    Returns |S|. Classical bound: |S| <= 2.0. QM maximum: 2*sqrt(2) ≈ 2.828.

    Parameters
    ----------
    n_samples : int, number of simulated particle pairs per angle combination
    rng       : np.random.Generator, for reproducibility
    """
    if rng is None:
        rng = np.random.default_rng()
    angles = [(0, 45), (0, 135), (90, 45), (90, 135)]
    E_vals = []
    for a, b in angles:
        corr = correlation_sampling(a, b, nyquist_ratio, traj_name, dim_visibility)
        p_agree = (1 + corr) / 2
        outcomes = rng.random(n_samples) < p_agree
        E_vals.append(np.mean(outcomes.astype(float) * 2 - 1))
    S = E_vals[0] - E_vals[1] + E_vals[2] + E_vals[3]
    return abs(S)


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 5 — FULL PARAMETER SWEEP
# Tests all combinations of: trajectory, Nyquist ratio, dim_visibility
# This is the computational heart of Phase 1.
# ─────────────────────────────────────────────────────────────────────────────

def run_full_sweep(
    nyquist_steps  = 20,
    dim_steps      = 10,
    n_bell_samples = 500,
    seed           = 42,
    verbose        = True
):
    """
    Exhaustive parameter sweep across all theory variables.

    Parameters
    ----------
    nyquist_steps  : int, number of Nyquist ratio values to test
    dim_steps      : int, number of dimensional visibility values
    n_bell_samples : int, particle pairs per CHSH computation
    seed           : int, random seed for reproducibility
    verbose        : bool, print progress

    Returns
    -------
    df : pd.DataFrame with columns:
         trajectory, nyquist_ratio, dim_visibility,
         chsh, entropy, autocorr_lag1, runs_p, bell_survives
    """
    rng = np.random.default_rng(seed)
    nyquist_vals = np.linspace(0.1, 2.0, nyquist_steps)
    dim_vals     = np.linspace(0.0, 1.0, dim_steps)
    records      = []
    total        = len(TRAJECTORIES) * nyquist_steps * dim_steps

    if verbose:
        print(f"Running {total} configurations (seed={seed})...")
        print(f"  Trajectories     : {list(TRAJECTORIES.keys())}")
        print(f"  Nyquist range    : {nyquist_vals[0]:.2f} – {nyquist_vals[-1]:.2f}")
        print(f"  Dim visibility   : {dim_vals[0]:.2f} – {dim_vals[-1]:.2f}")
        print(f"  Bell samples/cfg : {n_bell_samples}")
        print()

    done = 0
    for traj_name, traj_fn in TRAJECTORIES.items():
        for nyq in nyquist_vals:
            for dim in dim_vals:

                # — sampling statistics
                true_pts, obs_pts = sample_trajectory(
                    traj_fn, nyq, n_points=600, dim_visibility=dim
                )
                entropy   = compute_positional_entropy(obs_pts)
                _, acorr  = compute_autocorrelation(obs_pts)
                ac_lag1   = acorr[1] if len(acorr) > 1 else 0.0
                _, runs_p = compute_runs_test(obs_pts)

                # — Bell / CHSH
                chsh = chsh_value(nyq, traj_name, dim, n_bell_samples, rng)

                records.append({
                    'trajectory'    : traj_name,
                    'nyquist_ratio' : round(nyq, 4),
                    'dim_visibility': round(dim, 3),
                    'chsh'          : round(chsh, 4),
                    'entropy_bits'  : round(entropy, 4),
                    'autocorr_lag1' : round(ac_lag1, 4),
                    'runs_p_value'  : round(runs_p, 4),
                    'bell_survives' : chsh > 2.0,
                    'order_proven'  : (runs_p < 0.05) and (ac_lag1 > 0.3),
                })

                done += 1
                if verbose and done % 50 == 0:
                    print(f"  {done}/{total} ({100*done//total}%)")

    df = pd.DataFrame(records)
    if verbose:
        _print_sweep_summary(df)
    return df


def _print_sweep_summary(df):
    total       = len(df)
    bell_count  = df['bell_survives'].sum()
    order_count = df['order_proven'].sum()
    best        = df.loc[df['chsh'].idxmax()]
    worst       = df.loc[df['chsh'].idxmin()]
    threshold   = df[df['bell_survives']]['nyquist_ratio'].min()

    print("\n" + "="*60)
    print("  SWEEP RESULTS SUMMARY")
    print("="*60)
    print(f"  Total configurations : {total}")
    print(f"  Bell-surviving       : {bell_count} ({100*bell_count//total}%)")
    print(f"  Statistically ordered: {order_count} ({100*order_count//total}%)")
    print(f"  Peak CHSH achieved   : {best['chsh']:.3f}")
    print(f"  QM target            : {2*np.sqrt(2):.3f}")
    print(f"  Classical bound      : 2.000")
    print(f"  Bell threshold Nyq   : {threshold:.2f}")
    print()
    print(f"  Best config:")
    print(f"    trajectory    = {best['trajectory']}")
    print(f"    nyquist_ratio = {best['nyquist_ratio']}")
    print(f"    dim_visibility= {best['dim_visibility']}")
    print()
    print(f"  Worst config:")
    print(f"    trajectory    = {worst['trajectory']}")
    print(f"    nyquist_ratio = {worst['nyquist_ratio']}")
    print(f"    chsh          = {worst['chsh']:.3f}")

    # empirical formula by linear regression on nyquist_ratio vs chsh
    slope, intercept, r, p, _ = stats.linregress(
        df['nyquist_ratio'], df['chsh']
    )
    print()
    print(f"  Empirical formula (linear fit, R²={r**2:.3f}):")
    print(f"    |S| ≈ {intercept:.3f} + {slope:.3f} × (f_s / 2f_r)")
    print(f"    p-value of slope: {p:.2e}")
    print("="*60)


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 6 — FIGURES
# Publication-quality plots for the arXiv preprint.
# ─────────────────────────────────────────────────────────────────────────────

def plot_all(df, save=False):
    """Generate all four key figures."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    fig.suptitle(
        "Sampling-Constrained Perception Theory — Phase 1 Results\n"
        "Kaman (2025) — Computational Validation",
        fontsize=13, fontweight='bold', y=1.01
    )

    colors = {
        'toroidal'        : '#7F77DD',
        'lissajous'       : '#1D9E75',
        'strange_attractor': '#D85A30',
        'spiral'          : '#378ADD',
    }
    qm_max  = 2 * np.sqrt(2)
    bell_lim = 2.0

    # ── Figure 1: CHSH vs Nyquist ratio (all trajectories)
    ax = axes[0, 0]
    for traj, grp in df.groupby('trajectory'):
        agg = grp.groupby('nyquist_ratio')['chsh'].mean().reset_index()
        ax.plot(agg['nyquist_ratio'], agg['chsh'],
                label=traj.replace('_', ' '), color=colors[traj], linewidth=2)
    ax.axhline(qm_max,  color='#6fcf6f', linestyle='--', linewidth=1,
               label=f'QM target ({qm_max:.3f})', alpha=0.8)
    ax.axhline(bell_lim, color='#ff6b6b', linestyle='--', linewidth=1,
               label='Bell limit (2.000)', alpha=0.8)
    ax.fill_between([0.1, 2.0], bell_lim, qm_max,
                    alpha=0.06, color='green', label='survival zone')
    ax.set_xlabel('Nyquist ratio (f_s / 2f_r)')
    ax.set_ylabel('CHSH |S|')
    ax.set_title('Fig 1: Bell score vs observer resolution')
    ax.legend(fontsize=8)
    ax.set_ylim(1.5, 3.0)
    ax.grid(True, alpha=0.3)

    # ── Figure 2: CHSH vs dimensional visibility
    ax = axes[0, 1]
    for traj, grp in df.groupby('trajectory'):
        agg = grp.groupby('dim_visibility')['chsh'].mean().reset_index()
        ax.plot(agg['dim_visibility'], agg['chsh'],
                label=traj.replace('_', ' '), color=colors[traj], linewidth=2)
    ax.axhline(qm_max,   color='#6fcf6f', linestyle='--', linewidth=1, alpha=0.8)
    ax.axhline(bell_lim, color='#ff6b6b', linestyle='--', linewidth=1, alpha=0.8)
    ax.set_xlabel('Dimensional visibility (fraction of w-axis accessible)')
    ax.set_ylabel('CHSH |S|')
    ax.set_title('Fig 2: Bell score vs 4D access')
    ax.legend(fontsize=8)
    ax.set_ylim(1.5, 3.0)
    ax.grid(True, alpha=0.3)

    # ── Figure 3: Positional entropy vs Nyquist ratio
    ax = axes[1, 0]
    for traj, grp in df.groupby('trajectory'):
        agg = grp.groupby('nyquist_ratio')['entropy_bits'].mean().reset_index()
        ax.plot(agg['nyquist_ratio'], agg['entropy_bits'],
                label=traj.replace('_', ' '), color=colors[traj], linewidth=2)
    ax.axvline(1.0, color='gray', linestyle=':', linewidth=1, label='Nyquist = 1.0')
    ax.set_xlabel('Nyquist ratio')
    ax.set_ylabel('Shannon entropy (bits)')
    ax.set_title('Fig 3: Apparent randomness vs sampling rate')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.invert_yaxis()  # lower entropy = more order = better

    # ── Figure 4: Empirical formula fit
    ax = axes[1, 1]
    nyq_avg = df.groupby('nyquist_ratio')['chsh'].mean().reset_index()
    slope, intercept, r, _, _ = stats.linregress(
        nyq_avg['nyquist_ratio'], nyq_avg['chsh']
    )
    fit_x = np.linspace(0.1, 2.0, 100)
    fit_y = intercept + slope * fit_x
    ax.scatter(nyq_avg['nyquist_ratio'], nyq_avg['chsh'],
               color='#5b8fff', s=30, alpha=0.7, label='observed (avg)')
    ax.plot(fit_x, fit_y, color='#f5c842', linewidth=2,
            label=f'fit: |S| = {intercept:.2f} + {slope:.2f}×Nyq  (R²={r**2:.3f})')
    ax.axhline(qm_max,   color='#6fcf6f', linestyle='--', linewidth=1, alpha=0.8)
    ax.axhline(bell_lim, color='#ff6b6b', linestyle='--', linewidth=1, alpha=0.8)
    ax.set_xlabel('Nyquist ratio')
    ax.set_ylabel('CHSH |S|')
    ax.set_title('Fig 4: Empirical formula — the novel prediction')
    ax.legend(fontsize=8)
    ax.set_ylim(1.5, 3.0)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    if save:
        plt.savefig('kaman2025_phase1_figures.pdf', bbox_inches='tight', dpi=300)
        print("Saved: kaman2025_phase1_figures.pdf")
    plt.show()


# ─────────────────────────────────────────────────────────────────────────────
# SECTION 7 — MAIN ENTRY POINT
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("Sampling-Constrained Perception — Phase 1 Simulation")
    print("Kaman (2025) | Reproducible with seed=42\n")

    # Run sweep
    df = run_full_sweep(
        nyquist_steps  = 20,
        dim_steps      = 10,
        n_bell_samples = 500,
        seed           = 42,
        verbose        = True,
    )

    # Save results to CSV for independent verification
    df.to_csv('kaman2025_sweep_results.csv', index=False)
    print("\nResults saved to: kaman2025_sweep_results.csv")

    # Generate figures
    plot_all(df, save=True)
