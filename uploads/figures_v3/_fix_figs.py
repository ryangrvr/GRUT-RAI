import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt; import numpy as np
from matplotlib.patches import FancyBboxPatch
NAVY="#20305f"; SLATE="#3f4d6b"; ACCENT="#b3402f"; GOLD="#b8860b"; GRAY="#8a93a6"; LIGHT="#e7ebf2"; GREEN="#2e6e4f"
plt.rcParams.update({"font.family":"serif","font.size":11,"axes.titlesize":13,"axes.labelsize":11.5,
  "axes.edgecolor":SLATE,"axes.linewidth":0.8,"axes.titlecolor":NAVY,"axes.labelcolor":SLATE,
  "xtick.color":SLATE,"ytick.color":SLATE,"text.color":SLATE,"figure.dpi":200,"savefig.dpi":200,
  "savefig.bbox":"tight","savefig.pad_inches":0.15,"figure.facecolor":"white","axes.facecolor":"white"})
def finish(ax):
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.grid(True, which="both", color=LIGHT, lw=0.7, zorder=0)

# 1) PROFILE MISMATCH — fixed: continuous steepening, no spike
fig,ax=plt.subplots(figsize=(6.6,4.3))
r=np.logspace(0,2,400)                      # 1..100 kpc
halo=(r/8.0)**-2.0                           # 1/r^2, =1 at 8 kpc
rb=22.0                                      # interior->exterior break
A=(8.0)**-4.0                                # so interior matches ~halo near 8
rho=np.where(r<=rb,(r/8.0)**-4.0,((rb/8.0)**-4.0)*(r/rb)**-6.0)  # continuous: -4 then -6
ax.loglog(r,halo,color=NAVY,lw=2.4,label=r"dark-matter halo $\sim 1/r^2$ (flat rotation curve)",zorder=3)
ax.loglog(r,rho,color=ACCENT,lw=2.4,label=r"$W^2$ response: $1/r^4 \to 1/r^6$ (too steep)",zorder=3)
ax.axvline(rb,color=GRAY,ls=":",lw=1.0,zorder=1)
ax.text(rb*1.06,3e-4,"slope steepens\n"+r"$-4 \to -6$",color=GRAY,fontsize=9,style="italic")
ax.set_xlim(1,100); ax.set_ylim(1e-5,3)
ax.set_xlabel("radius  r  (kpc)"); ax.set_ylabel(r"effective density  $\rho$  (arb. units)")
ax.set_title(r"Why the $W^2$ dark sector fails: shape, not size")
finish(ax); ax.legend(loc="upper right",fontsize=9.5,framealpha=0.95)
ax.annotate("right magnitude,\nwrong shape —\na locality theorem",xy=(30,((rb/8.0)**-4.0)*(30/rb)**-6.0),
            xytext=(2.2,8e-4),fontsize=10,color=NAVY,weight="bold",
            arrowprops=dict(arrowstyle="->",color=SLATE,lw=1.2))
fig.savefig("fig_profile_mismatch.png"); plt.close(fig)

# 2) SUSCEPTIBILITY — fixed: clean non-overlapping annotations
fig,ax=plt.subplots(figsize=(6.6,4.3))
x=np.logspace(-2,2,500)
ax.loglog(x,1/(1+x**2),color=NAVY,lw=2.2,label=r"$\mathrm{Re}[\chi]=1/(1+(\omega\tau_0)^2)$")
ax.loglog(x,x/(1+x**2),color=ACCENT,lw=2.2,label=r"$\mathrm{Im}[\chi]=\omega\tau_0/(1+(\omega\tau_0)^2)$")
ax.loglog(x,1/np.sqrt(1+x**2),color=GREEN,lw=2.2,ls="--",label=r"$|\chi|=1/\sqrt{1+(\omega\tau_0)^2}$")
ax.axvline(1,color=GRAY,ls=":",lw=1.0); ax.text(1.12,2e-2,r"$\omega\tau_0=1$",color=GRAY,fontsize=9)
ax.axvspan(1e-2,1,color=LIGHT,alpha=0.5,zorder=0)
ax.set_xlim(1e-2,1e2); ax.set_ylim(1e-2,1.6)
ax.set_xlabel(r"$\omega\tau_0$"); ax.set_ylabel(r"$\chi(\omega)$")
ax.set_title("The single-pole vacuum susceptibility")
finish(ax); ax.legend(loc="lower left",fontsize=9,framealpha=0.95)
ax.text(3e-2,1.30,"memory regime\n(responds; deviates from GR)",color=SLATE,fontsize=8.5,style="italic")
ax.text(12,0.8,"high-frequency\nlimit ($\\chi\\to0$;\nGR recovered)",color=GREEN,fontsize=8.5,style="italic",ha="center")
fig.savefig("fig_susceptibility.png"); plt.close(fig)

# 3) BH SATURATION — fixed: conjectural tag not occluded
fig,ax=plt.subplots(figsize=(6.6,4.2))
t=np.linspace(0,10,300); R=1-np.exp(-0.6*t)
ax.plot(t,R,color=NAVY,lw=2.4,zorder=3); ax.fill_between(t,0,R,color=LIGHT,alpha=0.6,zorder=1)
ax.axhline(1.0,color=GOLD,ls="--",lw=1.6,zorder=2)
ax.set_xlim(0,10); ax.set_ylim(0,1.18); ax.set_xticks([]); ax.set_yticks([])
ax.set_xlabel("time / matter compression"); ax.set_ylabel("interior curvature")
ax.set_title("Finite-memory curvature saturation")
box=dict(boxstyle="round,pad=0.4",fc=LIGHT,ec=NAVY,lw=1.0)
ax.text(9.7,1.02,r"$R_{\max}=\dfrac{\alpha}{c^2\tau_0^2}\approx 2.1\times10^{-48}\,\mathrm{m^{-2}}$",
        ha="right",va="bottom",fontsize=10.5,bbox=box)
ax.text(0.3,0.10,r"$\rho_{\max}\approx 1.1\times10^{-22}\,\mathrm{kg/m^3}$  (mass-independent)",
        fontsize=10,color=SLATE,style="italic")
ax.text(0.0,1.245,"conjectural (v3 re-audit)",transform=ax.transAxes,ha="left",va="bottom",
        fontsize=9.5,color=ACCENT,style="italic")
fig.savefig("fig_bh_saturation.png"); plt.close(fig)

# 4) NEUTRINO HIERARCHY — fixed: clean ✗ for inverted, no stray box
fig,ax=plt.subplots(figsize=(6.6,4.2)); ax.axis("off")
ax.set_xlim(0,10); ax.set_ylim(0,10)
def lvl(x,y,c,lbl):
    ax.add_patch(FancyBboxPatch((x,y-0.18),2.6,0.36,boxstyle="round,pad=0.02",fc=c,ec=NAVY,lw=1.0))
    ax.text(x-0.25,y,lbl,ha="right",va="center",fontsize=11,color=NAVY)
ax.text(2.3,9.4,"Normal ordering\n(GRUT predicts)",ha="center",fontsize=12,color=NAVY,weight="bold")
lvl(1.0,8.3,GOLD,"m₃"); lvl(1.0,4.0,SLATE,"m₂"); lvl(1.0,3.3,SLATE,"m₁")
ax.text(7.4,9.4,"Inverted ordering\n(would falsify)",ha="center",fontsize=12,color=NAVY,weight="bold")
lvl(6.1,8.3,"#c98b86","m₂"); lvl(6.1,7.6,"#c98b86","m₁"); lvl(6.1,3.3,"#aab4c6","m₃")
ax.text(9.15,8.0,"✗",ha="center",va="center",fontsize=30,color=ACCENT,weight="bold")
ax.text(5.0,0.7,"the Z₃ flavor structure (anchored to Koide K=2/3) forces normal ordering",
        ha="center",fontsize=10.5,color=SLATE,style="italic")
ax.set_title("Neutrino mass ordering: a falsifiable prediction")
fig.savefig("fig_neutrino_hierarchy.png"); plt.close(fig)

# 5) DILATATION BREAKING — fixed: ACCENT red, annotation clear of legend
fig,ax=plt.subplots(figsize=(6.6,4.3))
k=np.logspace(-2,1,400)
ax.loglog(k,1/(1+k**2),color=NAVY,lw=2.3,label=r"$\chi_{\rm eq}=1/(1+(L_0 k)^2)$")
ax.loglog(k,1/(1+np.exp(-1.4)*k**2),color=ACCENT,lw=2.3,ls="--",
          label=r"$\chi_{\rm eq}^{\rm dilated}=1/(1+e^{-2\lambda}(L_0 k)^2),\ \lambda=0.7$")
ax.set_xlim(1e-2,1e1); ax.set_ylim(8e-3,1.4)
ax.set_xlabel(r"$L_0\,k_{\rm phys}$"); ax.set_ylabel(r"susceptibility  $\chi_{\rm eq}$")
ax.set_title("Finite memory breaks the rescaling redundancy")
finish(ax); ax.legend(loc="lower left",fontsize=9,framealpha=0.95)
ax.annotate("curves diverge:\nnon-invariant ⇒\nredundancy D broken",xy=(4,1/(1+np.exp(-1.4)*16)),
            xytext=(1.15,0.5),fontsize=9.5,color=ACCENT,
            arrowprops=dict(arrowstyle="->",color=ACCENT,lw=1.1))
fig.savefig("fig_dilatation_breaking.png"); plt.close(fig)
print("rebuilt 5 figures")
