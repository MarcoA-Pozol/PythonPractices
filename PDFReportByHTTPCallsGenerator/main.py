from classes.http_client import HTTPClient
from classes.table_generator import TableGenerator
from classes.pdf_documentor import PDFDocumentor
from prettytable import PrettyTable
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


table = PrettyTable

# Obtaining data from HTTP response
url = 'http://localhost:10200/services'
http_client = HTTPClient()
data = http_client.execute_get_request(url=url)

# Generate table with the obtained data
table = PrettyTable()
table_generator = TableGenerator(table=table, data=data, table_name='Services Report')
table_generator.add_fields()
table_generator.add_rows()
table_generator.show_table()
table_data = table_generator.retrieve_data()

# Generate a PDF file using the table's data
pdf_table = Table(table_data)
style = TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),  # Header row background color
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),  # Header row text color
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),  # Center-align all cells
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),  # Header row font
    ("FONTSIZE", (0, 0), (-1, 0), 14),  # Header row font size
    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),  # Header row bottom padding
    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),  # Table body background color
    ("GRID", (0, 0), (-1, -1), 1, colors.black),  # Add grid lines
])
pdf_documentor = PDFDocumentor(pdf_table=pdf_table, data=table_data)
pdf_documentor.set_style(style=style)
pdf_documentor.build_pdf_table()