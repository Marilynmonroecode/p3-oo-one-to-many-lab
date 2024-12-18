class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        # Validate pet type
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type. Must be one of {self.PET_TYPES}")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = None
        
        # Set owner if provided
        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of Owner class")
            self.owner = owner
            owner.add_pet(self)
        
        # Add to class list of all pets
        self.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        """Return a list of all pets owned by this owner."""
        return self._pets

    def add_pet(self, pet):
        """Add a pet to the owner's list of pets."""
        # Validate that pet is an instance of Pet class
        if not isinstance(pet, Pet):
            raise Exception("Can only add Pet instances")
        
        # Only add if not already in the list
        if pet not in self._pets:
            self._pets.append(pet)
            
            # Set the pet's owner if not already set
            if pet.owner is None:
                pet.owner = self

    def get_sorted_pets(self):
        """Return a list of pets sorted by name."""
        return sorted(self._pets, key=lambda pet: pet.name)