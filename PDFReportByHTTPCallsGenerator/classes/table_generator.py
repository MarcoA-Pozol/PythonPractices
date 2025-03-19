from prettytable import PrettyTable

class TableGenerator():
	def __init__(self, table:PrettyTable, data:list[dict]|dict):
	self.__table = table
    self.__data = data
    self.__table.name = table_name
	
	@property
	def table(self) -> PrettyTable:
		return self.__table
	
    def add_fields(self):
        data = self.__data
        if isinstance(data, list) and data:
            self.table.field_names = data[0].keys()
	
    def add_rows(self):
        for item in self.__data:
            self.table.add_row(item.values())
            
    def show_table(self) -> PrettyTable:
        print(self.table)
        return self.table
        
    def retrieve_data(self) -> list:
        table_data = [self.table.field_names]
        for row in self.table._rows:
            table_data.append(row)
        return table_data