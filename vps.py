import subprocess,collections,os
os.chdir("/mnt/c/Users/Micro/Desktop/Philosophy of Intimacy and the Theory of Justice/book_src/volumes")
c=collections.Counter()
import re
r=subprocess.run(["pdfinfo","volume_1.pdf"],capture_output=True,text=True).stdout
print([l for l in r.splitlines() if "Page size" in l or l.startswith("Pages")])
for pg in [1,2,3,5,100,400]:
    rr=subprocess.run(["pdfinfo","-f",str(pg),"-l",str(pg),"volume_1.pdf"],capture_output=True,text=True).stdout
    for l in rr.splitlines():
        if "Page size" in l: c[l.split(":",1)[1].strip()]+=1
print("distinct page sizes sampled:",dict(c))
