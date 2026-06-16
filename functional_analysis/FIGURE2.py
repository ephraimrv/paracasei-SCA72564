#!/usr/bin/env python3
"""Generates Figure 2: Multi-panel functional genomic enrichment of L. paracasei SCA72564.

Produces a three-panel lollipop figure summarising Z-score enrichment across
COG functional categories (Panel A), KEGG metabolic pathway groups (Panel B),
and representative CAZy family distributions (Panel C). Bubble area scales
with the absolute gene count per category; colour encodes enrichment direction
relative to the L. paracasei species-level baseline (ProbioMinServer2).

Output files:
    SCA72564_Figure2_functional_enrichment.tiff  — 600 dpi TIFF for journal submission
    SCA72564_Figure2_functional_enrichment.png   — 300 dpi PNG for draft review

Usage:
    python3 figure2_functional_enrichment.py

Todo:
    Confirm PANEL_B_DATA and PANEL_C_DATA values flagged with [VERIFY] comments
    against raw ProbioMinServer2 output tables before final submission.

References:
    Vallente, J.E. et al. (2026). Prebiotic Adaptations of Lacticaseibacillus
    paracasei subsp. paracasei SCA72564 Isolated from Dioscorea esculenta in
    Ilocos Norte, Philippines.

    eggNOG-mapper v2.1.12; KEGG (Kanehisa, 2000); CAZy (Drula et al., 2022).
    Raw outputs archived at: https://github.com/ephraimrv/<repo>
"""

__author__ = "Jan Ephraim R. Vallente"
__email__ = "ephrvallente@gmail.com"
__version__ = "1.0.0"
__license__ = "MIT"
__status__ = "Final"


# ─── third-party ─────────────────────────────────────────────────────────────
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# ─── figure configuration constants ──────────────────────────────────────────
# Journal target: double-column width (7.0 in) with 3 stacked panels.
# Increase FIGURE_HEIGHT to 10.5 if label text overflows on narrow displays.
FIGURE_WIDTH: float = 7.0
FIGURE_HEIGHT: float = 9.0
DPI_TIFF: int = 600  # minimum for most journals; use 1200 for line art only
DPI_PNG: int = 300
FONT_FAMILY: str = "monospace"
FONT_MONOSPACE: str = "JetBrainsMonoNL NFM"
BASE_FONT_SIZE: int = 9

# Bubble area scaling: s = BUBBLE_BASE + sqrt(count) * BUBBLE_SCALE
# Matplotlib scatter 's' is area in typographic points².
# Practical visible range: ~30 (single gene) → ~300 (300+ genes).
BUBBLE_BASE: float = 30.0
BUBBLE_SCALE: float = 14.0

# Shared x-axis range across all three panels (enables visual comparison).
XAXIS_MIN: float = -2.0
XAXIS_MAX: float = 8.0

# ─── panel data ──────────────────────────────────────────────────────────────
# Each dict contains:
#   label  : panel heading string (e.g. "A. COG Categories")
#   labs   : y-axis category labels (top → bottom)
#   vals   : corresponding Z-scores
#   counts : absolute gene count per category (drives bubble area)
#
# IMPORTANT — counts drive bubble size only; they do not affect Z-scores.
# All vals and counts should match the values reported in the manuscript
# Results section. Items marked [VERIFY] need confirmation from raw output
# before this figure is submitted.

PANEL_A_DATA: dict = {
    "label": "A.  COG Functional Categories",
    "labs": [
        "Extracellular struct. (W)",
        "Cell motility (N)",
        "Signal transduction (T)",
        "Carbohydrate metab. (G)",
        "Cell wall/membrane (M)",
        "Replication/repair (L)",
    ],
    # Z = 5.688 for Category W — corrected from 5.689 in earlier draft.
    # All values confirmed against manuscript Results section.
    "vals": [5.688, 1.290, 0.718, 0.713, 0.687, -1.143],
    # Gene counts confirmed from manuscript:
    #   W=1 (tetratricopeptide repeat protein), G=295, M=143, L=132.
    #   N=9 and T=62: [VERIFY] — confirm from eggNOG COG output table.
    "counts": [1, 9, 62, 295, 143, 132],
}

PANEL_B_DATA: dict = {
    "label": "B.  KEGG Metabolic Pathway Groups",
    "labs": [
        "Immune System",
        "Folding/Sorting/Deg.",
        "Membrane Transport",
        "Glycan Biosynth./Metab.",
        "Carbohydrate Metab.",
        "Environmental Adapt.",
    ],
    # Z-scores confirmed from raw KEGG pathway Z-score output:
    #   Immune System 0.908, Folding 0.812, Membrane Transport 0.752,
    #   Glycan Biosynthesis/Metabolism 0.705, Carbohydrate Metabolism 0.676,
    #   Environmental Adaptation -0.434.
    "vals": [0.908, 0.812, 0.752, 0.705, 0.676, -0.434],
    # Counts confirmed from manuscript where stated:
    #   Membrane Transport = 225, Carbohydrate Metabolism = 284.
    # Immune System, Folding, Glycan, and Environmental Adaptation counts:
    #   [VERIFY] — confirm gene counts from the KEGG mapping output table
    #   (the Z-score file does not contain per-group gene counts).
    "counts": [12, 42, 225, 30, 284, 38],
}

PANEL_C_DATA: dict = {
    "label": "C.  Representative CAZy Families",
    "labs": [
        "GH94 (cellobiose phosphorylase)",
        "GT36 (EPS glycosyltransferase)",
        "GT84 (EPS glycosyltransferase)",
        "GH3 (\u03b2-glucosidase)",
        "GT4 (PG/EPS precursor)",
        "GH13 (\u03b1-amylase)",
        # GH31 (α-glucosidase) IS cited in the manuscript Results; GH32 from an
        # earlier draft was an error and has been removed. All values below are
        # confirmed against the raw --isolate-s CAZy SCAT Z-score output.
        "GH31 (\u03b1-glucosidase)",
    ],
    # All Z-scores confirmed from raw SCAT output:
    #   GH94/GT36/GT84 = 6.245; GH3 = 2.347; GT4 = 1.520;
    #   GH13 = -0.544; GH31 = -0.434.
    "vals": [6.245, 6.245, 6.245, 2.347, 1.520, -0.544, -0.434],
    # Family gene counts in SCA72564. GT4=9, GH13=7 retained from draft;
    # confirm single-gene families (GH94/GT36/GT84) against annotation if needed.
    "counts": [1, 1, 1, 2, 9, 7, 4],  # GH31=4 confirmed from SCA72564_COUNTS.tsv
}

PANEL_DATA: list[dict] = [PANEL_A_DATA, PANEL_B_DATA, PANEL_C_DATA]

# ─── figure caption (for reference; not rendered in the figure itself) ────────
FIGURE_CAPTION: str = (
    "Figure 2. Functional genomic enrichment of L. paracasei SCA72564 relative to "
    "the species-level baseline. Z-scores were computed as Z = (x − μ) / σ, where x "
    "is the gene count per category in SCA72564, μ the mean count across reference "
    "L. paracasei genomes, and σ the standard deviation. "
    "(A) COG functional category distribution. "
    "(B) KEGG metabolic pathway group enrichment. "
    "(C) Representative CAZy family enrichment. "
    "Bubble area is proportional to the absolute gene count per category. "
    "Orange bubbles indicate enrichment (Z > 0); red bubbles indicate depletion (Z < 0). "
    "The dashed vertical line marks Z = 0."
)


# ─── helper functions ─────────────────────────────────────────────────────────


def compute_bubble_sizes(counts: list[int]) -> list[float]:
    """Convert gene counts to matplotlib scatter marker areas.

    Uses a square-root scaling law so that bubble area grows sub-linearly
    with gene count, preventing low-count families from disappearing and
    high-count families from overwhelming the panel.

    Args:
        counts: Absolute gene counts for each category.

    Returns:
        List of marker areas (points²) suitable for the ``s`` parameter
        of :func:`matplotlib.axes.Axes.scatter`.
    """
    return [BUBBLE_BASE + np.sqrt(c) * BUBBLE_SCALE for c in counts]


def category_color(
    z_score: float, cmap: matplotlib.colors.Colormap, z_max_pos: float
) -> tuple[float, float, float, float]:
    """Map a single Z-score to an RGBA colour.

    Enriched categories (Z ≥ 0) receive a warm orange hue scaled by
    relative enrichment magnitude.  Depleted categories (Z < 0) receive
    a fixed semantic red.

    Args:
        z_score:   Z-score for one category.
        cmap:      Matplotlib colourmap instance for positive values.
        z_max_pos: Maximum positive Z-score in the current panel (used for
                   normalisation).

    Returns:
        RGBA tuple in [0, 1] range.
    """
    if z_score >= 0:
        normalised = 0.30 + (z_score / z_max_pos) * 0.65
        return cmap(min(normalised, 1.0))
    return (0.80, 0.15, 0.15, 1.00)  # desaturated red for depletion


def draw_panel(
    ax: plt.Axes,
    data: dict,
    panel_letter: str,
    cmap: matplotlib.colors.Colormap,
    is_bottom: bool = False,
) -> None:
    """Render one lollipop panel onto a pre-existing Axes object.

    Args:
        ax:           Target Axes.
        data:         Panel data dict with keys ``label``, ``labs``,
                      ``vals``, and ``counts``.
        panel_letter: Single uppercase letter for the panel label (e.g., "A").
        cmap:         Colourmap for enriched categories.
        is_bottom:    If True, draw the shared x-axis label.

    Returns:
        None
    """
    labels = data["labs"]
    values = data["vals"]
    counts = data["counts"]
    sizes = compute_bubble_sizes(counts)
    z_max = max((v for v in values if v > 0), default=1.0)
    colours = [category_color(v, cmap, z_max) for v in values]

    # Strip panel background fill for transparent output
    ax.set_facecolor("none")

    # --- reference line at Z = 0 ---
    ax.axvline(0, color="black", linewidth=0.9, linestyle="--", alpha=0.50, zorder=1)

    # --- light horizontal grid ---
    ax.set_axisbelow(True)
    ax.grid(axis="x", color="grey", linestyle=":", linewidth=0.4, alpha=0.5)

    # --- lollipop stems ---
    ax.hlines(
        y=labels,
        xmin=0,
        xmax=values,
        color=colours,
        alpha=0.55,
        linewidth=1.8,
        zorder=2,
    )

    # --- bubbles ---
    ax.scatter(
        values,
        labels,
        s=sizes,
        color=colours,
        zorder=3,
        edgecolors="black",
        linewidths=0.5,
    )

    # --- axes configuration ---
    ax.set_xlim(XAXIS_MIN, XAXIS_MAX)
    ax.invert_yaxis()
    ax.tick_params(axis="both", which="major", labelsize=BASE_FONT_SIZE)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # --- panel title (flush left, inside axes) ---
    ax.set_title(
        data["label"],
        loc="left",
        fontweight="bold",
        fontsize=BASE_FONT_SIZE,
        pad=4,
    )

    # --- bold panel letter (top-left corner) ---
    ax.text(
        -0.08,
        1.02,
        panel_letter,
        transform=ax.transAxes,
        fontsize=BASE_FONT_SIZE + 1,
        fontweight="bold",
        va="bottom",
        ha="left",
    )

    # --- x-axis label on bottom panel only ---
    if is_bottom:
        ax.set_xlabel("Z-score (relative to species baseline)", fontsize=BASE_FONT_SIZE)


def add_legend(ax: plt.Axes) -> None:
    """Attach a compact bubble-size legend to Panel B's axes.

    Placed inside Panel B (KEGG), which has the most white space —
    all Z-scores top out at 0.908 on an x-axis that runs to 8, leaving
    the right ~85% of that panel empty.  Anchoring the legend here avoids
    the bottom-panel overlap caused by a figure-level legend.

    Args:
        ax: The Panel B Axes object (KEGG panel).

    Returns:
        None
    """
    legend_counts = [1, 50, 250]
    legend_sizes = compute_bubble_sizes(legend_counts)
    handles = [
        plt.scatter(
            [],
            [],
            s=s,
            color="grey",
            edgecolors="black",
            linewidths=0.4,
            label=f"n = {cnt} genes",
        )
        for s, cnt in zip(legend_sizes, legend_counts)
    ]
    ax.legend(
        handles=handles,
        title="Gene count",
        title_fontsize=BASE_FONT_SIZE - 1,
        fontsize=BASE_FONT_SIZE - 1,
        loc="center right",
        frameon=True,
        framealpha=0.92,
        edgecolor="grey",
        facecolor="none",  # Force legend frame to be transparent/clear
        handletextpad=0.4,
        labelspacing=0.6,
        borderpad=0.7,
    )


# ─── main entry point ────────────────────────────────────────────────────────


def generate_figure(
    output_stem: str = "SCA72564_Figure2_functional_enrichment",
) -> None:
    """Generate and save Figure 2 as high-resolution TIFF and PNG.

    Creates a three-panel lollipop figure and writes:
        ``{output_stem}.tiff`` — 600 dpi TIFF for journal submission.
        ``{output_stem}.png``  — 300 dpi PNG for draft review.

    Args:
        output_stem: File name stem (without extension) for both outputs.

    Returns:
        None

    Raises:
        OSError: If matplotlib cannot locate the configured font, change
            ``FONT_MONOSPACE`` to ``"Courier New"`` or ``"DejaVu Sans Mono"``
            as a cross-platform fallback.
    """
    # --- global typography ---
    plt.rcParams["font.family"] = FONT_FAMILY
    plt.rcParams["font.monospace"] = [FONT_MONOSPACE]
    plt.rcParams["font.size"] = BASE_FONT_SIZE
    plt.rcParams["axes.linewidth"] = 0.8

    # --- colourmap (use new API; falls back gracefully on older matplotlib) ---
    try:
        cmap = matplotlib.colormaps["Oranges"]
    except AttributeError:  # matplotlib < 3.5
        cmap = plt.get_cmap("Oranges")  # type: ignore[attr-defined]

    # --- build figure ---
    panel_letters = ["A", "B", "C"]
    fig, axes = plt.subplots(
        3,
        1,
        figsize=(FIGURE_WIDTH, FIGURE_HEIGHT),
        dpi=DPI_PNG,
        constrained_layout=True,
    )

    # Strip figure canvas background fill for transparent output
    fig.patch.set_facecolor("none")

    for idx, (ax, data, letter) in enumerate(zip(axes, PANEL_DATA, panel_letters)):
        draw_panel(
            ax=ax,
            data=data,
            panel_letter=letter,
            cmap=cmap,
            is_bottom=(idx == len(PANEL_DATA) - 1),
        )

    add_legend(axes[1])  # anchor legend inside Panel B (most empty space)

    # --- save TIFF (submission) ---
    tiff_path = f"{output_stem}.tiff"
    fig.savefig(tiff_path, format="tiff", dpi=DPI_TIFF, bbox_inches="tight")
    print(f"Saved: {tiff_path}  ({DPI_TIFF} dpi)")

    # --- save PNG (draft review — transparent background) ---
    # Transparent background floats cleanly in Word/Slides without a white box.
    # The TIFF stays white as journals expect for print.
    png_path = f"{output_stem}.png"
    fig.savefig(
        png_path, format="png", dpi=DPI_PNG, bbox_inches="tight", transparent=True
    )
    print(f"Saved: {png_path}  ({DPI_PNG} dpi, transparent)")

    plt.close(fig)
    print(f"\nFigure caption (for manuscript):\n{FIGURE_CAPTION}")


def main() -> None:
    """Entry point when the script is executed directly."""
    generate_figure()


if __name__ == "__main__":
    main()
