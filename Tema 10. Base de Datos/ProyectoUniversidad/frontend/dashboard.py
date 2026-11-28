
import requests

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QLabel, QPushButton, QLineEdit, QTableWidget,
    QTableWidgetItem, QMessageBox, QFrame, QHeaderView,
    QAbstractItemView
)

API_URL = "http://127.0.0.1:5000/api"


class Dashboard(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestión de Ciclos Formativos")
        self.setMinimumSize(1050, 650)
        self.codigo_seleccionado = None

        self.crear_interfaz()
        self.cargar_ciclos()

    def crear_interfaz(self):
        contenedor = QWidget()
        self.setCentralWidget(contenedor)

        layout_principal = QHBoxLayout(contenedor)
        layout_principal.setContentsMargins(0, 0, 0, 0)
        layout_principal.setSpacing(0)

        # MENÚ LATERAL
        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(230)

        layout_sidebar = QVBoxLayout(sidebar)
        layout_sidebar.setContentsMargins(20, 30, 20, 20)

        logo = QLabel("UAX")
        logo.setObjectName("logo")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        titulo_menu = QLabel("GESTIÓN ACADÉMICA")
        titulo_menu.setObjectName("tituloMenu")
        titulo_menu.setAlignment(Qt.AlignmentFlag.AlignCenter)

        texto_menu = QLabel("Administración de\nciclos formativos")
        texto_menu.setObjectName("textoMenu")
        texto_menu.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout_sidebar.addWidget(logo)
        layout_sidebar.addSpacing(15)
        layout_sidebar.addWidget(titulo_menu)
        layout_sidebar.addWidget(texto_menu)
        layout_sidebar.addSpacing(40)

        boton_inicio = QPushButton("  Inicio")
        boton_inicio.setObjectName("botonMenu")
        boton_inicio.setEnabled(False)

        boton_ciclos = QPushButton("  Ciclos formativos")
        boton_ciclos.setObjectName("botonMenu")
        boton_ciclos.clicked.connect(self.cargar_ciclos)

        layout_sidebar.addWidget(boton_inicio)
        layout_sidebar.addWidget(boton_ciclos)
        layout_sidebar.addStretch()

        pie = QLabel("Proyecto académico")
        pie.setObjectName("pieMenu")
        pie.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_sidebar.addWidget(pie)

        # CONTENIDO PRINCIPAL
        contenido = QWidget()
        layout_contenido = QVBoxLayout(contenido)
        layout_contenido.setContentsMargins(35, 30, 35, 30)
        layout_contenido.setSpacing(18)

        titulo = QLabel("Panel de administración")
        titulo.setObjectName("tituloPrincipal")

        subtitulo = QLabel(
            "Gestiona los ciclos formativos registrados en el sistema."
        )
        subtitulo.setObjectName("subtitulo")

        # TARJETA DE ESTADÍSTICAS
        tarjeta = QFrame()
        tarjeta.setObjectName("tarjeta")

        layout_tarjeta = QVBoxLayout(tarjeta)

        etiqueta_total = QLabel("TOTAL DE CICLOS FORMATIVOS")
        etiqueta_total.setObjectName("etiquetaTarjeta")

        self.lbl_total = QLabel("0")
        self.lbl_total.setObjectName("numeroTarjeta")

        layout_tarjeta.addWidget(etiqueta_total)
        layout_tarjeta.addWidget(self.lbl_total)

        # FORMULARIO
        titulo_formulario = QLabel("Datos del ciclo formativo")
        titulo_formulario.setObjectName("tituloSeccion")

        formulario = QFrame()
        formulario.setObjectName("tarjeta")

        layout_formulario = QHBoxLayout(formulario)
        layout_formulario.setSpacing(12)

        columna_codigo = QVBoxLayout()
        columna_nombre = QVBoxLayout()
        columna_duracion = QVBoxLayout()

        columna_codigo.addWidget(QLabel("Código"))
        self.txt_codigo = QLineEdit()
        self.txt_codigo.setPlaceholderText("Ej. DAM")
        columna_codigo.addWidget(self.txt_codigo)

        columna_nombre.addWidget(QLabel("Nombre"))
        self.txt_nombre = QLineEdit()
        self.txt_nombre.setPlaceholderText("Nombre del ciclo")
        columna_nombre.addWidget(self.txt_nombre)

        columna_duracion.addWidget(QLabel("Duración"))
        self.txt_duracion = QLineEdit()
        self.txt_duracion.setPlaceholderText("Ej. 2000")
        columna_duracion.addWidget(self.txt_duracion)

        layout_formulario.addLayout(columna_codigo, 1)
        layout_formulario.addLayout(columna_nombre, 2)
        layout_formulario.addLayout(columna_duracion, 1)

        # BOTONES
        layout_botones = QHBoxLayout()

        self.btn_guardar = QPushButton("Guardar")
        self.btn_guardar.setObjectName("botonGuardar")
        self.btn_guardar.clicked.connect(self.guardar_ciclo)

        self.btn_modificar = QPushButton("Modificar")
        self.btn_modificar.setObjectName("botonModificar")
        self.btn_modificar.clicked.connect(self.modificar_ciclo)

        self.btn_eliminar = QPushButton("Eliminar")
        self.btn_eliminar.setObjectName("botonEliminar")
        self.btn_eliminar.clicked.connect(self.eliminar_ciclo)

        self.btn_limpiar = QPushButton("Limpiar")
        self.btn_limpiar.setObjectName("botonLimpiar")
        self.btn_limpiar.clicked.connect(self.limpiar_formulario)

        layout_botones.addWidget(self.btn_guardar)
        layout_botones.addWidget(self.btn_modificar)
        layout_botones.addWidget(self.btn_eliminar)
        layout_botones.addWidget(self.btn_limpiar)

        # TABLA
        titulo_tabla = QLabel("Ciclos formativos registrados")
        titulo_tabla.setObjectName("tituloSeccion")

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(3)
        self.tabla.setHorizontalHeaderLabels(
            ["Código", "Nombre", "Duración (horas)"]
        )

        self.tabla.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.tabla.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        self.tabla.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        self.tabla.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        self.tabla.itemSelectionChanged.connect(
            self.seleccionar_ciclo
        )

        self.btn_actualizar = QPushButton("Actualizar listado")
        self.btn_actualizar.setObjectName("botonActualizar")
        self.btn_actualizar.clicked.connect(self.cargar_ciclos)

        # AÑADIR ELEMENTOS AL CONTENIDO
        layout_contenido.addWidget(titulo)
        layout_contenido.addWidget(subtitulo)
        layout_contenido.addWidget(tarjeta)
        layout_contenido.addWidget(titulo_formulario)
        layout_contenido.addWidget(formulario)
        layout_contenido.addLayout(layout_botones)
        layout_contenido.addWidget(titulo_tabla)
        layout_contenido.addWidget(self.tabla, 1)
        layout_contenido.addWidget(self.btn_actualizar)

        layout_principal.addWidget(sidebar)
        layout_principal.addWidget(contenido, 1)

    def cargar_ciclos(self):
        try:
            respuesta = requests.get(
                f"{API_URL}/ciclos",
                timeout=5
            )
            respuesta.raise_for_status()

            ciclos = respuesta.json()

            self.tabla.setRowCount(0)

            for ciclo in ciclos:
                fila = self.tabla.rowCount()
                self.tabla.insertRow(fila)

                self.tabla.setItem(
                    fila, 0,
                    QTableWidgetItem(str(ciclo["codigo"]))
                )

                self.tabla.setItem(
                    fila, 1,
                    QTableWidgetItem(str(ciclo["nombre"]))
                )

                self.tabla.setItem(
                    fila, 2,
                    QTableWidgetItem(str(ciclo["duracion"]))
                )

            self.lbl_total.setText(str(len(ciclos)))

        except requests.RequestException as error:
            QMessageBox.critical(
                self,
                "Error de conexión",
                f"No se ha podido conectar con el servidor Flask.\n\n{error}"
            )

        except (ValueError, KeyError) as error:
            QMessageBox.critical(
                self,
                "Error de datos",
                f"No se han podido interpretar los datos recibidos.\n\n{error}"
            )

    def guardar_ciclo(self):
        codigo = self.txt_codigo.text().strip()
        nombre = self.txt_nombre.text().strip()
        duracion = self.txt_duracion.text().strip()

        if not codigo or not nombre or not duracion:
            QMessageBox.warning(
                self,
                "Campos obligatorios",
                "Debes completar todos los campos."
            )
            return

        try:
            duracion_numero = int(duracion)

            if duracion_numero <= 0:
                raise ValueError

        except ValueError:
            QMessageBox.warning(
                self,
                "Duración incorrecta",
                "La duración debe ser un número entero positivo."
            )
            return

        try:
            respuesta = requests.post(
                f"{API_URL}/ciclos",
                json={
                    "codigo": codigo,
                    "nombre": nombre,
                    "duracion": duracion_numero
                },
                timeout=5
            )

            if respuesta.status_code in (200, 201):
                QMessageBox.information(
                    self,
                    "Operación correcta",
                    "El ciclo formativo se ha guardado correctamente."
                )
                self.limpiar_formulario()
                self.cargar_ciclos()
            else:
                self.mostrar_error(respuesta)

        except requests.RequestException as error:
            QMessageBox.critical(
                self,
                "Error",
                f"No se ha podido guardar el ciclo.\n\n{error}"
            )

    def seleccionar_ciclo(self):
        fila = self.tabla.currentRow()

        if fila < 0:
            return

        self.codigo_seleccionado = self.tabla.item(fila, 0).text()

        self.txt_codigo.setText(self.codigo_seleccionado)
        self.txt_nombre.setText(self.tabla.item(fila, 1).text())
        self.txt_duracion.setText(self.tabla.item(fila, 2).text())

        self.txt_codigo.setReadOnly(True)

    def modificar_ciclo(self):
        if not self.codigo_seleccionado:
            QMessageBox.warning(
                self,
                "Selecciona un ciclo",
                "Selecciona primero un ciclo de la tabla."
            )
            return

        nombre = self.txt_nombre.text().strip()
        duracion = self.txt_duracion.text().strip()

        if not nombre or not duracion:
            QMessageBox.warning(
                self,
                "Campos obligatorios",
                "Debes completar el nombre y la duración."
            )
            return

        try:
            duracion_numero = int(duracion)

            if duracion_numero <= 0:
                raise ValueError

        except ValueError:
            QMessageBox.warning(
                self,
                "Duración incorrecta",
                "La duración debe ser un número entero positivo."
            )
            return

        try:
            respuesta = requests.put(
                f"{API_URL}/ciclos/{self.codigo_seleccionado}",
                json={
                    "nombre": nombre,
                    "duracion": duracion_numero
                },
                timeout=5
            )

            if respuesta.ok:
                QMessageBox.information(
                    self,
                    "Operación correcta",
                    "El ciclo se ha modificado correctamente."
                )
                self.limpiar_formulario()
                self.cargar_ciclos()
            else:
                self.mostrar_error(respuesta)

        except requests.RequestException as error:
            QMessageBox.critical(
                self,
                "Error",
                f"No se ha podido modificar el ciclo.\n\n{error}"
            )

    def eliminar_ciclo(self):
        if not self.codigo_seleccionado:
            QMessageBox.warning(
                self,
                "Selecciona un ciclo",
                "Selecciona primero un ciclo de la tabla."
            )
            return

        confirmacion = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Seguro que quieres eliminar el ciclo "
            f"{self.codigo_seleccionado}?",
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )

        if confirmacion != QMessageBox.StandardButton.Yes:
            return

        try:
            respuesta = requests.delete(
                f"{API_URL}/ciclos/{self.codigo_seleccionado}",
                timeout=5
            )

            if respuesta.ok:
                QMessageBox.information(
                    self,
                    "Operación correcta",
                    "El ciclo se ha eliminado correctamente."
                )
                self.limpiar_formulario()
                self.cargar_ciclos()
            else:
                self.mostrar_error(respuesta)

        except requests.RequestException as error:
            QMessageBox.critical(
                self,
                "Error",
                f"No se ha podido eliminar el ciclo.\n\n{error}"
            )

    def limpiar_formulario(self):
        self.txt_codigo.clear()
        self.txt_nombre.clear()
        self.txt_duracion.clear()

        self.txt_codigo.setReadOnly(False)
        self.codigo_seleccionado = None

        self.tabla.clearSelection()

    def mostrar_error(self, respuesta):
        try:
            mensaje = respuesta.json().get(
                "error",
                respuesta.text
            )
        except ValueError:
            mensaje = respuesta.text

        QMessageBox.warning(
            self,
            "No se ha podido completar la operación",
            mensaje
        )
