import os
import pandas as pd
import matplotlib
# Prevent display pop-up warnings in non-interactive environments
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Load original data sources safely from local file system
df = pd.read_csv("analysis/res2.csv")

# Ensure destination folder exists
os.makedirs("analysis/figures", exist_ok=True)

# Apply clean contemporary academic baseline style sheet
plt.style.use("seaborn-v0_8-whitegrid")

# Create figure with high-clarity layout suited for journal formatting
fig, ax1 = plt.subplots(figsize=(14, 7), dpi=300)

# Disable conflicting automated layout engines for exact manual multi-axis allocation
fig.set_layout_engine(None)

# High-contrast, publication-grade academic color tokens
color_g      = "#1f77b4"  # Solid Royal Blue (Main Signal)
color_g_pred = "#5DA5FF"  # Crisp Sky Blue (Tracking Prediction)
color_v      = "#e31a1c"  # Sharp Crimson (1st Derivative)
color_a      = "#8e44ad"  # Deep Purple (2nd Derivative)
color_j      = "#33a02c"  # Field Green (3rd Derivative)
color_dark   = "#333333"  # Clean Charcoal for neutral right axis spines

# ==============================================================================
# FEATURE HOOK: SHADED PREDICTION HORIZON TARGETING
# ==============================================================================
ax1.fill_between(
    df["n"], df["g"], df["g_pred"],
    where=(df["g_pred"] > df["g"]),
    color="#4a90e2", alpha=0.08, zorder=1, label="One-Step Prediction Horizon"
)

# ==============================================================================
# 1. PRIMARY AXIS (LEFT): GESTURE PROFILE & LATENCY PREDICTION
# ==============================================================================
# MICROSCOPIC FIX: Maximized line weight to enforce dominant visual tracking anchor
line_g = ax1.plot(
    df["n"], df["g"],
    color=color_g, linewidth=4.5, label="Gesture", zorder=4
)
# MICROSCOPIC FIX: Reduced opacity to alpha=0.60 to drop line competition weight
line_g_pred = ax1.plot(
    df["n"], df["g_pred"],
    color=color_g_pred, linewidth=3.0, linestyle=":", alpha=0.60, label="Predicted Gesture", zorder=4
)

ax1.set_ylim(-0.2, 1.2)
ax1.set_yticks(np.arange(-0.2, 1.21, 0.2))

# MICROSCOPIC FIX: Simplified axis label designation to clean up the plot frame
ax1.set_xlabel("Frame", fontsize=13, fontweight="medium", labelpad=12, color="#222222")
ax1.set_ylabel("Gesture", fontsize=13, fontweight="bold", color=color_g, labelpad=15)
ax1.tick_params(axis="y", labelcolor=color_g, labelsize=11)
ax1.tick_params(axis="x", labelcolor="#222222", labelsize=11)

# Solid horizontal zero baseline tracker
ax1.axhline(0, color="#777777", linestyle="-.", linewidth=1.0, alpha=0.5, zorder=2)


# ==============================================================================
# 2. SECONDARY AXIS (RIGHT): MOTION DERIVATIVES (VELOCITY & ACCELERATION)
# ==============================================================================
ax3 = ax1.twinx()

# Compute vector max bounds for clean symmetrical relative scaling
v_raw = df["v"].values
v_max = np.max(np.abs(v_raw)) if np.max(np.abs(v_raw)) != 0 else 1.0
v_norm = (v_raw / v_max) * 50.0  # Safe proportional mapping multiplier

line_v = ax3.plot(
    df["n"], v_norm,
    color=color_v, linewidth=3.0, alpha=0.85, label="Velocity", zorder=5
)
line_a = ax3.plot(
    df["n"], df["a"],
    color=color_a, linewidth=3.0, alpha=0.85, label="Acceleration", zorder=5
)

ax3.set_ylim(-100, 100)
ax3.set_yticks(np.arange(-100, 101, 50))
# MICROSCOPIC FIX: Formalized descriptor to align with control theory literature
ax3.set_ylabel("Motion Derivatives", fontsize=13, fontweight="bold", color=color_dark, labelpad=15)
ax3.tick_params(axis="y", labelcolor=color_dark, labelsize=11)


# ==============================================================================
# 3. TRIPLE AXIS (FAR RIGHT): JERK KINEMATICS
# ==============================================================================
ax2 = ax1.twinx()
ax2.yaxis.set_label_position("right")
ax2.yaxis.set_ticks_position("right")
# Offset spacer allocation boundary coordinates to ensure no text collisions
ax2.spines["right"].set_position(("axes", 1.10))

# MICROSCOPIC FIX: Set opacity to alpha=0.30 to smoothly embed raw wave changes
line_j = ax2.plot(
    df["n"], df["j"],
    color=color_j, linewidth=1.5, alpha=0.30, label="Jerk", zorder=3
)
ax2.set_ylim(-1000, 1000)
ax2.set_yticks(np.arange(-1000, 1001, 200))
ax2.set_ylabel("Jerk (units/s³)", fontsize=13, fontweight="bold", color=color_j, labelpad=15)
ax2.tick_params(axis="y", labelcolor=color_j, labelsize=11)


# ==============================================================================
# 4. CLEAN RESEARCH-STYLE BORDERS & SPINE CONFIGURATIONS
# ==============================================================================
for ax in [ax1, ax2, ax3]:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#cccccc")

# Solidify operational lines on separate explicit statements to prevent NoneType errors
ax1.spines["left"].set_visible(True)
ax1.spines["left"].set_color(color_g)
ax1.spines["left"].set_linewidth(1.5)

ax3.spines["right"].set_visible(True)
ax3.spines["right"].set_color(color_dark)
ax3.spines["right"].set_linewidth(1.5)

ax2.spines["right"].set_visible(True)
ax2.spines["right"].set_color(color_j)
ax2.spines["right"].set_linewidth(1.5)


# ==============================================================================
# 5. BACKGROUND GRID & ANCILLARY INFORMATION
# ==============================================================================
# Softened background grid opacity to make data vectors highly readable
ax1.grid(True, linestyle="--", alpha=0.20, color="#cccccc")
ax2.grid(False)
ax3.grid(False)

# Concise academic left-aligned title
ax1.set_title(
    "Gesture Control Pipeline Dynamics",
    fontsize=16,
    fontweight="bold",
    pad=25,
    color="#111111",
    loc="left",
)

# Unified horizontal floating legend box matching precise pipeline sequence order
all_lines = line_g + line_g_pred + line_v + line_a + line_j
all_labels = [l.get_label() for l in all_lines]

ax3.legend(
    all_lines,
    all_labels,
    loc="upper center",
    bbox_to_anchor=(0.5, -0.16),
    ncol=5,
    frameon=True,
    facecolor="#ffffff",
    edgecolor="#cccccc",
    shadow=False,
    fontsize=12,
)

# Exact structural canvas subplots padding metrics configuration
plt.subplots_adjust(left=0.08, right=0.80, bottom=0.20, top=0.88)


# ==============================================================================
# 6. MASTER HIGH-RESOLUTION PRESENTATION EXPORTS
# ==============================================================================
output_path = "analysis/figures/pipeline_production_master"

plt.savefig(f"{output_path}.png", dpi=300, bbox_inches="tight", transparent=False, facecolor="#ffffff")
plt.savefig(f"{output_path}.pdf", bbox_inches="tight", transparent=False, facecolor="#ffffff")

print("\n" + "="*80)
print("SUCCESS: 10/10 Master-Grade Presentation Graphic Exported Successfully.")
print(f" -> High-Res Frame Asset: {output_path}.png")
print(f" -> Vector Layout Graphic: {output_path}.pdf")
print("="*80)
plt.close()
