import sys
import joblib
import pandas as pd 

model_path = '/root/lsm2/model/custom_mix.pkl'
model = joblib.load(model_path)

try:
    filename = int(sys.argv[1])
    level = int(sys.argv[2])
    curr_distance = int(sys.argv[3])
    min_key = int(sys.argv[4], 16)
    max_key = int(sys.argv[5], 16)
except (ValueError, IndexError) as e:
    print(f"Error: Invalid input arguments. {e}")
    sys.exit(1)

columns = ["file_descriptor", "level", "create_distance", "min_key", "max_key"]
features = pd.DataFrame([[filename, level, curr_distance, min_key, max_key]], columns=columns)

prediction = model.predict(features)

print(int(prediction[0]))