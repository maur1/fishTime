import logging
import azure.functions as func
import csv
import requests as req
import boto3

from .util import getFishData

final_data_dict = {
    'Species': [],
    'Vulnerability': [],
    'Price Category': [],
    'Used as bait': []
}


def gather_data_local():
    return "TODO"


def gather_data():

    with open("fishy_data.csv", 'w') as file:
        header = list(final_data_dict.keys())
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()

        specie = getFishData()

        for specie in list(specie['data']):
            print(specie['Species'])
            spec = specie['Species']
            vuln = specie['Vulnerability']
            priceCat = specie['PriceCateg']
            bait = specie['UsedasBait']
            writer.writerow({'Species': spec,
                             'Vulnerability': vuln,
                             'Price Category': priceCat,
                             'Used as bait': bait})

            final_data_dict['Species'].append(spec)
            final_data_dict['Vulnerability'].append(vuln)
            final_data_dict['Price Category'].append(priceCat)
            final_data_dict['Used as bait'].append(bait)

    return final_data_dict


def handler():
    return "TODO"
