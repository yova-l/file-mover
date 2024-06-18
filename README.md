The GUI looks fine in 3160p, 1080p, 720p(acceptable)
Versions to come would improve how the GUI behaves for different display resolutions.

### Icon
<a href="https://www.freepik.es/icono/bola-magica_8490285#fromView=search&page=1&position=6&uuid=edbfdd7b-fe94-413a-9e44-c3645ec0ac4b">Icono de Freepik</a>

### Building a new executable
Once you are done changing the code you can rebuild the executable by running:

`pyinstaller main.py --noconsole --noconfirm --onefile --icon icon.png` (Linux)
`python -m PyInstaller main.py --noconsole --noconfirm --onefile --icon icon.png` (Windows)

Please make sure you have installed pyinstaller pillow in your current python enviroment

### Troubleshooting:
* If you have trouble building with pyinstaller, make sure you are using the right command and also check for the requirements.txt version (newest version gave me trouble)