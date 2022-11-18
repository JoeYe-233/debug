import argparse
import gnupg
import os


parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--publicKey', type=str, default=None)
args = parser.parse_args()

print("参数信息：", args)

gpg=gnupg.GPG()
data="Hello world"
import_result = gpg.import_keys(args.publicKey)
fingerprints=import_result.fingerprints
os.system("gpg --edit-key \'"+fingerprints[0]+"\'")
#os.system("gpg --import-ownertrust "+fingerprints[0]+":6:")
os.system("echo \""+fingerprints[0]+":6:\" | gpg --import-ownertrust")
os.system("gpg --list-keys")
# gpg.trust_keys(fingerprints, 'TRUST_ULTIMATE')
print("添加了",import_result.count,"个密钥对")


print(fingerprints[0])



encrypted_data = gpg.encrypt(data,fingerprints,sign=True)
# print(encrypted_data.status_detail)available after python-gnupg 0.5.1
print(encrypted_data.status)
print(encrypted_data.ok)
print(str(encrypted_data))
