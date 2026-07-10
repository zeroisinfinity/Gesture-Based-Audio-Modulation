import os
import pandas as pd
import matplotlib.pyplot as plt

# Load results
df = pd.read_csv("analysis/results.csv")
# Ensure output directory exists
os.makedirs("analysis/figures", exist_ok=True)

# Set contemporary academic design baseline
plt.style.use("seaborn-v0_8-whitegrid")

# Create figure with ample breathing room for dual-axis typography
fig, ax1 = plt.subplots(figsize=(12, 6), dpi=600)

# High-contrast, publication-grade colors
color_gesture = "#2b5c8f"   # Muted slate blue
color_velocity = "#d95f02"  # Muted energetic orange

# 1. Primary Axis (Left): Gesture Position
line1 = ax1.plot(
    df["frame"],
    df["gesture"],
    color=color_gesture,
    linewidth=3.5,          # Beefed up for strong printing/scaling presence
    label="Gesture",
    alpha=0.95,
)
ax1.set_xlabel(
    "Frame", fontsize=14, fontweight="medium", labelpad=12, color="#222222"
)
ax1.set_ylabel(
    "Gesture Position (normalized)", fontsize=14, fontweight="bold", color=color_gesture, labelpad=12
)
ax1.tick_params(axis="y", labelcolor=color_gesture, labelsize=12) # Increased point size
ax1.tick_params(axis="x", labelcolor="#222222", labelsize=12)

# 2. Secondary Axis (Right): Velocity
ax2 = ax1.twinx()
line2 = ax2.plot(
    df["frame"],
    df["velocity"],
    color=color_velocity,
    linewidth=3.5,          # Matching structural weight
    label="Velocity",
    alpha=0.95,
)
ax2.set_ylabel(
    "Velocity (normalized units/s)", fontsize=14, fontweight="bold", color=color_velocity, labelpad=14
)
ax2.tick_params(axis="y", labelcolor=color_velocity, labelsize=12) # Increased point size

# 3. Clean Research-Style Borders & Structural Spines
for ax in [ax1, ax2]:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("#cccccc")

# Bind structural bounds to color-coded scales
ax1.spines["left"].set_visible(True)
ax1.spines["left"].set_color(color_gesture)
ax1.spines["left"].set_linewidth(1.5)

ax2.spines["right"].set_visible(True)
ax2.spines["right"].set_color(color_velocity)
ax2.spines["right"].set_linewidth(1.5)

# 4. Refined Dashed Grid
ax1.grid(True, linestyle="--", alpha=0.5, color="#cccccc")
ax2.grid(False)  # Turn off to prevent alignment clashes

# 5. Concise Academic Title
ax1.set_title(
    "Gesture to Velocity Transformation",
    fontsize=18,
    fontweight="bold",
    pad=25,
    color="#111111",
    loc="left",
)

# 6. Unified Floating Legend Box
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(
    lines,
    labels,
    loc="upper right",
    frameon=True,
    facecolor="#ffffff",
    edgecolor="none",
    shadow=True,
    fontsize=12,
)

# Tight layout formatting
plt.tight_layout()

# 7. Ultra-High Resolution Dual-Format Exports
output_base_path = "analysis/figures/gesture_velocity"

# Save as 600 DPI master raster image
plt.savefig(
    f"{output_base_path}.png",
    dpi=600,
    bbox_inches="tight",
    transparent=False,
    facecolor="#ffffff",
)

# Save as vector graphic PDF for LaTeX/Direct insertion
plt.savefig(
    f"{output_base_path}.pdf",
    bbox_inches="tight",
    transparent=False,
    facecolor="#ffffff",
)

print(f"Success! Figures exported at 600 DPI to {output_base_path}.png/.pdf")
plt.show()
plt.close()