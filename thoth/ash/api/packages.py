import os
from typing import List
from thoth.storages import CephStore


store = CephStore(prefix='data/thoth/ash-api/CrossWalk/packages')
store.connect()


def retrieve_n_most_similar(package_name, n) -> List:
    package_dict = store.retrieve_document(package_name)
    return [t for t in package_dict['most_similar'][:n]]


def get(package_name):
    """ Retrieves the 25 most similar packages to {name} path param """

    if not store.document_exists(package_name):
        return {'error': f'The package: {package_name} is not found.'}, 404

    return {
            'package-name': package_name,
            'most-similar-tokens': retrieve_n_most_similar(package_name, n=25),
        }, 200
