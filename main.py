import requests
from os import path, mkdir

def IsRealCert(certid):
    if requests.get("https://www.sololearn.com/Certificate/" + certid + "/pdf/?mode=download", stream=True).headers.get("content-disposition") :
        return True
    else:
        return False


def Main():
    CertificateID = input("Cert ID > ")
    if IsRealCert(CertificateID):
        if not path.exists("certs"):
            mkdir("certs")

        with open("certs\\" + CertificateID + ".pdf", "w+b") as f:
            f.write(requests.get("https://www.sololearn.com/Certificate/" + CertificateID + "/pdf/?mode=download").content)
            f.close()
            
        print("Valid Certificate")
    else:
        print("Invalid/Fake Certificate")

if __name__ == "__main__":
    Main()