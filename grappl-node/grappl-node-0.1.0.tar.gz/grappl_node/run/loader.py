from .creator import create


def load_node(configuration: dict):
    return create(configuration['node_module_name'],
                  configuration['node_name'], configuration['node_arguments'])

                  
def load_input(configuration: dict):
    return create(configuration['input_module_name'],
                  configuration['input_name'], configuration['input_arguments'])

                  
def load_output(configuration: dict):
    return create(configuration['output_module_name'],
                  configuration['output_name'], configuration['output_arguments'])
