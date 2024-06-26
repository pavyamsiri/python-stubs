from _typeshed import Incomplete

__all__ = ["tr_interior_point"]

class BarrierSubproblem:
    n_vars: Incomplete
    x0: Incomplete
    s0: Incomplete
    fun: Incomplete
    grad: Incomplete
    lagr_hess: Incomplete
    constr: Incomplete
    jac: Incomplete
    barrier_parameter: Incomplete
    tolerance: Incomplete
    n_eq: Incomplete
    n_ineq: Incomplete
    enforce_feasibility: Incomplete
    global_stop_criteria: Incomplete
    xtol: Incomplete
    fun0: Incomplete
    grad0: Incomplete
    constr0: Incomplete
    jac0: Incomplete
    terminate: bool
    def __init__(
        self,
        x0,
        s0,
        fun,
        grad,
        lagr_hess,
        n_vars,
        n_ineq,
        n_eq,
        constr,
        jac,
        barrier_parameter,
        tolerance,
        enforce_feasibility,
        global_stop_criteria,
        xtol,
        fun0,
        grad0,
        constr_ineq0,
        jac_ineq0,
        constr_eq0,
        jac_eq0,
    ) -> None: ...
    def update(self, barrier_parameter, tolerance) -> None: ...
    def get_slack(self, z): ...
    def get_variables(self, z): ...
    def function_and_constraints(self, z): ...
    def scaling(self, z): ...
    def gradient_and_jacobian(self, z): ...
    def lagrangian_hessian_x(self, z, v): ...
    def lagrangian_hessian_s(self, z, v): ...
    def lagrangian_hessian(self, z, v): ...
    def stop_criteria(
        self,
        state,
        z,
        last_iteration_failed,
        optimality,
        constr_violation,
        trust_radius,
        penalty,
        cg_info,
    ): ...

def tr_interior_point(
    fun,
    grad,
    lagr_hess,
    n_vars,
    n_ineq,
    n_eq,
    constr,
    jac,
    x0,
    fun0,
    grad0,
    constr_ineq0,
    jac_ineq0,
    constr_eq0,
    jac_eq0,
    stop_criteria,
    enforce_feasibility,
    xtol,
    state,
    initial_barrier_parameter,
    initial_tolerance,
    initial_penalty,
    initial_trust_radius,
    factorization_method,
): ...
