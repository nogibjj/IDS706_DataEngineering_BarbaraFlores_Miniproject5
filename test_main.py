"""
Test goes here

"""
import unittest
import os
from mylib.extract import extract


class TestExtractFunction(unittest.TestCase):

    def test_extract(self):
        # Definir rutas de archivo para entrada y salida
        input_url = "https://raw.githubusercontent.com/nickeubank/practicaldatascience/master/Example_Data/world-small.csv"
        output_file_path = "data/WorldSmall.csv"

        # Asegurarse de que el archivo de salida no exista antes de ejecutar la función
        if os.path.exists(output_file_path):
            os.remove(output_file_path)

        # Llamar a la función extract
        result = extract(url=input_url, file_path=output_file_path)

        # Verificar que la función devuelve la ruta correcta del archivo
        self.assertEqual(result, output_file_path)

        # Verificar que el archivo de salida se ha creado
        self.assertTrue(os.path.exists(output_file_path))

        # Limpiar después de la prueba
        if os.path.exists(output_file_path):
            os.remove(output_file_path)

if __name__ == '__main__':
    unittest.main()