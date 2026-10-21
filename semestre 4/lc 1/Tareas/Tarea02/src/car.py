from pathlib import Path
import math

inp = Path(r"c:\Users\bruhs\Cosas U\lc 1\Tareas\Tarea02\Compl\datos_carrito.txt")
out = inp.with_name("datos_carrito_rad.txt")

with inp.open("r", encoding="utf-8") as f_in, out.open("w", encoding="utf-8") as f_out:
    for line in f_in:
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("//"):
            f_out.write(line)
            continue
        parts = s.split()
        try:
            deg = float(parts[0])
            rad = math.radians(deg)
            parts[0] = f"{rad:.6f}"
            f_out.write(" ".join(parts) + "\n")
        except Exception:
            # si la línea no es numérica, se copia tal cual
            f_out.write(line)
print(f"Guardado: {out}")