import os


def _prepend_hydra_prefix(path):
    """Hydra creates a working directory depending on the time stamps.
       The format is:
            outputs/*-*-*/*-*-*/
       This makes it inconvenient to pass relative paths arguments as
       the relative paths will be evaluated from the working directory.

       This function prepends a prefix to the relative path to move out
       of the current working directory into the directory where the cli
       was initially executed. It then turns the relative path into an
       absolute path and returns it.
    """
    path = os.path.join('../../../', path)
    return os.path.abspath(path)


def fix_input_path(path):
    """Fix broken relative paths.

    """
    if not os.path.isabs(path):
        path = _prepend_hydra_prefix(path)
    return path


def filter_state_dict(state_dict):
    """Prevent unexpected key error when loading PyTorch-Lightning checkpoints
       by removing the unnecessary prefix model. from each key.

    """
    new_state_dict = {}
    for key, item in state_dict.items():
        new_key = '.'.join(key.split('.')[1:])
        new_state_dict[new_key] = item
    return new_state_dict


def _is_url(checkpoint):
    is_url = ('https://storage.googleapis.com' in checkpoint)
    return is_url


def _model_zoo(model):

    zoo = {
        'resnet-18': 'https://storage.googleapis.com/models_boris/resnet18-SSLI-ef4314d5.pth',
    }

    if model in zoo.keys():
        return zoo[model]
    else:
        return ''


