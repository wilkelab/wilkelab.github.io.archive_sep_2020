#download an enzyme helicase with PDB ID 2XZP
cmd.fetch("132L")

#show catalytic residues as white spheres
cmd.hide("all") #hide everything	

cmd.select("cat_rsd", "resi 35+52") #select catalytic residues from CSA

cmd.show("spheres", "cat_rsd") #show catalytic residues as spheres
cmd.color("white", "(cat_rsd)") #color them white

#show the rest of the structure as cartoon
cmd.show("cartoon", "132L")

#color the structure according to b-factors
cmd.spectrum("b", selection=132L)
