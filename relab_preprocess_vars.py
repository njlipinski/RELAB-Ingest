# attributes of database to classify into
material_classes = {
    "Meteorites", "Mineral", "Mixture", "Organic", "Spacecraft Observations", 
    "Reference", "Rock", "Sediment", "Synthetic", "Volatiles", 
    "Returned Planetary Samples"
}

# defined classifications  
meteorites = {
    'Mars-Met', 'Moon-Met', 'Other-Ast', 'Other-Qet', 'Other-Vet', 'Other-Met'
}

sediments = {
    'Sand', 'Ash', 'Regolith'
}

organics = {
    'Biological', 'Organic'
}

minerals = {
    'Element', 'MineralPwdr', 'Coating'
}

rocks = {
    'Glass', 'PockPowder', 'RockCoating', 'RockFines', 'Rocks', 
    'RocksSlab', 'Spherule', 'Tektite'
}

synthetics = {
    'Polymer', 'Reagent'
}

# outlier classifications
# format: generalType1, type1, subtype
minerals_o = {
    ', , Albertite ',
    ', , Amersil (BC) Qtz',
    ', , Anatase ',
    ', , Antrharxolite ',
    ', , Fe2O3 ',
    ', , Nacholite ',
    'Mineral, Bromide, KBr Potassium Bromide',
    'Mineral, Bromide, Potassium Bromide KBr',
    'Mineral, Carbonate , Anhydrous Oxalate Acid',
    'Mineral, Carbonate , Ankerite',
    'Mineral, Carbonate , Aragonite ',
    'Mineral, Carbonate , Artinite',
    'Mineral, Carbonate , Azurite',
    'Mineral, Carbonate , Brugnatellite ',
    'Mineral, Carbonate , Calcite ',
    'Mineral, Carbonate , Cerussite',
    'Mineral, Carbonate , Coalingite',
    'Mineral, Carbonate , Dawsonite ',
    'Mineral, Carbonate , Dolomite',
    'Mineral, Carbonate , Gaspeite',
    'Mineral, Carbonate , Gaylussite',
    'Mineral, Carbonate , Heated Gaylussite ',
    'Mineral, Carbonate , Heated Hydromagnesite ',
    'Mineral, Carbonate , Heated Hydrotalcite ',
    'Mineral, Carbonate , Heated Manasseite ',
    'Mineral, Carbonate , Heated Pirssonite ',
    'Mineral, Carbonate , Heated Thermonatrite',
    'Mineral, Carbonate , Heated Trona',
    'Mineral, Carbonate , Huntite ',
    'Mineral, Carbonate , Hydrocalcite',
    'Mineral, Carbonate , Hydrocerussite',
    'Mineral, Carbonate , Hydromagnesite',
    'Mineral, Carbonate , Hydrotalcite',
    'Mineral, Carbonate , Magnesite',
    'Mineral, Carbonate , Magnesite ',
    'Mineral, Carbonate , Malachite',
    'Mineral, Carbonate , Manasseite',
    'Mineral, Carbonate , Manganocalcite',
    'Mineral, Carbonate , Monohydrocalcite',
    'Mineral, Carbonate , Nahcolite ',
    'Mineral, Carbonate , Northupite',
    'Mineral, Carbonate , Pirssonite',
    'Mineral, Carbonate , Pyroaurite',
    'Mineral, Carbonate , Rhodochrosite',
    'Mineral, Carbonate , Shortite',
    'Mineral, Carbonate , Siderite',
    'Mineral, Carbonate , Sodium Carbonate',
    'Mineral, Carbonate , Sodium Oxalate',
    'Mineral, Carbonate , Thermonatrite ',
    'Mineral, Carbonate , Trona ',
    'Mineral, Carbonate, Artinite',
    'Mineral, Carbonate, Bruganatellite',
    'Mineral, Carbonate, Coalingite',
    'Mineral, Carbonate, Dypingite Yoshikawaite',
    'Mineral, Carbonate, Gaylussite',
    'Mineral, Carbonate, Hydromagnesite',
    'Mineral, Carbonate, Magnesite',
    'Mineral, Carbonate, Pirssonite',
    'Mineral, Carbonate, Pokrovskite',
    'Mineral, Carbonate, Sjogrenite',
    'Mineral, Carbonate, Thermonatrite ',
    'Mineral, Carbonate, Trona ',
    'Mineral, Chloride, Ammonium Chloride (NH4)Cl ',
    'Mineral, Chloride, Atacamite',
    'Mineral, Chloride, Paratacamite',
    'Mineral, Element, Iron',
    'Mineral, Glass, Basaltic Volcanic Glass',
    'Mineral, Glass, Rhyolitic Volcanic Glass',
    'Mineral, Hydroxide , Brucite ',
    'Mineral, Melt, Melt Inclusion',
    'Mineral, Oxide , Corundum',
    'Mineral, Oxide , Hematite',
    'Mineral, Oxide, Alexandrite',
    'Mineral, Phosphate, Apatite',
    'Mineral, Silicate (Ino) , Pyroxene Orthopyroxene Enstatite Reduced',
    'Mineral, Silicate (Ino) , Pyroxene Shocked',
    'Mineral, Silicate (Ino), Orthopyroxene',
    'Mineral, Silicate (Ino), Pyroxene',
    'Mineral, Silicate (Ino), Pyroxene Clinopyroxene Augite',
    'Mineral, Silicate (Ino), Pyroxene Clinopyroxene Diopside',
    'Mineral, Silicate (Ino), Pyroxene Orthopyroxene Hypersthene',
    'Mineral, Silicate (Neso), Olivine',
    'Mineral, Silicate (Neso), Olivine Forsterite',
    'Mineral, Silicate (Neso), Olivine Heated',
    'Mineral, Silicate (Neso), Olivine Shocked ',
    'Mineral, Silicate (Neso), OlivineForsterite ',
    'Mineral, Silicate (Ortho), Forsterite ',
    'Mineral, Silicate (Phyllo) , Berthierine ',
    'Mineral, Silicate (Phyllo) , Chamosite ',
    'Mineral, Silicate (Phyllo) , Chlorite',
    'Mineral, Silicate (Phyllo) , Heated Chlorite ',
    'Mineral, Silicate (Phyllo) , Heated Serpentine Antigorite',
    'Mineral, Silicate (Phyllo) , Kaolinite',
    'Mineral, Silicate (Phyllo) , Nontronite',
    'Mineral, Silicate (Phyllo) , Serpentine Antigorite ',
    'Mineral, Silicate (Phyllo) , Smectite',
    'Mineral, Silicate (Phyllo), Allophane',
    'Mineral, Silicate (Phyllo), Beidellite',
    'Mineral, Silicate (Tecto), Anorthite ',
    'Mineral, Silicate (Tecto), Feldspar Plagioclase Anorthite',
    'Mineral, Silicate (Tecto), Feldspar Plagioclase Bytownite',
    'Mineral, Silicate (Tecto), Feldspar Plagioclase Labradorite',
    'Mineral, Silicate (Tecto), Laser-Irradiated Anorthite',
    'Mineral, Silicate (Tecto), Natrolite',
    'Mineral, Silicate (Tecto), Plagioclase Feldspar',
    'Mineral, Silicate (Tecto), Quartz',
    'Mineral, Silicate (Tecto), Zeolite',
    'Mineral, Sulfate , Alunite ',
    'Mineral, Sulfate , Anhydrite ',
    'Mineral, Sulfate , Calcium Sulfate Dihydrate Gypsum',
    'Mineral, Sulfate , Copiapite ',
    'Mineral, Sulfate , Gypsum',
    'Mineral, Sulfate , Jarosite',
    'Mineral, Sulfate , Kieserite ',
    'Mineral, Sulfate , Magnesium Sulfate ',
    'Mineral, Sulfate , Water Dissolved Copiapite ',
    'Mineral, Sulfate, Gypsum',
    'Mineral, Sulfide , Chalcopyrite',
    'Mineral, Sulfide , Pentlandite ',
    'Mineral, , ',
    'Mineral, Glass , ',
    'Mineral, Iron Oxide, '
}

mixtures_o = {
    'Mineral, Mixture , Hypersthene Augite',
    'Mineral, Mixture'
}

organics_o = {
    ', Organic , Asphaltite'
}

rocks_o = {
    'RockSlab, Sedimentary , Sandstone '
}

sediments_o = {
    'Soil, Volcanic, Volcanic Alteration'
}