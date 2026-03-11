# main.py
import os
import numpy as np
from src.detector_pose import process_video_with_ai
from config.settings import VIDEO_DIR
from src.visualizer_3d import show_real_3d_dashboard

def main():
    if not os.path.exists(VIDEO_DIR):
        os.makedirs(VIDEO_DIR)
        print(f"Por favor, coloca tus videos en la carpeta: {VIDEO_DIR}")
        return

    # Mapeo de qué cámara corresponde a qué archivo de video
    # AJUSTA ESTOS NOMBRES SEGÚN LOS ARCHIVOS QUE TENGAS
    videos_a_procesar = [
        {"cam_id": 0, "filename": "campus4-c0.avi"}, # Reemplaza con tu archivo real de la cam 0
        {"cam_id": 1, "filename": "campus4-c1.avi"}, # Reemplaza con tu archivo real de la cam 1
        {"cam_id": 2, "filename": "campus4-c2.avi"}  # Reemplaza con tu archivo real de la cam 2
    ]

    todos_los_puntos = []

    for video_info in videos_a_procesar:
        cam_id = video_info["cam_id"]
        filename = video_info["filename"]
        
        # Verificar que el video existe antes de procesarlo
        if not os.path.exists(os.path.join(VIDEO_DIR, filename)):
            print(f" Video no encontrado: {filename}. Saltando...")
            continue
            
        puntos_camara = process_video_with_ai(cam_id, filename)
        
        if len(puntos_camara) > 0:
            todos_los_puntos.append(puntos_camara)

    # Consolidar todos los puntos de todas las cámaras en una sola matriz
    if todos_los_puntos:
        puntos_unificados = np.vstack(todos_los_puntos)
        print(f"\n PROCESAMIENTO TOTAL COMPLETADO.")
        print(f"Total de coordenadas topográficas reales extraídas: {len(puntos_unificados)}")
        
        # --- Mostrar el Dashboard ---
        print("Generando Dashboard 3D con coordenadas reales...")
        show_real_3d_dashboard(puntos_unificados)
    else:
        print("\n No se extrajeron datos. Verifica los videos o las detecciones.")

if __name__ == "__main__":
    main()