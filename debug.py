import traceback
try:
    from casestudy import load_model, DEVICE
    from utils import ESMEmbedder
    print("Loading model...")
    model = load_model()
    print("Loading ESM...")
    esm = ESMEmbedder(device=str(DEVICE))
    print("Success")
except Exception as e:
    traceback.print_exc()
