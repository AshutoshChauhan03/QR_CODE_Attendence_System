from MyQR import myqr
import os
import base64

# Opening a file in read mode
file = open("inputData.txt", "r")
# Getting elements in file in list
lines = file.read().split('\n')
try:
    # Generating qr code of each element in list
    for i in range(len(lines)):
        # changing element into bytes-stream
        data = lines[i].encode()
        # encoding bytes-stream on base64
        codedName = base64.b64encode(data)
        # making and saving qr codes
        myqr.run(
        # providing encoded data to be put on qr code
        str(codedName),
        # providing name to save file with extension
        save_name=str(lines[i] + '.png'),
        # providing directory where qr code should be saved
        save_dir=os.getcwd() + "\QR Codes"
        )
except Exception:
    print("All Entries Converted!")
