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
encrypted_data = gpg.encrypt(data,fingerprints)
print(encrypted_data)

