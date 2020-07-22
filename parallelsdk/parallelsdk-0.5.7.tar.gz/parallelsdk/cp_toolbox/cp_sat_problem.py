from parallelsdk.proto import optimizer_model_pb2
from parallelsdk.proto import constraint_model_pb2
from . import cp_problem
from .CPModels.variable import Variable
from .CPModels.constraint import Constraint
from ortools.sat.python import cp_model


class CPSatProblem(cp_problem.CPProblem):
    def __init__(self, name):
        super().__init__(name)

        # Create OR-Tools CP-Sat
        self.__model = cp_model.CpModel()

        # Map of variables in the model
        self.__var_map = {}
        self.__var_idx_map = {}

        # Objective bound and value for optimization problems
        self.__is_optimization = False
        self.__objective_name = 'objective'
        self.__objective_value = None
        self.__objective_bound = None

    # Constructor for an integer variable
    def IntVar(self, lb, ub, name=''):
        var = Variable(self.__model, lb, ub, name)
        self.__add_variable_mapping(var)
        return var

    # Constructor for an 'expression' constraint
    def Constraint(self, expr, name=''):
        return Constraint(self.__model, expr, name)

    def __add_variable_mapping(self, var):
        self.__var_map[var.Name()] = var
        self.__var_idx_map[len(self.__var_idx_map)] = var.Name()

    def __set_variable_value(self, var_idx, var_val):
        self.__var_map[self.__var_idx_map[var_idx]].set_value(var_val)

    def get_solution(self):
        solution = {}
        for var_id in sorted(self.__var_map.keys()):
            var = self.__var_map[var_id]
            solution[var.Name()] = var.get_value()
        if self.__is_optimization:
            solution[self.__objective_name] = self.__objective_value
            solution[self.__objective_name + '_bound'] = self.__objective_bound
        return solution

    def upload_problem_proto_solution(self, solution_proto):
        var_idx = 0
        for var_val in solution_proto.cp_sat_solution.cp_solver_solution.solution:
            self.__set_variable_value(var_idx, var_val)
            var_idx += 1
        if self.__is_optimization:
            self.__objective_value = solution_proto.cp_sat_solution.cp_solver_solution.objective_value
            self.__objective_bound = solution_proto.cp_sat_solution.cp_solver_solution.best_objective_bound

    def to_protobuf(self):
        # Create a CP-Sat model
        optimizer_model = optimizer_model_pb2.OptimizerModel()
        optimizer_model.cp_model.model_id = self.name()
        optimizer_model.cp_model.cp_sat_model.cp_model.CopyFrom(self.__model.Proto())
        return optimizer_model
