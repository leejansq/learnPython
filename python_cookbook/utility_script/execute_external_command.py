# -*-coding:utf-8-*-
import subprocess
#
# outbytes = subprocess.getoutput(['netstat', '-a'])
# print("outbytes", outbytes)
# outtext = outbytes.decode('utf-8')
# print("outtext", outtext)


try:
    out_bytes = subprocess.check_output(['ls', '-a', '-l'], timeout=5)
    print(out_bytes.decode('utf-8'))
except subprocess.CalledProcessError as e:
    out_bytes = e.output  # Output generated before error
    code = e.returncode  # Return code

out_bytes = subprocess.check_output('grep python | wc > out', shell=True)
