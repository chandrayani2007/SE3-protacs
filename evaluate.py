import torch
from torch.utils.data import DataLoader
from dataset import PROTACDataset, collater
from casestudy import load_model, DEVICE
from sklearn.metrics import accuracy_score, roc_auc_score

print("Loading dataset...")
test_dataset = PROTACDataset(data_dir='data/mol2_files/', clean_data='data/test.csv')
test_loader = DataLoader(test_dataset, batch_size=8, collate_fn=collater, shuffle=False)

print("Loading model...")
model = load_model()

model.eval()
all_preds = []
all_labels = []
all_probs = []

print("Evaluating...")
with torch.no_grad():
    for batch in test_loader:
        logits, _, _ = model(
            batch['ligase_ligand'].to(DEVICE),
            batch['ligase'].to(DEVICE),
            batch['target_ligand'].to(DEVICE),
            batch['target'].to(DEVICE),
            batch['linker'].to(DEVICE)
        )
        probs = torch.softmax(logits, dim=1)
        preds = torch.argmax(probs, dim=1)
        
        all_probs.extend(probs[:, 1].cpu().numpy())
        all_preds.extend(preds.cpu().numpy())
        all_labels.extend(batch['label'].cpu().numpy())

acc = accuracy_score(all_labels, all_preds)
try:
    auc = roc_auc_score(all_labels, all_probs)
except:
    auc = 0.0

print(f"Accuracy: {acc:.4f}")
print(f"AUC: {auc:.4f}")
unique, counts = torch.tensor(all_preds).unique(return_counts=True)
print(f"Predictions distribution: {dict(zip(unique.numpy(), counts.numpy()))}")
