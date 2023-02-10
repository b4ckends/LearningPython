set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(f'set set_countries = {set_countries}')
print(f'the len of the set set_countries = {size}')

print(f'col is in the set set_countries = {"col" in set_countries}')
print(f'dos is inside of the set set_countries = {"dos" in set_countries}')
print(f'deu is in the set set_countries before of be added = {"deu" in set_countries}')

# adding values
set_countries.add('deu')
print(f'added a new countrie inside of the set set_countries = {set_countries}')

print(f'deu is in the set set_countries = {"deu" in set_countries}')

# updating values
set_countries.update({'ar', 'ecua', 'pe'})
print(f'update = {set_countries}')

# remove
set_countries.remove('ar')
print(f'removing one value = {set_countries}')

# remove differents values
to_remove = ['ar', 'ecua', 'pe']

for item in to_remove:
    set_countries.discard(item)
    
print(f'removing diferents values = {set_countries}')

# remove all values
set_countries.clear()
print(f'removing all values of set_countries = {set_countries}')

print(f'The new len of the set after removing all values is = {len(set_countries)}')

# Ejemplo del metodo update
# Crear un set original
# original_set = {1, 2, 3}

# Crear un nuevo set con elementos adicionales
# new_set = {3, 4, 5}

# Actualizar el set original con los elementos del nuevo set
# original_set.update(new_set)

# Verificar el set actualizado
# print(original_set) # Output: {1, 2, 3, 4, 5}