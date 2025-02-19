#!/usr/bin/env python3

from pathlib import Path
import frida

frida.spawn("/home/fake/Downloads/Ankama Launcher-Setup-x86_64.appimage")

SCRIPT = (Path(__file__).parent / "script.js").read_text()

session = frida.attach("dofus")

script = session.create_script(SCRIPT)
script.load()
