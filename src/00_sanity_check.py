from pathlib import Path
import sys

import numpy as np
import pandas as pd
import matplotlib
import astropy
import h5py

# Criar pasta de logs
log_dir = Path("results/logs")
log_dir.mkdir(parents=True, exist_ok=True)

# Operação simples
x = np.linspace(0, 10, 5)
y = x**2

# Criar arquivo de log
log = log_dir / "00_sanity_check.txt"

with open(log, "w") as f:
    f.write("Sanity check executado com sucesso!\n\n")
    f.write(f"Python: {sys.version}\n")
    f.write(f"NumPy: {np.__version__}\n")
    f.write(f"Pandas: {pd.__version__}\n")
    f.write(f"Matplotlib: {matplotlib.__version__}\n")
    f.write(f"Astropy: {astropy.__version__}\n")
    f.write(f"h5py: {h5py.__version__}\n")
    f.write(f"Resultado: {y.tolist()}\n")

print("✓ Sanity check OK!")
print(f"Log salvo em: {log}")
