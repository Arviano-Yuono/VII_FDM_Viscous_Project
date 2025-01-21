import numpy as np

class Fluid:
    """
    Represents the fluid properties, discretization grid, and velocity field.
    """
    def __init__(self, 
                 L: int, 
                 H: int, 
                 Nx: int, 
                 Ny:int, 
                 nu: float, 
                 U_inf: np.array) -> None:
        
        self.L = L  # plate length
        self.H = H  # domain height
        self.Nx = Nx  # N grid points in x
        self.Ny = Ny  # N grid points in y
        self.nu = nu  # kinematic viscosity
        self.U_inf = U_inf  # inviscid vel
        
        #Discretization
        self.dx = L / Nx
        self.dy = H / Ny  
        self.x = np.linspace(0, L, Nx)
        self.y = np.linspace(0, H, Ny)
        
        #Vel fields
        self.u = np.zeros((Nx, Ny))  # x velocity
        self.v = np.zeros((Nx, Ny))  # y velocity
        
        #BC
        self.u[:, -1] = U_inf  # U_inv at the edge of BL
        self.u[0, :] = 0       # No slip at wall
        self.v[0, :] = 0       # No pen at wall
    
    # def finite_difference(self, arr, axis, order=1):
    #     """
    #     Utility for computing finite differences.
    #     - arr: array to differentiate
    #     - axis: axis along which to differentiate
    #     - order: order of the derivative (1 or 2)
    #     """
    #     if order == 1:
    #         return np.gradient(arr, axis=axis) / (self.dx if axis == 0 else self.dy)
    #     elif order == 2:
    #         return np.gradient(np.gradient(arr, axis=axis), axis=axis) / \
    #                ((self.dx if axis == 0 else self.dy) ** 2)
    #     else:
    #         raise ValueError("Only 1st and 2nd order derivatives are supported.")