import mpmath as mp
mp.mp.dps=30; I=mp.mpc(0,1)
def Cl(l): return mp.mpf(2)**l*mp.gamma(mp.mpf(l)+mp.mpf(3)/2)/mp.sqrt(mp.pi)
def Wron(l,w):    # W[psi_reg,psi_out] = -2 C_l / prod_{k=1}^{l}(k - i w)
    p=mp.mpf(1)
    for k in range(1,l+1): p*= (k-I*w)
    return -2*Cl(l)/p
print("### Wronskian W[psi_reg,psi_out] = -2 C_l / prod_{k=1}^{l}(k-i w)")
print("    zeros of W = poles of G_R = quasinormal modes")
for l in [2,3,4]:
    print(f"\n l={l}  (C_l={mp.nstr(Cl(l),8)}):")
    for w in [mp.mpc(0,0), mp.mpc(0,-1), mp.mpc(0,-2), mp.mpc(0,-3), mp.mpc(0,-7),
              mp.mpc(2,-3), mp.mpc(-4,-9), mp.mpc(0,5), mp.mpc(30,-30)]:
        try: Wv=Wron(l,w); s=f"{mp.nstr(Wv,8):>30}  |W|={mp.nstr(abs(Wv),6)}"
        except ZeroDivisionError: s="POLE of W (not a zero)"
        print(f"   w/H={str(w):>14}: W = {s}")
print("\n  min |W| over a grid in the lower half plane (searching for a zero):")
for l in [2,3]:
    best=None
    for i in range(-60,61):
        for j in range(-60,1):
            w=mp.mpc(i*0.25, j*0.25)
            try: v=abs(Wron(l,w))
            except ZeroDivisionError: continue
            if best is None or v<best[0]: best=(v,w)
    print(f"   l={l}: min|W| = {mp.nstr(best[0],8)} at w/H={mp.nstr(best[1],6)}   (|W| -> 0 only as |w|->inf)")
print("\n### => G_R(omega,l) is analytic in the WHOLE finite complex omega plane:")
print("       no quasinormal poles, no bound-state poles, no branch cut in omega.")
