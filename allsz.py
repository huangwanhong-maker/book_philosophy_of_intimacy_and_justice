import subprocess,os
os.chdir("/mnt/c/Users/Micro/Desktop/Philosophy of Intimacy and the Theory of Justice/book_src/volumes")
for v in (1,2,3):
    r=subprocess.run(["pdfinfo",f"volume_{v}.pdf"],capture_output=True,text=True).stdout
    pg=[l.split(":",1)[1].strip() for l in r.splitlines() if l.startswith("Pages")]
    sz=[l.split(":",1)[1].strip() for l in r.splitlines() if "Page size" in l]
    print(f"volume_{v}: pages={pg} size={sz}")
