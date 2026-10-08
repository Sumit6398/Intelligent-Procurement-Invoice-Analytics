import joblib
import pandas as pd

MODEL_PATH = "models/predict_freight_model.pkl"

def load_model(model_path: str = MODEL_PATH):
    """
    Load trained freight cost prediction model.
    """
    with open(model_path,"rb") as f:
        model = joblib.load(f)
        return model

def predict_freight_cost(intput_data):
    """
    Predict freight cost for new vendor invoices.
    Parameters
    ---------- 
    input_data : dict
    Returens
    ----------
    pd.DataFrame with predicted freight cost
    """
    model = load_model()
    input_df = pd.DataFrame(input_data)
    input_df['Predicted_Freight'] = model.predict(intput_df).round()
    return input_df

    if__name__ == "__main__":

        sample_data = {
            "Dollars": [18500,9000,3000,200]
    }
    prediction = predict_freight_cost(sample_data)
    print(prediction)
    