# Miguel now correct plus sign plot

import numpy as np
import matplotlib.pyplot as plt

# Define alpha values
alpha = np.linspace(0, 1, 1000)

# Define S(alpha)
S = np.sqrt(2) * (1 + 2 * alpha * np.sqrt(1 - alpha**2))

# Important points
alpha_max = 1 / np.sqrt(2)
S_max = 2 * np.sqrt(2)

# Bell violation threshold
threshold = 2

# Plot
plt.figure(figsize=(8, 5))

plt.plot(alpha, S, linewidth=2, label=r"$S(\alpha)$")

# Horizontal line S = 2
plt.axhline(y=2, linestyle='--', label=r"$S = 2$")

# Shade Bell-violation region
plt.fill_between(alpha, S, 2, where=(S > 2), alpha=0.3)

# Mark maximum point
plt.plot(alpha_max, S_max, 'o')
plt.text(alpha_max + 0.02, S_max - 0.05,
         r"$\left(\frac{1}{\sqrt{2}},\,2\sqrt{2}\right)$")

# Labels and title
plt.xlabel(r"$\alpha$")
plt.ylabel(r"$S(\alpha)$")
plt.title(r"CHSH S-waarde als functie van $\alpha$")

# Limits
plt.xlim(0, 1)
plt.ylim(1.3, 3.0)

# Grid and legend
plt.grid(True)
plt.legend()

# Save figure
plt.savefig("grafiek_swaarde_opdracht1_correct.png", dpi=300)

# Show plot
plt.show()

#################################################

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# -----------------------------
# Fixed parameters
# -----------------------------
Delta_t = 30e-9   # 30 ns
T = 1

# -----------------------------
# Parameter ranges
# -----------------------------
R1 = np.linspace(0, 2e4, 100)
R2 = np.linspace(0, 2e4, 100)

R1_grid, R2_grid = np.meshgrid(R1, R2)

# -----------------------------
# Poisson parameter
# -----------------------------
lam = R1_grid * R2_grid * Delta_t * T
P_acc = 1 - np.exp(-lam)

# -----------------------------
# Figure with subplots
# -----------------------------
fig = plt.figure(figsize=(14, 6))
fig.suptitle("De kans op minstens één accidentele coincidentie", fontsize=14, fontweight="bold")

# ---- 3D plot ----
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
surf = ax1.plot_surface(R1_grid, R2_grid, P_acc, cmap='viridis')

ax1.set_xlabel('R1 (s⁻¹)')
ax1.set_ylabel('R2 (s⁻¹)')
ax1.set_zlabel('P_acc')
ax1.set_title('3D weergave')

fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=10)

# ---- Heatmap ----
ax2 = fig.add_subplot(1, 2, 2)
cont = ax2.contourf(R1_grid, R2_grid, P_acc, levels=50, cmap='viridis')

ax2.set_xlabel('R1 (s⁻¹)')
ax2.set_ylabel('R2 (s⁻¹)')
ax2.set_title('Heatmap weergave')

fig.colorbar(cont, ax=ax2)

plt.tight_layout()
plt.savefig("belltest_chance_opdracht2.png", dpi=600, bbox_inches="tight")
plt.show()

####################################

import numpy as np
import matplotlib.pyplot as plt

n = 50
p_values = np.linspace(0.01, 0.4, 200)

S_values = [0.5, 0.9, 0.99]

def k_required(p, n, S):
    k = np.log(1 - S**(1/n)) / np.log(p)
    return np.ceil(k)

def n_extra(p, n, S):
    k = k_required(p, n, S)
    return n * (k - 1)

plt.figure()

for S in S_values:
    N_vals = n_extra(p_values, n, S)
    plt.plot(p_values, N_vals, label=f"S = {S}")

plt.xlabel("Detectorfaalkans p")
plt.ylabel("Aantal extra fotonen $N_{extra}$")
plt.title("Herhalingsmodel: $N_{extra}$ vs p voor verschillende betrouwbaarheden")
plt.legend()
plt.grid(True)

plt.savefig("Nextra_vs_p.png", dpi=600)
plt.show()

#############################

import numpy as np
import matplotlib.pyplot as plt
from math import comb

# Parameters
n = 50
p_values = np.linspace(0.01, 0.4, 60)

S_values = [0.5, 0.9, 0.99]

# Kans op correcte bitdetectie
def P_bit(k, p):
    start = (k + 1) // 2
    return sum(
        comb(k, i) * (1 - p)**i * p**(k - i)
        for i in range(start, k + 1)
    )

# Zoek kleinste oneven k
def k_required(p, n, S):
    k = 1
    while True:
        if (P_bit(k, p))**n >= S:
            return k
        k += 2

plt.figure()

for S in S_values:

    N_extra_vals = []

    for p in p_values:
        k = k_required(p, n, S)
        N_extra = n * (k - 1)
        N_extra_vals.append(N_extra)

    plt.plot(p_values, N_extra_vals, label=f"S = {S}")

plt.xlabel("Detectorfaalkans p")
plt.ylabel("Aantal extra fotonen $N_{extra}$")
plt.title("Meerderheidsmodel: $N_{extra}$ vs p voor verschillende betrouwbaarheden")
plt.legend()
plt.grid(True)

plt.savefig("majority_model_Nextra.png", dpi=600)
plt.show()

############## RQ2 ##################

import numpy as np
import matplotlib.pyplot as plt

t_values = np.arange(1, 30)

def P_detect(t):
    return 1 - (3/4)**t

# detectiekans per t
y_values = P_detect(t_values)

plt.figure()

plt.plot(t_values, y_values, label=r"$P(\mathrm{detectie}) = 1 - (3/4)^t$")

# horizontale lijnen (targets)
plt.axhline(y=0.9, color='orange', linestyle='--', label='90% detectie')
plt.axhline(y=0.99, color='green', linestyle='--', label='99% detectie')

# optioneel: markeer snijpunten visueel
t_90 = np.log(0.1) / np.log(3/4)
t_99 = np.log(0.01) / np.log(3/4)

plt.scatter([t_90, t_99], [0.9, 0.99], color=['orange', 'green'])

plt.xlabel("Aantal testbits $t$")
plt.ylabel("Detectiekans")
plt.title("Detectiekans van Charlie vs aantal testbits")
plt.grid(True)
plt.legend()

plt.savefig("detectiekans_RQ3.png", dpi=600)
plt.show()

###########################################################################

import numpy as np
import matplotlib.pyplot as plt

# ------------------------
# Parameters
# ------------------------
t = np.linspace(0, 50, 600)

S_values = [0.90, 0.99]
threshold_colors = {0.90: "gray", 0.99: "black"}

F = 0.30

# uncertainty on F
sigma_F = 0.02

# ------------------------
# Models
# ------------------------
P_exact_F0 = 1 - (3/4)**t
P_poisson_F0 = 1 - np.exp(-t/4)

P_exact_F = 1 - ((3 + F)/4)**t
P_poisson_F = 1 - np.exp(-(1 - F)*t/4)

# ------------------------
# Plot setup
# ------------------------
plt.figure(figsize=(10, 6))

# Curves
plt.plot(
    t, P_exact_F0,
    color="tab:blue",
    linewidth=2,
    label="Exact (F = 0)"
)

plt.plot(
    t, P_poisson_F0,
    color="tab:orange",
    linestyle="--",
    linewidth=2,
    label="Poisson (F = 0)"
)

plt.plot(
    t, P_exact_F,
    color="tab:green",
    linewidth=2,
    label=f"Exact (F = {F})"
)

plt.plot(
    t, P_poisson_F,
    color="tab:red",
    linestyle="--",
    linewidth=2,
    label=f"Poisson (F = {F})"
)

# ------------------------
# Threshold lines
# ------------------------
for S in S_values:

    plt.axhline(
        S,
        color=threshold_colors[S],
        linestyle=":",
        linewidth=2,
        label=f"S = {S}"
    )

# ------------------------
# Intersection formulas
# ------------------------
def t_exact(S, F=0):

    if F == 0:
        return np.log(1 - S) / np.log(3/4)

    return np.log(1 - S) / np.log((3 + F)/4)

def t_poisson(S, F=0):

    if F == 0:
        return -4 * np.log(1 - S)

    return -4 * np.log(1 - S) / (1 - F)

# ------------------------
# Error propagation
# dt/dF
# ------------------------
def dt_exact_dF(S, F):

    A = np.log(1 - S)
    B = np.log((3 + F)/4)

    dB_dF = 1 / (3 + F)

    return -A * dB_dF / (B**2)

def dt_poisson_dF(S, F):

    return -4 * np.log(1 - S) / ((1 - F)**2)

# ------------------------
# Intersection points + error bars
# ------------------------
for S in S_values:

    # --------------------
    # F = 0 points
    # --------------------
    t1 = t_exact(S, 0)
    t2 = t_poisson(S, 0)

    plt.scatter(t1, S, color="tab:blue", edgecolor="black", zorder=5)
    plt.scatter(t2, S, color="tab:orange", edgecolor="black", zorder=5)

    # --------------------
    # F = 0.30 points
    # --------------------
    t3 = t_exact(S, F)
    t4 = t_poisson(S, F)

    # propagated uncertainties
    sigma_t3 = abs(dt_exact_dF(S, F)) * sigma_F
    sigma_t4 = abs(dt_poisson_dF(S, F)) * sigma_F

    # points
    plt.scatter(t3, S, color="tab:green", edgecolor="black", zorder=5)
    plt.scatter(t4, S, color="tab:red", edgecolor="black", zorder=5)

    # horizontal error bars
    plt.errorbar(
        t3,
        S,
        xerr=sigma_t3,
        fmt='none',
        ecolor="black",
        elinewidth=1,
        capsize=3,
        alpha=0.8,
        zorder=4
    )

    plt.errorbar(
        t4,
        S,
        xerr=sigma_t4,
        fmt='none',
        ecolor="black",
        elinewidth=1,
        capsize=3,
        alpha=0.8,
        zorder=4
    )

# ------------------------
# Labels
# ------------------------
plt.xlabel("Aantal testbits $t$")
plt.ylabel("Detectiekans $P(\\mathrm{detectie})$")
plt.title("Detectiekans Charlie: exact vs Poisson (met en zonder detectorfoutkansen)")

plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig("RQ2_full_colored_plot_with_errors.png", dpi=600)

plt.show()
################################%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

import numpy as np
import matplotlib.pyplot as plt

# ------------------------
# Parameters
# ------------------------
S_values = [0.90, 0.99]
N = 1000  # vast aantal fotonen

# verschillende afluisterfracties (x)
x_values = [50, 100, 200, 400]

colors = ["tab:blue", "tab:orange", "tab:green", "tab:red"]

# onzekerheid op x
sigma_x = 5

# ------------------------
# t-as
# ------------------------
t = np.linspace(1, 500, 1000)

# ------------------------
# Model
# ------------------------
def P_detect(t, x, N):
    return 1 - (1 - x/(4*N))**t

# analytische oplossing
def t_required(S, x, N):
    return np.log(1 - S) / np.log(1 - x/(4*N))

# ------------------------
# foutpropagatie
# dt/dx
# ------------------------
def dt_dx(S, x, N):

    A = np.log(1 - S)
    B = np.log(1 - x/(4*N))

    dB_dx = -1 / (4*N*(1 - x/(4*N)))

    return -A * dB_dx / (B**2)

# ------------------------
# Plot
# ------------------------
plt.figure(figsize=(10, 6))

# curves
for x, c in zip(x_values, colors):

    P = P_detect(t, x, N)

    plt.plot(
        t,
        P,
        color=c,
        linewidth=2,
        label=f"x = {x}"
    )

# horizontale lijnen (S)
for S, c in zip(S_values, ["grey", "black"]):

    plt.axhline(
        S,
        linestyle="--",
        color=c,
        linewidth=1.5,
        label=f"S = {S}"
    )

# ------------------------
# analytische snijpunten + foutbalken
# ------------------------
for x, c in zip(x_values, colors):

    for S in S_values:

        # centrale waarde
        t_s = t_required(S, x, N)

        # foutpropagatie
        sigma_t = abs(dt_dx(S, x, N)) * sigma_x

        # punt
        plt.scatter(
            t_s,
            S,
            color=c,
            edgecolor="black",
            zorder=5
        )

        # horizontale foutbalk
        plt.errorbar(
            t_s,
            S,
            xerr=sigma_t,
            fmt='none',
            ecolor="black",
            elinewidth=1.5,
            capsize=4,
            zorder=4
        )

# ------------------------
# labels
# ------------------------
plt.xlabel("Aantal testbits $t$")
plt.ylabel("Detectiekans $P(\\mathrm{detectie})$")
plt.title("Partiële afluistering: detectiekans vs aantal testbits")

plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig("RQ5_different_x_values_plot_with_errors.png", dpi=600)

plt.show()
