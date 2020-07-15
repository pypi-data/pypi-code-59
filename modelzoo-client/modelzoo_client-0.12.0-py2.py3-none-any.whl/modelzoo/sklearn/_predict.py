from typing import Optional

import numpy as np

from modelzoo import predict as base_predict


def predict(
    model_name: str, input_value: np.ndarray, api_key: Optional[str] = None
) -> np.ndarray:
    """
    Send a prediction to a scikit-learn model.

    Args:
        model_name: String name of the model.
        input_value:
            A ``numpy.ndarray`` to use for prediction. The input data should
            conform to the shape expected by the model.
        api_key: Will override the environment api key, if present.

    Returns:
        The output prediction value as a numpy array.
    """

    # Numpy arrays are not JSON serializable: convert to a native Python list
    # that can be serialized.
    if isinstance(input_value, np.ndarray):
        input_value = input_value.tolist()

    prediction = base_predict(
        model_name, input_value, headers={"Accept": "application/json"}
    )
    return np.array(prediction)
