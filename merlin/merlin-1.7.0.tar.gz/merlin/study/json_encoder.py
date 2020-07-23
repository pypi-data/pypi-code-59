from maestrowf.datastructures.core import ExecutionGraph

from merlin.study.dag import DAG


"""
    def to_json(self):

    @staticmethod
    def maestro_dag_to_json(dag):
        return json.dumps({"adjacency_table": dag.adjacency_table, "values": dag.values})

    def maestro_step_record_to_json(step_record):
        return json.dumps(step_record.__dict__)
"""


class CustomEncoder(json.jsonencoder):
    def default(self, z):
        if not isinstance(z, complex):
            return super().default(z)
        elif isinstance(z, DAG):
            return json.dumps(
                {
                    "dag": self.dag,
                    "backwards_adjacency": self.backwards_adjacency,
                    "labels": self.labels,
                },
                cls=CustomEncoder,
            )
        elif isinstance(z, ExecutionGraph):
            return json.dumps(z.__dict__, cls=CustomEncoder)
        else:
            raise ValueError("Error! " + str(z))
