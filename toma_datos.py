from sense_hat import SenseHat
import csv
import time
import os

# Inicializar el SenseHat
sense = SenseHat()

# Nombre del directorio para guardar los datos
folder_name = 'datos11'
os.makedirs(folder_name, exist_ok=True)

# Información de la persona y el ejercicio
persona = 'usuarioX'
# ej = 'brazos-alante-atras'
# ej = 'brazos-arriba-abajo'
# ej = 'brazos-circulos'
# ej = 'rodillas-pecho'
# ej = 'flexion-mano-hombro'
# ej = 'sentadilla-brazos-ext'
ej = 'jumping-jacks'

# Nombre y ruta del archivo CSV
csv_name = f'{ej}_{persona}.csv'
csv_file_path = os.path.join(folder_name, csv_name)

# Espera para iniciar
time.sleep(2)

# Abrir el archivo CSV para escritura
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Escribir el encabezado (Timestamp, acelerómetro y giroscopio)
    writer.writerow(['Timestamp', 'Acc_X', 'Acc_Y', 'Acc_Z', 'Gyro_X', 'Gyro_Y', 'Gyro_Z'])
    
    # Tiempo de inicio
    start_time = time.time()
    
    try:
        while True:
            # Detener la recolección de datos después de 40 segundos
            if time.time() - start_time > 40:
                break
            
            # Leer datos del acelerómetro
            acceleration = sense.get_accelerometer_raw()
            acc_x = acceleration['x']
            acc_y = acceleration['y']
            acc_z = acceleration['z']
            
            # Leer datos del giroscopio
            gyroscope = sense.get_gyroscope_raw()
            gyro_x = gyroscope['x']
            gyro_y = gyroscope['y']
            gyro_z = gyroscope['z']
            
            # Timestamp actual
            timestamp = time.time()
            
            # Imprimir los datos en la consola
            print(f"Time: {timestamp:.2f}, Acc: x={acc_x:.2f}, y={acc_y:.2f}, z={acc_z:.2f} | Gyro: x={gyro_x:.2f}, y={gyro_y:.2f}, z={gyro_z:.2f}")
            
            # Escribir los datos en el archivo CSV
            writer.writerow([timestamp, acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z])
            
            # Esperar 0.01 segundos
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("Data collection stopped.")
