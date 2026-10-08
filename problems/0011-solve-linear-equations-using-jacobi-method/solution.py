import torch

def solve_jacobi(A, b, n) -> torch.Tensor:
    """
    Solve Ax = b using the Jacobi iterative method for n iterations.
    A: (m,m) tensor; b: (m,) tensor; n: number of iterations.
    Returns a 1-D tensor of length m, rounded to 4 decimals.
    """
    A_t = torch.as_tensor(A, dtype=torch.float)
    b_t = torch.as_tensor(b, dtype=torch.float)
    # Your implementation here
    m=A_t.shape[0]
    x=torch.zeros(m,dtype=torch.float)
    for _ in range(n):
        x_new=torch.zeros(m,dtype=torch.float)
        for i in range(m):
            s=torch.sum(A_t[i,:]*x)-A_t[i,i]*x[i]
            x_new[i]=(b[i]-s)/A_t[i,i]
        x=x_new
    return torch.round(x,decimals=4)
