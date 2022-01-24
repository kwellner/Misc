from ppi_data_importer import ppi_data_importer

# initialize an instance of the importer
data_importer = ppi_data_importer.initialize()

# load data from the specified site
df = data_importer.read_tags(source='PIC',
                             tag_list='DORPFMZ-V700CA36F0009-XISA.PV',
                             load_type='recorded',
                             start='2021-10-01 12:00',
                             end='2021-10-05 12:00',
                             additional_columns=['Unit', 'Description'],
                             digital_type='numeric')