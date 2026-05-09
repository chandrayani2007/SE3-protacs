
import pandas as pd
import torch
from casestudy import load_model, predict_single, DEVICE
from utils import ESMEmbedder

def main():
    print("Loading test data...")
    df = pd.read_csv('data/test.csv')
    sample = df.iloc[1]
    
    print(f"Sample Compound ID: {sample['compound id']}")
    
    print("Loading model and embedder...")
    model = load_model()
    esm = ESMEmbedder(device=str(DEVICE))
    
    print("Running prediction...")
    pred, score = predict_single(
        model,
        sample['e3_ligase_smiles'],
        sample['e3_ligase_sequence'],
        sample['warhead_smiles'],
        sample['target_sequence'],
        sample['linker_smiles'],
        esm
    )
    
    print("\n================ PREDICTION RESULT ================")
    print(f"Compound ID       : {sample['compound id']}")
    print(f"Degradation Score : {score:.4f}")
    print(f"Prediction        : {'Good Degrader' if pred == 1 else 'Bad Degrader'} ({pred})")
    print("====================================================")

if __name__ == "__main__":
    main()
