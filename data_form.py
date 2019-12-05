##바이너리 데이터  vs 텍스트데이터

#파일 이름가ㅗ 데이터
filenae = "a.bin"
data = 100

#쓰기

with open(filenae, "wb") as f:
    f.write(bytearray([data]))