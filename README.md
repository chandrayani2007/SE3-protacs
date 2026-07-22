# 🧬 SE3-PROTACs: Structure-Equivariant Transformer for PROTAC Degradation Prediction

## 📖 Overview

**SE3-PROTACs** is a deep learning framework for predicting **PROTAC-mediated targeted protein degradation** using geometric deep learning. The model combines **3D molecular structural information** with **protein sequence embeddings** to accurately classify whether a PROTAC molecule can induce degradation of a target protein.

The framework utilizes an **SE(3)-Transformer** to preserve rotational and translational equivariance while learning molecular representations and integrates **ESM-2 protein embeddings** for enhanced biological understanding.

---

## ✨ Key Features

- 🧬 **SE(3)-Transformer** for learning 3D molecular graph representations
- 🔬 **ESM-2 Protein Embeddings** for encoding target proteins and E3 ligases
- 🔗 **Feature Fusion Network** combining molecular and protein features
- ⚡ Binary classification of PROTAC degradation activity
- 📊 End-to-end training and inference pipeline
- 🧪 Case study prediction support
- 📈 Model checkpointing and training logs

---

# 🏗️ Model Architecture

The prediction pipeline consists of four major stages:

1. **Data Preprocessing**
   - Convert SMILES to 3D molecular structures (.mol2)
   - Prepare protein FASTA sequences
   - Generate ESM embeddings

2. **Feature Extraction**
   - SE(3)-Transformer for molecular graph learning
   - ESM-2 encoder for protein representation

3. **Feature Fusion**
   - Combine molecular and protein embeddings
   - Learn interaction-aware representations

4. **Prediction**
   - Binary classification
   - Output:
     - **1 → Degrader**
     - **0 → Non-Degrader**

---

# 📂 Project Structure

```text
SE3-PROTACs/
│
├── data/                 # Training and inference datasets
├── model/                # Saved checkpoints
├── utils/                # Utility scripts
├── prepare_data.py       # Data preprocessing
├── pre_compute_emb.py    # Generate ESM embeddings
├── main.py               # Model training
├── casestudy.py          # Inference script
├── environment.yml       # Conda environment
├── requirements.txt      # Python dependencies
└── README.md
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/drugparadigm/SE3-protacs.git
cd SE3-protacs
```

## Create the Environment

```bash
conda env create -f environment.yml
conda activate se3protacs
```

Or install dependencies using pip:

```bash
pip install -r requirements.txt
```

---

# 📥 Dataset Preparation

Prepare the dataset before training.

### Input Files

### PROTAC Components

- Warhead (SMILES)
- Linker (SMILES)
- E3 Ligase Ligand (SMILES)

### Protein Sequences

- Protein of Interest (POI)
- E3 Ligase

Store all input files inside the **data/** directory.

### Convert SMILES to 3D Structures

```bash
python prepare_data.py
```

This generates `.mol2` molecular graph files.

### Generate Protein Embeddings

```bash
python pre_compute_emb.py
```

This computes **ESM-2 embeddings** for all protein sequences.

---

# 🚀 Training

Train the SE3-PROTACs model using:

```bash
python main.py
```

During training the framework automatically:

- Loads molecular graphs
- Loads ESM embeddings
- Trains the SE(3)-Transformer
- Saves checkpoints
- Stores training logs

Model weights are saved inside:

```text
model/
```

---

# 🔍 Inference

Predict degradation activity for a single PROTAC molecule.

```bash
python casestudy.py \
  --ligase_smi data/casestudy/e3_ligase_ligand.smi \
  --ligase_fa data/casestudy/e3_ligase.fa \
  --target_smi data/casestudy/warhead.smi \
  --target_fa data/casestudy/target.fa \
  --linker_smi data/casestudy/linker.smi
```

### Output

```text
Prediction : 1

Status : Degrader
```

or

```text
Prediction : 0

Status : Non-Degrader
```

---

# 🛠️ Technologies Used

| Category | Technologies |
|-----------|--------------|
| Programming | Python |
| Deep Learning | PyTorch |
| Geometric Learning | SE(3)-Transformer |
| Protein Representation | ESM-2 |
| Molecular Processing | RDKit, Mol2 |
| Data Processing | NumPy, Pandas |
| Model Training | CUDA, PyTorch |
| Visualization | Matplotlib |

---

# 📊 Applications

- 💊 AI-Assisted Drug Discovery
- 🧬 Targeted Protein Degradation
- 🧪 Pharmaceutical Research
- 🔬 Computational Biology
- 🧠 Geometric Deep Learning
- ⚕️ Precision Medicine

---

# 🚀 Future Enhancements

- Multi-class degradation prediction
- Web-based prediction interface
- Cloud deployment
- Explainable AI (XAI)
- Large-scale PROTAC database integration
- Support for additional protein encoders

---

# 📚 References

- **SE(3)-Transformer**
- **ESM-2 Protein Language Model**
- **PROTAC-DB**
- **PyTorch**

---

# 👨‍💻 Contributors

Konda Neha

Computer Science Engineering Student

GitHub: https://github.com/Neh-0613

---

# ⭐ Support

If you find this project useful, consider giving the repository a **⭐ Star** to support future development.
