FILE_NAME = "/calabash/test/chenyu.zheng/10169019_RADS1012092000052026.ts"

with open("/calabash/MezzanineArchive/563/138042563/10169019_RADS1012092000052026.ts", "r") as f:
    while True:
        a = f.read(4096)
        if a == "":
            break

a = " " * 1024 * 1024 * 900

print "finished"
