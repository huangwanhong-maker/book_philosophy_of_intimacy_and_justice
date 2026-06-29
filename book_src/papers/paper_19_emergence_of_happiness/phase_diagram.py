import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.family']='serif'
rosedeep='#9E4256'; rose='#C76B7E'; gold='#B08A4C'; ink='#342E37'; blush='#FDF6F8'

def vdp(z,mu=1.0):
    x,y=z
    return np.array([y, mu*(1-x*x)*y - x])

def integrate(z0,t_end,dt=0.01):
    # fixed-step RK4 (numpy-only; avoids the scipy dependency)
    n=int(t_end/dt)
    t=np.empty(n+1); ys=np.empty((2,n+1))
    z=np.array(z0,dtype=float); t[0]=0.0; ys[:,0]=z
    for i in range(n):
        k1=vdp(z); k2=vdp(z+0.5*dt*k1); k3=vdp(z+0.5*dt*k2); k4=vdp(z+dt*k3)
        z=z+(dt/6.0)*(k1+2*k2+2*k3+k4)
        t[i+1]=(i+1)*dt; ys[:,i+1]=z
    return t,ys

fig,ax=plt.subplots(figsize=(7.2,5.4))
fig.patch.set_facecolor(blush); ax.set_facecolor(blush)

# vector field (faint)
X,Y=np.meshgrid(np.linspace(-3.2,3.2,22),np.linspace(-4.2,4.2,22))
U,V=Y, 1.0*(1-X*X)*Y - X
N=np.sqrt(U*U+V*V); N[N==0]=1
ax.quiver(X,Y,U/N,V/N,color=gold,alpha=0.30,width=0.0028,scale=42,headwidth=3)

# several trajectories from different initial conditions, all spiralling onto the same cycle
ics=[(0.12,0.0),(0.05,0.05),(3.0,3.8),(-3.0,-3.8),(2.6,-3.6),(-2.6,3.6)]
for (x0,y0) in ics:
    _,ys=integrate((x0,y0),40)
    ax.plot(ys[0],ys[1],color=rose,alpha=0.55,lw=0.9)

# the limit cycle itself (long integration, plot the tail)
t,ys=integrate((0.1,0.0),80)
m=t>60
ax.plot(ys[0][m],ys[1][m],color=rosedeep,lw=2.6,label='asymptotically stable limit cycle')

# the unstable fixed point at origin
ax.plot(0,0,'o',color=ink,ms=6,zorder=5)
ax.annotate('unstable fixed point',(0,0),(0.35,0.55),color=ink,fontsize=9,
            arrowprops=dict(arrowstyle='-',color=ink,alpha=0.6))

ax.set_xlim(-3.4,3.4); ax.set_ylim(-4.4,4.4)
ax.set_xlabel('$x$ (state)',color=ink,fontsize=11)
ax.set_ylabel(r'$\dot{x}$ (rate)',color=ink,fontsize=11)
ax.tick_params(colors=ink,labelsize=9)
for s in ax.spines.values(): s.set_color(gold); s.set_alpha(0.5)
ax.set_title('Trajectories from many initial conditions converge on one cycle',
             color=rosedeep,fontsize=11,pad=12)
ax.legend(loc='upper right',framealpha=0.0,fontsize=9,labelcolor=ink)
plt.tight_layout()
plt.savefig('figures/limit_cycle.png',dpi=150,facecolor=blush,bbox_inches='tight')
print("saved figures/limit_cycle.png")
