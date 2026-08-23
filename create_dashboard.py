import pandas as pd
import matplotlib.pyplot as plt

# Load YOUR security events data
df = pd.read_csv("security_events.csv")

# ==========================================================
# CALCULATE KEY NUMBERS
# ==========================================================

total_events = len(df)

high_critical = len(
    df[df["severity"].isin(["High", "Critical"])]
)

most_common_event = df["event_type"].value_counts().idxmax()

top_source = df["source"].value_counts().idxmax()

# ==========================================================
# CREATE DASHBOARD
# ==========================================================

fig = plt.figure(figsize=(14, 9))

fig.suptitle(
    "IT SECURITY OPERATIONS DASHBOARD",
    fontsize=22,
    fontweight="bold"
)

# ----------------------------------------------------------
# KPI 1
# ----------------------------------------------------------

fig.text(
    0.15, 0.87,
    f"TOTAL EVENTS\n{total_events}",
    ha="center",
    va="center",
    fontsize=16
)

# ----------------------------------------------------------
# KPI 2
# ----------------------------------------------------------

fig.text(
    0.38, 0.87,
    f"HIGH / CRITICAL\n{high_critical}",
    ha="center",
    va="center",
    fontsize=16
)

# ----------------------------------------------------------
# KPI 3
# ----------------------------------------------------------

fig.text(
    0.63, 0.87,
    f"TOP EVENT\n{most_common_event}",
    ha="center",
    va="center",
    fontsize=13
)

# ----------------------------------------------------------
# KPI 4
# ----------------------------------------------------------

fig.text(
    0.86, 0.87,
    f"TOP SOURCE\n{top_source}",
    ha="center",
    va="center",
    fontsize=13
)

# ==========================================================
# CHART 1 — SEVERITY
# ==========================================================

ax1 = fig.add_axes([0.08, 0.52, 0.38, 0.25])

df["severity"].value_counts().plot(
    kind="bar",
    ax=ax1
)

ax1.set_title("Security Events by Severity")
ax1.set_xlabel("Severity")
ax1.set_ylabel("Number of Events")

# ==========================================================
# CHART 2 — DEPARTMENT
# ==========================================================

ax2 = fig.add_axes([0.55, 0.52, 0.38, 0.25])

df["department"].value_counts().plot(
    kind="bar",
    ax=ax2
)

ax2.set_title("Security Events by Department")
ax2.set_xlabel("Department")
ax2.set_ylabel("Number of Events")

ax2.tick_params(axis="x", rotation=45)

# ==========================================================
# CHART 3 — SECURITY TECHNOLOGY
# ==========================================================

ax3 = fig.add_axes([0.08, 0.12, 0.38, 0.25])

df["source"].value_counts().plot(
    kind="bar",
    ax=ax3
)

ax3.set_title("Events by Security Technology")
ax3.set_xlabel("Technology")
ax3.set_ylabel("Number of Events")

ax3.tick_params(axis="x", rotation=20)

# ==========================================================
# CHART 4 — EVENT TYPES
# ==========================================================

ax4 = fig.add_axes([0.55, 0.12, 0.38, 0.25])

df["event_type"].value_counts().plot(
    kind="bar",
    ax=ax4
)

ax4.set_title("Most Common Security Events")
ax4.set_xlabel("Event Type")
ax4.set_ylabel("Number of Events")

ax4.tick_params(axis="x", rotation=45)

# ==========================================================
# SAVE DASHBOARD
# ==========================================================

plt.savefig(
    "security_dashboard.png",
    dpi=200,
    bbox_inches="tight"
)

plt.close()

print("Security dashboard created successfully!")
print("File: security_dashboard.png")
