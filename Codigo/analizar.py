import os
import numpy as np
import pandas as pd
import librosa

CARPETA_SCRIPT = os.path.dirname(os.path.abspath(__file__))
CARPETA_CANCIONES = os.path.join(CARPETA_SCRIPT, "..", "Canciones_favs")

#Puntuación subjetiva
#Organizado en tuplas

#Tempo (BPM, Beats per minute)
RANGOS_TEMPO = [
    (0, 60, 40, 50),
    (60, 90, 51, 65),
    (90, 110, 66, 80),
    (110, 130, 81, 90),
    (130, 200, 91, 100),
]

#Energía (RMS) - qué tan "fuerte"/inteso suena en promedio

RANGOS_ENERGIA = [
    (0.00, 0.05, 40, 55),
    (0.05, 0.10, 56, 75),
    (0.10, 0.15, 71, 90),
    (0.15, 0.30, 91, 100),
]

#Brillantez (Hz) - sonido "brillante" vs "oscuro"

RANGOS_BRILLANTEZ = [
    (0, 1000, 40, 55),
    (1000, 2000, 56, 70),
    (2000, 3000, 71, 85),
    (3000, 5000, 86, 100),
]

#Ancho de banda espectral - qué tan "amplio/variado" es el sonido

RANGOS_ANCHO_BANDA = [
    (0, 1000, 40, 55),
    (1000, 2000, 56, 70),
    (2000, 3000, 71, 85),
    (3000, 5000, 86, 100),
]

#Zero Crossing Rate - relacionado con percusividad/ruido

RANGOS_ZCR = [
    (0.00, 0.03, 40, 55),
    (0.03, 0.06, 56, 70),
    (0.06, 0.10, 71, 85),
    (0.10, 0.30, 86, 100),
]

#Contraste especial - diferencia entre picos y valles de frecuencia
#Valores altos = sonido "nítido"/"definido" (graves y agudos marcados)

RANGOS_CONTRASTE = [
    (0, 15, 40, 55),
    (15, 20, 56, 70),
    (20, 25, 71, 85),
    (25, 40, 86, 100),
]

#2. Ponderación para el puntaje final

#Define que tanto influye cada característica en el puntaje de "cuanto te gusta la canción". La suma
#debe ser 1.0

PONDERACION = {
    "tempo": 0.35,
    "energia": 0.25,
    "brillantez": 0.15,
    "ancho_banda": 0.10,
    "zcr": 0.05,
    "contraste": 0.10
}

#3. Funciones de operación

def asignar_puntaje(valor, rangos):  #
    """
    Convierte un valor númerico en un puntaje subjetivo,
    usando interpolación lineal dentro del rango correspondiente
    """
    for (v_min, v_max, p_min, p_max) in rangos:
        if v_min <= valor <= v_max:
            if v_max == v_min:
                return p_min
            proporcion = (valor - v_min) / (v_max - v_min)
            return p_min + proporcion * (p_max - p_min)
        
    if valor < rangos[0][0]:  #Solo por si el valor cae fuera de todos los rangos definidos, se asigna al extremo mas cercano
        return rangos[0][2]
    return rangos[-1][3]

def extraer_caracteristicas(ruta):
    """
    Carga un archivo de audio y extrae las caracteristicas 
    cuantificables más relevantes con Librosa
    """

    y, sr = librosa.load(ruta)

#TEMPO (BPM)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    tempo = float(np.atleast_1d(tempo)[0])

#Energía (RMS)

    rms = librosa.feature.rms(y=y) #El RMS es la medición del volumen promedio o la potencia real y continua de una señal de audio
    energia = float(np.mean(rms)) #el np.mean convierte todos los valores que arroja el rms en un promedio que sea mas facil de cuantificar

#Brillantez (centroide espectral)

    centroide = librosa.feature.spectral_centroid(y=y, sr=sr)
    brillantez = float(np.mean(centroide))

#Ancho de banda espectral

    ancho_banda = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    ancho_banda = float(np.mean(ancho_banda))

#Zero Crossing Rate

    zcr = librosa.feature.zero_crossing_rate(y)
    zcr = float(np.mean(zcr))

#Contraste espectral

    contraste = librosa.feature.spectral_contrast(y=y, sr=sr)
    contraste_promedio = float(np.mean(contraste))

#Nota dominante

    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    chroma_prom = np.mean(chroma, axis=1)
    notas = ["Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si"]
    
    nota_dominante = notas[int(np.argmax(chroma_prom))] #?????

#Duración total

    duracion = librosa.get_duration(y=y, sr=sr)
 
    return {               #Explicar
        "tempo": tempo,
        "energia": energia,
        "brillantez": brillantez, 
        "ancho_banda": ancho_banda,
        "zcr": zcr, 
        "contraste": contraste_promedio,
        "nota_dominante": nota_dominante,
        "duracion": duracion,
    }

def calcular_puntajes(caracteristicas):
    """
    Aplica los rangos subjetivos a cada característica numérica y
    calcula el puntaje final ponderado
    """
    puntaje_tempo = asignar_puntaje(caracteristicas["tempo"], RANGOS_TEMPO)
    puntaje_energia = asignar_puntaje(caracteristicas["energia"], RANGOS_ENERGIA)
    puntaje_brillantez = asignar_puntaje(caracteristicas["brillantez"], RANGOS_BRILLANTEZ)
    puntaje_ancho = asignar_puntaje(caracteristicas["ancho_banda"], RANGOS_ANCHO_BANDA)
    puntaje_zcr = asignar_puntaje(caracteristicas["zcr"], RANGOS_ZCR)
    puntaje_contraste = asignar_puntaje(caracteristicas["contraste"], RANGOS_CONTRASTE)

    puntaje_final= (
        puntaje_tempo * PONDERACION["tempo"]
        + puntaje_energia * PONDERACION["energia"]
        + puntaje_brillantez * PONDERACION["brillantez"]
        + puntaje_ancho * PONDERACION["ancho_banda"]
        + puntaje_zcr * PONDERACION["zcr"]
        + puntaje_contraste * PONDERACION["contraste"]
    )

    return {
        "puntaje_tempo": puntaje_tempo,
        "puntaje_energia": puntaje_energia,
        "puntaje_brillantez": puntaje_brillantez,
        "puntaje_ancho_banda": puntaje_ancho,
        "puntaje_zcr": puntaje_zcr,
        "puntaje_contraste": puntaje_contraste,
        "puntaje_final": puntaje_final,
    }

#Main Code:

def main():
    resultados = []

    archivos = [f for f in os.listdir(CARPETA_CANCIONES) if f.lower().endswith(".mp3")]

    if not archivos:
        print(f"No se encontraron archivos .mp3 en la carpeta '{CARPETA_CANCIONES}'")
        return
    
    for archivo in archivos:
        print(f"Analizando: {archivo}...")
        ruta = os.path.join(CARPETA_CANCIONES, archivo)

        caracteristicas = extraer_caracteristicas(ruta)
        puntajes = calcular_puntajes(caracteristicas)

        fila = {"cancion": archivo}
        fila.update(caracteristicas)
        fila.update(puntajes)
        resultados.append(fila)

    df = pd.DataFrame(resultados)
    print("Columnas disponibles", df.columns.tolist()) #Linea temporal de prueba

#Ordenar de la canción que "más te gusta" a la que "menos"

    df = df.sort_values(by="puntaje_final", ascending=False).reset_index(drop=True)

#Redondear para que la tabla sea más legible

    columnas_numericas = df.select_dtypes(include=[float, int]).columns
    df[columnas_numericas] = df[columnas_numericas].round(2)

    columnas_tabla = [
        "cancion", "tempo", "energia", "brillantez", "ancho_banda", 
        "zcr", "contraste", "nota_dominante", "duracion", "puntaje_final"
    ]

    print("\n=== TABLA COMPARATIVA ===\n")
    print(df[columnas_tabla].to_string(index=False))

    print("\n=== DETALLE DE PUNTAJES POR CARACTERÍSTICA ===\n")
    columnas_puntajes = [
        "cancion", "puntaje_tempo", "puntaje_energia", "puntaje_brillantez", 
        "puntaje_ancho_banda", "puntaje_zcr", "puntaje_contraste", "puntaje_final"
    ]
    print(df[columnas_puntajes].to_string(index=False))

if __name__ == "__main__":
    main()