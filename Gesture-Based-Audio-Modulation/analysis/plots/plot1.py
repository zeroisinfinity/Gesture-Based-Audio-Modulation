import os
import pandas as pd
import matplotlib
# Prevent display pop-up warnings in non-interactive environments
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Load results
df = pd.read_csv("analysis/results.csv")
# Ensure output directory exists
os.makedirs("analysis/figures", exist_ok=True)

# Set contemporary academic design baseline
plt.style.use("seaborn-v0_8-whitegrid")

# Create figure with high-clarity layout
fig, ax1 = plt.subplots(figsize=(12, 6.5), dpi=600)
fig.set_layout_engine(None)

# High-contrast, publication-grade colors
color_gesture = "#2b5c8f"   # Muted slate blue
color_velocity = "#d95f02"  # Muted energetic orange

# 1. Primary Axis (Left): Gesture Position
line1 = ax1.plot(
    df["frame"],
    df["gesture"],
    color=color_gesture,
    linewidth=3.5,          # Strong printing presence
    label="Gesture",
    alpha=0.95,
)

# Balanced primary normalized layout limits (7 intervals total)
ax1.set_ylim(-0.2, 1.2)
ax1.set_yticks(np.arange(-0.2, 1.21, 0.2))

ax1.set_xlabel("Frame", fontsize=14, fontweight="medium", labelpad=12, color="#222222")
ax1.set_ylabel("Gesture Position (normalized)", fontsize=14, fontweight="bold", color=color_gesture, labelpad=15)
ax1.tick_params(axis="y", labelcolor=color_gesture, labelsize=12)
ax1.tick_params(axis="x", labelcolor="#222222", labelsize=12)

# Symmetrical horizontal reference line matching the zero mark exactly
ax1.axhline(0.2, color="#777777", linestyle="-.", linewidth=1.0, alpha=0.5)

# 2. Secondary Axis (Right): Velocity with Perfect Buffer Padding
ax2 = ax1.twinx()

line2 = ax2.plot(
    df["frame"],
    df["velocity"],
    color=color_velocity,
    linewidth=3.5,
    label="Velocity",
    alpha=0.95,
)

# FIXED: Set bounds to (-14, 14) with a step of 4.
# This gives the -12 data points a clean safety margin above the frame border,
# while maintaining exactly 7 intervals to lock perfectly with the left grid lines.
ax2.set_ylim(-14, 14)
ax2.set_yticks(np.arange(-14, 15, 4))

ax2.set_ylabel("Velocity (normalized units/s)", fontsize=14, fontweight="bold", color=color_velocity, labelpad=18)
ax2.tick_params(axis="y", labelcolor=color_velocity, labelsize=12)

# 3. Clean Research-Style Borders & Structural Spines
for ax in [ax1, ax2]:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#cccccc")

ax1.spines["left"].set_visible(True)
ax1.spines["left"].set_color(color_gesture)
ax1.spines["left"].set_linewidth(1.5)

ax2.spines["right"].set_visible(True)
ax2.spines["right"].set_color(color_velocity)
ax2.spines["right"].set_linewidth(1.5)

# 4. Refined Dashed Grid
ax1.grid(True, linestyle="--", alpha=0.5, color="#cccccc")
ax2.grid(False)

# 5. Concise Academic Title
ax1.set_title(
    "Gesture to Velocity Transformation",
    fontsize=18,
    fontweight="bold",
    pad=25,
    color="#111111",
    loc="left",
)

# 6. Unified Legend Box positioned horizontally beneath the graph
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(
    lines,
    labels,
    loc="upper center",
    bbox_to_anchor=(0.5, -0.16),
    ncol=2,
    frameon=True,
    facecolor="#ffffff",
    edgecolor="#cccccc",
    shadow=False,
    fontsize=12,
)

# Rigid canvas margins to preserve positions exactly
plt.subplots_adjust(left=0.10, right=0.90, bottom=0.20, top=0.88)

# 7. Ultra-High Resolution Dual-Format Exports
output_base_path = "analysis/figures/gesture_velocity"

plt.savefig(
    f"{output_base_path}.png",
    dpi=600,
    bbox_inches=None,
    transparent=False,
    facecolor="#ffffff",
)
plt.savefig(
    f"{output_base_path}.pdf",
    bbox_inches=None,
    transparent=False,
    facecolor="#ffffff",
)

print(f"Success! Perfect raw figures exported at 600 DPI to {output_base_path}.png/.pdf")
plt.close()
