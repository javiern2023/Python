
import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication
from frontend.dashboard import Dashboard


def main():
    app = QApplication(sys.argv)

    # Cargar estilos de la aplicación
    ruta_estilos = Path(__file__).parent / "estilos" / "styles.qss"

    if ruta_estilos.exists():
        with open(ruta_estilos, "r", encoding="utf-8") as archivo:
            app.setStyleSheet(archivo.read())

    ventana = Dashboard()
    ventana.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
