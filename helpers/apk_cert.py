#!/usr/bin/env python3

import subprocess
import textwrap

KEYTOOL_PATH = 'apksigner'

def get_sha256_cert_fingerprint(apk):
    apk_cert = subprocess.Popen(
        KEYTOOL_PATH + ' verify --print-certs ' + apk, shell=True, stdout=subprocess.PIPE
    ).stdout.read().decode()
    if 'SHA-256 digest: ' in apk_cert:
        components = apk_cert.split('1 certificate SHA-256 digest: ')
        print(components)
        if len(components) > 1:
            sha256_digest = components[1].split('\n')[0]
            return ':'.join(textwrap.wrap(sha256_digest.upper(), 2))
    return None 
