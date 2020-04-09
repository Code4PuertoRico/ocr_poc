from PIL import Image
import pytesseract
import re

regular_expressions = {
    "date": re.compile("Fecha de actualización de datos:\s(?P<day>\d+)\sde\s(?P<month>.+)\sde\s(?P<year>\d{4})"),
    "new_cases": re.compile("Total de casos nuevos desde último informe:\s(?P<new_cases>\d+)"),
    "dept_salud_new_cases": re.compile("\* Departamento de Salud\:*\s*(?P<dept_salud_new_cases>.)"),
    "va_new_cases": re.compile("\* Administración de Veteranos:\s*(?P<va_new_cases>.)"),
    "private_labs_new_cases": re.compile("\* Laboratorios Privados\:*\s*(?P<private_labs_cases_new_cases>.)"),
    "result_summary_positive": re.compile("Positivos\s(?P<dept_salud_positives_total>\d+)\s(?P<va_positives_total>\d+)\s(?P<private_labs_positives_total>\d+)\s(?P<total_pr_number_positives>\d+)\s(?P<total_pr_percent_positives>\d+)"),
    "result_summary_nagative": re.compile("Negativos\s(?P<dept_salud_negatives_total>\d+)\s(?P<va_negatives_total>\d+)\s(?P<private_labs_negatives_total>\d+)\s(?P<total_pr_number_negatives>\d+)\s(?P<total_pr_percent_negatives>\d+)"),
    "result_summary_waiting": re.compile("Pendientes\s(?P<dept_salud_waiting_totals>\d+)\s(?P<va_waiting_totals>\d+)\s(?P<private_labs_waiting_totals>\d+)\s(?P<total_pr_number_waiting>\d+)\s(?P<total_pr_percent_waiting>\d+)"),
    "result_summary_totals": re.compile("Total\s(?P<dept_salud_totals>\d+)\s(?P<va_totals>\d+)\s(?P<private_labs_totals>\d+)\s(?P<results_pr_number_totals>\d+)\s(?P<results_pr_percent_totals>\d+)"),
}
data = {}
def extract_data(line_data):
    for key, value in regular_expressions.items():
        match = value.match(line_data)
        if match:
            return {key: match.groupdict()}

def extract_text(image):
    image = Image.open(image)
    data = pytesseract.image_to_string(image, lang="spa")
    return [x for x in data.splitlines() if x.strip()]

extracted_text = extract_text("03-25-2020_1.jpg")

for line in extracted_text:
    extracted_data = extract_data(line)
    if extracted_data:
        data.update(extracted_data)

print(data)