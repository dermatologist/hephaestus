# CCI Intervention Code (Canada)

Hephaestus can import CCI definitions into a 

STEPS

1. Download CCI xlsx file from CIHI

```python
from hephaestus.utils.import_cci import Cci
Cci.get_cci()

```

2. Do an etl with the downloaded file in the
resources folder

```bash

python -m hephaestus -f etl -m cci

```

* cci table is created in hephaestus schema

## TODO

* Implement similarity lookup search