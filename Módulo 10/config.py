def main():
    try:
        configuration = open('config.txt')
    except OSError as err:
        if err.errno == 2:
            print("Couldn't find the config.txt file!")
        elif err.errno == 13:
            print("Found config.txt but couldn't read it")
    except FileNotFoundError as err:
        print("No se encontró el archivo 'config.txt'.", err)
    except PermissionError: # Ejercicio no fiel al ejemplo para adaptarlo a mi caso específico.
        print("¡Se encontró pero fue detectado como un error de permiso!")
    except (BlockingIOError, TimeoutError):
        print("Archivo del sistema bajo carga pesada. No se puede completar la lectura de configuración del archivo.")


if __name__ == '__main__':
    main()