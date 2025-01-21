import numpy as np
from fluid import Fluid
from utils.utils import inviscid_solver, viscous_solver, convergence_checker 

if __name__ == "__main__":
    converged = False
    max_iterations = 100
    iteration = 0
    fluid = Fluid(L=1.0, H=0.1, Nx=100, Ny=100, nu=1e-5, U_inf=1.0)
    
    #intialize inviscidnya
    U_e = inviscid_solver(fluid)

    while not converged and iteration < max_iterations:
        old_state = fluid.u.copy()
        
        #BL dulu
        viscous_solver(fluid, U_e)
        
        #cek converge atau belum
        converged = convergence_checker(fluid, old_state)
        iteration += 1
        print(f"Iteration {iteration}, Converged: {converged}")
    
    #pltting, kerjain nanti aja
    import matplotlib.pyplot as plt
    plt.figure()
    for i in range(0, fluid.Nx, 10):
        plt.plot(fluid.u[i, :], fluid.y, label=f"x = {fluid.x[i]:.2f} m")
    plt.xlabel("u (m/s)")
    plt.ylabel("y (m)")
    plt.title("Velocity Profiles")
    plt.legend()
    plt.show()
