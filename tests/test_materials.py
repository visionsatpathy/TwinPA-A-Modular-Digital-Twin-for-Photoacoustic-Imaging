from core.materials import MaterialLibrary

blood = MaterialLibrary.BLOOD

print("Material:", blood.name)
print("Absorption:", blood.mu_a)
print("Speed of sound:", blood.speed_of_sound)