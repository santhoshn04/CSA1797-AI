class MapColoringCSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, assignment, var, value):
        for constraint in self.constraints.get(var, []):
            if constraint[0] in assignment and assignment[constraint[0]] == value:
                return False
        return True

    def backtracking_search(self, assignment={}):
        if len(assignment) == len(self.variables):
            return assignment

        unassigned_vars = [var for var in self.variables if var not in assignment]

        first_unassigned_var = unassigned_vars[0]
        for value in self.domains[first_unassigned_var]:
            if self.is_consistent(assignment, first_unassigned_var, value):
                new_assignment = assignment.copy()
                new_assignment[first_unassigned_var] = value

                result = self.backtracking_search(new_assignment)
                if result is not None:
                    return result

        return None

def main():
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    domains = {
        'WA': ['red', 'green', 'blue'],
        'NT': ['red', 'green', 'blue'],
        'SA': ['red', 'green', 'blue'],
        'Q': ['red', 'green', 'blue'],
        'NSW': ['red', 'green', 'blue'],
        'V': ['red', 'green', 'blue'],
        'T': ['red', 'green', 'blue'],
    }
    constraints = {
        'WA': [('NT',)],
        'NT': [('WA', 'SA')],
        'SA': [('WA', 'NT', 'Q', 'NSW', 'V')],
        'Q': [('SA', 'NSW')],
        'NSW': [('SA', 'Q', 'V')],
        'V': [('SA', 'NSW')],
    }

    csp = MapColoringCSP(variables, domains, constraints)
    solution = csp.backtracking_search()

    if solution:
        print("Map Coloring Solution:")
        for var, color in solution.items():
            print(f"{var}: {color}")
    else:
        print("No solution found!")

if __name__ == "__main__":
    main()
