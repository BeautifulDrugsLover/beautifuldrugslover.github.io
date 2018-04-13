from pathlib import Path

asm_pths = [pth for pth in Path.cwd().iterdir()
            if pth.suffix == '.png']