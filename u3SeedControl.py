import torch
import random

class U3SeedControl:
    def __init__(self):
        pass
    
    SEED_MAX = 0xffffffffffffffff

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "seed_next": ("INT", {"default": 0, "min": 0, "max": U3SeedControl.SEED_MAX}),
            },
        }

    CATEGORY = "sampling"
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("seed",)
    FUNCTION = "generate_seed"


    seed_last = -1

    def generate_seed(self, seed_next):
        seed = 0
        if (seed_next == 0):
            #seed = random.randint(1, U3SeedControl.SEED_MAX)
            #generator = torch.Generator(device="cuda");
            #seed = generator.seed();
            seed = U3SeedControl.SEED_MAX
        else:
            seed = seed_next
        self.seed_last = seed
        print("U3SeedControl: generated seed: ", seed);
        return (seed,)
    
    def IS_CHANGED(self, seed_next):
        return (seed_next == self.seed_last)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "U3SeedControl": U3SeedControl
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "U3SeedControl": "u3 Seed Control"
}
