from DashAI.back.core.schema_fields import BaseSchema, schema_field
from DashAI.back.models.base_model import BaseModel
from DashAI.back.config_object import ConfigObject


class ExampleModelSchema(BaseSchema):
    example_param_name: schema_field(  # Change example_param_name
        type_field(), # Choose between different types_fields e.g. int_field, string_field, etc
        placeholder=, # Placeholde to display in UI
        description=(
            "Field description"
        ),
    )  # type: ignore


class ExampleModelClass(BaseModel, ConfigObject):

    SCHEMA = ExampleModelSchema
    COMPATIBLE_COMPONENTS = ["TaskName"]

    def __init__(self, **kwargs): # Params are passed when the model is initialized
        super().__init__(**kwargs)
        self.model = None

    def fit(self, x_train, y_train) -> None:
        """ Fit the model to the data

        Parameters
        ----------
        x_train : Datasets
            Input data.
        y_train : Datasets
            Output data.

        """
        raise NotImplementedError
    
    def predict(self, x_pred) -> list:
        """Make a prediction with the model.

        Parameters
        ----------
        x_pred : Union[Dataset, pd.DataFrame]
            Dataset with the input data columns.

        Returns
        -------
        array-like
            Array with the predicted probabilities values for x_pred
        """
        raise NotImplementedError

    def save(self, filename: str) -> None:
        """Store an instance of a model.

        filename (Str): Indicates where to store the model,
        if filename is None, this method returns a bytes array with the model.
        """
        raise NotImplementedError
    
    @staticmethod
    def load(self, filename: str):
        """Restores an instance of a model.

        filename (Str): Indicates where the model was stored.
        """
        raise NotImplementedError
