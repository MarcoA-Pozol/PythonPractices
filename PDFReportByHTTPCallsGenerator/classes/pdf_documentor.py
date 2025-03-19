from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

class PDFDocumentor():
    def __init__(self, pdf_table:Table, data:list):
        self.__pdf_table = pdf_table(data)
        self.__style = None
        
    def set_table_style(self, style:TableStyle):
        self.__style = style
        self.__pdf_table.setStyle(self.__style)
    
    def build_pdf_table(self):
        doc.build([self.__pdf_table])