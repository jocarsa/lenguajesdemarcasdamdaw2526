# pip3 install pandas --break-system-packages
# pip3 install odfpy --break-system-packages

import pandas as pd

df = pd.read_excel('empresa.ods', engine='odf')
data = df.to_dict(orient='records')
print(data)
