import configs
import os

phaxio_client = configs.phaxio_client

def send_fax(pdf):

    f = open(pdf, "rb")
    phaxio_client.send(to=configs.fax_number, files=(pdf, f))
