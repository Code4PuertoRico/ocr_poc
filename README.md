# ocr_poc
Un repositorio para probar OCR

## Requisitos

- Tesseract: necesitas intalar tesseract-ocr en tu maquina. Esto es lo que esta realmente haciendo el OCR.

  Para instalar siga las [instrucciones para su plataforma](https://github.com/tesseract-ocr/tesseract/wiki#installation).

- Python 3.7
- [Pipenv](https://pipenv.pypa.io/en/latest/install/#installing-pipenv)

  Una vez instalado ejecuta `$ pipenv install` para instalar todas las dependencias de Python.

## Ejecutando el programa

- Necesitas activar el virtual env que creo pipenv en el paso anterior. Para hacer esto ejecuta `$ pipenv shell`
- Luego ejecta `python app.py`
- Para cambiar la foto que se esta procesando necesitas cambiarla dentro del `app.py`

### Output

Al procesar la imagen obtendras un output similar a esto:

```
{
    'new_cases': {'new_cases': '13'},
    'dept_salud_new_cases': {'dept_salud_new_cases': '3'},
    'va_new_cases': {'va_new_cases': '0'},
    'private_labs_new_cases': {'private_labs_cases_new_cases': 'o'},
    'result_summary_positive': {'dept_salud_positives_total': '47',
    'va_positives_total': '16',
    'private_labs_positives_total': '1',
    'total_pr_number_positives': '64',
    'total_pr_percent_positives': '82'},
    'result_summary_nagative': {'dept_salud_negatives_total': '31', 'va_negatives_total': '50', 'private_labs_negatives_total': '16', 'total_pr_number_negatives': '377', 'total_pr_percent_negatives': '486'}, 'result_summary_totals': {'dept_salud_totals': '454', 'va_totals': '134', 'private_labs_totals': '188', 'results_pr_number_totals': '776', 'results_pr_percent_totals': '100'}
}
```
