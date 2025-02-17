import numpy as np
from src.fluid import Fluid
import scipy.integrate as spi
from numba import njit

@njit
def viscous_solver(fluid: Fluid, U_e: np.array) -> None:
    """
    Solve the viscous boundary layer problem using FDM.
    - fluid: instance of the Fluid class
    - U_e: edge velocity from inviscid solver
    Updates the velocity field in the Fluid class.
    """
    for i in range(1, fluid.Nx):
        for j in range(1, fluid.Ny - 1):
            u_x = (fluid.u[i, j] - fluid.u[i - 1, j]) / fluid.dx
            u_y = (fluid.u[i, j + 1] - fluid.u[i, j - 1]) / (2 * fluid.dy)
            u_yy = (fluid.u[i, j + 1] - 2 * fluid.u[i, j] + fluid.u[i, j - 1]) / (fluid.dy ** 2)
            fluid.v[i, j] = -spi.trapezoid(u_x, fluid.y[:j + 1])  # Continuity
            fluid.u[i + 1, j] = fluid.u[i, j] + fluid.dx * (-fluid.u[i, j] * u_x - fluid.v[i, j] * u_y + fluid.nu * u_yy) # conv. of Momentum

def inviscid_solver(fluid: Fluid) -> np.array:
    """
    Solve the inviscid flow problem.
    - fluid: instance of the Fluid class
    Returns updated edge velocity U_e(x).
    """
    U_e = np.ones_like(fluid.x) * fluid.U_inf 
    #tulis fungsi asli untuk solve inviscid di sini, returnya updated array U_e
    return U_e

def convergence_checker(fluid: Fluid, old_u: np.array, tolerance: float = 1e-5 ) -> bool:
    """
    Checks convergence by comparing the current and previous velocity fields.
    - fluid: instance of the Fluid class
    - old_u: previous velocity field for comparison
    - tolerance: convergence criterion
    Returns True if converged, False otherwise.
    """
    error = np.max(np.abs(fluid.u - old_u))
    return error < tolerance