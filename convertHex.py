import sys
import numpy as np
from math import sqrt
from ast import literal_eval


def padHex(strVal, size):
    if size > 0 and len(strVal) % 2 != 0:
        strVal = strVal + "0"

    if size > 1 and len(strVal) % 4 != 0:
        strVal = strVal + "00"

    if size > 3 and len(strVal) % 8 != 0:
        strVal = strVal + "0000"

    return strVal


def decompress(strHex, size, scale, signed=False):
    floatArray = np.array([])
    str_aux = padHex(strHex, size)
    limit = 0

    for i in range(0, len(str_aux) - 1, size * 2):
        limit += size * 2
        transformToDecimal = 0
        try:
            if limit != 4:
                strAux1 = '0x'+str_aux[i:limit]
                transformToDecimal = literal_eval(strAux1)
            else:
                transformToDecimal = literal_eval(str_aux[i:limit])
        except:
            print('')

        if signed and size == 1 and transformToDecimal >= 128:
            transformToDecimal = transformToDecimal - 256

        if signed and size == 2 and transformToDecimal >= 128 * 256:
            transformToDecimal = transformToDecimal - 256 * 256

        if signed and size == 3 and transformToDecimal >= 128 * 256 * 256:
            transformToDecimal = transformToDecimal - 256 * 256 * 256

        if signed and size == 4 and transformToDecimal >= 128 * 256 * 256 * 256:
            transformToDecimal = transformToDecimal - 256 * 256 * 256 * 256

        floatArray = np.append(floatArray, transformToDecimal / scale)

    return floatArray


def strSplitArray(strHex):
    hexs = np.array([])

    if ',' in strHex:
        pos = strHex.find(',')
        hexs = np.append(hexs, strHex[0:pos])
        strHex = strHex[pos + 1:]

    hexs = np.append(hexs, strHex)
    return hexs


def calculateAverage(strHexadecimal, type='Acc'):
    if strHexadecimal is None or strHexadecimal == '': return ''
    if strHexadecimal == '0' or strHexadecimal == '80': return ''

    avgArray = np.array([])
    output = 0.0
    count = 0
    strArr = strSplitArray(strHexadecimal)

    for i, val in enumerate(strArr):
        if type == 'Gyr':
            avgArray = np.append(avgArray, decompress(val, 2, 512))
        if type == 'Mag':
            avgArray = np.append(avgArray, decompress(val, 2, 8))
        if type == 'Acc':
            avgArray = np.append(avgArray, decompress(val, 2, 256))

    for i in range(len(avgArray)):
        sum = 0

        if avgArray[i] is not None:
            sum += avgArray[i]

        # output += sqrt(sum)
        count += 1

    if count == 0:
        return 0

    return sum / count
