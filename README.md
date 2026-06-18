# 🎵 ¿Cómo cuantificar mi gusto por la música?

Proyecto del Parcial I de Programación. Analiza características musicales cuantificables de canciones favoritas usando la librería de Python **Librosa**, y genera un puntaje personalizado que intenta responder: ¿qué tiene una canción que hace que me guste?

## Sobre el proyecto

Todos tenemos una canción favorita, sin importar su ritmo, el artista que la escribió, o si es popular o no. Pero, ¿por qué nos gusta? ¿Qué tiene esa canción que la hace sentir diferente? Muchos piensan que es una pregunta sin respuesta, ya que la música es, al final del día, un gusto subjetivo. Este proyecto plantea que no del todo, y usa la librería **Librosa** para demostrarlo.

Toda composición musical, sea reggaetón, pop, country o balada, tiene un ritmo, una melodía, una estructura de coros y versos que la hacen sentir como una experiencia única. Es decir, tiene características cuantificables que se pueden medir, analizar e interpretar. Librosa convierte una canción en datos numéricos que Python puede estudiar: ritmo, volumen, tono, energía, frecuencias, y más.

El propósito de este programa es analizar qué aspectos de la composición musical (tempo, energía, armonía, brillantez, entre otros) hacen que una canción favorita lo sea, comparando varias canciones entre sí e infiriendo qué características comparten.

## 🎧 Sobre los archivos de audio

Este repositorio **no incluye los archivos MP3** de las canciones analizadas, por restricciones de derechos de autor. La carpeta `Canciones_favs/` está excluida mediante `.gitignore`.

El usuario debe crear su propia carpeta e incluirle las canciones (en .mp3) que desea analizar.

## ⚠️ Estructura de carpetas necesaria

Para que el código funcione, la carpeta `Canciones_favs` (creada por el usuario) debe estar **en la misma carpeta** donde están `analizar.py`:

```
CarpetaDelProyecto/
├── Canciones_favs/      ← tus archivos .mp3 van aquí
│   ├── cancion1.mp3
│   ├── cancion2.mp3
│   └── ...
├── analizar.py
├── .gitignore
└── README.md
```

El nombre debe ser exactamente `Canciones_favs` (esa mayúscula y ese guion bajo). Si el script no la encuentra, la terminal mostrará exactamente qué rutas intentó, para ayudarte a corregirlo.

## 📌 Características analizadas

- **Tempo**: qué tan rápida es la canción (BPM)
- **Energía**: qué tan intensa/fuerte se siente (RMS)
- **Brillantez**: qué tan aguda o clara suena (centroide espectral)
- **Ancho de banda**: qué tan variado es el rango de sonidos
- **Zero crossing rate (ZCR)**: qué tan ruidosa o percusiva es la señal
- **Contraste espectral**: qué tan definido/nítido suena
- **Nota dominante**: la nota musical que predomina
- **Duración**

Cada característica se convierte en un puntaje subjetivo según rangos configurables en el código, y se combinan en un **puntaje final ponderado** por canción.

## 🛠️ Tecnologías utilizadas

- Python
- Librosa
- Pandas
- NumPy
- Streamlit (para la app web interactiva)

## 📦 Instalación

```bash
pip install librosa pandas numpy streamlit mathplotlib
```

## 🌐 Cómo correr la app web interactiva

Este modo abre una página interactiva con tablas, colores, gráficas y sliders. Usa el archivo `analizar.py`.

> ⚠️ **Antes de correrla, confirma tu ubicación.** Si la terminal no está parada exactamente en la carpeta que contiene `analizar.py`, el comando fallará con un error como `File does not exist`.

1. Verifica dónde estás parado:
   ```bash
   pwd       # Mac/Linux
   cd        # Windows
   ```
   Si no es la carpeta correcta, navega con `cd "ruta\a\tu\carpeta"`.

2. Ejecuta:
   ```bash
   python -m streamlit run analizar.py      # Windows
   python3 -m streamlit run analizar.py     # Mac
   ```
   (Si el comando `streamlit` se reconoce directamente en tu sistema, también puedes usar `streamlit run app.py` sin el `python -m` al inicio.)

3. Se abrirá automáticamente en tu navegador en `http://localhost:8501`. Si no se abre solo, copia esa URL y pégala manualmente.

## 🩹 Solución de problemas comunes

| Error | Causa probable | Solución |
|---|---|---|
| `File does not exist: app.py` | La terminal no está en la carpeta donde vive `app.py` | Verifica con `pwd`/`cd` y navega a la carpeta correcta |
| `ModuleNotFoundError: No module named 'streamlit'` (o `librosa`, `pandas`) | Falta instalar la librería | `pip install librosa pandas numpy streamlit` |
| `ERROR: no se encontró la carpeta 'Canciones_favs'...` | La carpeta no existe, está mal ubicada, o tiene otro nombre | Revisa la sección de estructura de carpetas arriba |
| La página de Streamlit aparece vacía o con errores raros | Se ejecutó `streamlit run analizar.py` por error | Usa `analizar.py`, para la versión web |
