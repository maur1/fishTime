import requests as req

def getFishData(species = "none"):
    """
     Gets data from API, consider args to decide on what specie to fetch
    some times multiple data is returned?

    returns all fishes as def, and specie when specified else wise

     :return: json dict
     """
    #r = req.get("https://fishbase.ropensci.org/species?Species=" + species)
    r = req.get("https://fishbase.ropensci.org/species")
    my_dict = r.json()
    return my_dict

def getFishPopulation(genus):
    """
     Gets data from API, consider args to decide on what specie to fetch

     :return: json dict
     """
    r = req.get("https://fishbase.ropensci.org/popchar?fields="+genus)
    my_dict = r.json()
    return my_dict['count']

def getCollectionOfFish():
    '''
    def count is 10 species
    set limit=5000 to adjust amount of fish collected
    '''
    r = req.get("https://fishbase.ropensci.org/species?fields=Species")
    my_dict = r.json()
    return my_dict # TODO get specie name from data array

