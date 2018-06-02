
```python
import os
from pyfaidx import Fasta
```

```python
test=Fasta("test.fa")
```

```python
with open ("ids.txt",) as f:
    ids=f.readlines()
print(ids)
```

    ['sp|P17672.2|E75BA_DROMERecName:Full=Ecdysone-inducedprotein75B,isoformA;Short=E75-B;AltName:Full=Nuclearreceptorsubfamily1groupDmember3,isoformA\t415\t484\n', 'sp|P45447.4|E78C_DROMERecName:Full=Ecdysone-inducedprotein78C;Short=DR-78;AltName:Full=Nuclearreceptorsubfamily1groupEmember1\t363\t443\n']

```python
sids=[s.split() for s in ids]
```

```python
final_results=[test[i[0]][int(i[1]):int(i[2])] for i in sids]
```

```python
with open ("output.txt","w") as f:
    for i in final_results:
        print (">"+i.name,"\n",i.seq,file=f)
```
