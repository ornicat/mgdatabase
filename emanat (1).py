# -*- coding: utf-8 -*-

import pandas as pd
dt = pd.read_excel('MG-Database.xlsx')

# I)
dt.info()
dt.columns
dt['Yoxlanışa alınma tarixi'] = pd.to_datetime(dt['Yoxlanışa alınma tarixi'])
dt['Status verilmə tarixi'] = pd.to_datetime(dt['Status verilmə tarixi'])
dt.info()
dt['cycletime'] = dt['Status verilmə tarixi'] - dt['Yoxlanışa alınma tarixi']



# II)
cem = dt['Ümumi məbləğ AZN'].sum()
dt['Ümumi məbləğ faiz'] = (dt.groupby('MG Şirkət')['Ümumi məbləğ AZN'].transform('sum') * 100)/ cem   



# III)
dt['mm'] = pd.to_datetime(dt['Tarix Vaxt']).dt.month
aylar = dt.groupby('mm')['Ümumi məbləğ AZN'].sum()

# neticede 4cu ay en cox alish olan aydir- mebleg = 91700.60


# IV)
companies = dt.groupby('Satıcı Şirkət')['Ümumi məbləğ AZN'].sum()
companies = pd.DataFrame(companies)
companies[companies['Ümumi məbləğ AZN'] == companies['Ümumi məbləğ AZN'].max()]





