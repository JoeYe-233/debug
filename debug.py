import argparse
import gnupg



parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--publicKey', type=str, default=None)
args = parser.parse_args()

print("参数信息：", args)

gpg=gnupg.GPG()
data="Hello world"
import_result = gpg.import_keys(args.publicKey)
fingerprints=import_result.fingerprints
print("添加了",import_result.count,"个密钥对")
print(fingerprints)
encrypted_data = gpg.encrypt(data,fingerprints[0])
print(encrypted_data.data)
print(encrypted_data.status)
print(encrypted_data.ok)
print(str(encrypted_data))
print(len(encrypted_data))
