import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
NAVY="#20305f"; SLATE="#3f4d6b"; ACCENT="#b3402f"; GOLD="#9a7d28"; GRAY="#8a93a6"; LIGHT="#eef1f6"
GREEN="#2e6e4f"; REDF="#f3e3e1"; GRNF="#e3efe8"; AMBF="#f4eedd"; OPENF="#fbfbfd"
plt.rcParams.update({"font.family":"serif","figure.dpi":200,"savefig.dpi":200,
  "savefig.bbox":"tight","savefig.pad_inches":0.12,"figure.facecolor":"white"})
def newfig(w=6.9,h=4.4):
    fig,ax=plt.subplots(figsize=(w,h)); ax.axis("off"); ax.set_xlim(0,100); ax.set_ylim(0,100)
    ax.set_aspect("auto"); return fig,ax
def title(ax,t): ax.text(50,97,t,ha="center",va="top",fontsize=14.5,color=NAVY,weight="bold")
def cap(ax,t,y=3.5): ax.text(50,y,t,ha="center",va="bottom",fontsize=9.5,color=SLATE,style="italic")
def box(ax,x,y,w,h,text,edge=NAVY,fill=LIGHT,fs=9.5,tc=None,dashed=False,lw=1.4,bold=False):
    ax.add_patch(Rectangle((x,y),w,h,facecolor=fill,edgecolor=edge,lw=lw,
                 linestyle=(0,(5,3)) if dashed else "-",joinstyle="round",zorder=2))
    ax.text(x+w/2,y+h/2,text,ha="center",va="center",fontsize=fs,color=tc or NAVY,
            zorder=3,weight="bold" if bold else "normal")
def arr(ax,x1,y1,x2,y2,color=SLATE,lw=1.8):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle="-|>",mutation_scale=15,
                 color=color,lw=lw,shrinkA=3,shrinkB=3,zorder=1))

# 1) Q/F/D PILLARS
fig,ax=newfig(); title(ax,"The three pillars and their standing")
def pillar(x,letter,desc,tier,edge,fill):
    w,y,h=28,50,30
    ax.add_patch(Rectangle((x,y),w,h,facecolor=fill,edgecolor=edge,lw=1.6,joinstyle="round",zorder=2))
    cx=x+w/2
    ax.text(cx,y+h-5.5,letter,ha="center",va="center",fontsize=14,color=NAVY,weight="bold",zorder=3)
    ax.text(cx,y+h/2,desc,ha="center",va="center",fontsize=10.5,color=NAVY,zorder=3)
    ax.text(cx,y+5,tier,ha="center",va="center",fontsize=11,color=edge,weight="bold",zorder=3)
pillar(4, "Q","CTP unitarity","PROVEN",GREEN,GRNF)
pillar(36,"F","Finite memory τ₀","POSTULATED",GOLD,AMBF)
pillar(68,"D","Separate-universe\nredundancy","PARTIAL",GRAY,LIGHT)
ax.text(50,42,"F  breaks  D",ha="center",fontsize=12.5,color=ACCENT,weight="bold")
ax.text(50,34,"controlled breaking at order $(L_0 k)^2$ — observed through Q",
        ha="center",fontsize=10,color=SLATE)
cap(ax,"Q is proven; F is a postulate; D is partial — not yet a proven symmetry of the full theory.")
fig.savefig("fig_qfd_pillars.png"); plt.close(fig)

# 2) CTP CONTOUR
fig,ax=newfig(); title(ax,"The closed-time-path (in-in) contour")
arr(ax,18,66,82,66,color=NAVY,lw=2.2); ax.text(50,71,r"$\varphi_+$  (forward)",ha="center",fontsize=11,color=NAVY)
arr(ax,82,52,18,52,color=NAVY,lw=2.2); ax.text(50,46,r"$\varphi_-$  (return)",ha="center",fontsize=11,color=NAVY)
ax.add_patch(FancyArrowPatch((82,66),(82,52),connectionstyle="arc3,rad=-0.6",arrowstyle="-",color=NAVY,lw=2.2))
ax.text(90,59,"turning\npoint",ha="center",fontsize=9,color=SLATE)
box(ax,16,28,68,9,r"$S_{IF}[\varphi_+=\varphi_-]=0$   (vanishes on the diagonal)",fill=LIGHT,fs=10.5)
box(ax,16,15,68,9,r"physical response $= \delta S_{IF}/\delta h_q\,|_{q=0}$",fill=LIGHT,fs=10.5)
cap(ax,"the response is the difference between the forward and return branches.")
fig.savefig("fig_ctp_contour.png"); plt.close(fig)

# 3) NO-GO -> mu_linear=1  (vertical flow)
fig,ax=newfig(7.0,5.6); title(ax,"Why linear cosmology is forced to ΛCDM")
ys=[82,67.5,53,38.5,24]; txt=[
 "Long-wavelength adiabatic mode\n= separate-universe rescaling",
 "Vacuum cannot respond to it  (Q ∩ D)",
 "conformal enhancement ⊥\nseparate-universe invariance",
 "μ_linear = 1",
 "Linear cosmology = ΛCDM\n(derived requirement)"]
for i,(y,t) in enumerate(zip(ys,txt)):
    bold = i in (3,4)
    box(ax,14,y,50,11,t,fs=9.3,bold=bold,
        edge=GREEN if i==4 else NAVY, fill=GRNF if i==4 else LIGHT)
    if i>0: arr(ax,39,ys[i-1],39,y+11)
box(ax,70,49,27,16,"μ → 4/3\nenhancement\nRULED OUT\n(32σ CMB-ISW)",edge=ACCENT,fill=REDF,fs=8.5,tc=ACCENT)
ax.plot([71,96],[64,50],color=ACCENT,lw=2.0)   # strike
cap(ax,"the once-hoped linear modified-gravity signal is forbidden — and excluded by data.",y=6)
fig.savefig("fig_nogo_mulinear.png"); plt.close(fig)

# 4) TERMINAL VELOCITY
fig,ax=newfig(); title(ax,"The cosmological constant as a terminal velocity")
box(ax,6,64,38,16,"Gibbons–Hawking instability\n(drives expansion)",edge=GREEN,fill=GRNF,fs=9.8)
box(ax,6,22,38,16,"Memory-kernel friction\n(damps expansion)",edge=SLATE,fill=LIGHT,fs=9.8)
box(ax,58,42,38,16,r"$H_{\rm inf}=\dfrac{2-R}{S\,\tau_0}$"+"\n(terminal velocity)",edge=NAVY,fill=LIGHT,fs=11,bold=True)
arr(ax,44,70,58,54); arr(ax,44,32,58,46)
cap(ax,r"$\Omega_\Lambda=(H_{\rm inf}/H_0)^2$;  anchored value 0.6886 (Planck 2018: 0.6889).")
fig.savefig("fig_terminal_velocity.png"); plt.close(fig)

# 5) K2 FOUR STAGES
fig,ax=newfig(7.2,4.6); title(ax,r"The $K^{(2)}$ four-stage investigation")
sx=[3,27,51,75]; sw=22
labs=["Stage A\n\nW² is the unique\nO(2) operator",
      "Stage B\n\nscale forced to L₀\n(no 1/k² pole)",
      "Stage C\n\nmagnitude O(1–100)\nviable",
      "Stage D\n\nradial profile 1/r⁴\nWRONG"]
ec=[NAVY,NAVY,NAVY,ACCENT]
for i,(x,t) in enumerate(zip(sx,labs)):
    box(ax,x,58,sw,26,t,fs=8.8,edge=ec[i],fill=REDF if i==3 else LIGHT,tc=ACCENT if i==3 else NAVY)
    if i>0: arr(ax,sx[i-1]+sw,71,x,71)
arr(ax,86,58,60,34)
box(ax,20,18,60,14,"Verdict: dark matter is a hosted input\n(open_negative)",edge=ACCENT,fill=REDF,fs=11,tc=ACCENT,bold=True)
cap(ax,"each stage survives until the radial profile — the failure is shape, not size.")
fig.savefig("fig_k2_stages.png"); plt.close(fig)

# 6) LOCALITY THEOREM
fig,ax=newfig(); title(ax,"The locality theorem")
box(ax,7,52,38,24,"polynomial in k²\n\n(local; entire,\nno singularity)",edge=NAVY,fill=LIGHT,fs=10.5)
box(ax,55,52,38,24,r"$1/\nabla^2$  ($\equiv 1/k^2$ pole)"+"\n\nFORBIDDEN\nby locality",edge=ACCENT,fill=REDF,fs=10.5,tc=ACCENT)
ax.text(50,64,"vs",ha="center",fontsize=12,color=SLATE,style="italic")
box(ax,14,24,72,12,"shallowing  1/r⁴ → 1/r²  would need  1/∇²,\nwhich a local, causal kernel cannot contain",fill=LIGHT,fs=10)
cap(ax,"the same locality that fixes the scale L₀ forbids the operator a halo would require.")
fig.savefig("fig_locality_theorem.png"); plt.close(fig)

# 7) FALSIFIERS
fig,ax=newfig(7.2,4.4); title(ax,"How to kill GRUT: three independent tests")
fx=[3,35.5,68]; fw=29
fl=["1.  Decoherence\nplateau ≈ 689 Hz\n\n(table-top)",
    "2.  Normal neutrino\nhierarchy\n\n(JUNO / DUNE)",
    "3.  No linear μ ≠ 1\non cosmic scales\n\n(DESI / Euclid /\nCMB-S4)"]
for x,t in zip(fx,fl): box(ax,x,40,fw,38,t,fs=9.8)
cap(ax,"a real theory names where it can die — these span lab, particle, and cosmological scales.",y=22)
fig.savefig("fig_falsifiers.png"); plt.close(fig)

# 8) AXIOM + CONDITIONAL
fig,ax=newfig(7.0,4.6); title(ax,"The one axiom and its conditional theorem")
box(ax,3,58,30,22,"conformal mode\n= IR carrier?\n\nOPEN antecedent",edge=GRAY,fill=OPENF,fs=9.8,dashed=True,tc=SLATE)
box(ax,55,58,42,22,"a/c = 1/3\n\n(a = 1/360,  c = 1/120;\nKomargodski–Schwimmer 2011)",edge=NAVY,fill=LIGHT,fs=9.3)
arr(ax,33,69,55,69); ax.text(44,73.5,"IF … THEN",ha="center",fontsize=9.5,color=SLATE,style="italic")
arr(ax,76,58,52,38)
box(ax,28,24,48,14,"α = 1/3\nsingle dimensionless AXIOM (adopted)",edge=GREEN,fill=GRNF,fs=10.5,bold=True)
cap(ax,"the conditional theorem is proven; the antecedent is the open frontier (Riegert/Paneitz).")
fig.savefig("fig_axiom_conditional.png"); plt.close(fig)

# 9) STATUS LEDGER
fig,ax=newfig(7.2,4.6); title(ax,"GRUT v3 at a glance: what survived the audit")
cols=[("SURVIVES",GREEN,GRNF,3,["Q  (CTP structure)","Finite-memory framework","μ_linear = 1","derived a₀ scale","QM recovered","arrow of time"]),
      ("REFUTED",ACCENT,REDF,35.5,["linear Ω_dm = 1/3","linear enhancement","orbital-gate dark matter","C5a radial profile"]),
      ("OPEN",GOLD,AMBF,68,["α-selection (Riegert)","full redundancy proof","covariant K⁽²⁾"])]
for hdr,ec,fc,x,items in cols:
    box(ax,x,76,29,9,hdr,edge=ec,fill=fc,fs=11,tc=ec,bold=True)
    for j,it in enumerate(items):
        ax.text(x+1.5,69-j*7,"• "+it,ha="left",va="center",fontsize=9,color=SLATE)
cap(ax,"v3 is defined more by what it forbids than by what it predicts; 28 open negatives are ledgered.",y=6)
fig.savefig("fig_status_ledger.png"); plt.close(fig)

# 10) NEUTRINO — re-polish title/header spacing
from matplotlib.patches import Rectangle as Rect
fig,ax=plt.subplots(figsize=(6.9,4.6)); ax.axis("off"); ax.set_xlim(0,100); ax.set_ylim(0,100)
ax.text(50,99,"Neutrino mass ordering: a falsifiable prediction",ha="center",va="top",fontsize=14,color=NAVY,weight="bold")
def lvl(x,y,c,lbl):
    ax.add_patch(Rect((x,y-2),26,4,facecolor=c,edgecolor=NAVY,lw=1.0)); ax.text(x-2.5,y,lbl,ha="right",va="center",fontsize=11,color=NAVY)
ax.text(23,86,"Normal ordering\n(GRUT predicts)",ha="center",fontsize=11.5,color=NAVY,weight="bold")
lvl(10,72,GOLD,"m₃"); lvl(10,34,SLATE,"m₂"); lvl(10,27,SLATE,"m₁")
ax.text(70,86,"Inverted ordering\n(would falsify)",ha="center",fontsize=11.5,color=NAVY,weight="bold")
lvl(57,72,"#c98b86","m₂"); lvl(57,65,"#c98b86","m₁"); lvl(57,27,"#aab4c6","m₃")
ax.plot([88,95],[65,72],color=ACCENT,lw=4,solid_capstyle="round"); ax.plot([88,95],[72,65],color=ACCENT,lw=4,solid_capstyle="round")
ax.text(50,9,"the Z₃ flavor structure (anchored to Koide K = 2/3) forces normal ordering",ha="center",fontsize=10.5,color=SLATE,style="italic")
fig.savefig("fig_neutrino_hierarchy.png",dpi=200,bbox_inches="tight",pad_inches=0.12); plt.close(fig)
print("rebuilt 9 schematics + neutrino")
