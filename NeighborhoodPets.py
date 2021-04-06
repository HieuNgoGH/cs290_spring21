# Hieu Ngo
# 10/28/2020
#Assignment 5d - Create a class that has methods to add a pet to a file, delete a pet from a file, get its owner,
# save and load a json file, and retrieve all spcecies of pets.

import json

class NeighborhoodPets:
    """Class of neighborhood pets that has methods to add a pet, delete a pet,
    get pet owner, save and read a json file, and retrieve all species of pets."""
    def __init__(self):
        self._pet_names_dict = []

    def add_pet(self, pet_name, pet_species, pet_owner):
        """Adds pet name, pet species, and pet owner to a file."""

        new_dict = self._pet_names_dict
        for pet in new_dict:
            for key, value in pet.items():
                if key == 'pet_name' and value == pet_name:
                    return 'pet already in database'
        else:
            pet_dict = {}
            pet_dict['pet_name'] = pet_name
            pet_dict['pet_species'] = pet_species
            pet_dict['pet_owner'] = pet_owner
            #print(pet_dict)
            self._pet_names_dict.append(pet_dict)

    def delete_pet(self, pet_name):
        """Takes as a parameter name of pet and deletes that pet."""
        for pet in self._pet_names_dict:
            #print(pet)
            for key, value in pet.items():
                if key == 'pet_name' and value == pet_name:
                    #print(pet)
                    self._pet_names_dict.remove(pet)
                    #print(self._pet_names_dict)

    def get_owner(self, pet_name):
        """Takes as a parameter pet's name then return pet's owner."""
        for pet in self._pet_names_dict:
            for key, value in pet.items():
                if key == 'pet_name' and value == pet_name:
                    owner = pet['pet_owner']
                    #print(owner)
                    return owner

    def save_as_json(self, filename):
        """Takes a filename and saves a file in JSON format in that name."""
        with open(filename, 'w') as outfile:
            json.dump(self._pet_names_dict, outfile)

    def read_json(self, filename):
        """Reads a JSON file given the filename."""
        with open(filename, 'r') as infile:
            working_file = json.load(infile)

    def get_all_species(self):
        """Returns all species of pets in database."""
        pet_species_set = set()

        for pet in self._pet_names_dict:
            #print(pet)
            for key, value in pet.items():
                if key == 'pet_species':
                    species = pet['pet_species']
                    pet_species_set.add(species)

        return pet_species_set

#np = NeighborhoodPets()
#np.add_pet("Fluffy", "gila monster", "Oksana")
#np.add_pet("Tiny", "stegasaurus", "Rachel")
#np.add_pet("Spot", "zebra", "Farrokh")
#np.add_pet("Fluffy", "gila monster", "Oksana")
#np.test()
#np.save_as_json("pets.json")
#np.delete_pet("Tiny")
#np.test()
#spot_owner = np.get_owner("Spot")
#np.test()
#np.read_json("other_pets.json")  # where other_pets.json is a file it saved in some previous session
#species_set = np.get_all_species()
