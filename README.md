# Parcial-I-Programacion

*PROPÓSITO DEL PROYECTO* 

Aqui se encuentra mi proyecto llamado: ¿Cómo cuantifficar mi gusto por la música? Realizado utilizando la librería de python librosa. 
Yo sé que todos tenemos una canción favorita; independientemente de su ritmo, el artista que la escribió, si es popular o no, si te hace llorar, saltar, cantar, lo que sea. Sin embargo, alguna vez se preguntaron: ¿Por qué? ¿Qué tiene esta canción que me hace sentir diferente? ¿Cuál es la magia de la música? Muchos piensan que esta es una pregunta sin respuesta, ya que la música es, al final del día, un gusto simple y subjetivo, ¿no? Bueno, yo opino que no del todo y la librería “Librosa” me ayudará a demostrarlo. 

Una composición musical, ya sea una canción de reggaetón, pop, country, balada, etcétera, tiene características muy puntuales que la definen. Tienen un ritmo, una melodía, una letra, un conjunto de coros y versos que hacen que cada canción se sienta como una experiencia totalmente única. Es decir, toda una composición musical tiene características cuantificables que podemos medir, analizar e interpretar. Es aquí donde entra la librería “Librosa”.

Librosa es una librería de Python utilizada para analizar audio, especialmente música. Sirve para convertir una canción, una grabación, o un sonido en datos numéricos que Python puede estudiar. Esta librería puede detectar ritmo, volumen, tono, duración, energía, frecuencias, espectrogramas, entre muchas otras. 

Mi propósito con este programa es analizar, ¿Qué aspectos hacen que tu canción favorita, sea tu canción favorita? Con esta librería puedo analizar los datos cuantificables de mis canciones favoritas, su ritmo, su BPM, armonía, energía y estructura; puedo compararlas e inferir que tipo de canciones y que características en su composición musical son las que hacen que una canción me guste o no. 

## 🎵 Sobre los archivos de audio

Este repositorio **no incluye los archivos MP3** de las canciones analizadas, debido a restricciones de derechos de autor. La carpeta `Canciones_favs/` está excluida mediante `.gitignore`.

Los resultados del análisis ya generados se encuentran en `resultados_analisis.csv`, por lo que no es necesario tener los audios para revisar los datos obtenidos.

### ¿Quieres analizar tus propias canciones?

1. Dentro de la carpeta del proyecto (la misma que descargaste o clonaste de este repositorio), crea una carpeta llamada `Canciones_favs`.
2. Coloca ahí tus archivos `.mp3` (los que quieras analizar).
3. Asegúrate de tener instaladas las dependencias necesarias:
```bash
   pip install librosa pandas numpy streamlit
```
4. Ejecuta el script de análisis:
```bash
   cd Codigo
   python analizar.py
```
   O, si prefieres la versión interactiva con interfaz web:
```bash
   python -m streamlit run app.py
```

# 🎵 Analizador Musical con Python

Este proyecto permite analizar canciones en formato `.mp3` usando Python y librerías de análisis de audio.  
La aplicación extrae características musicales como tempo, energía, brillantez, ancho de banda, ZCR y contraste para comparar canciones y generar un puntaje final.

---

## 📌 Características principales

- Carga y análisis de canciones en formato `.mp3`
  
- Extracción de características musicales:
  - Tempo: qué tan rápida es la canción
  - Energía: qué tan intensa se siente
  - Brillantez: qué tan aguda o clara suena.
  - Ancho de banda: qué tan variado es el rango de sonidos
  - ZCR: qué tan ruidoso, cortante o percusivo puede ser el sonido
  - Contraste: qué tanto se diferencian los sonidos entre sí
    
- Cálculo de puntajes por canción
- Ranking de canciones según su puntaje final
- Visualización de resultados en una app interactiva con Streamlit

---

## 🛠️ Tecnologías utilizadas

- Python
- Streamlit
- Pandas
- Librosa
- NumPy

---

## ▶️ Cómo correr el programa

Para ejecutar correctamente este proyecto, sigue estos pasos:

### 1. Descargar el repositorio

Descarga o clona el repositorio completo desde la rama **main**.

Es importante utilizar todos los archivos del proyecto, ya que el programa necesita la estructura completa de carpetas para funcionar correctamente.

---

### 2. Abrir la terminal

Una vez descargado el repositorio, abre la terminal.

> ⚠️ **IMPORTANTE:**  
> No ejecutes el archivo directamente desde Python.  
> El programa debe correrse desde la terminal usando Streamlit.

---

### 3. Entrar a la carpeta del código

En la terminal, copia y pega el siguiente comando:

```bash
cd "C:\Users\Lenovo\OneDrive - Universidad Francisco Marroquin\Escritorio\Parcial I\Parcial-I-Programacion\Codigo"

### 4. Ejecutar la página web

Luego, copia y pega este comando en la terminal:

```bash
python -m streamlit run analizar.py
```

---

### 5. Abrir la aplicación

Después de ejecutar el comando anterior, Streamlit abrirá la página web automáticamente en tu navegador.

Si no se abre automáticamente, copia el enlace que aparece en la terminal y pégalo en tu navegador.

Normalmente se verá parecido a esto:

```text
http://localhost:8501
```